[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## guguwebui

### 基本信息

- 插件 ID: `guguwebui`
- 插件名: GUGU WebUI
- 版本: 1.6.8
  - 元数据版本: 1.6.8
  - 发布版本: 1.6.8
- 总下载量: 1679
- 作者: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- 仓库: https://github.com/LoosePrince/PF-MCDR-WebUI
- 仓库插件页: https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src
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

为 MCDR 开发的在线 WebUI 插件

[![仓库大小](https://img.shields.io/github/repo-size/LoosePrince/PF-MCDR-WebUI?style=flat-square&label=仓库占用)](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src//)
[![最新版](https://img.shields.io/github/v/release/LoosePrince/PF-MCDR-WebUI?style=flat-square&label=最新版)](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/latest/)
[![议题](https://img.shields.io/github/issues/LoosePrince/PF-MCDR-WebUI?style=flat-square&label=Issues)](https://github.com/LoosePrince/PF-MCDR-WebUI/issues)
[![已关闭issues](https://img.shields.io/github/issues-closed/LoosePrince/PF-MCDR-WebUI?style=flat-square&label=已关闭%20Issues)](https://github.com/LoosePrince/PF-MCDR-WebUI/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/LoosePrince/PF-MCDR-WebUI/total?style=flat-square&label=下载量)](https://github.com/LoosePrince/PF-MCDR-WebUI/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/LoosePrince/PF-MCDR-WebUI/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/latest)

> [!NOTE]
> 由于 **GUGUbot** 和 **WebUI** 项目庞大，但迄今为止仅有开发者一名，所以我们从现在开始招募有志者加入我们！<br>
> 有意者请加 QQ[1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 或 QQ群[726741344](https://qm.qq.com/q/TqmRHmTmcU)

## 插件说明

WebUI 文档：[WebUI 文档](https://pf-doc.pfingan.com/main/#PF-webui/)

### 演示站

> [!NOTE]
> **演示站地址：** [https://looseprince.github.io/PF-MCDR-WebUI/](https://looseprince.github.io/PF-MCDR-WebUI/)
> 
> **重要说明：** 该演示站仅为UI界面和功能演示，**没有实际功能**。所有操作均为模拟演示，不会对真实的MCDR服务器产生任何影响。如需体验完整功能，请按照下方说明安装到您的MCDR服务器中。

### 主要功能
> 
> 为MCDR提供一个 `在线WebUI管理界面` 和 `MCDR插件管理` 及 `表单配置功能`（可选使用在线编辑器）。

#### pip包管理

#### 本地插件管理

- [x] 列出全部插件
- [x] 一键更新
- [x] 启动插件
- [x] 停止插件
- [x] 重载插件
- [x] 切换插件版本（第三方仓库于1.4.3起支持）
- [x] 插件配置文件的在线编辑器
- [x] 插件配置文件的在线表单

#### 表单配置功能

- [x] **配置修改:** 使用在线表单 **或** 在线编辑器进行配置文件的修改（在 **`所有插件`** 选项卡处修改）。
- [x] **支持的配置:** `yaml` 、 `json` 、 `html`

#### 服务器终端

- [x] 提供服务器命令执行界面
- [x] 支持RCON实时反馈和命令历史记录。

#### AI辅助

- [x] 终端集成DeepSeek AI接口
- [x] 支持日志分析和问题解答，减少您的反复横跳。

#### 主题切换

- [x] 支持`浅色主题`、`深色主题`，默认为浅色，您可以在右上角切换显示模式

#### 在线插件安装仓库

- [x] 提供一个插件安装管理器
- [x] 插件搜索、安装、卸载、更新、查看插件信息。
- [x] 多仓库支持，您可以添加多个仓库，并选择不同的仓库进行插件安装，不过请您注意风险。（v1.3.4）

### 公开聊天页

- 提供一个页面，这样页面会与游戏中的聊天消息同步，并且可以发送消息到游戏内
- 需要独立登录，与后端管理登录不互通
- 端点：`/chat`
- 想要使用此功能需要启用`public_chat_enabled`项

公开聊天页玩家使用流程

1. 访问 `/chat` 页面
2. 生成验证码（第一次）
3. 在游戏内发送 `!!webui verify <验证码>`
4. 回到网页设置密码（设置完会自动登录）
5. 使用 `游戏ID+密码` 直接登录（设置完密码后）

修改密码直接走第一次的流程使用验证码即可重新设置密码

> [!IMPORTANT]
> **关于数据:** 重载 *本插件* **会** 自动更新 `guguwebui_static` 文件夹中的内容，如果您修改过内部的文件请自行保存，以防您的数据丢失。

> [!IMPORTANT]
> **关于V1.3.0版本:** 本项目于v1.3.0版本重构前端，如您是从v1.3.0版本之前升级的，请删除 `guguwebui_static` 文件夹中的内容，保留 `db.json` 即可。

## 依赖配置

### Python 依赖

在v1.4.0起WebUI将自行处理python依赖，在1.4.0前可参考 [requirements.txt](https://github.com/LoosePrince/PF-MCDR-WebUI/blob/main/requirements.txt) 文件，使用命令 `pip install -r requirements.txt` 进行安装。

### 前置插件

PIM 插件，已内置 WebUI，如有需要可以在设置页面将其安装到外部，以为其他可能需要的插件提供帮助。

### 插件兼容性支持

WebUI 对以下插件提供特殊支持，以增强功能体验（v1.6.2，非必须）：

- `player_ip_logger`：当检测到 `player_ip_logger` 插件时，WebUI 的在线玩家列表会自动集成其玩家验证功能，并显示假人状态

- `fastapi_mcdr`：当检测到 `fastapi_mcdr` 插件时，WebUI 会自动挂载为其子应用
  当检测到 `fastapi_mcdr` 插件卸载时，WebUI 会自动切换到独立服务器模式，需要重新启动WebUI才会重新挂载到 `fastapi_mcdr` 的子应用

## 使用方式

> 目前未对接 GUGUbot 账号系统；当账号为 QQ 号时会显示 QQ 头像和昵称作为管理员名称和头像。

**创建账户**

```bash
!!webui create <username> <password>
```

**更改密码**

```bash
!!webui change <username> <old password> <newpassword>
```

**临时密码**

```bash
!!webui temp
```

## Q&A 问答

Q: 为什么要开发这个插件？<br>
A: 因为我乐意。

Q: 会支持MC服务器管理的功能吗？如模组管理、玩家管理、白名单等等……<br>
A: 并不会深入涉及管理MC服务器，如有这方面的需求请查询MC服务器面板，仅可能会支持很小一部分，例如终端、重启服务器，更多的不在我们的范畴中。

Q: 可以加入开发吗？<br>
A: 当然可以，您可以提交 [pr](https://github.com/LoosePrince/PF-MCDR-WebUI/pulls) 或者参与交流来参与开发。

Q: 会支持我的语言吗？<br>
A: 我只会中文，你要是愿意可以参与，目前已有中文（zh-CN）和英文（en-US），在 [lang文件夹](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/v1.5.0/src/guguwebui/lang)。

Q: 为什么有私货（有未使用的插件，如gugubot等）？<br>
A: 因为这就是为它所开发（虽然GUGUbot的配置一直不完善[doge]）。

Q: 如何获取实时最新版？<br>
A: 前往 [Releases页面](https://github.com/LoosePrince/PF-MCDR-WebUI/releases?q=beta+build) 下载最新的预发布版本（Pre-release），这些版本会在每次代码更新后自动生成。或者你也可以自己打包`src`中的文件到`zip`，修改后缀为`.mcdr`。

Q: 我有个插件，我觉得很适合WebUI，可以作为WebUI的前置吗？<br>
A: WebUI不打算使用任何插件前置，如果有好的方案我们会考虑直接加入WebUI并在关于页感谢贡献。

Q: [PIM插件](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src/guguwebui/utils/PIM) 是什么？<br>
A: [PIM插件](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src/guguwebui/utils/PIM) 是WebUI的插件安装管理器，它可以帮助您安装、卸载、更新插件，并且可以查看插件信息。

Q: 对于开发者如何提供配置文件以支持多语言（中文、英文等）描述？

A: 查看 [插件兼容](https://pf-doc.pfingan.com/main/#/PF-webui/开发/插件兼容) 文档。

## 功能开发

### 事件系统

> [!NOTE]
> 本功能尚处于测试开发阶段，可能会随时更新，请注意本文档的更新情况。

- 为WebUI的聊天消息提供事件分发机制
- 其他MCDR插件可以监听 `webui.chat_message_sent` 事件
- 发送消息到WebUI `send_message_to_webui` 函数
- 详细文档请参考 [WebUI事件系统文档](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src/docs/WebUI事件系统.md)
- 示例插件请参考 [examples/](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src/examples/) 目录

## 示例图

> 截图来源v1.3.4本地测试(部分未改动截图为v1.3.0)

登录页![image](https://github.com/user-attachments/assets/3439beb0-4325-406f-9443-9a6015edb2c6)
仪表盘![image](https://github.com/user-attachments/assets/2fe582f2-7d51-4666-9e0e-f8314fe27520)
MCDR配置![image](https://github.com/user-attachments/assets/141c1416-33ca-4a62-83ef-574cd494ba70)
MC服务器配置![image](https://github.com/user-attachments/assets/08b3bdd5-ba33-48f6-926c-96333df622d8)
本地插件![image](https://github.com/user-attachments/assets/252941b6-f1f1-4b4b-9736-eb75324c09f6)
插件配置![image](https://github.com/user-attachments/assets/bf04660b-03a1-4b6e-ac82-03821c273989)
插件仓库![image](https://github.com/user-attachments/assets/b7c41f92-1b4c-4a37-82e9-4b865af365bf)
插件安装![image](https://github.com/user-attachments/assets/eb701e46-9e09-4b2d-b4f3-685b74792bb2)
终端![image](https://github.com/user-attachments/assets/66b1db2c-ef36-4639-95ef-b685cc64692a)
AI分析![image](https://github.com/user-attachments/assets/91276765-ec5b-47eb-8a85-d5faf6629fbb)
设置![image](https://github.com/user-attachments/assets/eb333411-3e59-4939-a957-c2e956f70f2f)
浅色模式![image](https://github.com/user-attachments/assets/e514d1e4-09f7-41c4-ad27-5b46a8245513)
公开聊天页登录（1.6.0新增）![IMAGE](https://github.com/user-attachments/assets/2caa2bfd-c63d-48cb-bc81-0ab45dae8d21)
公开聊天页![](https://github.com/user-attachments/assets/90959aea-a9c9-4379-8811-6365abedfa42)

# TODO

- [ ] [[更新] 关于后续（饼）](https://github.com/LoosePrince/PF-MCDR-WebUI/issues/8) #8

# 有BUG或是新的IDEA

如果需要更多联动或提交想法和问题请提交 [issues](https://github.com/LoosePrince/PF-MCDR-WebUI/issues) 或 QQ [树梢 (1377820366)](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 提交！ <br />
如需要帮助或者交流请通过 QQ群 [726741344](https://qm.qq.com/q/TqmRHmTmcU) 进行询问或者交流 <br />
视情况添加，请勿联系他人。

# 贡献

| 贡献人                                                | 说明                   |
| -------------------------------------------------- | -------------------- |
| [树梢 (LoosePrince)](https://github.com/LoosePrince) | 功能设计、文档编写、Web设计、前端编写 |
| [雪开 (XueK66)](https://github.com/XueK66)           | 代码开发、维护、功能设计         |

| 贡献项目                                                                 | 功能                       | 备注      |
| -------------------------------------------------------------------- | ------------------------ | ------- |
| [Ace Editor](https://ace.c9.io/)                                     | 在线编辑器                    | 已不再使用   |
| [CodeMirror](https://codemirror.net/)                                | 在线编辑器                    | 目前使用    |
| [MC-Server-Info](https://github.com/Spark-Code-China/MC-Server-Info) | Python Minecraft 服务器信息查询 | 仓库被作者删除 |
| [DeepSeek AI](https://deepseek.com/)                                 | AI辅助功能接口支持               |         |
| [Vditor](https://vditor.b3log.org/)                                  | Markdown编辑器              |         |
| [TailwindCSS](https://tailwindcss.com/)                              | CSS框架                    |         |
| [Alpine.js](https://alpinejs.dev/)                                   | JS框架                     |         |
| [Font Awesome](https://fontawesome.com/)                             | 图标库                      |         |

| 特别鸣谢                           | 说明          |
| ------------------------------ | ----------- |
| 反馈者                            | 感谢你们的反馈     |
| [ChatGPT](https://chatgpt.com) | ChatGPT协助编写 |
| [Cursor](https://cursor.com/)  | Cursor协助编写  |

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [guguweb_v1.6.8.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.8) | 1.6.8 | 2025/09/27 08:05:31 | 369.29KB | 62 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.8/guguweb_v1.6.8.mcdr) |
| [guguweb_v1.6.7.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.7) | 1.6.7 | 2025/09/17 10:10:43 | 352.49KB | 57 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.7/guguweb_v1.6.7.mcdr) |
| [guguweb_v1.6.6.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.6) | 1.6.6 | 2025/08/29 06:02:25 | 349.66KB | 89 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.6/guguweb_v1.6.6.mcdr) |
| [guguweb_v1.6.5.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.5) | 1.6.5 | 2025/08/28 14:28:46 | 339.54KB | 27 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.5/guguweb_v1.6.5.mcdr) |
| [guguweb_v1.6.4.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.4) | 1.6.4 | 2025/08/27 01:06:23 | 339.26KB | 32 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.4/guguweb_v1.6.4.mcdr) |
| [guguweb_v1.6.3.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.3) | 1.6.3 | 2025/08/23 01:01:31 | 337.82KB | 40 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.3/guguweb_v1.6.3.mcdr) |
| [guguweb_v1.6.2.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.2) | 1.6.2 | 2025/08/20 06:15:12 | 336.64KB | 43 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.2/guguweb_v1.6.2.mcdr) |
| [guguweb_v1.6.1.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.1) | 1.6.1 | 2025/08/18 16:47:25 | 328.93KB | 34 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.1/guguweb_v1.6.1.mcdr) |
| [guguweb_v1.6.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.6.0) | 1.6.0 | 2025/08/18 10:37:24 | 324.18KB | 23 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.6.0/guguweb_v1.6.0.mcdr) |
| [guguwebui-v1.5.1.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.5.1) | 1.5.1 | 2025/08/12 07:18:35 | 300.79KB | 51 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.5.1/guguwebui-v1.5.1.mcdr) |
| [guguwebui-v1.5.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.5.0) | 1.5.0 | 2025/08/12 04:03:44 | 298.85KB | 21 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.5.0/guguwebui-v1.5.0.mcdr) |
| [guguwebui-v1.4.3.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.4.3) | 1.4.3 | 2025/08/01 15:51:17 | 264.46KB | 71 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.4.3/guguwebui-v1.4.3.mcdr) |
| [guguwebui-v1.4.2.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.4.2) | 1.4.2 | 2025/07/11 11:03:57 | 255.01KB | 93 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.4.2/guguwebui-v1.4.2.mcdr) |
| [guguwebui-v1.4.1.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.4.1) | 1.4.1 | 2025/06/04 07:02:07 | 252.19KB | 141 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.4.1/guguwebui-v1.4.1.mcdr) |
| [guguwebui-v1.4.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.4.0) | 1.4.0 | 2025/06/04 06:23:13 | 252.55KB | 22 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.4.0/guguwebui-v1.4.0.mcdr) |
| [guguwebui-v1.3.10.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.10) | 1.3.10 | 2025/06/02 11:30:47 | 420.91KB | 23 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.10/guguwebui-v1.3.10.mcdr) |
| [guguwebui-v1.3.9.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.9) | 1.3.9 | 2025/05/19 11:54:00 | 254.32KB | 83 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.9/guguwebui-v1.3.9.mcdr) |
| [guguwebui-v1.3.8.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.8) | 1.3.8 | 2025/05/13 11:10:29 | 248.9KB | 74 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.8/guguwebui-v1.3.8.mcdr) |
| [guguwebui-v1.3.7.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.7) | 1.3.7 | 2025/05/05 09:15:31 | 247.46KB | 51 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.7/guguwebui-v1.3.7.mcdr) |
| [guguwebui-v1.3.6.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.6) | 1.3.6 | 2025/05/04 14:45:18 | 241.03KB | 26 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.6/guguwebui-v1.3.6.mcdr) |
| [guguwebui-v1.3.5.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.5) | 1.3.5 | 2025/05/04 06:01:21 | 226.55KB | 34 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.5/guguwebui-v1.3.5.mcdr) |
| [guguwebui-v1.3.4.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.4) | 1.3.4 | 2025/04/23 08:46:34 | 223.36KB | 72 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.4/guguwebui-v1.3.4.mcdr) |
| [guguwebui-v1.3.3.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.3) | 1.3.3 | 2025/04/15 10:05:53 | 197.07KB | 49 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.3/guguwebui-v1.3.3.mcdr) |
| [guguwebui-v1.3.2.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.2) | 1.3.2 | 2025/04/08 01:04:38 | 187.58KB | 56 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.2/guguwebui-v1.3.2.mcdr) |
| [guguwebui-v1.3.1.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.1) | 1.3.1 | 2025/04/07 09:01:56 | 179.37KB | 25 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.1/guguwebui-v1.3.1.mcdr) |
| [guguwebui-v1.3.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.0) | 1.3.0 | 2025/04/04 05:44:22 | 131.38KB | 30 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.0/guguwebui-v1.3.0.mcdr) |
| [guguwebui-v1.2.5.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.5) | 1.2.5 | 2025/03/12 00:44:19 | 107.53KB | 69 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.5/guguwebui-v1.2.5.mcdr) |
| [guguwebui-v1.2.4.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.4) | 1.2.4 | 2025/01/25 12:56:01 | 105.43KB | 31 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.4/guguwebui-v1.2.4.mcdr) |
| [guguwebui-v1.2.3.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.3) | 1.2.3 | 2025/01/22 15:03:59 | 97.76KB | 59 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.3/guguwebui-v1.2.3.mcdr) |
| [guguwebui-v1.2.2.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.2) | 1.2.2 | 2025/01/21 10:46:29 | 92.95KB | 32 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.2/guguwebui-v1.2.2.mcdr) |
| [guguwebui-v1.2.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.0) | 1.2.0 | 2025/01/19 12:34:03 | 123.17KB | 36 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.0/guguwebui-v1.2.0.mcdr) |
| [guguwebui-v1.1.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.1.0) | 1.1.0 | 2025/01/18 11:07:05 | 89.12KB | 27 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.1.0/guguwebui-v1.1.0.mcdr) |
| [guguwebui-v1.0.0-beta.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.0.0) | 1.0.0 | 2024/11/12 06:31:18 | 112.38KB | 96 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.0.0/guguwebui-v1.0.0-beta.mcdr) |

