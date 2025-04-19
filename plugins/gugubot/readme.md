**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## gugubot

### Basic Information

- Plugin ID: `gugubot`
- Plugin Name: GUGUbot
- Version: 1.9.12
  - Metadata version: 1.9.12
  - Release version: 1.9.12
- Total downloads: 999
- Authors: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- Repository: https://github.com/LoosePrince/PF-GUGUBot
- Repository plugin page: https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot
- Labels: [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: A QQ bot connect MC and QQ

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [cq_qq_api](/plugins/cq_qq_api/readme.md) | \>=1.2.1 |
| [online_player_api](/plugins/online_player_api/readme.md) | \>=1.0.0 |
| [player_ip_logger](/plugins/player_ip_logger/readme.md) | \>=1.1.0 |
| [whitelist_api](/plugins/whitelist_api/readme.md) | \>=1.3.0 |
| [mg_events](/plugins/mg_events/readme.md) | \>=0.2.3 |

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

[![页面浏览量计数](https://badges.toozhao.com/badges/01H98QXADB4DYZBRC2EHSEJ4HW/green.svg)](https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot//) 
[![查看次数起始时间](https://img.shields.io/badge/查看次数统计起始于-2023%2F9%2F2-1?style=flat-square)](https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot//)
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
> 访问腾讯文档查看更详细的说明: https://docs.qq.com/aio/p/sct29j7ammzw142
> 
> 第三方授权文档（编写中）：https://docs.pfingan.com/PF-gugubot/

## 腾讯文档快速导航
### [GUGUbot](https://docs.qq.com/aio/p/sct29j7ammzw142?p=8zf59bKLGJK66HBlVLjqwJ)
1. [前置依赖](https://docs.qq.com/aio/p/sct29j7ammzw142?p=5lMm6oYzWp4nMSHHrcR1DG)
2. [安装（快速开始）](https://docs.qq.com/aio/p/sct29j7ammzw142?p=zdYp7EVd2d04QBQ0FrD7sX)
3. [功能列表](https://docs.qq.com/aio/p/sct29j7ammzw142?p=kKIaQMdRR7IvJ2AMa30Din)
   - [自定义说明](https://docs.qq.com/aio/p/sct29j7ammzw142?p=pEQyDIrFanCo9ErEZZPncf)
4. [配置](https://docs.qq.com/aio/p/sct29j7ammzw142?p=iXyl6g1K1p1dK2rujfGH7u)
5. [疑难解答](https://docs.qq.com/aio/p/sct29j7ammzw142?p=8kJWVjHPK8Zkujhwd73Zbb)
6. [多服互联](https://docs.qq.com/aio/p/sct29j7ammzw142?p=Ply25UKYNFiWqDdNDTLgWY)
7. [开发指南](https://docs.qq.com/aio/p/sct29j7ammzw142?p=EY13Ly9HEWslxTOyB62KdW)
   - [接口](https://docs.qq.com/aio/p/sct29j7ammzw142?p=pTowgV8359jVGjsobNQEst)
8. [贡献](https://docs.qq.com/aio/p/sct29j7ammzw142?p=OreXhO8piOO7Ak7RnpPCMp)
### [CQ-QQ-API](https://docs.qq.com/aio/p/sct29j7ammzw142?p=NJ5GySzVisEJ9xQp7iW8P7)
1. [快速开始](https://docs.qq.com/aio/p/sct29j7ammzw142?p=5PaUIBXxTwyMouazErWqIT)
2. [配置](https://docs.qq.com/aio/p/sct29j7ammzw142?p=vUShdYdligIgQvmxLZu3s8)
3. [群友提供的机器人食用指南](https://docs.qq.com/aio/p/sct29j7ammzw142?p=MgrkYFk9OPpK8wZEY8IeBU)
   - [LiteLoaderQQNT + LLOneBot](https://docs.qq.com/aio/p/sct29j7ammzw142?p=uFoW8O80TsvZ1ccJB7Wxum)
   - [NapCat](https://docs.qq.com/aio/p/sct29j7ammzw142?p=UggIX3zxZcpl4PamYNA1Nd)
4. [开发指南](https://docs.qq.com/aio/p/sct29j7ammzw142?p=kCIVuht8VcP2vDGLqA9VUW)
5. [致谢](https://docs.qq.com/aio/p/sct29j7ammzw142?p=w6BO9iUIonwXPN8xBof94F)

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

- [GUGUbot - 功能列表 - 腾讯文档](https://docs.qq.com/aio/p/sct29j7ammzw142?p=kKIaQMdRR7IvJ2AMa30Din)

## 配置

### 机器人的必要配置
| 配置项 | 默认值 | 说明 |
| - | - | - |
| 正向websocket服务端口 | `8080` | 接收数据上报的端口 |
| 消息上报格式 | CQ码 | 机器人基于CQ码进行解析 |

### 前置cq_qq_api配置

- 请前往：[CQ-QQ-API - 配置 - 腾讯文档](https://docs.qq.com/aio/p/sct29j7ammzw142?p=vUShdYdligIgQvmxLZu3s8)

### GUGUbot机器人配置
> [!IMPORTANT]
> 非常建议看看[默认的配置文件](https://github.com/LoosePrince/PF-GUGUBot/blob/main/config_default.yml)<br>

**QQ相关设置 - 必要项**
- admin_id: 管理员QQ号 默认拥有GUGUbot管理员权限(仅私聊)
- group_id: 聊天转发的群

**QQ相关设置 - 可选项**
- 请前往：[GUGUbot - 配置 - 腾讯文档](https://docs.qq.com/aio/p/sct29j7ammzw142?p=iXyl6g1K1p1dK2rujfGH7u)

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
| [GUGUbot-v1.9.12.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.12) | 1.9.12 | 2025/03/07 06:24:15 | 11.79MB | 104 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.12/GUGUbot-v1.9.12.mcdr) |
| [GUGUbot-v1.9.11.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.11) | 1.9.11 | 2025/02/12 06:54:27 | 11.93MB | 52 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.11/GUGUbot-v1.9.11.mcdr) |
| [GUGUbot-v1.9.10.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.10) | 1.9.10 | 2025/02/11 07:04:25 | 11.93MB | 6 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.10/GUGUbot-v1.9.10.mcdr) |
| [GUGUbot-v1.9.8.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.8) | 1.9.8 | 2025/01/09 06:57:55 | 11.81MB | 128 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.8/GUGUbot-v1.9.8.mcdr) |
| [GUGUbot-v1.9.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.6) | 1.9.6 | 2025/01/06 05:33:39 | 11.81MB | 27 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.6/GUGUbot-v1.9.6.mcdr) |
| [GUGUbot-v1.9.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.5) | 1.9.5 | 2025/01/05 08:22:09 | 11.81MB | 7 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.5/GUGUbot-v1.9.5.mcdr) |
| [GUGUbot-v1.9.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.4) | 1.9.4 | 2025/01/02 05:57:02 | 11.8MB | 37 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.4/GUGUbot-v1.9.4.mcdr) |
| [GUGUbot-v1.9.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.3) | 1.9.3 | 2024/12/22 06:25:08 | 11.8MB | 66 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.3/GUGUbot-v1.9.3.mcdr) |
| [GUGUbot-v1.9.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.2) | 1.9.2 | 2024/12/21 06:11:31 | 11.8MB | 15 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.2/GUGUbot-v1.9.2.mcdr) |
| [GUGUbot-v1.9.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.1) | 1.9.1 | 2024/12/20 07:42:45 | 11.8MB | 23 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.1/GUGUbot-v1.9.1.mcdr) |
| [GUGUbot-v1.9.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.9.0) | 1.9.0 | 2024/12/20 06:08:19 | 11.8MB | 9 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.9.0/GUGUbot-v1.9.0.mcdr) |
| [GUGUbot-v1.8.7.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.7) | 1.8.7 | 2024/12/09 06:32:41 | 11.66MB | 43 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.7/GUGUbot-v1.8.7.mcdr) |
| [GUGUbot-v1.8.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.6) | 1.8.6 | 2024/11/25 16:44:06 | 11.66MB | 53 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.6/GUGUbot-v1.8.6.mcdr) |
| [GUGUbot-v1.8.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.5) | 1.8.5 | 2024/11/25 16:38:10 | 11.66MB | 5 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.5/GUGUbot-v1.8.5.mcdr) |
| [GUGUbot-v1.8.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.4) | 1.8.4 | 2024/11/16 06:43:51 | 11.66MB | 35 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.4/GUGUbot-v1.8.4.mcdr) |
| [GUGUbot-v1.8.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.3) | 1.8.3 | 2024/11/01 00:25:26 | 11.66MB | 32 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.3/GUGUbot-v1.8.3.mcdr) |
| [GUGUbot-v1.8.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.2) | 1.8.2 | 2024/10/28 02:31:41 | 11.66MB | 15 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.2/GUGUbot-v1.8.2.mcdr) |
| [GUGUbot-v1.8.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.1) | 1.8.1 | 2024/10/26 21:17:31 | 11.66MB | 9 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.1/GUGUbot-v1.8.1.mcdr) |
| [GUGUbot-v1.8.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.0) | 1.8.0 | 2024/10/20 19:33:18 | 11.66MB | 19 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.0/GUGUbot-v1.8.0.mcdr) |
| [GUGUbot-v1.7.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.5) | 1.7.5 | 2024/10/05 05:12:29 | 11.66MB | 22 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.5/GUGUbot-v1.7.5.mcdr) |
| [GUGUbot-v1.7.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.4) | 1.7.4 | 2024/10/04 02:06:53 | 11.66MB | 7 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.4/GUGUbot-v1.7.4.mcdr) |
| [GUGUbot-v1.7.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.3) | 1.7.3 | 2024/10/03 17:42:45 | 11.66MB | 9 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.3/GUGUbot-v1.7.3.mcdr) |
| [GUGUbot-v1.7.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.2) | 1.7.2 | 2024/09/22 16:20:10 | 11.66MB | 57 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.2/GUGUbot-v1.7.2.mcdr) |
| [GUGUbot-v1.7.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.1) | 1.7.1 | 2024/09/22 14:12:52 | 11.66MB | 9 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.1/GUGUbot-v1.7.1.mcdr) |
| [GUGUbot-v1.1.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.6) | 1.1.6 | 2024/09/18 17:55:55 | 11.65MB | 22 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.6/GUGUbot-v1.1.6.mcdr) |
| [GUGUbot-v1.1.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.5) | 1.1.5 | 2024/09/17 04:47:21 | 11.65MB | 15 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.5/GUGUbot-v1.1.5.mcdr) |
| [GUGUbot-v1.1.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.4) | 1.1.4 | 2024/08/27 05:26:45 | 11.65MB | 79 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.4/GUGUbot-v1.1.4.mcdr) |
| [GUGUbot-v1.1.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.2) | 1.1.2 | 2024/08/18 00:31:47 | 11.65MB | 37 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.2/GUGUbot-v1.1.2.mcdr) |
| [GUGUbot-v1.1.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.1) | 1.1.1 | 2024/08/17 14:05:21 | 11.65MB | 5 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.1/GUGUbot-v1.1.1.mcdr) |
| [GUGUbot-v1.1.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.0) | 1.1.0 | 2024/08/14 16:02:43 | 11.65MB | 13 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.0/GUGUbot-v1.1.0.mcdr) |
| [GUGUbot-v1.0.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.6) | 1.0.6 | 2024/08/13 15:55:00 | 11.65MB | 14 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.6/GUGUbot-v1.0.6.mcdr) |
| [GUGUbot.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.5) | 1.0.5 | 2023/08/30 11:34:34 | 23.25MB | 16 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.5/GUGUbot.mcdr) |
| [GUGUbot.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.4) | 1.0.4 | 2023/08/29 05:25:28 | 23.25MB | 9 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.4/GUGUbot.mcdr) |

