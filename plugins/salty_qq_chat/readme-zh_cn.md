[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## salty_qq_chat

### 基本信息

- 插件 ID: `salty_qq_chat`
- 插件名: SaltyQQChat
- 版本: 1.1.8
  - 元数据版本: 1.1.8
  - 发布版本: 1.1.8
- 总下载量: 44
- 作者: [SALTWOOD](https://github.com/SALTWOOD)
- 仓库: https://github.com/SALTWOOD/SaltyQQChat
- 仓库插件页: https://github.com/SALTWOOD/SaltyQQChat/tree/master
- 标签: [`API`](/labels/api/readme-zh_cn.md), [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一个基于 QQAPI 的可扩展的 QQ 机器人

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [qq_api](/plugins/qq_api/readme-zh_cn.md) | ^1.2.0 |
| [online_player_api](/plugins/online_player_api/readme-zh_cn.md) | ^1.0.0 |
| [python](/plugins/python/readme-zh_cn.md) | \>=3.10 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

<div align="center">

![SaltyQQChat](https://socialify.git.ci/SALTWOOD/SaltyQQChat/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto)

# SaltyQQChat
✨🎉 **基于 QQAPI 的、可拓展的 QQ 机器人插件！** 🎉✨
</div>

> [!WARNING]
> 因为有点大病的腾讯，此插件暂缓开发，新款插件将采用网页端机器人的形式。
> 所有新功能都将会更新，但不保证任何功能的可用性。
> 您要用就您自己测试吧.png

# 简介
这是一个使用 [QQAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_api) 的 QQ 机器人插件，相当于是另一个 [QQChat](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_chat)，砍掉了很多个人认为没必要的功能，优化了代码结构。

同时，它还支持通过 **API 调用**的方式，简单地扩展机器人，添加属于你的命令！

目前相比 QQChat 新增功能：
- [x] 支持通过 `/bot-ban` `/bot-pardon` 拒绝响应某用户
- [x] 支持通过机器人执行更多原版命令而不使用 `/command`（如 `/ban` `/pardon`）
- [x] 支持通过机器人启停服务器
- [x] 支持艾特机器人进行答复，而不是发一句什么命令就答复
- [x] 支持 MC 内执行 QQ 机器人命令
- [x] 通过 `/ping` 命令、`/info` 命令检查机器人状态
- [x] **[开发特性]** 通过 `/reload` 远程重载插件
- [x] 可自定义的单向/双向 MC <==> QQ 群转发
- [x] 基于正则表达式的易扩展命令树
- [x] 自动处理加群、加好友、邀请入群申请
- [x] 绑定玩家时验证正版玩家档案是否存在

同时，还去除/修改了以下功能：
- [x] 没有“管理群”、“主群”、“消息同步群”的功能，改为多群同步（不过一般就一个群而已）
- [x] 没有“MultiServer”特性，因为会导致难以预料的 bug 且应用面小
- [x] 对 `!!qq` 命令做了权限限制，因为没有对 CQ 码进行转义，可能会导致机器人账号被用于发布违规信息
- [x] 中文和数字、英文之间做了间隔，且语气更加诙谐

# 使用
## 通过 MCDR 安装
在 MCDR 控制台使用 `!!MCDR plugin install salty_qq_chat`，然后 `!!MCDR confirm`。

## 通过 Release 安装
在 [Releases 页面](https://github.com/SALTWOOD/SaltyQQChat/releases) 下载对应版本的 `.mcdr` 文件，放入 `plugins` 文件夹重载。

## 通过源代码
在 `plugins` 下执行 `git clone https://github.com/SALTWOOD/SaltyQQChat` 或者 `git clone git@github.com:SALTWOOD/SaltyQQChat`，然后重载插件。

# API
这是这个插件最有意思的功能之一，可以通过添加其他 MCDR 插件的方式为这个插件添加自定义命令。
这里展出一个单文件插件的代码作为示例：
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

    sqc.commands.add_command(re.compile(r'/你的命令 (.*)'), [str], handler)

def handler(server: PluginServerInterface, event, command: List[str],
            event_type):
    message = command[0]
    reply(
        event,
        f"[CQ:at,qq={event.user_id}] 你提供的参数是：\"{message}\""
    )
```

# 特别鸣谢
- [QQAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_api) - 提供正向 WebSocket 接入到 CQHttp 的接口
- **SALTWO∅D 服务器的各位** - 帮我测试机器人，还赶在发布 Release 之前帮我发现了越权漏洞（

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [SaltyQQChat-1.1.8.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.8) | 1.1.8 | 2025/01/13 10:49:11 | 22.74KB | 7 | [下载](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.8/SaltyQQChat-1.1.8.mcdr) |
| [SaltyQQChat-1.1.7.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.7) | 1.1.7 | 2025/01/12 13:18:07 | 22.74KB | 2 | [下载](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.7/SaltyQQChat-1.1.7.mcdr) |
| [SaltyQQChat-1.1.6.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.6) | 1.1.6 | 2025/01/12 12:17:00 | 22.73KB | 7 | [下载](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.6/SaltyQQChat-1.1.6.mcdr) |
| [SaltyQQChat-1.1.5.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.5) | 1.1.5 | 2025/01/05 08:36:13 | 22.42KB | 11 | [下载](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.5/SaltyQQChat-1.1.5.mcdr) |
| [SaltyQQChat-1.1.4.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.4) | 1.1.4 | 2025/01/04 19:38:26 | 22.33KB | 4 | [下载](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.4/SaltyQQChat-1.1.4.mcdr) |
| [SaltyQQChat-1.1.3.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.3) | 1.1.3 | 2025/01/04 17:03:38 | 24.22KB | 6 | [下载](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.3/SaltyQQChat-1.1.3.mcdr) |
| [SaltyQQChat-1.1.2.mcdr](https://github.com/SALTWOOD/SaltyQQChat/releases/tag/v1.1.2) | 1.1.2 | 2025/01/04 16:23:09 | 22.19KB | 7 | [下载](https://github.com/SALTWOOD/SaltyQQChat/releases/download/v1.1.2/SaltyQQChat-1.1.2.mcdr) |

