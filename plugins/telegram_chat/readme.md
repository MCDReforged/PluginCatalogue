**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## telegram_chat

### Basic Information

- Plugin ID: `telegram_chat`
- Plugin Name: TelegramChat
- Version: 2.0.4
  - Metadata version: 2.0.4
  - Release version: 2.0.4
- Total downloads: 128
- Authors: [SALTWOOD](https://github.com/SALTWOOD)
- Repository: https://github.com/SALTWOOD/TelegramChat
- Repository plugin page: https://github.com/SALTWOOD/TelegramChat/tree/master
- Labels: [`API`](/labels/api/readme.md), [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: Scalable Telegram-Bot.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [online_player_api](/plugins/online_player_api/readme.md) | ^1.0.0 |
| [python](/plugins/python/readme.md) | \>=3.10 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [python-telegram-bot](https://pypi.org/project/python-telegram-bot) | \>=21.10 |

```
pip install "python-telegram-bot>=21.10"
```

### Introduction

<div align="center">

![TelegramChat](https://socialify.git.ci/SALTWOOD/TelegramChat/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto)

# TelegramChat
✨🎉 **An Extensible Telegram Bot Plugin Powered by python-telegram-bot!** 🎉✨
</div>

> [!WARNING]  
> Due to f**king Tencent's issues, the entire plugin is now being developed for Telegram. QQ-based versions will no longer be supported.
> The plugin wrote for SaltyQQChat can still be used; simply modify a little of the codes.

# Introduction
This is a Telegram bot plugin based on [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

Additionally, it supports simple bot extension through **API calls**, allowing you to add your own custom commands!

**Features we have:**
- [x] Supports ignoring commands from specific users via `/ban` and `/pardon`
- [x] Allows the bot to execute more Minecraft native commands without using `/command` (such as `/ban`, `/pardon`)
- [x] Allows starting and stopping the server through the bot
- [x] Supports replying when the bot is mentioned, instead of just responding to a command
- [x] Supports executing bot commands within Minecraft
- [x] Check bot status via `/ping` and `/info` commands
- [x] **[Development Feature]** Remote plugin reload via `/reload`
- [x] Customizable one-way/two-way MC <==> Telegram group forwarding
- [x] Easily extendable command tree based on regular expressions
- [x] Automatically handle group join requests, friend requests, and group invitations.
- [x] Verify if the Minecraft player exists when binding to a player.
- [x] Spacing added between Chinese, numbers, and English, with a more humorous tone in the responses

**Features we don't have:**
- [x] No "management group", "main group", or "message sync group" functionality. Instead, it uses multi-group synchronization (though typically, only one group is used)
- [x] No "MultiServer" feature, as it leads to unpredictable bugs and has limited use

# Installation
## Install via MCDR
Use `!!MCDR plugin install telegram_chat` in the MCDR console, then `!!MCDR confirm`.

## Install via Release
Download the corresponding `.mcdr` file from the [Releases page](https://github.com/SALTWOOD/TelegramChat/releases) and place it in the `plugins` folder, then reload the plugin.

## Install via Source Code
Run `git clone https://github.com/SALTWOOD/TelegramChat` or `git clone git@github.com:SALTWOOD/TelegramChat` in the `plugins` folder, then reload the plugin.

# API
One of the most interesting features of this plugin is that you can extend it by adding custom commands via other MCDR plugins. Here's an example of a single-file plugin:

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

    plugin.command_tree.add_command(re.compile(r'/your-command (.*)'), [str], handler)

async def handler(server: PluginServerInterface, event: Update, context: ContextTypes.DEFAULT_TYPE, command: List[str],
                  event_type: MessageType):
    message = command[0]
    await send_to(
        event,
        context,
        f"You provided the parameter: \"{message}\""
    )
```

# Special Thanks
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Provides a way to access Telegram.
- **SALTWO∅D server members** - For helping me test the bot and discovering security vulnerabilities before the release

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [TelegramChat-v2.0.4.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.4) | 2.0.4 | 2025/07/19 12:43:38 | 22.09KB | 37 | [Download](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.4/TelegramChat-v2.0.4.mcdr) |
| [TelegramChat-v2.0.3.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.3) | 2.0.3 | 2025/07/18 11:36:32 | 21.99KB | 26 | [Download](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.3/TelegramChat-v2.0.3.mcdr) |
| [TelegramChat-v2.0.2.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.2) | 2.0.2 | 2025/07/15 10:23:48 | 21.98KB | 25 | [Download](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.2/TelegramChat-v2.0.2.mcdr) |
| [TelegramChat-v2.0.1.mcdr](https://github.com/SALTWOOD/TelegramChat/releases/tag/v2.0.1) | 2.0.1 | 2025/03/24 15:09:04 | 21.56KB | 40 | [Download](https://github.com/SALTWOOD/TelegramChat/releases/download/v2.0.1/TelegramChat-v2.0.1.mcdr) |

