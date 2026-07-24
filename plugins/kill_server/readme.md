**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## kill_server

### Basic Information

- Plugin ID: `kill_server`
- Plugin Name: KillServer
- Version: 1.1.0
  - Metadata version: 1.1.0
  - Release version: 1.1.0
- Total downloads: 313
- Authors: [xieyuen](https://github.com/xieyuen)
- Repository: https://github.com/xieyuen/MCDR-Plugins
- Repository plugin page: https://github.com/xieyuen/MCDR-Plugins/tree/master/src/KillServer
- Labels: [`Management`](/labels/management/readme.md)
- Description: Force to kill mc server

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [python](/plugins/python/readme.md) | \>=3.12 |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [dowhen](https://pypi.org/project/dowhen) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.15.0 |

```
pip install dowhen "mcdreforged>=2.15.0"
```

### Introduction

﻿# KillServer

在关服卡死时强制关闭服务器

> [!WARNING]
> 此插件使用 [dowhen](http://github.com/gaogaotiantian/dowhen/) 模块实现, 可能不够稳定

> [!TIP]
> BUG Report: [GitHub issues](https://github.com/xieyuen/MCDR-Plugins/issues/new)

## 介绍

对于下面的情况(实际可能还有更多适用的情况):

1. Fabric 服务器卡死不关闭
   - [MCDReforged/MCDReforged#150](https://github.com/MCDReforged/MCDReforged/issues/150)
   - [EngineHub/WorldEdit#2459](https://github.com/EngineHub/WorldEdit/issues/2459)
2. `pause` 命令诱发用户Ctrl+C操作，导致 MCDR 关闭与存档恢复冲突，最终致使存档损坏
   - [TISUnion/PrimeBackup#85](https://github.com/TISUnion/PrimeBackup/issues/85)
   - [MCDReforged/MCDReforged#394](https://github.com/MCDReforged/MCDReforged/issues/394)

本插件提供监听服务器关闭并且在这些情况下强制关闭服务器的功能, 给小白腐竹们提供一个简单且无脑的解决方案

## 使用方法

直接安装到 MCDR 的插件文件夹下即可, 可以从 [GitHub](https://github/xieyuen/MCDR-Plugins)
或 [PluginCatalogue](https://mcdreforged.com/zh-CN/plugin/kill_server) 手动下载插件文件

你也可以用下面的 MCDR 命令安装 KillServer

```mcdr
!!MCDR plg install kill_server
```

安装后只需要注意服务器关闭不要用 Minecraft 原生的 `/stop` 命令, 换用 MCDR 命令来关闭,
比如 `!!MCDR server stop` `!!MCDR server restart`

> 你都用 MCDR 了竟然还不知道原生 `/stop` 会让 MCDR 关闭吗?<br>
> 你都用 MCDR 了竟然还用不支持运行时回档的备份模组而不是 PrimeBackup、QuickBackupM 吗?

## 配置

|      配置项       |   类型    |   默认值   | 含义                                                              | 注释      |
| :------------: | :-----: | :-----: | --------------------------------------------------------------- | ------- |
|    `enable`    | `bool`  | `True`  | 是否启用插件                                                          | 不影响事件分发 |
| `waiting_time` | `float` |  `60`   | 等待服务器关闭的时间, 超时强制关闭                                              | 单位为秒    |
|  `mcdr_only`   | `bool`  | `False` | 是否只监听 [`PluginStoppingServerEvent`](#PluginStoppingServerEvent) |         |

## 新的事件

见 [Read the Docs 文档](https://mcdr-plugins.readthedocs.io/zh-cn/latest/kill_server/events.html)

> [!IMPORTANT]
> 自 1.1.0 版本起, 插件事件已经完全重构,
> 使用 `from kill_server import *` 导入 `ServerStoppingEvent` 这些事件变量的的已不再适用, 
> 它们全部合并到了 [`ServerEvents`](https://mcdr-plugins.readthedocs.io/zh-cn/latest/kill_server/events.html#kill_server.events.server_event.ServerEvents) 中
> 
> 使用事件 ID 监听事件的, 依然可以继续使用


### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [KillServer-v1.1.0.mcdr](https://github.com/xieyuen/MCDR-Plugins/releases/tag/kill_server-v1.1.0) | 1.1.0 | 2026/03/14 13:07:19 | 5.54KB | 81 | [Download](https://github.com/xieyuen/MCDR-Plugins/releases/download/kill_server-v1.1.0/KillServer-v1.1.0.mcdr) |
| [KillServer-v1.0.0.mcdr](https://github.com/xieyuen/MCDR-Plugins/releases/tag/kill_server-v1.0.0) | 1.0.0 | 2026/02/24 07:56:05 | 2.5KB | 65 | [Download](https://github.com/xieyuen/MCDR-Plugins/releases/download/kill_server-v1.0.0/KillServer-v1.0.0.mcdr) |
| [KillServer-v0.1.2.mcdr](https://github.com/xieyuen/MCDR-Plugins/releases/tag/kill_server-v0.1.2) | 0.1.2 | 2026/02/20 08:50:05 | 1.94KB | 54 | [Download](https://github.com/xieyuen/MCDR-Plugins/releases/download/kill_server-v0.1.2/KillServer-v0.1.2.mcdr) |
| [KillServer-v0.1.1.mcdr](https://github.com/xieyuen/MCDR-Plugins/releases/tag/kill_server-v0.1.1) | 0.1.1 | 2026/02/18 13:01:21 | 1.4KB | 52 | [Download](https://github.com/xieyuen/MCDR-Plugins/releases/download/kill_server-v0.1.1/KillServer-v0.1.1.mcdr) |
| [KillServer-v0.1.0.mcdr](https://github.com/xieyuen/MCDR-Plugins/releases/tag/kill_server-v0.1.0) | 0.1.0 | 2026/02/17 15:29:27 | 1.39KB | 61 | [Download](https://github.com/xieyuen/MCDR-Plugins/releases/download/kill_server-v0.1.0/KillServer-v0.1.0.mcdr) |

