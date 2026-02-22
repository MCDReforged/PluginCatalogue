[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## meowtiwhitelist

### 基本信息

- 插件 ID: `meowtiwhitelist`
- 插件名: MeowtiWhitelist
- 版本: 2.4.0
  - 元数据版本: 2.4.0
  - 发布版本: 2.4.0
- 总下载量: 410
- 作者: [MliroLirrorsIngenuity](https://github.com/MliroLirrorsIngenuity)
- 仓库: https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist
- 仓库插件页: https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一个多验证服务(Yggdrasil)白名单管理插件。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.12.0 |
| [requests](https://pypi.org/project/requests) | \>=2.31.0 |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0.2 |

```
pip install "mcdreforged>=2.12.0" "requests>=2.31.0" "PyYAML>=6.0.2"
```

### 介绍

<div align="center">
  <h1 align="center">MeowtiWhitelist</h1>
  <p align="center">
    一款基于 <a href="https://mcdreforged.com/"><strong>MCDReforged</strong></a> 开发的多验证服务白名单管理插件，解决多验证服务环境下的白名单问题。
    <br />
    <br />
    <a href="https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/blob/main/README.md">简体中文</a>
    |
    <a href="https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/blob/main/README_EN.md">English</a>
  </p>
</div>

<details>
  <summary>目录</summary>

- [特性](#特性)
- [使用方式](#使用方式)
  - [依赖](#依赖)
  - [安装](#安装)
  - [配置&指令&API](#配置指令api)
- [提问前必看](#提问前必看)
- [贡献者](#贡献者)
- [致谢](#致谢)

</details>

## 特性

- 解决使用多个不同 **Yggdrasil** 验证服务导致的UUID冲突或不正确的问题。
- 使用简单命令，管理来自不同 **Yggdrasil** 验证来源的白名单添加。
- 不再需要手动添加对应验证来源的正确UUID到 `whitelist.json` 。 ~~不是哥们谁又手动改`whitelist.json`~~
- 我们提供了一系列API供开发者调用，你可以使用本插件来管理并获取多个来源的UUID。

## 使用方式

### 依赖

`MCDReforged`>=2.12.0

`requests`>=2.31.0

`PyYAML`>=6.0.2

### 安装

在运行的 MCDReforged 实例中执行以下命令，根据提示引导进行安装。
```
!!MCDR plugin install meowtiwhitelist
```

如果服务端网络环境访问安装源存在困难或出于其他原因，可以尝试下面的手动安装

<details>
  <summary>手动安装</summary>

1. 从 [GitHub Releases](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases)中下载最新版本的 MeowtiWhitelist
2. 将下载的插件放入MCDR的`plugins`目录中
3. 安装所需的[依赖](#依赖)
4. [通过MCDReforged启动服务器](https://docs.mcdreforged.com/zh-cn/latest/quick_start/first_run.html#run)

</details>

## 配置&指令&API
详见 [Wiki](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/wiki)

## 提问前必看

在提问之前，请确保：

- 已经尝试了所有可能的解决方案

- 已经尝试搜索了解决方案（包括但不限于本仓库的[Issues](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/issues)）

- 你提供了**足够的信息**帮助开发人员定位问题，包括但不限于下列：

  - 服务端日志（MCDR日志、服务端日志等）

  - 插件配置文件

  - 插件列表

  - MCDR 版本号、Minecraft 服务端版本号和插件版本号

- 提问渠道说明
  - **使用问题/配置疑问/其他问题** → [Discussions](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/discussions)
  - **Bug/功能请求** → [Issues](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/issues)

## 贡献者
<a href="https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MliroLirrorsIngenuity/MeowtiWhitelist&" alt="Contributors" />
</a>

## 致谢

[Lazy-Bing-Server/MCDR-offline-whitelist-manager](https://github.com/Lazy-Bing-Server/MCDR-offline-whitelist-manager)：提供了插件主体构建思路

[CaaMoe/MultiLogin](https://github.com/CaaMoe/MultiLogin)：提供了配置插件的方案灵感

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MeowtiWhitelist-v2.4.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.4.0) | 2.4.0 | 2025/10/16 19:41:27 | 11.68KB | 52 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.4.0/MeowtiWhitelist-v2.4.0.mcdr) |
| [MeowtiWhitelist-v2.3.1.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.3.1) | 2.3.1 | 2025/10/05 10:34:13 | 11.41KB | 19 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.3.1/MeowtiWhitelist-v2.3.1.mcdr) |
| [MeowtiWhitelist-v2.3.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.3.0) | 2.3.0 | 2025/06/26 16:24:12 | 11.48KB | 80 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.3.0/MeowtiWhitelist-v2.3.0.mcdr) |
| [MeowtiWhitelist-v2.2.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.2.0) | 2.2.0 | 2025/03/22 14:27:05 | 10.12KB | 60 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.2.0/MeowtiWhitelist-v2.2.0.mcdr) |
| [MeowtiWhitelist-v2.1.2.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.1.2) | 2.1.2 | 2025/03/11 15:59:39 | 9.48KB | 36 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.1.2/MeowtiWhitelist-v2.1.2.mcdr) |
| [MeowtiWhitelist-v2.1.1.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.1.1) | 2.1.1 | 2025/03/08 15:03:12 | 9.48KB | 35 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.1.1/MeowtiWhitelist-v2.1.1.mcdr) |
| [MeowtiWhitelist-v2.1.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.1.0) | 2.1.0 | 2025/03/06 18:27:06 | 9.46KB | 27 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.1.0/MeowtiWhitelist-v2.1.0.mcdr) |
| [MeowtiWhitelist-v2.0.3.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.0.3) | 2.0.3 | 2025/03/04 18:57:26 | 8.88KB | 32 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.0.3/MeowtiWhitelist-v2.0.3.mcdr) |
| [MeowtiWhitelist-v2.0.2.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.0.2) | 2.0.2 | 2025/03/04 16:27:08 | 8.81KB | 40 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.0.2/MeowtiWhitelist-v2.0.2.mcdr) |
| [MeowtiWhitelist-v2.0.1.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.0.1) | 2.0.1 | 2025/03/03 19:08:45 | 8.82KB | 29 | [下载](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.0.1/MeowtiWhitelist-v2.0.1.mcdr) |

