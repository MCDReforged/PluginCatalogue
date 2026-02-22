[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## location_api

### 基本信息

- 插件 ID: `location_api`
- 插件名: LocationAPI
- 版本: 0.4.4
  - 元数据版本: 0.4.4
  - 发布版本: 0.4.4
- 总下载量: 65
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/LocationAPI-MCDR
- 仓库插件页: https://github.com/Mooling0602/LocationAPI-MCDR/tree/main
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 一个用于定义路标和位置点的API。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [moolings_rcon_api](/plugins/moolings_rcon_api/readme-zh_cn.md) | \>=0.1.0 |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |
| [python](/plugins/python/readme-zh_cn.md) | \>=3.11 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.1 |
| [beartype](https://pypi.org/project/beartype) |  |
| [returns](https://pypi.org/project/returns) |  |
| [primitive-type](https://pypi.org/project/primitive-type) | \>=0.1.2 |

```
pip install "mcdreforged>=2.14.1" beartype returns "primitive-type>=0.1.2"
```

### 介绍

# LocationAPI-MCDR

An API to define location or positon points.

Documentation is [here](https://docs.clemooling.top/location_api).
> 可点击蓝色字体进入文档，支持中文，会自动根据浏览器环境提供正确的语言。

## 描述

LocationAPI是一个用于定义Minecraft中位置点的API。它提供了Point2D、Point3D、MCPosition和Location类，可以方便地表示游戏中的坐标和位置信息。

LocationAPI同时也是ModernTeleport（现代化传送）插件的核心依赖。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [LocationAPI-v0.4.4.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/v0.4.4) | 0.4.4 | 2026/02/12 09:23:33 | 6.04KB | 6 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/v0.4.4/LocationAPI-v0.4.4.mcdr) |
| [LocationAPI-v0.4.3.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/v0.4.3) | 0.4.3 | 2026/02/12 09:05:48 | 6.03KB | 2 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/v0.4.3/LocationAPI-v0.4.3.mcdr) |
| [LocationAPI-v0.4.2.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/v0.4.2) | 0.4.2 | 2026/02/12 08:49:48 | 6.02KB | 2 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/v0.4.2/LocationAPI-v0.4.2.mcdr) |
| [LocationAPI-v0.4.1.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/v0.4.1) | 0.4.1 | 2026/02/09 09:28:58 | 6.08KB | 2 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/v0.4.1/LocationAPI-v0.4.1.mcdr) |
| [LocationAPI-v0.4.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/v0.4.0) | 0.4.0 | 2026/02/09 08:30:29 | 6.06KB | 1 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/v0.4.0/LocationAPI-v0.4.0.mcdr) |
| [LocationAPI-v0.3.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/v0.3.0) | 0.3.0 | 2026/02/02 05:17:39 | 4.66KB | 8 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/v0.3.0/LocationAPI-v0.3.0.mcdr) |
| [LocationAPI-v0.2.2.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.2) | 0.2.2 | 2025/10/08 14:56:39 | 2.5KB | 20 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.2/LocationAPI-v0.2.2.mcdr) |
| [LocationAPI-v0.2.1.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.1) | 0.2.1 | 2025/09/26 10:10:33 | 2.37KB | 4 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.1/LocationAPI-v0.2.1.mcdr) |
| [LocationAPI-v0.2.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.0) | 0.2.0 | 2025/09/25 07:27:36 | 2.38KB | 8 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.0/LocationAPI-v0.2.0.mcdr) |
| [LocationAPI-v0.1.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.1.0) | 0.1.0 | 2025/09/21 14:24:49 | 2.38KB | 6 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.1.0/LocationAPI-v0.1.0.mcdr) |
| [LocationAPI-v0.0.1.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.0.1) | 0.0.1 | 2025/09/20 09:35:34 | 2.31KB | 6 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.0.1/LocationAPI-v0.0.1.mcdr) |

