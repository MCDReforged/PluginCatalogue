[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## easybot_mcdr

### 基本信息

- 插件 ID: `easybot_mcdr`
- 插件名: EasyBot
- 版本: 1.2.5
  - 元数据版本: 1.2.5
  - 发布版本: 1.2.5
- 总下载量: 1163
- 作者: [MiuxuE](https://github.com/easybot-team)
- 仓库: https://github.com/easybot-team/easybot-mcdr
- 仓库插件页: https://github.com/easybot-team/easybot-mcdr/tree/main
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一款集消息同步、自定义命令、绑定管理、高级权限控制、群组互动、自定义模板支持以及自定义插件支持等全方位功能于一体的服务器管理工具，全方位优化游戏社区体验!

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [websockets](https://pypi.org/project/websockets) | \>=14.2 |
| [requests](https://pypi.org/project/requests) | \>=2.32.3 |

```
pip install "websockets>=14.2" "requests>=2.32.3"
```

### 介绍

# EasyBot-MCDR

> 一款集消息同步、绑定管理、群组互动等功能于一体的 MCDR 服务器管理插件，全方位优化游戏社区体验。

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![MCDR](https://img.shields.io/badge/MCDR-%3E%3D2.14-green.svg)](https://github.com/Fallen-Breath/MCDReforged)
[![Python](https://img.shields.io/badge/Python-3.12+-yellow.svg)](https://www.python.org/)

## 简介

EasyBot-MCDR 通过 WebSocket 将 Minecraft 服务器与 EasyBot 中心服务器连接，实现游戏内消息与外部社交平台（如 QQ 群、管理面板）的双向同步。

**服务端 → 平台**: 转发游戏内聊天、玩家进出、死亡事件、服务器状态
**平台 → 服务端**: 接收指令发送消息、踢人、执行命令、管理绑定、跨服通信

## 功能特性

### 消息同步
- 游戏内聊天实时同步至社交平台，反之亦然
- 支持富文本渲染：文本、图片、@提及、表情、文件、回复
- 聊天图片支持：安装 [ChatImage](https://github.com/kitUIN/ChatImage) 客户端模组后，群聊图片可在游戏内直接预览
- 跨服消息转发（`!!say` / `!!esay`）

### 绑定系统
- 玩家通过 `!!bind` 命令将 Minecraft 账号与社交平台账号绑定
- 支持绑定/解绑时自动执行命令
- 支持绑定时自动加入白名单、解绑时自动移除并踢出

### 玩家事件
- 进入/退出/死亡通知同步至平台
- 机器人（假玩家）名称前缀过滤
- @提及时触发命令与音效

### 远程管理
- 平台远程执行服务器命令（通过 RCON）
- 远程踢出玩家
- PlaceholderAPI 变量解析（部分支持）

### 服务器适配
- 自动兼容 Forge / Fabric / Spigot / Paper / Vanilla 服务端日志格式
- 自动配置 RCON（检测、生成密码、写入配置）
- 在线/离线模式均支持，自动生成离线 UUID

### 其他
- 配置热重载（`!!ez reload`）

## 环境要求

| 依赖            | 版本                                                 |
| ------------- | -------------------------------------------------- |
| Python        | 3.12+                                              |
| MCDReforged   | >= 2.14                                            |
| Minecraft 服务端 | 原版 / CraftBukkit / Spigot / Paper / Fabric / Forge |

## 安装

1. 安装 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)
2. 下载本插件，放入 MCDR 的 `plugins/` 目录
3. 安装 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 重启 MCDR

## 快速开始

1. 启动 MCDR 后，编辑 `config/easybot_mcdr/config.json`：
   ```json
   {
     "token": "你的认证 Token",
     "ws": "ws://你的EasyBot服务器:26990/bridge",
     "server_name": "我的服务器"
   }
   ```
2. 在游戏内使用 `!!bind` 开始绑定流程
3. 在社交平台输入绑定码完成绑定

详细文档请查看：[在线文档](https://docs.inectar.cn/docs/easybot/quick_start/plugin/mcdr/install_mcdr)

## 命令

| 命令                         | 说明       | 权限   |
| -------------------------- | -------- | ---- |
| `!!bind` / `!!ez bind`     | 绑定社交平台账号 | 所有玩家 |
| `!!unbind` / `!!ez unbind` | 解绑账号     | 所有玩家 |
| `!!ez reload`              | 重载配置     | OP   |

## 配置说明

配置文件路径：`config/easybot_mcdr/config.json`

### 基础配置

| 字段                   | 类型     | 默认值                             | 说明                    |
| -------------------- | ------ | ------------------------------- | --------------------- |
| `token`              | string | `""`                            | EasyBot 中心服务器认证 Token |
| `ws`                 | string | `"ws://localhost:26990/bridge"` | WebSocket 服务地址        |
| `server_name`        | string | `"server_name"`                 | 服务器标识名                |
| `debug`              | bool   | `false`                         | 开启调试日志                |
| `kick_delay_seconds` | int    | `5`                             | 未绑定玩家踢出延迟（秒）          |
| `handler.enabled`    | bool   | `true`                          | 启用自定义日志处理器            |
| `enable_white_list`  | bool   | `true`                          | 启用白名单联动               |

### 消息同步

| 字段                                 | 类型   | 默认值    | 说明            |
| ---------------------------------- | ---- | ------ | ------------- |
| `message_sync.ignore_mcdr_command` | bool | `true` | 同步时忽略 `!!` 命令 |

### 绑定事件

| 字段                                  | 类型   | 说明                                           |
| ----------------------------------- | ---- | -------------------------------------------- |
| `events.bind_success.exec_command`  | bool | 绑定成功时执行命令                                    |
| `events.bind_success.add_whitelist` | bool | 绑定成功时加入白名单                                   |
| `events.bind_success.comamnds`      | list | 绑定成功执行的命令列表（支持 `#player` `#name` `#account`） |
| `events.un_bind.kick`               | bool | 解绑时踢出玩家                                      |
| `events.un_bind.remove_white_list`  | bool | 解绑时移除白名单                                     |
| `events.un_bind.exec_command`       | bool | 解绑时执行命令                                      |
| `events.un_bind.comamnds`           | list | 解绑时执行的命令列表                                   |

### @提及事件

| 字段                                       | 类型     | 说明                    |
| ---------------------------------------- | ------ | --------------------- |
| `events.message.on_at.exec_command`      | bool   | 被@时执行命令               |
| `events.message.on_at.comamnds`          | list   | 执行的命令列表（支持 `#player`） |
| `events.message.on_at.sound.play_sound`  | bool   | 被@时播放音效               |
| `events.message.on_at.sound.run`         | string | 音效命令（支持 `#player`）    |
| `events.message.on_at.sound.count`       | int    | 播放次数                  |
| `events.message.on_at.sound.interval_ms` | int    | 播放间隔（毫秒）              |

### 机器人过滤

| 字段                    | 类型   | 默认值                      | 说明          |
| --------------------- | ---- | ------------------------ | ----------- |
| `bot_filter.enabled`  | bool | `true`                   | 启用假玩家过滤     |
| `bot_filter.prefixes` | list | `["Bot_","BOT_","bot_"]` | 识别为机器人的名称前缀 |

### 图片上传（暂不可用）

启用后，QQ 群中的图片将在游戏内通过 [ChatImage](https://github.com/kitUIN/ChatImage) 模组渲染。

| 字段                           | 类型     | 默认值     | 说明                                              |
| ---------------------------- | ------ | ------- | ----------------------------------------------- |
| `image_upload.enabled`       | bool   | `false` | 启用图片上传                                          |
| `image_upload.imgbb_api_key` | string | `""`    | [imgbb](https://api.imgbb.com/) API Key（免费注册获取） |

> 未配置 imgbb API Key 时，将自动启动本地 HTTP 图片服务器（仅限局域网访问）。

## 兼容性

`EasyBot-MCDR` 是 `EasyBot` 插件的 MCDR 分支，与 `EasyBot-Bukkit` 功能有部分差异：

| 特性             | MCDR 支持 | 说明                                                                                         |
| -------------- | :-----: | ------------------------------------------------------------------------------------------ |
| 消息同步           |    ✅    |                                                                                            |
| 进入退出通知         |    ✅    |                                                                                            |
| 强制绑定           |    ✅    |                                                                                            |
| 命令绑定账号         |    ✅    |                                                                                            |
| 命令模式消息同步       |    ✅    |                                                                                            |
| 热重载            |    ✅    |                                                                                            |
| 执行命令           |    ✅    |                                                                                            |
| 绑定时执行命令        |    ✅    |                                                                                            |
| 联动原版白名单        |    ✅    |                                                                                            |
| 解绑时执行命令        |    ✅    |                                                                                            |
| 死亡同步           |   :x:   | 不同服务端实现原理不同，无法稳定判断死亡原因                                                                     |
| PlaceholderAPI |   ⚠️    | Bukkit 服务端通过 RCON 调用完整 PAPI，非 Bukkit 支持 `%player_name%`、`%player_uuid%`、`%player_ip%` 本地替换 |

## 开发

```
Python:  3.12.8
MCDR:    2.14.5
```

## 许可证

[GPL-3.0](https://github.com/easybot-team/easybot-mcdr/tree/main/LICENSE)

## 作者

- [LBY123165](https://github.com/LBY123165)
- [MiuxuE](https://github.com/MiuxuE)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [EasyBot-v1.2.5.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.2.5) | 1.2.5 | 2026/06/14 08:43:16 | 56.09KB | 69 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.2.5/EasyBot-v1.2.5.mcdr) |
| [EasyBot-MCDR-v1.2.1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.2.1) | 1.2.1 | 2026/01/01 03:00:34 | 40.01KB | 168 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.2.1/EasyBot-MCDR-v1.2.1.mcdr) |
| [EasyBot-v1.2.0-release.1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.2.0-release.1) | 1.2.0-release.1 | 2025/12/06 13:16:49 | 32.59KB | 89 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.2.0-release.1/EasyBot-v1.2.0-release.1.mcdr) |
| [EasyBot-v1.1.7-release.2.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.7-release.2) | 1.1.7-release.2 | 2025/11/22 10:30:17 | 31.05KB | 32 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.7-release.2/EasyBot-v1.1.7-release.2.mcdr) |
| [EasyBot-v1.1.7-release.1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.7-release.1) | 1.1.7-release.1 | 2025/11/22 08:10:50 | 30.63KB | 13 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.7-release.1/EasyBot-v1.1.7-release.1.mcdr) |
| [EasyBot-MCDR-v1.1.7.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.7) | 1.1.7-release1 | 2025/10/24 14:11:59 | 26.77KB | 114 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.7/EasyBot-MCDR-v1.1.7.mcdr) |
| [EasyBot-MCDR.V1.1.6Fix.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/V1.1.6) | 1.1.6 | 2025/10/01 12:49:06 | 27.26KB | 103 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/V1.1.6/EasyBot-MCDR.V1.1.6Fix.mcdr) |
| [EasyBot-MCDR.V1.1.4.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.4) | 1.1.4 | 2025/07/26 10:44:52 | 25.3KB | 97 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.4/EasyBot-MCDR.V1.1.4.mcdr) |
| [EasyBot-MCDR.V1.1.3pre1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.3-pre1) | 1.1.3 | 2025/06/10 12:06:02 | 24.14KB | 118 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.3-pre1/EasyBot-MCDR.V1.1.3pre1.mcdr) |
| [easybot_mcdr_V1.1.0.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.0) | 1.1.0 | 2025/05/06 12:10:08 | 21.94KB | 94 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.0/easybot_mcdr_V1.1.0.mcdr) |
| [EasyBot-v1.0.4.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.0.4) | 1.0.4 | 2025/03/26 09:17:07 | 19.11KB | 160 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.0.4/EasyBot-v1.0.4.mcdr) |
| [EasyBot-v1.0.3.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.0.3) | 1.0.3 | 2025/03/23 11:44:45 | 17.72KB | 53 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.0.3/EasyBot-v1.0.3.mcdr) |
| [EasyBot-v1.0.2.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.0.2) | 1.0.2 | 2025/03/16 15:59:16 | 17.15KB | 53 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.0.2/EasyBot-v1.0.2.mcdr) |

