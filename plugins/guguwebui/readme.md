**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## guguwebui

### Basic Information

- Plugin ID: `guguwebui`
- Plugin Name: GUGU WebUI
- Version: 1.4.1
  - Metadata version: 1.4.1
  - Release version: 1.4.1
- Total downloads: 647
- Authors: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- Repository: https://github.com/LoosePrince/PF-MCDR-WebUI
- Repository plugin page: https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src
- Labels: [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: WebUI for managing all plugins, MCDR configurations, online installation, terminals, and more.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# PF-MCDR-WebUI
为 MCDR 开发的在线 WebUI 插件

[![页面浏览量计数](https://badges.toozhao.com/badges/01JC0ZMB6718E924N6H2FEZRC5/green.svg)](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src//) 
[![查看次数起始时间](https://img.shields.io/badge/查看次数统计起始于-2024%2F11%2F06-2?style=flat-square)](https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src//)
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

### 主要功能
> 为MCDR提供一个 `在线WebUI管理界面` 和 `MCDR插件管理` 和 `表单配置功能`（可选使用在线编辑器）。

#### pip包管理

#### 本地插件管理

- [x] 列出全部插件
- [x] 一键更新
- [x] 启动插件
- [x] 停止插件
- [x] 重载插件
- [x] 切换插件版本（第三方仓库不支持）
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

> [!IMPORTANT]
> **关于数据:** 重载插件 *本插件* **会** 自动更新 `guguwebui_static` 文件夹中的内容，如果您修改过内部的文件请自行保存，以防您的数据丢失。

> [!IMPORTANT]
> **关于V1.3.0版本:** 本项目于v1.3.0版本重构前端，如您是从v1.3.0版本之前升级的，请删除 `guguwebui_static` 文件夹中的内容，保留 `db.json` 即可。


## 依赖配置

### Python 依赖

在v1.4.0起WebUI将自行处理python依赖，在1.4.0前可参考 [requirements.txt](https://github.com/LoosePrince/PF-MCDR-WebUI/blob/main/requirements.txt) 文件，使用命令 `pip install -r requirements.txt` 进行安装。

### 前置插件

PIM插件，已内置WebUI，如有需要可以在设置页面将其安装到外部以为其它可能需要的插件提供帮助。

## 使用方式

> 目前未对接GUGUbot账号系统；当账号为QQ号时会显示QQ头像和昵称作为管理员名称和头像。

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

Q:为什么要开发这个插件。<br>
A:因为我乐意。

Q:会支持MC服务器管理的功能吗？如模组管理，玩家管理，白名单等等..<br>
A:并不会深入涉及管理MC服务器，如有这方面的需求请查询MC服务器面板，仅可能会支持很小一部分，例如终端、重启服务器，更多的不在我们的范畴中。

Q:可以加入开发吗？<br>
A:当然可以，您可以提交 [pr](https://github.com/LoosePrince/PF-MCDR-WebUI/pulls) 或者 参与交流 来参与开发。

Q:会支持多语言吗。<br>
A:我只会中文，你要是愿意可以参与。

Q:为什么有私货（有未使用的插件，如gugubot等）。<br>
A:因为这就是为它所开发（虽然GUGUbot的配置一直不完善[doge]）。

Q:如何获取实时最新版<br>
A:自己打包`src`中的文件到`zip`，修改后缀为`.mcdr`，或者前往 [actions](https://github.com/LoosePrince/PF-MCDR-WebUI/actions/workflows/package-src.yml) 下载，解压提取其中的mcdr文件即可。

Q:我有个插件，我觉得很适合WebUI，可以作为WebUI的前置吗？<br>
A:WebUI不打算使用任何插件前置，如果有好的方案我们会考虑直接加入WebUI并在关于页感谢贡献。

Q:[PIM插件](https://github.com/LoosePrince/PF-MCDR-WebUI/blob/main/src/guguwebui/utils/PIM.py)是什么？<br>
A:[PIM插件](https://github.com/LoosePrince/PF-MCDR-WebUI/blob/main/src/guguwebui/utils/PIM.py)是WebUI的插件安装管理器，它可以帮助您安装、卸载、更新插件，并且可以查看插件信息。

Q:对于开发者如何提供配置文件以支持中文描述?

A:如下配置
> `yml文件` 识别每项上一行注释作为中文标题，使用 `::` 分割，第二项为副标题，例 `标题::副标题` ，请注意，使用的是英文的符号；
> 
> `json文件` 需要创建同级文件 `需要加标题的配置文件名_lang.josn` 例如 `abc_lang.json` 则会为 `abc.json` 创建中文标题，使用 `[标题,副标题]` 创建标题和副标题，参考示例: [config_lang.json](https://github.com/LoosePrince/PF-MCDR-WebUI/blob/main/config_lang.json)；
> 
> `html格式`, 使用 `main.json` 在其中使用键对值的方式指定每个配置文件对应的 `html文件` ，届时加载时会加载 `html文件内容` ，如果您有样式请不要使用外链式加载本地css和js，请使用 `style` 和 `script` 标签。


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

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [guguwebui-v1.4.1.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.4.1) | 1.4.1 | 2025/06/04 07:02:07 | 252.19KB | 107 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.4.1/guguwebui-v1.4.1.mcdr) |
| [guguwebui-v1.4.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.4.0) | 1.4.0 | 2025/06/04 06:23:13 | 252.55KB | 2 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.4.0/guguwebui-v1.4.0.mcdr) |
| [guguwebui-v1.3.10.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.10) | 1.3.10 | 2025/06/02 11:30:47 | 420.91KB | 3 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.10/guguwebui-v1.3.10.mcdr) |
| [guguwebui-v1.3.9.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.9) | 1.3.9 | 2025/05/19 11:54:00 | 254.32KB | 63 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.9/guguwebui-v1.3.9.mcdr) |
| [guguwebui-v1.3.8.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.8) | 1.3.8 | 2025/05/13 11:10:29 | 248.9KB | 53 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.8/guguwebui-v1.3.8.mcdr) |
| [guguwebui-v1.3.7.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.7) | 1.3.7 | 2025/05/05 09:15:31 | 247.46KB | 30 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.7/guguwebui-v1.3.7.mcdr) |
| [guguwebui-v1.3.6.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.6) | 1.3.6 | 2025/05/04 14:45:18 | 241.03KB | 7 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.6/guguwebui-v1.3.6.mcdr) |
| [guguwebui-v1.3.5.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.5) | 1.3.5 | 2025/05/04 06:01:21 | 226.55KB | 15 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.5/guguwebui-v1.3.5.mcdr) |
| [guguwebui-v1.3.4.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.4) | 1.3.4 | 2025/04/23 08:46:34 | 223.36KB | 52 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.4/guguwebui-v1.3.4.mcdr) |
| [guguwebui-v1.3.3.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.3) | 1.3.3 | 2025/04/15 10:05:53 | 197.07KB | 30 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.3/guguwebui-v1.3.3.mcdr) |
| [guguwebui-v1.3.2.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.2) | 1.3.2 | 2025/04/08 01:04:38 | 187.58KB | 38 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.2/guguwebui-v1.3.2.mcdr) |
| [guguwebui-v1.3.1.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.1) | 1.3.1 | 2025/04/07 09:01:56 | 179.37KB | 7 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.1/guguwebui-v1.3.1.mcdr) |
| [guguwebui-v1.3.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.3.0) | 1.3.0 | 2025/04/04 05:44:22 | 131.38KB | 12 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.3.0/guguwebui-v1.3.0.mcdr) |
| [guguwebui-v1.2.5.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.5) | 1.2.5 | 2025/03/12 00:44:19 | 107.53KB | 50 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.5/guguwebui-v1.2.5.mcdr) |
| [guguwebui-v1.2.4.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.4) | 1.2.4 | 2025/01/25 12:56:01 | 105.43KB | 13 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.4/guguwebui-v1.2.4.mcdr) |
| [guguwebui-v1.2.3.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.3) | 1.2.3 | 2025/01/22 15:03:59 | 97.76KB | 40 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.3/guguwebui-v1.2.3.mcdr) |
| [guguwebui-v1.2.2.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.2) | 1.2.2 | 2025/01/21 10:46:29 | 92.95KB | 14 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.2/guguwebui-v1.2.2.mcdr) |
| [guguwebui-v1.2.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.2.0) | 1.2.0 | 2025/01/19 12:34:03 | 123.17KB | 20 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.2.0/guguwebui-v1.2.0.mcdr) |
| [guguwebui-v1.1.0.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.1.0) | 1.1.0 | 2025/01/18 11:07:05 | 89.12KB | 11 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.1.0/guguwebui-v1.1.0.mcdr) |
| [guguwebui-v1.0.0-beta.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.0.0) | 1.0.0 | 2024/11/12 06:31:18 | 112.38KB | 80 | [Download](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.0.0/guguwebui-v1.0.0-beta.mcdr) |

