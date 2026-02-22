[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## guguwebui

### 基本信息

- 插件 ID: `guguwebui`
- 插件名: GUGU WebUI
- 版本: 1.7.9
  - 元数据版本: 1.7.9
  - 发布版本: 1.7.9
- 总下载量: 2642
- 作者: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- 仓库: https://github.com/PFingan-Code/PF-MCDR-WebUI
- 仓库插件页: https://github.com/PFingan-Code/PF-MCDR-WebUI/tree/main/src
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 通过webui来管理所有插件、MCDR配置、在线安装、终端等多种功能

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# PF-MCDR-WebUI

为 MCDReforged (MCDR) 开发的现代化、功能丰富的 Web 管理界面插件。

[![仓库大小](https://img.shields.io/github/repo-size/PFingan-Code/PF-MCDR-WebUI?style=flat-square&label=仓库占用)](https://github.com/PFingan-Code/PF-MCDR-WebUI/tree/main/src//)
[![最新版](https://img.shields.io/github/v/release/PFingan-Code/PF-MCDR-WebUI?style=flat-square&label=最新版)](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/latest/)
[![议题](https://img.shields.io/github/issues/PFingan-Code/PF-MCDR-WebUI?style=flat-square&label=Issues)](https://github.com/PFingan-Code/PF-MCDR-WebUI/issues)
[![已关闭issues](https://img.shields.io/github/issues-closed/PFingan-Code/PF-MCDR-WebUI?style=flat-square&label=已关闭%20Issues)](https://github.com/PFingan-Code/PF-MCDR-WebUI/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/PFingan-Code/PF-MCDR-WebUI/total?style=flat-square&label=下载量)](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases)

> [!TIP]
> 
> **文档中心**: [点击访问](https://pf-doc.pfingan.com/main/#PF-webui/)

---

## ✨ 主要功能

### 📦 插件与依赖管理
- **本地管理**: 实时列出插件状态，支持启动、停止、重载及一键更新。
- **在线仓库**: 集成插件安装管理器 (PIM)，支持多仓库搜索、安装、卸载及版本切换。
- **环境维护**: 自 v1.4.0 起自动处理 Python 依赖 (pip)。

### ⚙️ 配置与表单系统
- **动态表单**: 自动将 `json`、`yaml` 配置文件解析为直观的可视化表单。
- **在线编辑器**: 内置 Web 代码编辑器，支持直接修改原始配置文件。

### 💻 运维与监控
- **实时终端**: 提供支持 RCON 反馈和历史记录的服务器控制台。
- **AI 辅助分析**: 集成 AI 接口，支持自动化日志分析与故障排查。
- **兼容性增强**: 联动 `player_ip_logger` 显示详细在线玩家状态与验证信息。

### 💬 社交与 UI
- **公开聊天页**: 游戏消息实时同步，支持玩家通过验证后在 Web 端交互。
- **个性化体验**: 支持浅色与深色主题无缝切换。

---

## 🚀 快速开始

### 安装与更新
1. 从 [Releases](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases) 下载最新的 `.mcdr` 文件。
2. 放入 MCDR 的 `plugins` 文件夹。
3. 重启 MCDR 或在控制台执行 `!!MCDR admin reload all`。

> [!IMPORTANT]
> **升级提示 (v1.3.0+和v1.7.0+)**: 如果从旧版本升级，请删除 `guguwebui_static` 文件夹内文件和文件夹，仅保留 `db.json`。
> **数据说明**: 重载本插件会同步更新静态资源。若手动修改过插件目录内的文件，请注意备份。

### 账户初始化
在游戏内使用以下指令管理 WebUI 访问权限：
- **创建管理员**: `!!webui create <用户名> <密码>`
- **修改密码**: `!!webui change <用户名> <旧密码> <新密码>`
- **临时登录**: `!!webui temp` (生成一次性授权链接)

#### GUGUBot 集成（可选）
如果已安装 [GUGUBot](https://github.com/PFingan-Code/GUGUBot) 插件，可通过 QQ 使用以下命令：
- **显示帮助**: `#webui` （命令前缀根据 GUGUBot 命令前缀配置变化）
- **设置密码**: `#webui 设置密码 <密码>` - 设置或更新 WebUI 账户密码（用户名使用QQ号）
- **获取临时码**: `#webui 临时码` - 生成临时登录码（15分钟有效，自动关联QQ号）

> [!NOTE]
> GUGUBot 命令需要在 QQ 中对机器人发送（私聊机器人），且需要管理员权限。临时码会自动关联您的QQ号，登录时将显示QQ号作为用户名。

### 公开聊天页使用流程
1. 访问 `/chat` 路径。
2. 点击生成验证码，并在游戏内发送 `!!webui verify <验证码>`。
3. 回到页面设置独立密码并登录。

---

## 🛠️ 开发者指南

### 事件系统
WebUI 提供事件分发机制，允许其他插件监听或向 WebUI 发送消息：
- 核心事件: `webui.chat_message_sent`
- 详细参考: [WebUI 事件系统文档](https://github.com/PFingan-Code/PF-MCDR-WebUI/tree/main/src/docs/WebUI事件系统.md)
- 示例代码: [examples/](https://github.com/PFingan-Code/PF-MCDR-WebUI/tree/main/src/examples/)

### 框架兼容
- **fastapi_mcdr**: 检测到该插件时，WebUI 将自动挂载为其子应用。
- **PIM (内置)**: 已集成插件安装管理功能，亦可根据需要安装到外部。

---

## ❓ 常见问题 (FAQ)

**Q: 为什么要开发这个插件？** <br>
A: 因为我乐意。

**Q: 会支持MC服务器管理的功能吗？如模组管理、玩家管理、白名单等等……** <br>
A: 并不会深入涉及管理MC服务器，如有这方面的需求请查询MC服务器面板，仅可能会支持很小一部分，例如终端、重启服务器，更多的不在我们的范畴中。

**Q: 可以加入开发吗？** <br>
A: 当然可以，您可以提交 [pr](https://github.com/PFingan-Code/PF-MCDR-WebUI/pulls) 或者参与交流来参与开发。

**Q: 会支持我的语言吗？** <br>
A: 我只会中文，你要是愿意可以参与，目前已有中文（zh-CN）和英文（en-US），在 [i18n/locales 文件夹](https://github.com/PFingan-Code/PF-MCDR-WebUI/tree/main/src/guguwebui/frontend/src/i18n/locales)。

**Q: 如何获取正在测试的开发版？** <br>
A: 前往 [Releases页面](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases?q=beta+build) 下载最新的预发布版本（Pre-release），这些版本会在每次代码更新后自动生成。或者你也可以自己打包`src`中的文件到`zip`，修改后缀为`.mcdr`。

**Q: 我有个插件，我觉得很适合WebUI，可以作为WebUI的前置吗？** <br>
A: WebUI不打算使用任何插件前置，如果有好的方案我们会考虑直接加入WebUI并在关于页感谢贡献。

**Q: WebUI中提到的[PIM插件](https://github.com/PFingan-Code/PF-MCDR-WebUI/tree/main/src/guguwebui/PIM) 是什么？** <br>
A: [PIM插件](https://github.com/PFingan-Code/PF-MCDR-WebUI/tree/main/src/guguwebui/PIM) 是WebUI的插件安装管理器，它可以帮助您安装、卸载、更新插件，并且可以查看插件信息。请注意，这并非MCDR内置的PIM，这是两个不同的东西。

**Q: 对于开发者如何提供配置文件以支持多语言（中文、英文等）描述？** <br>
A: 查看 [插件兼容](https://pf-doc.pfingan.com/main/#/PF-webui/开发/插件兼容) 文档。

---

## 🤝 贡献与致谢

| 贡献人                                                                        | 说明                   |
| -------------------------------------------------------------------------- | -------------------- |
| [树梢 (LoosePrince)](https://github.com/LoosePrince)                         | 功能设计、文档编写、Web设计、前端编写 |
| [雪开 (XueK66)](https://github.com/XueK66)                                   | 代码开发、维护、功能设计         |
| 见 [贡献者](https://github.com/PFingan-Code/PF-MCDR-WebUI/graphs/contributors) | 贡献者                  |

| 贡献项目                                                                 | 功能                            | 备注                                   |
| -------------------------------------------------------------------- | ----------------------------- | ------------------------------------ |
| [MCDR 插件仓库](https://mcdreforged.com/zh-CN/plugins)                   | 插件生态                          | 提供了丰富的 MCDR 插件生态，是本项目功能的基础           |
| [MC-Server-Info](https://github.com/Spark-Code-China/MC-Server-Info) | Minecraft 服务器信息查询 [v1.6.8及以下] | 用于获取服务器状态与玩家信息的基础实现（仓库被作者删除）         |
| [MCDReforged](https://mcdreforged.com/)                              | MCDR 本体                       | 本插件所依赖的运行平台                          |
| [WolfgangFahl](https://github.com/zauberzeug/nicegui/issues/1956)    | uvicorn 线程化                   | 参考了其在 uvicorn 线程化运行方面的实现思路           |
| [Minecraft Wiki（文本组件）](https://zh.minecraft.wiki/w/文本组件)             | 文本组件格式规范                      | RText 解析器所依据的格式规范                    |
| [mcstatus](https://github.com/py-mine/mcstatus)                      | Minecraft 服务器状态查询             | 用于查询 Minecraft Java 版服务器状态的 Python 库 |

| 特别鸣谢 | 说明      |
| ---- | ------- |
| 反馈者  | 感谢你们的反馈 |

## 有BUG或是新的IDEA

如果需要更多联动或提交想法和问题请提交 [issues](https://github.com/PFingan-Code/PF-MCDR-WebUI/issues) 或 QQ [树梢 (1377820366)](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 提交！ <br />
如需要帮助或者交流请通过 QQ群 [726741344](https://qm.qq.com/q/TqmRHmTmcU) 进行询问或者交流 <br />
视情况添加，请勿联系他人。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [guguweb_v1.7.9.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.9) | 1.7.9 | 2026/02/20 09:55:38 | 571.96KB | 20 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.9/guguweb_v1.7.9.mcdr) |
| [guguweb_v1.7.8.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.8) | 1.7.8 | 2026/02/17 05:56:25 | 564.43KB | 32 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.8/guguweb_v1.7.8.mcdr) |
| [guguweb_v1.7.7.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.7) | 1.7.7 | 2026/02/11 13:20:39 | 575.9KB | 52 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.7/guguweb_v1.7.7.mcdr) |
| [guguweb_v1.7.6.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.6) | 1.7.6 | 2026/02/08 13:53:14 | 575.78KB | 28 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.6/guguweb_v1.7.6.mcdr) |
| [guguweb_v1.7.5.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.5) | 1.7.5 | 2026/02/08 11:15:08 | 575.78KB | 2 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.5/guguweb_v1.7.5.mcdr) |
| [guguweb_v1.7.4.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.4) | 1.7.4 | 2026/02/04 14:32:44 | 573.81KB | 28 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.4/guguweb_v1.7.4.mcdr) |
| [guguwebui_v1.7.3.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.3) | 1.7.3 | 2026/02/03 15:07:24 | 557.7KB | 6 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.3/guguwebui_v1.7.3.mcdr) |
| [guguweb_v1.7.2.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.2) | 1.7.2 | 2026/02/03 10:58:29 | 574.74KB | 4 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.2/guguweb_v1.7.2.mcdr) |
| [guguweb_v1.7.1.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.1) | 1.7.1 | 2026/01/31 12:53:21 | 597.49KB | 17 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.1/guguweb_v1.7.1.mcdr) |
| [guguweb_v1.7.0.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.7.0) | 1.7.0 | 2026/01/30 14:34:59 | 597.08KB | 19 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.7.0/guguweb_v1.7.0.mcdr) |
| [guguweb_v1.6.12.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.12) | 1.6.12 | 2026/01/16 13:56:17 | 371.22KB | 64 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.12/guguweb_v1.6.12.mcdr) |
| [guguweb_v1.6.11.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.11) | 1.6.11 | 2025/11/16 14:53:47 | 370.82KB | 201 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.11/guguweb_v1.6.11.mcdr) |
| [guguweb_v1.6.10.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.10) | 1.6.10 | 2025/11/05 10:33:08 | 370.65KB | 38 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.10/guguweb_v1.6.10.mcdr) |
| [guguweb_v1.3.9.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.9) | 1.6.9 | 2025/10/22 09:50:19 | 370.64KB | 66 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.9/guguweb_v1.3.9.mcdr) |
| [guguweb_v1.6.8.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.8) | 1.6.8 | 2025/09/27 08:05:31 | 369.29KB | 109 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.8/guguweb_v1.6.8.mcdr) |
| [guguweb_v1.6.7.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.7) | 1.6.7 | 2025/09/17 10:10:43 | 352.49KB | 68 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.7/guguweb_v1.6.7.mcdr) |
| [guguweb_v1.6.6.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.6) | 1.6.6 | 2025/08/29 06:02:25 | 349.66KB | 98 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.6/guguweb_v1.6.6.mcdr) |
| [guguweb_v1.6.5.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.5) | 1.6.5 | 2025/08/28 14:28:46 | 339.54KB | 39 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.5/guguweb_v1.6.5.mcdr) |
| [guguweb_v1.6.4.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.4) | 1.6.4 | 2025/08/27 01:06:23 | 339.26KB | 41 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.4/guguweb_v1.6.4.mcdr) |
| [guguweb_v1.6.3.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.3) | 1.6.3 | 2025/08/23 01:01:31 | 337.82KB | 50 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.3/guguweb_v1.6.3.mcdr) |
| [guguweb_v1.6.2.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.2) | 1.6.2 | 2025/08/20 06:15:12 | 336.64KB | 53 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.2/guguweb_v1.6.2.mcdr) |
| [guguweb_v1.6.1.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.1) | 1.6.1 | 2025/08/18 16:47:25 | 328.93KB | 46 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.1/guguweb_v1.6.1.mcdr) |
| [guguweb_v1.6.0.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.6.0) | 1.6.0 | 2025/08/18 10:37:24 | 324.18KB | 35 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.6.0/guguweb_v1.6.0.mcdr) |
| [guguwebui-v1.5.1.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.5.1) | 1.5.1 | 2025/08/12 07:18:35 | 300.79KB | 64 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.5.1/guguwebui-v1.5.1.mcdr) |
| [guguwebui-v1.5.0.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.5.0) | 1.5.0 | 2025/08/12 04:03:44 | 298.85KB | 34 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.5.0/guguwebui-v1.5.0.mcdr) |
| [guguwebui-v1.4.3.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.4.3) | 1.4.3 | 2025/08/01 15:51:17 | 264.46KB | 81 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.4.3/guguwebui-v1.4.3.mcdr) |
| [guguwebui-v1.4.2.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.4.2) | 1.4.2 | 2025/07/11 11:03:57 | 255.01KB | 103 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.4.2/guguwebui-v1.4.2.mcdr) |
| [guguwebui-v1.4.1.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.4.1) | 1.4.1 | 2025/06/04 07:02:07 | 252.19KB | 152 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.4.1/guguwebui-v1.4.1.mcdr) |
| [guguwebui-v1.4.0.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.4.0) | 1.4.0 | 2025/06/04 06:23:13 | 252.55KB | 34 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.4.0/guguwebui-v1.4.0.mcdr) |
| [guguwebui-v1.3.10.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.10) | 1.3.10 | 2025/06/02 11:30:47 | 420.91KB | 34 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.10/guguwebui-v1.3.10.mcdr) |
| [guguwebui-v1.3.9.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.9) | 1.3.9 | 2025/05/19 11:54:00 | 254.32KB | 94 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.9/guguwebui-v1.3.9.mcdr) |
| [guguwebui-v1.3.8.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.8) | 1.3.8 | 2025/05/13 11:10:29 | 248.9KB | 84 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.8/guguwebui-v1.3.8.mcdr) |
| [guguwebui-v1.3.7.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.7) | 1.3.7 | 2025/05/05 09:15:31 | 247.46KB | 63 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.7/guguwebui-v1.3.7.mcdr) |
| [guguwebui-v1.3.6.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.6) | 1.3.6 | 2025/05/04 14:45:18 | 241.03KB | 35 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.6/guguwebui-v1.3.6.mcdr) |
| [guguwebui-v1.3.5.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.5) | 1.3.5 | 2025/05/04 06:01:21 | 226.55KB | 46 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.5/guguwebui-v1.3.5.mcdr) |
| [guguwebui-v1.3.4.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.4) | 1.3.4 | 2025/04/23 08:46:34 | 223.36KB | 83 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.4/guguwebui-v1.3.4.mcdr) |
| [guguwebui-v1.3.3.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.3) | 1.3.3 | 2025/04/15 10:05:53 | 197.07KB | 59 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.3/guguwebui-v1.3.3.mcdr) |
| [guguwebui-v1.3.2.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.2) | 1.3.2 | 2025/04/08 01:04:38 | 187.58KB | 67 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.2/guguwebui-v1.3.2.mcdr) |
| [guguwebui-v1.3.1.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.1) | 1.3.1 | 2025/04/07 09:01:56 | 179.37KB | 38 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.1/guguwebui-v1.3.1.mcdr) |
| [guguwebui-v1.3.0.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.3.0) | 1.3.0 | 2025/04/04 05:44:22 | 131.38KB | 40 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.3.0/guguwebui-v1.3.0.mcdr) |
| [guguwebui-v1.2.5.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.2.5) | 1.2.5 | 2025/03/12 00:44:19 | 107.53KB | 78 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.2.5/guguwebui-v1.2.5.mcdr) |
| [guguwebui-v1.2.4.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.2.4) | 1.2.4 | 2025/01/25 12:56:01 | 105.43KB | 42 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.2.4/guguwebui-v1.2.4.mcdr) |
| [guguwebui-v1.2.3.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.2.3) | 1.2.3 | 2025/01/22 15:03:59 | 97.76KB | 68 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.2.3/guguwebui-v1.2.3.mcdr) |
| [guguwebui-v1.2.2.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.2.2) | 1.2.2 | 2025/01/21 10:46:29 | 92.95KB | 41 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.2.2/guguwebui-v1.2.2.mcdr) |
| [guguwebui-v1.2.0.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.2.0) | 1.2.0 | 2025/01/19 12:34:03 | 123.17KB | 45 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.2.0/guguwebui-v1.2.0.mcdr) |
| [guguwebui-v1.1.0.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.1.0) | 1.1.0 | 2025/01/18 11:07:05 | 89.12KB | 36 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.1.0/guguwebui-v1.1.0.mcdr) |
| [guguwebui-v1.0.0-beta.mcdr](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/tag/v1.0.0) | 1.0.0 | 2024/11/12 06:31:18 | 112.38KB | 105 | [下载](https://github.com/PFingan-Code/PF-MCDR-WebUI/releases/download/v1.0.0/guguwebui-v1.0.0-beta.mcdr) |

