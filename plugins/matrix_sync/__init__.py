# 导入所需的API
import asyncio
import json
import os
import sys
import re
import aiofiles

from mcdreforged.api.all import *
from nio import AsyncClient, LoginResponse

# 默认配置内容
default_config = {
    "homeserver": "https://matrix.example.org",
    "user_id": "@username:matrix.example.org",
    "password": "your_password",
    "room_id": "!your-room_id:matrix.example.org"
}

# 加载插件并初始化配置文件
def on_load(server: PluginServerInterface, old):
    global config, DATA_FOLDER, DATA_FILE, homeserver

    config = server.load_config_simple("config.json", default_config)
    DATA_FOLDER = server.get_data_folder()
    server.logger.info(f"登录缓存数据路径: {DATA_FOLDER}")
    DATA_FILE = f"{DATA_FOLDER}/token.json"
    homeserver = config["homeserver"]
    if not (homeserver.startswith("https://") or homeserver.startswith("http://")):
        homeserver = "https://" + config["homeserver"]

    check_config(server)

# 检查配置文件
def check_config(server: PluginServerInterface):
    if config["homeserver"] == "https://matrix.example.org" or config["user_id"] == "@username:matrix.example.org" or config["password"] == "your_password" or config["room_id"] == "!your-room_id:matrix.example.org":
        server.logger.info("请修改好所有配置项，然后重新加载插件! ")
        server.unload_plugin("matrix_sync")
    else:
        server.logger.info("[MatrixSync] 正在应用当前配置，请稍后...")

# 写入缓存
def cache_data(resp: LoginResponse):
    with open(DATA_FILE, "w") as f:
        json.dump(
            {
                "token": resp.access_token
            },
            f,
        )
    
# 初始化Matrix机器人
async def init_client(server: PluginServerInterface) -> None:
    if not os.path.exists(DATA_FILE):
        server.logger.info("检测到首次登录, 使用账号密码登录中...")
        user_id = config["user_id"]
        password = config["password"]
        
        client = AsyncClient(homeserver, user_id)
        resp = await client.login(password, device_name="matrix-nio")
        
        if isinstance(resp, LoginResponse):
            server.logger.info("登录成功, 正在写入缓存以供下次登录...")
            cache_data(resp)
            server.logger.info("缓存写入完成! ")
        else:
            server.logger.info(f"机器人登录失败: {resp}")
            server.logger.info(f'根服务器: "{homeserver}", 登录用户: "{user_id}"')
            sys.exit(1)

    else:
        async with aiofiles.open(DATA_FILE, "r") as f:
            contents = await f.read()
        cache = json.loads(contents)
        client = AsyncClient(f"{homeserver}")
        client.access_token = cache["token"]
        client.user_id = config["user_id"]
        client.device_id = "matrix-nio"
        room_id = config["room_id"]

        message = "MC服务器已启动！"
        
        await client.room_send(
            room_id,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": f"{message}"},
        )
        
        global test_status
        test_status = True
        if test_status:
            server.logger.info("机器人登录成功，已向群组发送测试消息.")
    await client.close()


# 检测连接和登录情况，并反馈状态
def on_server_startup(server: PluginServerInterface):
    asyncio.run(init_client(server))
        
def on_user_info(server: PluginServerInterface, info: Info):
        # server.logger.info("检测到玩家消息, 正在尝试发送到Matrix群组...")
        # 取消上面的注释以判断线上的游戏消息是否开始上报
        global message
        message = f"<{info.player}> {info.content}"
        flag = False
        if test_status:
            flag = True
        if flag:
            asyncio.run(use_client(server))

# 消息上报器 - 从线上游戏到Matrix群组
async def use_client(server: PluginServerInterface) -> None:
    async with aiofiles.open(DATA_FILE, "r") as f:
        contents = await f.read()
    cache = json.loads(contents)
    client = AsyncClient(f"{homeserver}")
    client.access_token = cache["token"]
    client.user_id = config["user_id"]
    client.device_id = "matrix-nio"
    room_id = config["room_id"]

    await client.room_send(
            room_id,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": f"{message}"},
    )

    await client.close()