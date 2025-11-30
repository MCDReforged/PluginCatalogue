**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## gugubot

### Basic Information

- Plugin ID: `gugubot`
- Plugin Name: GUGUbot
- Version: 1.11.19
  - Metadata version: 1.11.19
  - Release version: 1.11.19
- Total downloads: 3685
- Authors: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- Repository: https://github.com/LoosePrince/PF-GUGUBot
- Repository plugin page: https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot
- Labels: [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: A QQ bot connect MC and QQ

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [cq_qq_api](/plugins/cq_qq_api/readme.md) | \>=1.5.0 |
| [online_player_api](/plugins/online_player_api/readme.md) | \>=1.0.0 |
| [player_ip_logger](/plugins/player_ip_logger/readme.md) | \>=1.1.0 |
| [whitelist_api](/plugins/whitelist_api/readme.md) | \>=1.4.0 |
| [mg_events](/plugins/mg_events/readme.md) | \>=1.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [pygame](https://pypi.org/project/pygame) |  |
| [Requests](https://pypi.org/project/Requests) |  |
| [ruamel.yaml](https://pypi.org/project/ruamel.yaml) |  |

```
pip install pygame Requests ruamel.yaml
```

### Introduction

# PF-QQchat（支持离线服务器）

> PFingan服务器 MCDR的QQ机器人插件，集QQ群管理和白名单管理一体，添加许多功能。

[![仓库大小](https://img.shields.io/github/repo-size/LoosePrince/PF-GUGUBot?style=flat-square&label=仓库占用)](https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot//) 
[![最新版](https://img.shields.io/github/v/release/LoosePrince/PF-GUGUBot?style=flat-square&label=最新版)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest/download/GUGUbot.mcdr)
[![议题](https://img.shields.io/github/issues/LoosePrince/PF-GUGUBot?style=flat-square&label=Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues) 
[![已关闭issues](https://img.shields.io/github/issues-closed/LoosePrince/PF-GUGUBot?style=flat-square&label=已关闭%20Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/total?style=flat-square&label=下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest)

> [!NOTE]
> 由于 **GUGUbot** 和 **WebUI** 项目庞大，但迄今为止仅有开发者一名，所以我们从现在开始招募有志者加入我们！<br>
> 有意者请加 QQ[1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 或 QQ群[726741344](https://qm.qq.com/q/TqmRHmTmcU)

> [!TIP]
> [腾讯文档] GUGUbot文档<br>
> 此Github文档不再维护详细内容，仅保留必要说明<br>
> 访问官方文档查看更详细的说明: https://pf-doc.pfingan.com/main/#PF-gugubot/

## 文档快速导航
### [GUGUbot](https://pf-doc.pfingan.com/main/#PF-gugubot/)
1. [前置依赖](https://pf-doc.pfingan.com/main/#PF-gugubot/前置依赖)
2. [安装（快速开始）](https://pf-doc.pfingan.com/main/#PF-gugubot/快速开始)
3. [功能列表](https://pf-doc.pfingan.com/main/#PF-gugubot/功能列表)
4. [配置](https://pf-doc.pfingan.com/main/#PF-gugubot/配置)
5. [文件说明文档](https://pf-doc.pfingan.com/main/#PF-gugubot/文档说明文档)
6. [疑难解答](https://pf-doc.pfingan.com/main/#/常见问题/GUGUbot-疑难解答)
### [CQ-QQ-API](https://pf-doc.pfingan.com/main/#PF-cq-api)
1. [快速开始](https://pf-doc.pfingan.com/main/#PF-cq-api/快速开始)
2. [机器人食用指南](https://pf-doc.pfingan.com/main/#PF-cq-api/机器人食用指南)
   - [LiteLoaderQQNT + LLOneBot](https://pf-doc.pfingan.com/main/#PF-cq-api/LLOneBot)
   - [NapCat](https://pf-doc.pfingan.com/main/#PF-cq-api/NapCat)
   - [Lagrange](https://pf-doc.pfingan.com/main/#PF-cq-api/Lagrange)
3. [开发指南](https://pf-doc.pfingan.com/main/#PF-cq-api/开发指南)

## 安装
#### MCDR快捷安装:
1. MCDR服务端输入 `!!MCDR plugin install gugubot`
2. 加载后，在`/config/cq_qq_api/config.json`中配置接收api
3. 加载后，在`/config/GUGUbot/config.yml`中配置机器人
4. 重载 cq_qq_api: `!!MCDR plugin reload cq_qq_api`

#### github下载安装:
1. 下载[前置插件](#前置插件)并放入`/plugins`
2. 前往[Release](https://github.com/LoosePrince/PF-GUGUBot/releases)下载GUGUbot.mcdr放入`/plugins`
3. 加载后，在`/config/cq_qq_api/config.json`中配置服务
4. 加载后，在`/config/GUGUbot/config.yml`中配置机器人
5. 重载 cq_qq_api: `!!MCDR plugin reload cq_qq_api`

### 必要配置
*机器人*
- **正向websocket服务端口:** 接收数据上报的端口，例如`8080`
- **消息上报格式:** 机器人基于CQ码进行解析

*CQ-qq-api*
- **host:** 接收数据上报的地址，默认 `127.0.0.1`
- **port:** 对应数据上报的端口，默认`8080`

*GUGUbot*
- **admin_id:** 管理员QQ号 默认拥有GUGUbot管理员权限(仅私聊)
- **group_id:** 聊天转发的群

> [!IMPORTANT]
> 注: 如果您在安装完成后启动提示没有配置文件请下载[config_default.yml](https://github.com/LoosePrince/PF-GUGUBot/blob/main/config_default.yml)重名名为`config.yml`放入`/config/GUGUbot/config.yml`再运行<br>
> 请注意，以上仅为必要配置项，如果您想要更加私有的体验，请完整的阅读可选配置项！

## 功能列表
> QQ部分帮助，向QQ机器人发送，可以私聊也可以群聊发送 `#帮助`

#### 基本功能

- **聊天互相转发:** 支持 MCDR 与 QQ 群组/私聊之间的消息互通。
- **白名单绑定:** 支持在QQ群内进行白名单绑定，退群自动解绑；支持离线服务器或者正版与离线的混合服务器。

#### 详细功能

包括但不限于：关键词、机器人风格、服务器管理、违禁词等

- [GUGUbot - 功能列表](https://pf-doc.pfingan.com/main/#PF-gugubot/功能列表)

## 配置

### 机器人的必要配置
| 配置项 | 默认值 | 说明 |
| - | - | - |
| 正向websocket服务端口 | `8080` | 接收数据上报的端口 |
| 消息上报格式 | CQ码 | 机器人基于CQ码进行解析 |

### 前置cq_qq_api配置

- 请前往：[CQ-QQ-API - 配置](https://pf-doc.pfingan.com/main/#PF-cq-api/快速开始)

### GUGUbot机器人配置
> [!IMPORTANT]
> 非常建议看看[默认的配置文件](https://github.com/LoosePrince/PF-GUGUBot/blob/main/config_default.yml)<br>

**QQ相关设置 - 必要项**
- admin_id: 管理员QQ号 默认拥有GUGUbot管理员权限(仅私聊)
- group_id: 聊天转发的群

**QQ相关设置 - 可选项**
- 请前往：[GUGUbot - 配置](https://pf-doc.pfingan.com/main/#PF-gugubot/配置)

# 有BUG或是新的IDEA
如果需要更多联动或提交想法和问题请提交 [issues](https://github.com/LoosePrince/PF-GUGUBot/issues) 或 QQ [1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 提交！ <br />
如需要帮助或者交流请通过 QQ群 [726741344](https://qm.qq.com/q/TqmRHmTmcU) 进行询问或者交流 <br />
视情况添加，请勿联系他人（开发者: [雪开](https://github.com/XueK66)）

# TODO
- [ ] [多服聚合](https://github.com/LoosePrince/PF-GUGUBot/issues/106)
- [ ] [联动WebUI](https://github.com/LoosePrince/PF-GUGUBot/issues/107) & [WebUI的饼](https://github.com/LoosePrince/PF-MCDR-WebUI/issues/8)

# 贡献

代码贡献：[QQChat](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_chat) | [AnzhiZhang](https://github.com/AnzhiZhang)

技术支持：[@XueK__](https://github.com/XueK66)

反馈提交：请查发布版本

第三方文档：[@Dreamwxz](https://github.com/Dreamwxz) | [PF-plugins](https://docs.pfingan.com/PF-gugubot/)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [GUGUbot-v1.11.19.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.19) | 1.11.19 | 2025/10/05 00:27:23 | 12.05MB | 129 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.19/GUGUbot-v1.11.19.mcdr) |
| [GUGUbot-v1.11.18.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.18) | 1.11.18 | 2025/10/01 02:24:16 | 12.05MB | 40 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.18/GUGUbot-v1.11.18.mcdr) |
| [GUGUbot-v1.11.17.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.17) | 1.11.17 | 2025/09/17 03:32:07 | 12.05MB | 66 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.17/GUGUbot-v1.11.17.mcdr) |
| [GUGUbot-v1.11.16.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.16) | 1.11.16 | 2025/09/08 03:53:28 | 12.05MB | 62 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.16/GUGUbot-v1.11.16.mcdr) |
| [GUGUbot-v1.11.15.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.15) | 1.11.15 | 2025/09/02 02:45:05 | 12.05MB | 62 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.15/GUGUbot-v1.11.15.mcdr) |
| [GUGUbot-v1.11.14.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.14) | 1.11.14 | 2025/08/26 02:49:02 | 12.05MB | 71 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.14/GUGUbot-v1.11.14.mcdr) |
| [GUGUbot-v1.11.12.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.12) | 1.11.12 | 2025/08/20 02:08:31 | 12.05MB | 76 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.12/GUGUbot-v1.11.12.mcdr) |
| [GUGUbot-v1.11.11.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.11) | 1.11.11 | 2025/08/12 03:41:08 | 12.04MB | 72 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.11/GUGUbot-v1.11.11.mcdr) |
| [GUGUbot-v1.11.10.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.10) | 1.11.10 | 2025/08/11 02:22:17 | 12.04MB | 34 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.10/GUGUbot-v1.11.10.mcdr) |
| [GUGUbot-v1.11.9.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.9) | 1.11.9 | 2025/08/09 05:48:30 | 12.04MB | 46 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.9/GUGUbot-v1.11.9.mcdr) |
| [GUGUbot-v1.11.8.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.8) | 1.11.8 | 2025/07/21 03:21:26 | 11.94MB | 119 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.8/GUGUbot-v1.11.8.mcdr) |
| [GUGUbot-v1.11.7.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.7) | 1.11.7 | 2025/07/17 01:09:10 | 12.04MB | 64 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.7/GUGUbot-v1.11.7.mcdr) |
| [GUGUbot-v1.11.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.6) | 1.11.6 | 2025/07/15 04:43:58 | 11.94MB | 52 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.6/GUGUbot-v1.11.6.mcdr) |
| [GUGUbot-v1.11.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.5) | 1.11.5 | 2025/07/09 05:54:10 | 12.04MB | 72 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.5/GUGUbot-v1.11.5.mcdr) |
| [GUGUbot-v1.11.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.3) | 1.11.3 | 2025/07/06 06:06:00 | 12.03MB | 46 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.3/GUGUbot-v1.11.3.mcdr) |
| [GUGUbot-v1.11.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.2) | 1.11.2 | 2025/07/05 06:34:26 | 12.03MB | 36 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.2/GUGUbot-v1.11.2.mcdr) |
| [GUGUbot-v1.11.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.1) | 1.11.1 | 2025/07/05 04:26:16 | 12.03MB | 34 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.1/GUGUbot-v1.11.1.mcdr) |
| [GUGUbot-v1.11.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.11.0) | 1.11.0 | 2025/07/05 00:01:52 | 12.03MB | 33 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.11.0/GUGUbot-v1.11.0.mcdr) |
| [GUGUbot-v1.10.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.10.0) | 1.10.0 | 2025/06/23 03:06:07 | 11.93MB | 111 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.10.0/GUGUbot-v1.10.0.mcdr) |
| [GUGUbot-v1.9.19.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.19) | 1.9.19 | 2025/06/15 14:17:01 | 12.02MB | 64 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.19/GUGUbot-v1.9.19.mcdr) |
| [GUGUbot-v1.9.18.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.18) | 1.9.18 | 2025/06/15 00:55:50 | 12.02MB | 44 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.18/GUGUbot-v1.9.18.mcdr) |
| [GUGUbot-v1.9.17.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.17) | 1.9.17 | 2025/06/13 05:18:54 | 12.02MB | 52 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.17/GUGUbot-v1.9.17.mcdr) |
| [GUGUbot-v1.9.16.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.16) | 1.9.16 | 2025/06/08 18:30:43 | 12.02MB | 50 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.16/GUGUbot-v1.9.16.mcdr) |
| [GUGUbot-v1.9.15.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.15) | 1.9.15 | 2025/06/08 15:12:54 | 12.02MB | 34 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.15/GUGUbot-v1.9.15.mcdr) |
| [GUGUbot-v1.9.14.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.14) | 1.9.14 | 2025/06/06 02:35:11 | 11.93MB | 64 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.14/GUGUbot-v1.9.14.mcdr) |
| [GUGUbot-v1.9.13.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.13) | 1.9.13 | 2025/06/05 05:52:23 | 11.93MB | 41 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.13/GUGUbot-v1.9.13.mcdr) |
| [GUGUbot-v1.9.12.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.12) | 1.9.12 | 2025/03/07 06:24:15 | 11.79MB | 245 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.12/GUGUbot-v1.9.12.mcdr) |
| [GUGUbot-v1.9.11.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.11) | 1.9.11 | 2025/02/12 06:54:27 | 11.93MB | 83 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.11/GUGUbot-v1.9.11.mcdr) |
| [GUGUbot-v1.9.10.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.10) | 1.9.10 | 2025/02/11 07:04:25 | 11.93MB | 39 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.10/GUGUbot-v1.9.10.mcdr) |
| [GUGUbot-v1.9.8.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.8) | 1.9.8 | 2025/01/09 06:57:55 | 11.81MB | 159 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.8/GUGUbot-v1.9.8.mcdr) |
| [GUGUbot-v1.9.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.6) | 1.9.6 | 2025/01/06 05:33:39 | 11.81MB | 58 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.6/GUGUbot-v1.9.6.mcdr) |
| [GUGUbot-v1.9.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.5) | 1.9.5 | 2025/01/05 08:22:09 | 11.81MB | 38 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.5/GUGUbot-v1.9.5.mcdr) |
| [GUGUbot-v1.9.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.4) | 1.9.4 | 2025/01/02 05:57:02 | 11.8MB | 70 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.4/GUGUbot-v1.9.4.mcdr) |
| [GUGUbot-v1.9.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.3) | 1.9.3 | 2024/12/22 06:25:08 | 11.8MB | 99 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.3/GUGUbot-v1.9.3.mcdr) |
| [GUGUbot-v1.9.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.2) | 1.9.2 | 2024/12/21 06:11:31 | 11.8MB | 45 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.2/GUGUbot-v1.9.2.mcdr) |
| [GUGUbot-v1.9.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.1) | 1.9.1 | 2024/12/20 07:42:45 | 11.8MB | 53 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.1/GUGUbot-v1.9.1.mcdr) |
| [GUGUbot-v1.9.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.0) | 1.9.0 | 2024/12/20 06:08:19 | 11.8MB | 39 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.0/GUGUbot-v1.9.0.mcdr) |
| [GUGUbot-v1.8.7.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.7) | 1.8.7 | 2024/12/09 06:32:41 | 11.66MB | 74 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.7/GUGUbot-v1.8.7.mcdr) |
| [GUGUbot-v1.8.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.6) | 1.8.6 | 2024/11/25 16:44:06 | 11.66MB | 83 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.6/GUGUbot-v1.8.6.mcdr) |
| [GUGUbot-v1.8.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.5) | 1.8.5 | 2024/11/25 16:38:10 | 11.66MB | 36 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.5/GUGUbot-v1.8.5.mcdr) |
| [GUGUbot-v1.8.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.4) | 1.8.4 | 2024/11/16 06:43:51 | 11.66MB | 65 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.4/GUGUbot-v1.8.4.mcdr) |
| [GUGUbot-v1.8.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.3) | 1.8.3 | 2024/11/01 00:25:26 | 11.66MB | 64 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.3/GUGUbot-v1.8.3.mcdr) |
| [GUGUbot-v1.8.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.2) | 1.8.2 | 2024/10/28 02:31:41 | 11.66MB | 45 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.2/GUGUbot-v1.8.2.mcdr) |
| [GUGUbot-v1.8.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.1) | 1.8.1 | 2024/10/26 21:17:31 | 11.66MB | 42 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.1/GUGUbot-v1.8.1.mcdr) |
| [GUGUbot-v1.8.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.0) | 1.8.0 | 2024/10/20 19:33:18 | 11.66MB | 50 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.0/GUGUbot-v1.8.0.mcdr) |
| [GUGUbot-v1.7.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.5) | 1.7.5 | 2024/10/05 05:12:29 | 11.66MB | 51 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.5/GUGUbot-v1.7.5.mcdr) |
| [GUGUbot-v1.7.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.4) | 1.7.4 | 2024/10/04 02:06:53 | 11.66MB | 36 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.4/GUGUbot-v1.7.4.mcdr) |
| [GUGUbot-v1.7.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.3) | 1.7.3 | 2024/10/03 17:42:45 | 11.66MB | 38 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.3/GUGUbot-v1.7.3.mcdr) |
| [GUGUbot-v1.7.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.2) | 1.7.2 | 2024/09/22 16:20:10 | 11.66MB | 86 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.2/GUGUbot-v1.7.2.mcdr) |
| [GUGUbot-v1.7.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.1) | 1.7.1 | 2024/09/22 14:12:52 | 11.66MB | 39 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.1/GUGUbot-v1.7.1.mcdr) |
| [GUGUbot-v1.1.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.6) | 1.1.6 | 2024/09/18 17:55:55 | 11.65MB | 52 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.6/GUGUbot-v1.1.6.mcdr) |
| [GUGUbot-v1.1.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.5) | 1.1.5 | 2024/09/17 04:47:21 | 11.65MB | 44 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.5/GUGUbot-v1.1.5.mcdr) |
| [GUGUbot-v1.1.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.4) | 1.1.4 | 2024/08/27 05:26:45 | 11.65MB | 109 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.4/GUGUbot-v1.1.4.mcdr) |
| [GUGUbot-v1.1.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.2) | 1.1.2 | 2024/08/18 00:31:47 | 11.65MB | 66 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.2/GUGUbot-v1.1.2.mcdr) |
| [GUGUbot-v1.1.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.1) | 1.1.1 | 2024/08/17 14:05:21 | 11.65MB | 35 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.1/GUGUbot-v1.1.1.mcdr) |
| [GUGUbot-v1.1.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.0) | 1.1.0 | 2024/08/14 16:02:43 | 11.65MB | 43 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.0/GUGUbot-v1.1.0.mcdr) |
| [GUGUbot-v1.0.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.6) | 1.0.6 | 2024/08/13 15:55:00 | 11.65MB | 43 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.6/GUGUbot-v1.0.6.mcdr) |
| [GUGUbot.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.5) | 1.0.5 | 2023/08/30 11:34:34 | 23.25MB | 44 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.5/GUGUbot.mcdr) |
| [GUGUbot.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.4) | 1.0.4 | 2023/08/29 05:25:28 | 23.25MB | 38 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.4/GUGUbot.mcdr) |

