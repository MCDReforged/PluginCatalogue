[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## guguwebui

### 基本信息

- 插件 ID: `guguwebui`
- 插件名: GUGU WebUI
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 43
- 作者: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- 仓库: https://github.com/LoosePrince/PF-MCDR-WebUI
- 仓库插件页: https://github.com/LoosePrince/PF-MCDR-WebUI/tree/main/src
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 使用webui来管理所有插件参数设置

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [argon2-cffi](https://pypi.org/project/argon2-cffi) |  |
| [fastapi](https://pypi.org/project/fastapi) |  |
| [javaproperties](https://pypi.org/project/javaproperties) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.3.0 |
| [passlib](https://pypi.org/project/passlib) |  |
| [pydantic](https://pypi.org/project/pydantic) |  |
| [ruamel.yaml](https://pypi.org/project/ruamel.yaml) |  |
| [starlette[full]](https://pypi.org/project/starlette[full]) |  |
| [uvicorn](https://pypi.org/project/uvicorn) |  |

```
pip install argon2-cffi fastapi javaproperties "mcdreforged>=2.3.0" passlib pydantic ruamel.yaml "starlette[full]" uvicorn
```

### 介绍

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

**主要功能:** 为MCDR提供一个在线WebUI管理界面和MCDR插件管理和表单配置功能（可选使用在线编辑器）。

**插件管理:** 提供列出全部插件、一键更新 ( **推迟** ) 、启动插件、停止插件、重载插件、插件配置修改（需要符合格式）。

**配置修改:** 使用在线表单 **或** 在线编辑器进行配置文件的修改（在 **`所有插件`** 选项卡处修改）。

**支持的配置:** `yaml` 格式或者 `json` 文件。
- yml文件识别每项上一行注释作为中文标题，使用 `::` 分割，第二项为副标题，例 `标题::副标题` ，请注意，使用的是英文的符号；
- json文件需要创建同级文件 `需要加标题的配置文件名_lang.josn` 例如 `abc_lang.json` 则会为 `abc.json` 创建中文标题，使用 `[标题,副标题]` 创建标题和副标题，参考示例: [config_lang.json](https://github.com/LoosePrince/PF-MCDR-WebUI/blob/main/config_lang.json)

**自定义:** 支持全局css和js配置文件，在首页提供在线编辑。

> [!IMPORTANT]
> **关于更新:** 涉及 `HTML` 更新部分更新后请删除 `guguwebui_static` 文件夹中的数据文件，如果您修改过内部的文件请自行备份，更新时 *本插件* **不会**为您自动删除和更新 `guguwebui_static` 文件夹中的内容，以防您的数据丢失。

## 依赖配置

**Python 包:** 请确保已安装 [Python™](https://www.python.org/) 和 [pip](https://pypi.org/project/pip/) (pip通常在安装完python后会默认安装)。

**Python 模块:** 参考插件目录内的 `requirements.txt` 文件，使用命令 `pip install -r requirements.txt` 进行安装。

**前置插件:** 无

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
A:当然可以，您可以提交 pr 或者 参与交流 来参与开发。

Q:UI为什么这么丑（不美观、没有夜间模式...）<br>
A:实力受限，但是我们提供自定义 css 和 js ，您可以自行修改甚至提交给我们以进行采纳，我们会将你加入贡献名单中。

Q:会支持多语言吗。<br>
A:我只会中文，你要是愿意可以参与。

Q:为什么有私货（有未使用的插件，如gugubot等）。<br>
A:因为这就是为它所开发。

## 示例图

> 截图来源本地测试

![image](https://github.com/user-attachments/assets/b8556f19-25b1-433d-9691-72bb21816480)
![image](https://github.com/user-attachments/assets/5b868779-ec5c-4082-bf3e-f7564ba06e4b)
![image](https://github.com/user-attachments/assets/c1633bb7-de4d-4e5b-a091-ebae30322e19)
![image](https://github.com/user-attachments/assets/b1154e22-a111-4094-aab4-da3cefde7e14)
![image](https://github.com/user-attachments/assets/5b2ab04f-a4fb-4be5-b3a1-9da3a97709e3)
![image](https://github.com/user-attachments/assets/808c22e5-e3b4-46d7-8549-417c94438c16)
![image](https://github.com/user-attachments/assets/a50991e6-a281-4ec7-99e8-d8a921d15e95)
![image](https://github.com/user-attachments/assets/92ca8d19-40b1-444b-8aed-6c080c1b91a9)



## 开发进度

- 首页:90%
  - 主要功能:100%
  - 最近配置项:0%
- GUGUbot管理:90%
  - 配置:100%
  - 附加功能:0%
- cq-qq-api:80%
  - 配置:100%
  - 文档:0%
  - 附加功能:0%
- MC服务器配置:100%
- MCDR配置:100%
- 所有插件管理:90%
  - 管理:100%
  - 更新:10%（被推迟了）
  - 配置修改:100%
  - 附加功能:0%
- 服务器终端:0%
- Fabric（部分）:0%

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
| [Ace Editor](https://ace.c9.io/)                                     | 在线编辑器                    |         |
| [MC-Server-Info](https://github.com/Spark-Code-China/MC-Server-Info) | Python Minecraft 服务器信息查询 | 仓库被作者删除 |


| 特别鸣谢                           | 说明          |
| ------------------------------ | ----------- |
| 反馈者                            | 感谢你们的反馈     |
| [ChatGPT](https://chatgpt.com) | ChatGPT协助编写 |

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [guguwebui-v1.0.0-beta.mcdr](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/tag/v1.0.0) | 1.0.0 | 2024/11/12 06:31:18 | 112.38KB | 43 | [下载](https://github.com/LoosePrince/PF-MCDR-WebUI/releases/download/v1.0.0/guguwebui-v1.0.0-beta.mcdr) |

