**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## gugubot

### Basic Information

- Plugin ID: `gugubot`
- Plugin Name: GUGUbot
- Version: 2.0.27
  - Metadata version: 2.0.27
  - Release version: 2.0.27
- Total downloads: 4542
- Authors: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- Repository: https://github.com/PFingan-Code/PF-GUGUBot
- Repository plugin page: https://github.com/PFingan-Code/PF-GUGUBot/tree/main/GUGUbot
- Labels: [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: A QQ bot connect MC and QQ

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [whitelist_api](/plugins/whitelist_api/readme.md) | \>=1.3.0 |
| [mg_events](/plugins/mg_events/readme.md) | \>=0.2.3 |
| [player_ip_logger](/plugins/player_ip_logger/readme.md) | \>=1.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [requests](https://pypi.org/project/requests) |  |
| [ruamel.yaml](https://pypi.org/project/ruamel.yaml) |  |
| [websocket-client](https://pypi.org/project/websocket-client) | \>=1.0.0 |
| [websocket-server](https://pypi.org/project/websocket-server) | \>=0.6.0 |

```
pip install requests ruamel.yaml "websocket-client>=1.0.0" "websocket-server>=0.6.0"
```

### Introduction

# GUGUBot

<div align="center">

[![Visitor Count](https://count.getloli.com/get/@PF-GUGUBot)]

[![查看次数起始时间](https://img.shields.io/badge/查看次数统计起始于-2023%2F9%2F2-1?style=flat-square)](https://github.com/PFingan-Code/PF-GUGUBot/tree/main/GUGUbot//)
[![仓库大小](https://img.shields.io/github/repo-size/LoosePrince/PF-GUGUBot?style=flat-square&label=仓库占用)](https://github.com/PFingan-Code/PF-GUGUBot/tree/main/GUGUbot//) 
[![最新版](https://img.shields.io/github/v/release/LoosePrince/PF-GUGUBot?style=flat-square&label=最新版)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest/download/GUGUbot.mcdr)
[![议题](https://img.shields.io/github/issues/LoosePrince/PF-GUGUBot?style=flat-square&label=Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues) 
[![已关闭issues](https://img.shields.io/github/issues-closed/LoosePrince/PF-GUGUBot?style=flat-square&label=已关闭%20Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/total?style=flat-square&label=下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest)

**一个功能强大的 MCDR 插件，实现 Minecraft 服务器与 QQ 群的无缝互通**

[快速开始](#快速开始) • [功能特性](#功能特性) • [完整文档](https://looseprince.github.io/PF-GUGUBot/) • [问题反馈](https://github.com/LoosePrince/PF-GUGUBot/issues)

</div>

---

## 简介

GUGUBot 是一个专为 MCDReforged 设计的 QQ 机器人插件，支持离线服务器和正版/离线混合服务器。它不仅实现了游戏内外的聊天互通，还集成了白名单管理、玩家绑定、违禁词过滤等实用功能，让服务器管理更加便捷。

### 核心特性

- **🔄 双向聊天转发** - MC 服务器与 QQ 群消息实时互通，支持图片、表情等多种消息类型
- **👥 智能绑定系统** - 玩家 QQ 与游戏 ID 绑定，支持 Java 版和基岩版，退群自动解绑
- **🎯 白名单管理** - 完善的白名单系统，支持在线/离线/基岩版模式
- **🛡️ 违禁词过滤** - 自动检测并撤回包含违禁词的消息
- **🤖 多机器人风格** - 可切换的机器人回复风格，个性化定制
- **🔗 多服互联** - 支持多个 Minecraft 服务器之间的消息互通
- **📊 玩家管理** - 在线玩家查询、不活跃玩家检查、未绑定用户检查
- **⚙️ 命令执行** - 远程执行 MC 命令和 MCDR 命令（管理员权限）
- **📝 关键词回复** - 自定义关键词触发自动回复
- **✅ 待办管理** - 群内协作待办事项系统

> [!NOTE]
> **招募贡献者**
> 
> GUGUbot 和 WebUI 项目正在招募有志者加入开发！
> 
> 有意者请加 QQ [1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 或 QQ群 [726741344](https://qm.qq.com/q/TqmRHmTmcU)

---

## 快速开始

### 前置依赖

在安装 GUGUBot 之前，请确保已安装以下依赖：

| 依赖项                                                                                     | 版本要求    | 说明                |
| --------------------------------------------------------------------------------------- | ------- | ----------------- |
| [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)                             | ≥ 2.0.0 | Minecraft 服务器管理框架 |
| [whitelist_api](https://github.com/TISUnion/whitelist_api)                              | ≥ 1.3.0 | 白名单 API 插件        |
| [mg_events](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/mg_events) | ≥ 0.2.3 | 游戏事件监听插件          |

### 安装方式

#### 方式一：MCDR 一键安装（推荐）

```bash
!!MCDR plugin install gugubot
```

安装完成后：
1. 配置 `/config/GUGUbot/config.yml`（配置机器人基本信息）
2. 重载 gugubot：`!!MCDR plugin reload gugubot`

#### 方式二：手动安装

1. 下载前置插件并放入 `/plugins` 目录
2. 前往 [Releases](https://github.com/LoosePrince/PF-GUGUBot/releases) 下载 `gugubot-vX.X.X.mcdr`
3. 将 `gugubot-vX.X.X.mcdr` 放入 `/plugins` 目录
4. 按照上述步骤配置文件
5. 重启或重载插件

### 基础配置

#### 1. QQ 机器人配置

选择以下任一方案配置 QQ 机器人：

- **[NapCat](https://napneko.github.io/)** - 推荐，稳定高效
- **[LiteLoaderQQNT + LLOneBot](https://github.com/LLOneBot/LLOneBot)** - 轻量级方案

配置 WebSocket 服务端口（如 `8080`），消息上报格式选择 **CQ 码** 或者 **消息体**。

#### 3. GUGUBot 配置

编辑 `/config/GUGUbot/config.yml`，配置以下必要项：

```yaml
connector:
  QQ:
    connection:
      port: 8777  # WebSocket 服务端口
    permissions:
      admin_ids:  # 管理员 QQ 号
        - 1234567890
      group_ids:  # 要监听的 QQ 群号
        - 123456789
```

> [!TIP]
> 完整配置说明请查看 [在线文档 - 配置指南](https://looseprince.github.io/PF-GUGUBot/configuration/)

---

## 功能特性

### 聊天系统

- **双向消息转发**：游戏内聊天实时同步到 QQ 群，QQ 群消息显示在游戏内
- **多媒体支持**：支持图片、表情等多种消息类型
- **自定义模板**：可自定义消息格式和显示样式
- **游戏事件转发**：玩家加入/离开、成就、死亡消息等

### 玩家绑定系统

```
#绑定 <游戏ID> [基岩]     # 绑定自己的游戏账号
#绑定 [@QQ号] <游戏ID>    # 管理员为他人绑定
#解绑 [游戏ID]            # 解绑账号
#绑定 列表                # 查看绑定列表
```

- 支持 Java 版和基岩版账号分别绑定
- 退群自动解绑（可配置）
- 绑定时自动添加白名单（可配置）

### 白名单管理

```
#白名单 添加 <玩家名> [模式]   # 添加白名单
#白名单 删除 <玩家名>          # 删除白名单
#白名单 列表                   # 查看白名单
#白名单 开启/关闭              # 启用/禁用白名单
```

支持三种模式：
- `online` / `正版` - 正版验证
- `offline` / `离线` - 离线模式
- `bedrock` / `基岩` - 基岩版

### 命令执行系统

```
#执行 <MC命令>            # 执行 Minecraft 命令
#mcdr <MCDR命令>          # 执行 MCDR 命令
#执行@服务器名 <命令>      # 跨服执行（多服互联）
```

> 仅管理员可用

### 其他功能

- **关键词回复**：自定义关键词触发特定回复
- **违禁词过滤**：自动检测并处理违禁内容
- **风格系统**：切换机器人回复风格
- **待办管理**：群内协作管理待办事项
- **玩家列表查询**：查询当前在线玩家
- **不活跃检查**：定期检查不活跃玩家并通知
- **未绑定提醒**：提醒新成员绑定账号

查看更多功能详情，请访问 [完整文档 - 功能列表](https://looseprince.github.io/PF-GUGUBot/features/)

---

## 多服互联

GUGUBot 支持多个 Minecraft 服务器之间的消息互通，实现跨服聊天和命令执行。

配置示例：

```yaml
connector:
  minecraft_bridge:
    enable: true
    is_main_server: true  # 主服务器
    connection:
      host: 127.0.0.1
      port: 8787
```

详细配置请参考 [多服互联教程](https://looseprince.github.io/PF-GUGUBot/multi-server/)

---

## 文档

- 📖 [完整在线文档](https://looseprince.github.io/PF-GUGUBot/)
- 📝 [安装指南](https://looseprince.github.io/PF-GUGUBot/installation/)
- ⚙️ [配置说明](https://looseprince.github.io/PF-GUGUBot/configuration/)
- 🎯 [功能详解](https://looseprince.github.io/PF-GUGUBot/features/)
- 🔧 [API 文档](https://looseprince.github.io/PF-GUGUBot/api/)
- ❓ [疑难解答](https://looseprince.github.io/PF-GUGUBot/troubleshooting/)
- 🔗 [多服互联](https://looseprince.github.io/PF-GUGUBot/multi-server/)

---

## 开发与贡献

### 开发指南

GUGUBot 提供了丰富的 API 接口，方便开发者进行二次开发或集成。

查看 [API 文档](https://looseprince.github.io/PF-GUGUBot/api/) 了解更多。

### 贡献代码

欢迎提交 Pull Request！在提交之前，请确保：

1. 代码符合项目的编码规范
2. 添加必要的注释和文档
3. 测试新功能或修复

### 项目结构

```
PF-GUGUBot/
├── GUGUbot/
│   ├── gugubot/          # 核心代码
│   │   ├── builder/      # 消息构建器
│   │   ├── config/       # 配置管理
│   │   ├── connector/    # 连接器（QQ、MC、Bridge）
│   │   ├── logic/        # 逻辑系统
│   │   │   ├── system/   # 核心系统（绑定、白名单等）
│   │   │   └── plugins/  # 插件功能
│   │   ├── parser/       # 消息解析器
│   │   ├── utils/        # 工具类
│   │   └── ws/           # WebSocket 服务
│   ├── lang/             # 多语言支持
│   └── requirements.txt  # 依赖列表
├── docs/                 # 文档源文件
└── tests/                # 测试文件
```

---

## 问题反馈与支持

### 遇到问题？

1. 查看 [疑难解答](https://looseprince.github.io/PF-GUGUBot/troubleshooting/)
2. 搜索 [已有 Issues](https://github.com/LoosePrince/PF-GUGUBot/issues)
3. 提交新的 [Issue](https://github.com/LoosePrince/PF-GUGUBot/issues/new)

### 联系方式

- **QQ**：[1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes)
- **QQ 群**：[726741344](https://qm.qq.com/q/TqmRHmTmcU)
- **GitHub Issues**：[提交问题](https://github.com/LoosePrince/PF-GUGUBot/issues)

---

## 致谢

### 代码贡献

- [QQChat](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_chat) | [AnzhiZhang](https://github.com/AnzhiZhang) - 原始代码基础

### 技术支持

- [@XueK__](https://github.com/XueK66) - 核心开发与技术支持

### 文档贡献

- [@Dreamwxz](https://github.com/Dreamwxz) - 第三方文档 [PF-plugins](https://docs.pfingan.com/PF-gugubot/)

### 社区反馈

感谢所有提交 Issue、Pull Request 和提供反馈的用户！

---

## TODO

- [ ] [多服聚合](https://github.com/LoosePrince/PF-GUGUBot/issues/106)
- [ ] [联动 WebUI](https://github.com/LoosePrince/PF-GUGUBot/issues/107) & [WebUI 开发](https://github.com/LoosePrince/PF-MCDR-WebUI/issues/8)

---

## 许可证

本项目基于 GPL-3.0 许可证开源。详见 [LICENSE](https://github.com/PFingan-Code/PF-GUGUBot/tree/main/GUGUbot/LICENSE.txt)。

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个 Star！**

Made with ❤️ by [LoosePrince](https://github.com/LoosePrince) & [XueK__](https://github.com/XueK66)

</div>

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [gugubot-v2.0.27.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.27) | 2.0.27 | 2026/02/08 05:42:53 | 190.77KB | 4 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.27/gugubot-v2.0.27.mcdr) |
| [gugubot-v2.0.26.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.26) | 2.0.26 | 2026/02/07 06:04:08 | 190.54KB | 13 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.26/gugubot-v2.0.26.mcdr) |
| [gugubot-v2.0.25.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.25) | 2.0.25 | 2026/02/06 06:42:09 | 190.59KB | 11 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.25/gugubot-v2.0.25.mcdr) |
| [gugubot-v2.0.24.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.24) | 2.0.24 | 2026/02/05 05:33:19 | 187.74KB | 15 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.24/gugubot-v2.0.24.mcdr) |
| [gugubot-v2.0.23.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.23) | 2.0.23 | 2026/02/03 05:12:41 | 187.66KB | 27 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.23/gugubot-v2.0.23.mcdr) |
| [gugubot-v2.0.22.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.22) | 2.0.22 | 2026/02/01 01:33:54 | 187.61KB | 20 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.22/gugubot-v2.0.22.mcdr) |
| [gugubot-v2.0.21.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.21) | 2.0.21 | 2026/01/28 04:48:19 | 183.35KB | 28 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.21/gugubot-v2.0.21.mcdr) |
| [gugubot-v2.0.20.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.20) | 2.0.20 | 2026/01/25 06:28:31 | 183.25KB | 29 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.20/gugubot-v2.0.20.mcdr) |
| [gugubot-v2.0.19.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.19) | 2.0.19 | 2026/01/21 07:32:32 | 183.24KB | 27 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.19/gugubot-v2.0.19.mcdr) |
| [gugubot-v2.0.18.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.18) | 2.0.18 | 2026/01/20 06:32:27 | 183.1KB | 12 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.18/gugubot-v2.0.18.mcdr) |
| [gugubot-v2.0.17.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.17) | 2.0.17 | 2026/01/18 07:55:59 | 181.72KB | 28 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.17/gugubot-v2.0.17.mcdr) |
| [gugubot-v2.0.16.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.16) | 2.0.16 | 2026/01/13 05:54:04 | 176.14KB | 33 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.16/gugubot-v2.0.16.mcdr) |
| [gugubot-v2.0.15.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.15) | 2.0.15 | 2026/01/09 06:52:35 | 174.63KB | 42 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.15/gugubot-v2.0.15.mcdr) |
| [gugubot-v2.0.14.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.14) | 2.0.14 | 2026/01/04 04:46:22 | 171.89KB | 36 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.14/gugubot-v2.0.14.mcdr) |
| [gugubot-v2.0.13.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.13) | 2.0.13 | 2026/01/03 07:05:25 | 169.81KB | 15 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.13/gugubot-v2.0.13.mcdr) |
| [gugubot-v2.0.12.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.12) | 2.0.12 | 2025/12/31 04:30:57 | 169.46KB | 40 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.12/gugubot-v2.0.12.mcdr) |
| [gugubot-v2.0.10.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.10) | 2.0.10 | 2025/12/28 06:06:26 | 167.31KB | 22 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.10/gugubot-v2.0.10.mcdr) |
| [gugubot-v2.0.9.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.9) | 2.0.9 | 2025/12/25 05:37:00 | 167.06KB | 29 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.9/gugubot-v2.0.9.mcdr) |
| [gugubot-v2.0.8.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.8) | 2.0.8 | 2025/12/24 06:11:34 | 124.5KB | 12 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.8/gugubot-v2.0.8.mcdr) |
| [gugubot-v2.0.7.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.7) | 2.0.7 | 2025/12/10 06:39:17 | 123.49KB | 70 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.7/gugubot-v2.0.7.mcdr) |
| [gugubot-v2.0.6.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.6) | 2.0.6 | 2025/12/10 05:11:20 | 123.45KB | 5 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.6/gugubot-v2.0.6.mcdr) |
| [gugubot-v2.0.5.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.5) | 2.0.5 | 2025/12/04 04:27:27 | 123.47KB | 61 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.5/gugubot-v2.0.5.mcdr) |
| [gugubot-v2.0.4.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.4) | 2.0.4 | 2025/12/03 07:43:55 | 123.54KB | 19 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.4/gugubot-v2.0.4.mcdr) |
| [gugubot-v2.0.3.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.3) | 2.0.3 | 2025/12/02 08:42:43 | 123.05KB | 16 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.3/gugubot-v2.0.3.mcdr) |
| [gugubot-v2.0.2.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.2) | 2.0.2 | 2025/12/02 05:42:14 | 342.02KB | 12 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.2/gugubot-v2.0.2.mcdr) |
| [gugubot-v2.0.1.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.1) | 2.0.1 | 2025/12/01 08:01:02 | 124.96KB | 12 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.1/gugubot-v2.0.1.mcdr) |
| [gugubot-v2.0.0.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v2.0.0) | 2.0.0 | 2025/11/30 10:33:29 | 116.49KB | 22 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v2.0.0/gugubot-v2.0.0.mcdr) |
| [GUGUbot-v1.11.19.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.19) | 1.11.19 | 2025/10/05 00:27:23 | 12.05MB | 159 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.19/GUGUbot-v1.11.19.mcdr) |
| [GUGUbot-v1.11.18.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.18) | 1.11.18 | 2025/10/01 02:24:16 | 12.05MB | 42 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.18/GUGUbot-v1.11.18.mcdr) |
| [GUGUbot-v1.11.17.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.17) | 1.11.17 | 2025/09/17 03:32:07 | 12.05MB | 69 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.17/GUGUbot-v1.11.17.mcdr) |
| [GUGUbot-v1.11.16.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.16) | 1.11.16 | 2025/09/08 03:53:28 | 12.05MB | 64 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.16/GUGUbot-v1.11.16.mcdr) |
| [GUGUbot-v1.11.15.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.15) | 1.11.15 | 2025/09/02 02:45:05 | 12.05MB | 66 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.15/GUGUbot-v1.11.15.mcdr) |
| [GUGUbot-v1.11.14.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.14) | 1.11.14 | 2025/08/26 02:49:02 | 12.05MB | 74 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.14/GUGUbot-v1.11.14.mcdr) |
| [GUGUbot-v1.11.12.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.12) | 1.11.12 | 2025/08/20 02:08:31 | 12.05MB | 78 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.12/GUGUbot-v1.11.12.mcdr) |
| [GUGUbot-v1.11.11.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.11) | 1.11.11 | 2025/08/12 03:41:08 | 12.04MB | 74 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.11/GUGUbot-v1.11.11.mcdr) |
| [GUGUbot-v1.11.10.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.10) | 1.11.10 | 2025/08/11 02:22:17 | 12.04MB | 37 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.10/GUGUbot-v1.11.10.mcdr) |
| [GUGUbot-v1.11.9.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.9) | 1.11.9 | 2025/08/09 05:48:30 | 12.04MB | 50 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.9/GUGUbot-v1.11.9.mcdr) |
| [GUGUbot-v1.11.8.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.8) | 1.11.8 | 2025/07/21 03:21:26 | 11.94MB | 121 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.8/GUGUbot-v1.11.8.mcdr) |
| [GUGUbot-v1.11.7.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.7) | 1.11.7 | 2025/07/17 01:09:10 | 12.04MB | 66 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.7/GUGUbot-v1.11.7.mcdr) |
| [GUGUbot-v1.11.6.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.6) | 1.11.6 | 2025/07/15 04:43:58 | 11.94MB | 54 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.6/GUGUbot-v1.11.6.mcdr) |
| [GUGUbot-v1.11.5.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.5) | 1.11.5 | 2025/07/09 05:54:10 | 12.04MB | 76 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.5/GUGUbot-v1.11.5.mcdr) |
| [GUGUbot-v1.11.3.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.3) | 1.11.3 | 2025/07/06 06:06:00 | 12.03MB | 49 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.3/GUGUbot-v1.11.3.mcdr) |
| [GUGUbot-v1.11.2.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.2) | 1.11.2 | 2025/07/05 06:34:26 | 12.03MB | 39 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.2/GUGUbot-v1.11.2.mcdr) |
| [GUGUbot-v1.11.1.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.1) | 1.11.1 | 2025/07/05 04:26:16 | 12.03MB | 37 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.1/GUGUbot-v1.11.1.mcdr) |
| [GUGUbot-v1.11.0.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.11.0) | 1.11.0 | 2025/07/05 00:01:52 | 12.03MB | 37 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.11.0/GUGUbot-v1.11.0.mcdr) |
| [GUGUbot-v1.10.0.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.10.0) | 1.10.0 | 2025/06/23 03:06:07 | 11.93MB | 120 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.10.0/GUGUbot-v1.10.0.mcdr) |
| [GUGUbot-v1.9.19.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.19) | 1.9.19 | 2025/06/15 14:17:01 | 12.02MB | 67 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.19/GUGUbot-v1.9.19.mcdr) |
| [GUGUbot-v1.9.18.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.18) | 1.9.18 | 2025/06/15 00:55:50 | 12.02MB | 47 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.18/GUGUbot-v1.9.18.mcdr) |
| [GUGUbot-v1.9.17.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.17) | 1.9.17 | 2025/06/13 05:18:54 | 12.02MB | 55 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.17/GUGUbot-v1.9.17.mcdr) |
| [GUGUbot-v1.9.16.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.16) | 1.9.16 | 2025/06/08 18:30:43 | 12.02MB | 52 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.16/GUGUbot-v1.9.16.mcdr) |
| [GUGUbot-v1.9.15.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.15) | 1.9.15 | 2025/06/08 15:12:54 | 12.02MB | 36 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.15/GUGUbot-v1.9.15.mcdr) |
| [GUGUbot-v1.9.14.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.14) | 1.9.14 | 2025/06/06 02:35:11 | 11.93MB | 67 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.14/GUGUbot-v1.9.14.mcdr) |
| [GUGUbot-v1.9.13.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.13) | 1.9.13 | 2025/06/05 05:52:23 | 11.93MB | 45 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.13/GUGUbot-v1.9.13.mcdr) |
| [GUGUbot-v1.9.12.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.12) | 1.9.12 | 2025/03/07 06:24:15 | 11.79MB | 247 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.12/GUGUbot-v1.9.12.mcdr) |
| [GUGUbot-v1.9.11.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.11) | 1.9.11 | 2025/02/12 06:54:27 | 11.93MB | 85 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.11/GUGUbot-v1.9.11.mcdr) |
| [GUGUbot-v1.9.10.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.10) | 1.9.10 | 2025/02/11 07:04:25 | 11.93MB | 41 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.10/GUGUbot-v1.9.10.mcdr) |
| [GUGUbot-v1.9.8.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.8) | 1.9.8 | 2025/01/09 06:57:55 | 11.81MB | 162 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.8/GUGUbot-v1.9.8.mcdr) |
| [GUGUbot-v1.9.6.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.6) | 1.9.6 | 2025/01/06 05:33:39 | 11.81MB | 61 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.6/GUGUbot-v1.9.6.mcdr) |
| [GUGUbot-v1.9.5.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.5) | 1.9.5 | 2025/01/05 08:22:09 | 11.81MB | 40 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.5/GUGUbot-v1.9.5.mcdr) |
| [GUGUbot-v1.9.4.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.4) | 1.9.4 | 2025/01/02 05:57:02 | 11.8MB | 73 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.4/GUGUbot-v1.9.4.mcdr) |
| [GUGUbot-v1.9.3.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.3) | 1.9.3 | 2024/12/22 06:25:08 | 11.8MB | 102 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.3/GUGUbot-v1.9.3.mcdr) |
| [GUGUbot-v1.9.2.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.2) | 1.9.2 | 2024/12/21 06:11:31 | 11.8MB | 49 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.2/GUGUbot-v1.9.2.mcdr) |
| [GUGUbot-v1.9.1.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.1) | 1.9.1 | 2024/12/20 07:42:45 | 11.8MB | 56 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.1/GUGUbot-v1.9.1.mcdr) |
| [GUGUbot-v1.9.0.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.9.0) | 1.9.0 | 2024/12/20 06:08:19 | 11.8MB | 44 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.9.0/GUGUbot-v1.9.0.mcdr) |
| [GUGUbot-v1.8.7.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.7) | 1.8.7 | 2024/12/09 06:32:41 | 11.66MB | 78 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.7/GUGUbot-v1.8.7.mcdr) |
| [GUGUbot-v1.8.6.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.6) | 1.8.6 | 2024/11/25 16:44:06 | 11.66MB | 85 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.6/GUGUbot-v1.8.6.mcdr) |
| [GUGUbot-v1.8.5.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.5) | 1.8.5 | 2024/11/25 16:38:10 | 11.66MB | 38 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.5/GUGUbot-v1.8.5.mcdr) |
| [GUGUbot-v1.8.4.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.4) | 1.8.4 | 2024/11/16 06:43:51 | 11.66MB | 68 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.4/GUGUbot-v1.8.4.mcdr) |
| [GUGUbot-v1.8.3.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.3) | 1.8.3 | 2024/11/01 00:25:26 | 11.66MB | 67 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.3/GUGUbot-v1.8.3.mcdr) |
| [GUGUbot-v1.8.2.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.2) | 1.8.2 | 2024/10/28 02:31:41 | 11.66MB | 47 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.2/GUGUbot-v1.8.2.mcdr) |
| [GUGUbot-v1.8.1.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.1) | 1.8.1 | 2024/10/26 21:17:31 | 11.66MB | 44 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.1/GUGUbot-v1.8.1.mcdr) |
| [GUGUbot-v1.8.0.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.8.0) | 1.8.0 | 2024/10/20 19:33:18 | 11.66MB | 52 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.8.0/GUGUbot-v1.8.0.mcdr) |
| [GUGUbot-v1.7.5.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.7.5) | 1.7.5 | 2024/10/05 05:12:29 | 11.66MB | 53 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.7.5/GUGUbot-v1.7.5.mcdr) |
| [GUGUbot-v1.7.4.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.7.4) | 1.7.4 | 2024/10/04 02:06:53 | 11.66MB | 38 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.7.4/GUGUbot-v1.7.4.mcdr) |
| [GUGUbot-v1.7.3.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.7.3) | 1.7.3 | 2024/10/03 17:42:45 | 11.66MB | 41 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.7.3/GUGUbot-v1.7.3.mcdr) |
| [GUGUbot-v1.7.2.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.7.2) | 1.7.2 | 2024/09/22 16:20:10 | 11.66MB | 88 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.7.2/GUGUbot-v1.7.2.mcdr) |
| [GUGUbot-v1.7.1.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.7.1) | 1.7.1 | 2024/09/22 14:12:52 | 11.66MB | 43 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.7.1/GUGUbot-v1.7.1.mcdr) |
| [GUGUbot-v1.1.6.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.1.6) | 1.1.6 | 2024/09/18 17:55:55 | 11.65MB | 56 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.1.6/GUGUbot-v1.1.6.mcdr) |
| [GUGUbot-v1.1.5.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.1.5) | 1.1.5 | 2024/09/17 04:47:21 | 11.65MB | 49 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.1.5/GUGUbot-v1.1.5.mcdr) |
| [GUGUbot-v1.1.4.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.1.4) | 1.1.4 | 2024/08/27 05:26:45 | 11.65MB | 111 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.1.4/GUGUbot-v1.1.4.mcdr) |
| [GUGUbot-v1.1.2.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.1.2) | 1.1.2 | 2024/08/18 00:31:47 | 11.65MB | 68 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.1.2/GUGUbot-v1.1.2.mcdr) |
| [GUGUbot-v1.1.1.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.1.1) | 1.1.1 | 2024/08/17 14:05:21 | 11.65MB | 39 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.1.1/GUGUbot-v1.1.1.mcdr) |
| [GUGUbot-v1.1.0.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.1.0) | 1.1.0 | 2024/08/14 16:02:43 | 11.65MB | 45 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.1.0/GUGUbot-v1.1.0.mcdr) |
| [GUGUbot-v1.0.6.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.0.6) | 1.0.6 | 2024/08/13 15:55:00 | 11.65MB | 45 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.0.6/GUGUbot-v1.0.6.mcdr) |
| [GUGUbot.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.0.5) | 1.0.5 | 2023/08/30 11:34:34 | 23.25MB | 46 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.0.5/GUGUbot.mcdr) |
| [GUGUbot.mcdr](https://github.com/PFingan-Code/PF-GUGUBot/releases/tag/v1.0.4) | 1.0.4 | 2023/08/29 05:25:28 | 23.25MB | 40 | [Download](https://github.com/PFingan-Code/PF-GUGUBot/releases/download/v1.0.4/GUGUbot.mcdr) |

