**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## location_api

### Basic Information

- Plugin ID: `location_api`
- Plugin Name: LocationAPI
- Version: 0.2.2
  - Metadata version: 0.2.2
  - Release version: 0.2.2
- Total downloads: 44
- Authors: [Mooling0602](https://github.com/Mooling0602)
- Repository: https://github.com/Mooling0602/LocationAPI-MCDR
- Repository plugin page: https://github.com/Mooling0602/LocationAPI-MCDR/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: An API to define location or positon points.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |
| [python](/plugins/python/readme.md) | \>=3.11 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.1 |
| [beartype](https://pypi.org/project/beartype) |  |
| [returns](https://pypi.org/project/returns) |  |

```
pip install "mcdreforged>=2.14.1" beartype returns
```

### Introduction

> Translations are still in progress...

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

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [LocationAPI-v0.2.2.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.2) | 0.2.2 | 2025/10/08 14:56:39 | 2.5KB | 20 | [Download](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.2/LocationAPI-v0.2.2.mcdr) |
| [LocationAPI-v0.2.1.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.1) | 0.2.1 | 2025/09/26 10:10:33 | 2.37KB | 4 | [Download](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.1/LocationAPI-v0.2.1.mcdr) |
| [LocationAPI-v0.2.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.2.0) | 0.2.0 | 2025/09/25 07:27:36 | 2.38KB | 8 | [Download](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.2.0/LocationAPI-v0.2.0.mcdr) |
| [LocationAPI-v0.1.0.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.1.0) | 0.1.0 | 2025/09/21 14:24:49 | 2.38KB | 6 | [Download](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.1.0/LocationAPI-v0.1.0.mcdr) |
| [LocationAPI-v0.0.1.mcdr](https://github.com/Mooling0602/LocationAPI-MCDR/releases/tag/0.0.1) | 0.0.1 | 2025/09/20 09:35:34 | 2.31KB | 6 | [Download](https://github.com/Mooling0602/LocationAPI-MCDR/releases/download/0.0.1/LocationAPI-v0.0.1.mcdr) |

