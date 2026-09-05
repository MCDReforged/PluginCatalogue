[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## queqiao

### 基本信息

- 插件 ID: `queqiao`
- 插件名: QueQiao
- 版本: 1.0.1
  - 元数据版本: 1.0.1
  - 发布版本: 1.0.1
- 总下载量: 23
- 作者: [LonelySail](https://github.com/Lonely-Sails)
- 仓库: https://github.com/Minecraft-UniBot/QueQiao.MCDReforged
- 仓库插件页: https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/tree/master
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 鹊桥 V2 协议对接插件，支持正向/反向 WebSocket 连接，实现 Minecraft 与外部系统消息互通

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |
| [mg_events](/plugins/mg_events/readme-zh_cn.md) | * |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | * |
| [online_player_api](/plugins/online_player_api/readme-zh_cn.md) | * |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [websockets](https://pypi.org/project/websockets) | \>=12.0 |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0 |
| [psutil](https://pypi.org/project/psutil) | \>=5.9 |

```
pip install "websockets>=12.0" "PyYAML>=6.0" "psutil>=5.9"
```

### 介绍

# QueQiao MCDR

基于 MCDReforged 的**鹊桥 V2 协议**对接插件，支持**正向 WebSocket（客户端）**与**反向 WebSocket（服务端）**两种连接方式，实现 Minecraft 服务端与外部系统（如 NoneBot / 鹊桥服务端）的实时消息互通。

## 📖 对接项目

本插件遵循鹊桥 V2 协议，可与以下项目对接：

- [UniBot](https://github.com/MineJPGcraft/UniBot) — Minecraft 跨平台机器人框架，本插件为其 MCDR 端实现
- [nonebot-adapter-minecraft](https://github.com/17TheWord/nonebot-adapter-minecraft) — NoneBot 的 Minecraft 适配器，通过鹊桥协议与本插件互通
- [鹊桥项目](https://github.com/17TheWord/QueQiao) — 鹊桥协议官方实现

## ✨ 功能特性

### 连接能力
- 🔌 **双模式 WebSocket**：客户端模式主动连接鹊桥服务端；服务端模式被动等待鹊桥客户端接入
- 🔁 **自动重连**（客户端模式）：可配置重连间隔与最大重试次数
- 🔥 **热重载**：`!!queqiao reload` 重载配置并复用旧连接，无需重启服务器

### API 处理（鹊桥 → MCDR）
| API                 | 说明                        |
| ------------------- | ------------------------- |
| `broadcast`         | 广播消息到游戏                   |
| `send_private_msg`  | 发送私聊消息给指定玩家               |
| `send_title`        | 发送标题/副标题（可配置淡入/停留/淡出时长）   |
| `send_actionbar`    | 发送 ActionBar 消息           |
| `send_rcon_command` | 执行 RCON 命令并返回结果           |
| `get_status`        | 查询服务器状态（CPU/内存/玩家/MOTD 等） |

### 游戏事件转发（MCDR → 鹊桥）
| 事件        | 来源                                                                                        |
| --------- | ----------------------------------------------------------------------------------------- |
| 玩家加入 / 退出 | MCDR 内置事件                                                                                 |
| 玩家聊天 / 命令 | MCDR `USER_INFO` 事件                                                                       |
| 玩家死亡      | [MoreGameEvents](https://mcdreforged.com/zh-CN/plugin/mg_events) `PlayerDeathEvent`       |
| 玩家成就      | [MoreGameEvents](https://mcdreforged.com/zh-CN/plugin/mg_events) `PlayerAdvancementEvent` |

## 📦 安装

### 方式一：直接下载 .mcdr 包
从 [Releases](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/releases) 下载 `QueQiao-vX.X.X.mcdr`，放入 MCDR 的 `plugins/` 目录即可。

### 方式二：源码安装
```bash
git clone https://github.com/Minecraft-UniBot/QueQiao.MCDReforged.git
cd QueQiao.MCDReforged
uv sync
```
将整个目录作为 Directory Plugin 放入 MCDR 插件目录，或自行打包：
```bash
uv run python -m mcdreforged pack
```

## 🎮 命令

| 命令                 | 权限  | 说明                          |
| ------------------ | --- | --------------------------- |
| `!!queqiao`        | 2   | 显示帮助                        |
| `!!queqiao status` | 2   | 查看连接状态（模式、玩家、CPU、内存、MOTD 等） |
| `!!queqiao reload` | 2   | 重载配置并重新连接                   |

## 📋 依赖

### 运行环境
- **MCDReforged** >= 2.15.0
- **Python** >= 3.12

### Python 包
- `websockets` >= 16.0
- `PyYAML` >= 6.0
- `psutil` >= 5.9

### MCDR 插件依赖
| 插件                                                                            | 用途            | 必需                     |
| ----------------------------------------------------------------------------- | ------------- | ---------------------- |
| [MoreGameEvents](https://mcdreforged.com/zh-CN/plugin/mg_events)              | 玩家死亡、成就事件     | ✅                      |
| [Minecraft Data API](https://mcdreforged.com/zh-CN/plugin/minecraft_data_api) | 玩家坐标、生命值、经验等级 | ✅                      |
| [online_player_api](https://mcdreforged.com/zh-CN/plugin/online_player_api)   | 在线玩家列表        | ⚠️ 可选（缺失时回退 MCDR 内置接口） |

## �📄 License

[MIT](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/tree/master/docs/./LICENSE)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [QueQiao-v1.0.1.mcdr](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/releases/tag/v1.0.1) | 1.0.1 | 2026/08/02 23:46:22 | 21.32KB | 23 | [下载](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/releases/download/v1.0.1/QueQiao-v1.0.1.mcdr) |

