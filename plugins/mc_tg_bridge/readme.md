**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mc_tg_bridge

### Basic Information

- Plugin ID: `mc_tg_bridge`
- Plugin Name: Minecraft Telegram Bridge
- Version: 1.2.1
  - Metadata version: 1.2.1
  - Release version: 1.2.1
- Total downloads: 16
- Authors: [Azusa_mikan](https://github.com/Azusa-mikan)
- Repository: https://github.com/Azusa-mikan/minecraft_telegram_bridge
- Repository plugin page: https://github.com/Azusa-mikan/minecraft_telegram_bridge/tree/main
- Labels: [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: Control your Minecraft server via Telegram Bot, with chat sync and event forwarding

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15 |
| [mg_events](/plugins/mg_events/readme.md) | \>=1.1.2 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | \>=1.6.1 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [pydantic](https://pypi.org/project/pydantic) | \>=2.12.5 |
| [python-telegram-bot[rate-limiter]](https://pypi.org/project/python-telegram-bot[rate-limiter]) | ==22.7 |

```
pip install "pydantic>=2.12.5" "python-telegram-bot[rate-limiter]==22.7"
```

### Introduction

# Minecraft Telegram Bridge

一个用于 [MCDReforged](https://github.com/MCDReforged/MCDReforged) 的 Telegram 桥接插件。  
它可以把 Minecraft 服务器和 Telegram 群聊连接起来，实现聊天互通、服务器事件通知，以及基础的远程控制。

## 功能概览

- Minecraft 聊天转发到 Telegram（支持自定义格式）
- Telegram 消息转发到 Minecraft（支持在游戏内快捷回复）
- 玩家进出服通知、服务器启停通知
- Telegram 查看服务器状态（CPU、内存、线程、IO、队列）
- Telegram 远程控制服务器：启动、停止、重启
- Telegram 执行 Minecraft 命令 / MCDR 命令
- Telegram 用户与游戏玩家名绑定（验证码流程）

## 环境要求

- Python `>= 3.10`
- MCDReforged `>= 2.15`
- [mg_events](https://github.com/Mooling0602/MoreGameEvents-MCDR) `>=1.1.2`
- [minecraft_data_api](https://github.com/Fallen-Breath/MinecraftDataAPI) `>=1.6.1`

## 安装

直接使用下面的命令，它会搞定一切：

```
!!MCDR plugin install mc_tg_bridge
```

安装后插件会自动生成配置文件 `config/tgb/config.yaml`（具体路径取决于 MCDR 数据目录）

## 配置文件

### 字段说明

- `plugin_status`：是否启用插件（必须为 `true`）
- `to_tg_message_format`：Minecraft -> Telegram 聊天格式
- `to_mc_message_format`：Telegram -> Minecraft 聊天格式
- `joined_message` / `left_message`：玩家进出服通知模板
- `server_started_message` / `server_stopped_message`：服务器启停通知模板
- `mc_to_tg_send_events`: 启用额外事件消息转发（玩家死亡、获得进度）
- `telegram.bot_token`：BotFather 创建的机器人 Token
- `telegram.admin_id`：管理员 Telegram 用户 ID（高权限操作判定）
- `telegram.chat_ids`：允许交互的 Telegram 聊天 ID 列表（只能群组）

## 使用说明

### Telegram 侧命令

- `/start`：激活机器人（含绑定流程入口）
- `/status`：查看服务器状态
- `/bind <玩家名>`：发起绑定流程
- `/stop`：停止服务器（仅管理员）
- `/restart`：重启服务器（仅管理员）
- `/start_server`：启动服务器（仅管理员）
- `/exec <命令>`：执行命令
  - 以 `!!` 开头：执行 MCDR 命令（权限由 MCDR 权限系统判定）
  - 非 `!!`：执行 Minecraft 命令（仅管理员）

### Minecraft 侧命令

- `!!tgb reply <chat_id> <message_id> <text>`：回复某条 Telegram 消息
- `!!tgb bind <验证码>`：完成 Telegram 绑定验证

## 绑定流程

1. 在 Telegram 群中执行 `/bind 玩家名`
2. 点击机器人给出的验证按钮（跳转私聊）
3. 机器人私聊发送 6 位验证码
4. 在游戏内执行：`!!tgb bind 验证码`
5. 验证成功后，Telegram 用户与玩家名写入 `bind.json`

说明：
- 验证码默认 60 秒有效
- 同一时刻只允许一个待验证请求

## 权限与安全

- 只有 `telegram.chat_ids` 中的聊天可与机器人交互
- 管理操作（启停服、重启）仅 `admin_id` 可用
- `/exec !!...` 会以 Telegram 命令源执行 MCDR 命令：
  - `admin_id` 映射为较高权限等级
  - 其他用户为低权限等级

## 消息流向

- Minecraft -> Telegram：
  - 玩家聊天（非 `!!` 命令）
  - 玩家加入 / 离开
  - 玩家死亡 / 达成进度（若 `mc_to_tg_send_events` 为 `true`）
  - 服务器启动 / 停止
- Telegram -> Minecraft：
  - 群消息转发到游戏聊天
  - 未绑定用户显示为 Telegram 昵称（绑定后可显示玩家名）

## 常见问题

- 插件未加载：
  - 检查 `plugin_status` 是否为 `true`
  - 检查 `bot_token`、`chat_ids`、`admin_id` 是否正确
- Telegram 收不到消息：
  - 确认机器人已在目标群并关闭私有模式
  - 确认群 ID 已写入 `chat_ids`
- 未转发死亡消息和进度消息
  - 如果你所运行的服务端不会在控制台输出，那么 `MoreGameEvents-MCDR` 插件将无法捕获
  - 详见: [工作原理](https://github.com/Mooling0602/MoreGameEvents-MCDR#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)
- 死亡消息和进度消息有颜色符号
  - 只要把 `/config/mg_events/config.yml` 中的 `set_advancement_color_in_content_raw` 配置项改为 `false` 即可
  - 详见: [MoreGameEvents-MCDR 文档](https://github.com/Mooling0602/MoreGameEvents-MCDR#%E6%96%87%E6%A1%A3%E7%AE%80%E6%98%93%E7%89%88)
- 绑定失败：
  - 确认验证码未过期
  - 确认执行绑定命令的游戏玩家与发起绑定的 Telegram 用户一致

## 许可证

本项目使用 **GNU General Public License v3.0 (GPL-3.0)** 许可证发布。

Copyright (C) 2026 Azusa-Mikan

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MinecraftTelegramBridge-v1.2.1.mcdr](https://github.com/Azusa-mikan/minecraft_telegram_bridge/releases/tag/v1.2.1) | 1.2.1 | 2026/04/19 16:57:58 | 13.44KB | 16 | [Download](https://github.com/Azusa-mikan/minecraft_telegram_bridge/releases/download/v1.2.1/MinecraftTelegramBridge-v1.2.1.mcdr) |

