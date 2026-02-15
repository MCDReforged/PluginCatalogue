**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## im_share_chat

### Basic Information

- Plugin ID: `im_share_chat`
- Plugin Name: ImShareChat
- Version: 0.1.0
  - Metadata version: 0.1.0
  - Release version: 0.1.0
- Total downloads: 237
- Authors: [Mooling0602](https://github.com/Mooling0602), [XueK66](https://github.com/XueK66)
- Repository: https://github.com/Mooling0602/ImShareChat
- Repository plugin page: https://github.com/Mooling0602/ImShareChat/tree/main
- Labels: [`Tool`](/labels/tool/readme.md), [`Information`](/labels/information/readme.md)
- Description: A cross-platform instant message sharing plugin for MCDReforged.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |
| [im_api](/plugins/im_api/readme.md) | \>=0.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# ImShareChat
一个跨平台共享即时消息的MCDReforged插件。

## 前置
**im_api>0.1.0**或[**ImAPI-MatrixDriver**](https://github.com/Mooling0602/ImAPI-MatrixDriver)

用于连接到外部IM平台或其他MCDReforged实例。

后续随着插件功能的增加和开发需要，将会引入更多前置。

## 用法
在配置文件设置你想共享消息的目标平台的频道（群聊/房间）识别信息，例如QQ群号码或者Matrix房间ID。

关于详细的配置和使用文档，请参见[Docs](https://github.com/Mooling0602/ImShareChat/tree/main/DOCS.md)。

## 警告
此插件不考虑兼容其他同类插件（消息互通类插件），包括仅支持单外部IM平台的插件，如果同时使用可能会出现消息重复等体验问题，请选择弃用此插件或其他同类插件，或者自行解决！

此类问题不要在Issues或者其他任何渠道进行反馈！

## 功能
### 已实现
- 平台之间消息双向同步
- 服务器状态同步到外部IM平台
- 可配置消息转发格式
> 包括服务器启停消息、玩家上下线消息、聊天消息
- 同步玩家死亡和达成进度时的消息到外部IM平台（需要额外安装MoreGameEvents后启用相关配置）
- 执行服务器和MCDR命令，且支持权限配置

### 开发中
- 可配置消息转发方向
> 高级配置功能，预计将于v0.1.x版本更新
- 玩家上线时同步其IP归属地到外部IM平台
- 支持跨服互通游戏消息
> 需要上游提供相关的API支持，目前没有明确的预期时间

### 未计划
- 基于人工智能接口的服务
> 接受PR
- 私聊功能
> 不接受PR
- 推送功能（Webhook等）
> 接受PR
- 外部IM平台频道（群聊/房间）内成员管理功能
> 包括邀请/同意他人加入和踢出指定成员，不接受PR
- 面板（网页、GUI等）支持
> 不接受PR
- 其他

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ImShareChat-v0.1.0.mcdr](https://github.com/Mooling0602/ImShareChat/releases/tag/0.1.0) | 0.1.0 | 2025/06/07 08:26:28 | 11.13KB | 46 | [Download](https://github.com/Mooling0602/ImShareChat/releases/download/0.1.0/ImShareChat-v0.1.0.mcdr) |
| [ImShareChat-v0.0.6.mcdr](https://github.com/Mooling0602/ImShareChat/releases/tag/0.0.6) | 0.0.6 | 2025/04/24 18:06:37 | 6.99KB | 33 | [Download](https://github.com/Mooling0602/ImShareChat/releases/download/0.0.6/ImShareChat-v0.0.6.mcdr) |
| [ImShareChat-v0.0.5.mcdr](https://github.com/Mooling0602/ImShareChat/releases/tag/0.0.5) | 0.0.5 | 2025/04/03 10:18:47 | 6.94KB | 40 | [Download](https://github.com/Mooling0602/ImShareChat/releases/download/0.0.5/ImShareChat-v0.0.5.mcdr) |
| [ImShareChat-v0.0.4.mcdr](https://github.com/Mooling0602/ImShareChat/releases/tag/0.0.4) | 0.0.4 | 2025/04/03 09:41:30 | 6.94KB | 26 | [Download](https://github.com/Mooling0602/ImShareChat/releases/download/0.0.4/ImShareChat-v0.0.4.mcdr) |
| [ImShareChat-v0.0.3.mcdr](https://github.com/Mooling0602/ImShareChat/releases/tag/0.0.3) | 0.0.3 | 2025/03/04 12:20:44 | 6.56KB | 34 | [Download](https://github.com/Mooling0602/ImShareChat/releases/download/0.0.3/ImShareChat-v0.0.3.mcdr) |
| [ImShareChat-v0.0.2.mcdr](https://github.com/Mooling0602/ImShareChat/releases/tag/0.0.2) | 0.0.2 | 2025/02/10 06:33:48 | 5.03KB | 29 | [Download](https://github.com/Mooling0602/ImShareChat/releases/download/0.0.2/ImShareChat-v0.0.2.mcdr) |
| [ImShareChat-v0.0.1.mcdr](https://github.com/Mooling0602/ImShareChat/releases/tag/0.0.1) | 0.0.1 | 2025/02/10 04:30:16 | 4.36KB | 29 | [Download](https://github.com/Mooling0602/ImShareChat/releases/download/0.0.1/ImShareChat-v0.0.1.mcdr) |

