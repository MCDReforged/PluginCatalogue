[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## location_api

### 基本信息

- 插件 ID: `location_api`
- 插件名: LocationAPI
- 版本: 0.2.2
  - 元数据版本: 0.2.2
  - 发布版本: 0.2.2
- 总下载量: 25
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/LocationAPI-MCDR
- 仓库插件页: https://github.com/Mooling0602/LocationAPI-MCDR/tree/main
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 一个用于定义路标和位置点的API。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |
| [python](/plugins/python/readme-zh_cn.md) | \>=3.11 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.1.0 |
| [beartype](https://pypi.org/project/beartype) | \>=0.20.0 |

```
pip install "mcdreforged>=2.1.0" "beartype>=0.20.0"
```

### 介绍

# LocationAPI-MCDR

An API to define location or positon points.

## 描述

LocationAPI是一个用于定义Minecraft中位置点的API。它提供了Point2D、Point3D、MCPosition和Location类，可以方便地表示游戏中的坐标和位置信息。

LocationAPI同时也是ModernTeleport（现代化传送）插件的核心依赖。

测试内容如下：
```fish
(locationapi-mcdr) mooling@localhost /path/to/LocationAPI-MCDR (main)> .venv/bin/python location_api/__init__.py
Type coord x: 45
Type coord z: 456
Type coord y: 64
Type dimension: minecraft:the_end
Type location name: 小黑塔
Type location description: 末影人刷怪塔
Type other attributes by json string here: 
Location generating...
Location(position=MCPosition(point=x: 45.0, y: 64.0, z: 456.0, dimension=minecraft:the_end), name=小黑塔, description=末影人刷怪塔, other=None)
```

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [LocationAPI-v0.2.2.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.2) | 0.2.2 | 2025/10/08 14:56:39 | 2.5KB | 4 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.2/LocationAPI-v0.2.2.mcdr) |
| [LocationAPI-v0.2.1.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.1) | 0.2.1 | 2025/09/26 10:10:33 | 2.37KB | 4 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.1/LocationAPI-v0.2.1.mcdr) |
| [LocationAPI-v0.2.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.0) | 0.2.0 | 2025/09/25 07:27:36 | 2.38KB | 6 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.0/LocationAPI-v0.2.0.mcdr) |
| [LocationAPI-v0.1.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.1.0) | 0.1.0 | 2025/09/21 14:24:49 | 2.38KB | 5 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.1.0/LocationAPI-v0.1.0.mcdr) |
| [LocationAPI-v0.0.1.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.0.1) | 0.0.1 | 2025/09/20 09:35:34 | 2.31KB | 6 | [下载](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.0.1/LocationAPI-v0.0.1.mcdr) |

