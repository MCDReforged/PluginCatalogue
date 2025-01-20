**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## salty_qq_chat

### Basic Information

- Plugin ID: `salty_qq_chat`
- Plugin Name: SaltyQQChat
- Version: 1.1.8
  - Metadata version: 1.1.8
  - Release version: 1.1.8
- Total downloads: 44
- Authors: [SALTWOOD](https://github.com/SALTWOOD)
- Repository: https://github.com/SALTWOOD/SaltyQQChat
- Repository plugin page: https://github.com/SALTWOOD/SaltyQQChat/tree/master
- Labels: [`API`](/labels/api/readme.md), [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: Scalable QQ-Bot Built on QQAPI

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [qq_api](/plugins/qq_api/readme.md) | ^1.2.0 |
| [online_player_api](/plugins/online_player_api/readme.md) | ^1.0.0 |
| [python](/plugins/python/readme.md) | \>=3.10 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

<div align="center">

![SaltyQQChat](https://socialify.git.ci/SALTWOOD/SaltyQQChat/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto)

# SaltyQQChat
✨🎉 **An Extensible QQ Bot Plugin Powered by QQAPI!** 🎉✨
</div>

> [!WARNING]  
> Due to the f**king Tencent, the development of this plugin is temporarily suspended. The new version will be released as a web-based bot.  
> All new features will be updated, but no availability is promised for any feature.  
> If you decide to use it, testing is on you.

# Introduction
This is a QQ bot plugin based on [QQAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_api), essentially a reworked version of [QQChat](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_chat). It removes many features that I consider unnecessary and optimizes the code structure.

Additionally, it supports simple bot extension through **API calls**, allowing you to add your own custom commands!

**New features compared to QQChat include:**
- [x] Supports ignoring commands from specific users via `/bot-ban` and `/bot-pardon`
- [x] Allows the bot to execute more Minecraft native commands without using `/command` (such as `/ban`, `/pardon`)
- [x] Allows starting and stopping the server through the bot
- [x] Supports replying when the bot is mentioned, instead of just responding to a command
- [x] Supports executing QQ bot commands within Minecraft
- [x] Check bot status via `/ping` and `/info` commands
- [x] **[Development Feature]** Remote plugin reload via `/reload`
- [x] Customizable one-way/two-way MC <==> QQ group forwarding
- [x] Easily extendable command tree based on regular expressions
- [x] Automatically handle group join requests, friend requests, and group invitations.
- [x] Verify if the Minecraft player exists when binding to a player.

**Removed or modified features:**
- [x] No "management group", "main group", or "message sync group" functionality. Instead, it uses multi-group synchronization (though typically, only one group is used)
- [x] No "MultiServer" feature, as it leads to unpredictable bugs and has limited use
- [x] Permissions are added to the `!!qq` command to prevent misuse, as CQ codes are not escaped, potentially allowing the bot account to send inappropriate content
- [x] Spacing added between Chinese, numbers, and English, with a more humorous tone in the responses

# Installation
## Install via MCDR
Use `!!MCDR plugin install salty_qq_chat` in the MCDR console, then `!!MCDR confirm`.

## Install via Release
Download the corresponding `.mcdr` file from the [Releases page](https://github.com/SALTWOOD/SaltyQQChat/releases) and place it in the `plugins` folder, then reload the plugin.

## Install via Source Code
Run `git clone https://github.com/SALTWOOD/SaltyQQChat` or `git clone git@github.com:SALTWOOD/SaltyQQChat` in the `plugins` folder, then reload the plugin.

# API
One of the most interesting features of this plugin is that you can extend it by adding custom commands via other MCDR plugins. Here's an example of a single-file plugin:

```Python
from mcdreforged.api.types import PluginServerInterface
from typing import Callable, List
import re

reply: Callable
PLUGIN_METADATA = {
    'id': 'sqc_extension',
    'version': '1.0.0',
    'name': 'SQC extension plugin',
    'description': 'SaltyQQChat\'s extension plugin',
    'author': 'NONE',
    'link': 'https://github.com',
    'dependencies': {
        'salty_qq_chat': '>=1.0.0'
    }
}

def on_load(server: PluginServerInterface, old):
    global reply
    sqc = server.get_plugin_instance("salty_qq_chat")
    qqapi = server.get_plugin_instance("qq_api")

    reply = sqc.reply

    sqc.commands.add_command(re.compile(r'/your-command (.*)'), [str], handler)

def handler(server: PluginServerInterface, event, command: List[str],
            event_type):
    message = command[0]
    reply(
        event,
        f"[CQ:at,qq={event.user_id}] You provided the parameter: \"{message}\""
    )
```

# Special Thanks
- [QQAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_api) - Provides a WebSocket interface to CQHttp
- **SALTWO∅D server members** - For helping me test the bot and discovering security vulnerabilities before the release

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [SaltyQQChat-1.1.8.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.8) | 1.1.8 | 2025/01/13 10:49:11 | 22.74KB | 7 | [Download](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.8/SaltyQQChat-1.1.8.mcdr) |
| [SaltyQQChat-1.1.7.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.7) | 1.1.7 | 2025/01/12 13:18:07 | 22.74KB | 2 | [Download](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.7/SaltyQQChat-1.1.7.mcdr) |
| [SaltyQQChat-1.1.6.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.6) | 1.1.6 | 2025/01/12 12:17:00 | 22.73KB | 7 | [Download](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.6/SaltyQQChat-1.1.6.mcdr) |
| [SaltyQQChat-1.1.5.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.5) | 1.1.5 | 2025/01/05 08:36:13 | 22.42KB | 11 | [Download](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.5/SaltyQQChat-1.1.5.mcdr) |
| [SaltyQQChat-1.1.4.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.4) | 1.1.4 | 2025/01/04 19:38:26 | 22.33KB | 4 | [Download](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.4/SaltyQQChat-1.1.4.mcdr) |
| [SaltyQQChat-1.1.3.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.3) | 1.1.3 | 2025/01/04 17:03:38 | 24.22KB | 6 | [Download](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.3/SaltyQQChat-1.1.3.mcdr) |
| [SaltyQQChat-1.1.2.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.2) | 1.1.2 | 2025/01/04 16:23:09 | 22.19KB | 7 | [Download](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.2/SaltyQQChat-1.1.2.mcdr) |

