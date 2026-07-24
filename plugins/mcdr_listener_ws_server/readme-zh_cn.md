[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mcdr_listener_ws_server

### 基本信息

- 插件 ID: `mcdr_listener_ws_server`
- 插件名: mcdr_listener_ws_server
- 版本: 0.6.3
  - 元数据版本: 0.6.3
  - 发布版本: 0.6.3
- 总下载量: 118
- 作者: [VincentZyu](https://github.com/VincentZyuApps)
- 仓库: https://github.com/VincentZyuApps/mcdr_listener_ws_server
- 仓库插件页: https://github.com/VincentZyuApps/mcdr_listener_ws_server/tree/main
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md), [`API`](/labels/api/readme-zh_cn.md)
- 描述: 📡 群服互通网关，不止文字：游戏事件与群消息双向互通、图片消息游戏内渲染、RCON 远程命令执行

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.13.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.13.0 |
| [websockets](https://pypi.org/project/websockets) | \>=15.0.0 |
| [Pillow](https://pypi.org/project/Pillow) | \>=10.0.0 |
| [requests](https://pypi.org/project/requests) | \>=2.32.0 |

```
pip install "mcdreforged>=2.13.0" "websockets>=15.0.0" "Pillow>=10.0.0" "requests>=2.32.0"
```

### 介绍

🌐💬📡 群服互通 WebSocket 服务端：将玩家聊天和进出服事件推送到聊天平台，接收平台文字与图片消息并在游戏内渲染展示，支持通过 RCON 远程执行服务器命令。🎮🔗

- 🔑 支持 Token 认证，保障 WebSocket 连接安全
- 🖼️ 图片域名白名单，安全渲染展示

更多信息请阅读 [README](https://github.com/VincentZyuApps/mcdr_listener_ws_server)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [mcdr_listener_ws_server-v0.6.3-rc.5.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.6.3-rc.5) | 0.6.3-rc.5 | 2026/06/18 19:18:28 | 22.2KB | 8 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.6.3-rc.5/mcdr_listener_ws_server-v0.6.3-rc.5.mcdr) |
| [mcdr_listener_ws_server-v0.6.3-rc.4.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.6.3-rc.4) | 0.6.3-rc.4 | 2026/06/18 17:58:26 | 22.2KB | 4 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.6.3-rc.4/mcdr_listener_ws_server-v0.6.3-rc.4.mcdr) |
| [mcdr_listener_ws_server-v0.6.3.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.6.3) | 0.6.3 | 2026/06/18 19:33:47 | 22.2KB | 26 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.6.3/mcdr_listener_ws_server-v0.6.3.mcdr) |
| [mcdr_listener_ws_server-v0.6.3-rc.1.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.6.3-rc.1) | 0.6.3-rc.1 | 2026/06/02 16:11:16 | 22.2KB | 30 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.6.3-rc.1/mcdr_listener_ws_server-v0.6.3-rc.1.mcdr) |
| [mcdr_listener_ws_server-v0.6.3-beta.2.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.6.3-beta.2) | 0.6.3-beta.2 | 2026/06/02 12:45:53 | 22.17KB | 10 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.6.3-beta.2/mcdr_listener_ws_server-v0.6.3-beta.2.mcdr) |
| [mcdr_listener_ws_server-v0.6.3-beta.1.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.6.3-beta.1) | 0.6.3-beta.1 | 2026/06/02 08:43:33 | 22.1KB | 7 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.6.3-beta.1/mcdr_listener_ws_server-v0.6.3-beta.1.mcdr) |
| [mcdr_listener_ws_server-v0.6.0-beta.1.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.6.0-beta.1) | 0.6.0-beta.1 | 2026/06/02 07:07:18 | 20.08KB | 8 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.6.0-beta.1/mcdr_listener_ws_server-v0.6.0-beta.1.mcdr) |
| [mcdr_listener_ws_server-v0.5.0-beta.6.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.5.0-beta.6) | 0.5.0-beta.6 | 2026/06/02 06:07:57 | 20.08KB | 8 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.5.0-beta.6/mcdr_listener_ws_server-v0.5.0-beta.6.mcdr) |
| [mcdr_listener_ws_server-v0.5.0-beta.4.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.5.0-beta.4) | 0.5.0-beta.4 | 2026/06/02 04:56:02 | 20.17KB | 9 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.5.0-beta.4/mcdr_listener_ws_server-v0.5.0-beta.4.mcdr) |
| [mcdr_listener_ws_server-v0.5.0-beta.3.mcdr](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/tag/v0.5.0-beta.3) | 0.5.0-beta.3 | 2026/06/02 04:48:06 | 20.17KB | 8 | [下载](https://github.com/VincentZyuApps/mcdr_listener_ws_server/releases/download/v0.5.0-beta.3/mcdr_listener_ws_server-v0.5.0-beta.3.mcdr) |

