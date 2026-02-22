[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## telegram_chat

### 基本信息

- 插件 ID: `telegram_chat`
- 插件名: TelegramChat
- 版本: 2.0.4
  - 元数据版本: 2.0.4
  - 发布版本: 2.0.4
- 总下载量: 128
- 作者: [SALTWOOD](https://github.com/SALTWOOD)
- 仓库: https://github.com/SALTWOOD/TelegramChat
- 仓库插件页: https://github.com/SALTWOOD/TelegramChat/tree/master
- 标签: [`API`](/labels/api/readme-zh_cn.md), [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一个可扩展的 TG 机器人

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [online_player_api](/plugins/online_player_api/readme-zh_cn.md) | ^1.0.0 |
| [python](/plugins/python/readme-zh_cn.md) | \>=3.10 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [python-telegram-bot](https://pypi.org/project/python-telegram-bot) | \>=21.10 |

```
pip install "python-telegram-bot>=21.10"
```

### 介绍

<div align="center">

![TelegramChat](https://socialify.git.ci/SALTWOOD/TelegramChat/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto)

# TelegramChat
✨🎉 **基于 python-telegram-bot 的、可拓展的 Telegram 机器人插件！** 🎉✨
</div>

> [!WARNING]
> 因为有点大病的腾讯，所以整个插件转向 Telegram 方向进行开发，旧版本的基于 QQ 的将会被废弃。
> 为 SaltyQQChat 编写的插件仍可以使用，只需要更改一点点代码即可。

# 简介
这是一个使用 [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) 的 Telegram 机器人插件。

同时，它还支持通过 **API 调用**的方式，简单地扩展机器人，添加属于你的命令！

拥有的功能：
- [x] 支持通过 `/ban` `/pardon` 拒绝响应某用户
- [x] 支持通过机器人执行更多原版命令而不使用 `/command`（如 `/ban` `/pardon`）
- [x] 支持通过机器人启停服务器
- [x] 支持艾特机器人进行答复，而不是发一句什么命令就答复
- [x] 支持 MC 内执行机器人命令
- [x] 通过 `/ping` 命令、`/info` 命令检查机器人状态
- [x] **[开发特性]** 通过 `/reload` 远程重载插件
- [x] 可自定义的单向/双向 MC <==> Telegram 群转发
- [x] 基于正则表达式的易扩展命令树
- [x] 自动处理加群、加好友、邀请入群申请
- [x] 绑定玩家时验证正版玩家档案是否存在
- [x] 中文和数字、英文之间做了间隔，且语气更加诙谐

没有的功能：
- [x] 没有“管理群”、“主群”、“消息同步群”的功能，改为多群同步（不过一般就一个群而已）
- [x] 没有“MultiServer”特性，因为会导致难以预料的 bug 且应用面小

# 使用
## 通过 MCDR 安装
在 MCDR 控制台使用 `!!MCDR plugin install telegram_chat`，然后 `!!MCDR confirm`。

## 通过 Release 安装
在 [Releases 页面](https://github.com/SALTWOOD/TelegramChat/releases) 下载对应版本的 `.mcdr` 文件，放入 `plugins` 文件夹重载。

## 通过源代码
在 `plugins` 下执行 `git clone https://github.com/SALTWOOD/TelegramChat` 或者 `git clone git@github.com:SALTWOOD/TelegramChat`，然后重载插件。

# API
这是这个插件最有意思的功能之一，可以通过添加其他 MCDR 插件的方式为这个插件添加自定义命令。
这里展出一个单文件插件的代码作为示例：
```Python
from typing import Any, Callable, List

from mcdreforged.api.types import PluginServerInterface
from telegram import Update
from telegram.ext import ContextTypes

import re

PLUGIN_METADATA = {
    'id': 'tc_extension',
    'version': '1.0.0',
    'name': 'TC extension plugin',
    'description': 'TelegramChat\'s extension plugin',
    'author': 'NONE',
    'link': 'https://github.com',
    'dependencies': {
        'telegram_chat': '>=2.0.0'
    }
}

plugin: Any
send_to: Callable

def on_load(server: PluginServerInterface, old):
    global plugin, send_to
    plugin = server.get_plugin_instance("telegram_chat")

    send_to = plugin.tools.send_to

    plugin.command_tree.add_command(re.compile(r'/你的命令 (.*)'), [str], handler)

async def handler(server: PluginServerInterface, event: Update, context: ContextTypes.DEFAULT_TYPE, command: List[str],
                  event_type: MessageType):
    message = command[0]
    await send_to(
        event,
        context,
        f"你提供的参数是：\"{message}\""
    )
```

# 特别鸣谢
- [QQChat](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_chat) - TelegramChat 前身的前身
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - 提供接入到 Telegram 的接口
- **SALTWO∅D 服务器的各位** - 帮我测试机器人，还赶在发布 Release 之前帮我发现了越权漏洞（

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [TelegramChat-v2.0.4.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.4) | 2.0.4 | 2025/07/19 12:43:38 | 22.09KB | 37 | [下载](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.4/TelegramChat-v2.0.4.mcdr) |
| [TelegramChat-v2.0.3.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.3) | 2.0.3 | 2025/07/18 11:36:32 | 21.99KB | 26 | [下载](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.3/TelegramChat-v2.0.3.mcdr) |
| [TelegramChat-v2.0.2.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.2) | 2.0.2 | 2025/07/15 10:23:48 | 21.98KB | 25 | [下载](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.2/TelegramChat-v2.0.2.mcdr) |
| [TelegramChat-v2.0.1.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.1) | 2.0.1 | 2025/03/24 15:09:04 | 21.56KB | 40 | [下载](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.1/TelegramChat-v2.0.1.mcdr) |

