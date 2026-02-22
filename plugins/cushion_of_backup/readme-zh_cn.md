[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## cushion_of_backup

### 基本信息

- 插件 ID: `cushion_of_backup`
- 插件名: Cushion of Backup
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 31
- 作者: [HeTao_yz](https://github.com/HeTao-yz)
- 仓库: https://github.com/HeTao-yz/Cushion-of-Backup
- 仓库插件页: https://github.com/HeTao-yz/Cushion-of-Backup/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 优化服务器回档/重启时的玩家处理逻辑，让玩家游戏体验连贯顺畅

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged ](https://pypi.org/project/mcdreforged ) | \>= 2.0.0 |
| [rcon](https://pypi.org/project/rcon) |  |

```
pip install "mcdreforged >= 2.0.0" rcon
```

### 介绍

# Cushion of Backup - 回档缓冲

[English](https://github.com/HeTao-yz/Cushion-of-Backup/blob/main/README_EN.md)

优化服务器回档/重启时的玩家处理逻辑，让玩家游戏体验连贯顺畅

## 前言

> 请注意：该插件并不提供新的回档方式，而是基于现有需要重启服务器的回档方式上的回档体验改善插件。

在多人服务器中，回档/重启是不可避免的事情。但每次回档都需要重启服务器，玩家会被迫退出，回到服务器列表。 不仅体验被迫中断，还得反复手动重连，更不知道要等到什么时候才能再次进入…

作者想改变普遍如此的不良体验。于是尝试做出了一些改善。希望这个插件能为您，或是您所在的服务器，带来回档体验上的改善。

## 如何优化

演示视频：[也许是生电服中最好的回档体验](https://www.bilibili.com/video/BV1kD6ABjEwc)

Velocity下，当生存服（主服）重启时，玩家将被转移至大厅服（可以是任何子服务器，大厅仅为名字，无特别含义，于功能意义上为暂时转移玩家的服务器）。

当生存服回档成功，准备启动时和启动成功后，都将发送提示信息到大厅服。随后将玩家自动返回至生存服。从而实现在生存服重启时让玩家游戏体验连贯顺畅。

## 安装

### 先决条件

- 需要配置Velocity反代端，且需要安装 [Velocircon](https://modrinth.com/plugin/velocircon) 插件使其支持并配置rcon控制。

- 生存服和大厅服均为Velocity子服，且大厅服需要打开并配置rcon控制

- Velocity配置文件 try 块中，需要添加生存服和大厅服

### 注意

**需要将该插件安装在生存服（主服）**

## 配置文件

插件首次加载时会自动生成配置文件 `config/cushion_of_backup.json`。

```json
{
    "velocity_host": "127.0.0.1",
    "velocity_port": 25581,
    "velocity_passwd": "password123",
    "lobby_host": "127.0.0.1",
    "lobby_port": 25576,
    "lobby_passwd": "password123",
    "lobby_server": "lobby",
    "survival_server": "survival",
    "survival_server_start": "生存服正在启动中...",
    "survival_server_startup": "启动完成！正在将玩家返回至生存服...",
    "survival_server_failure": "生存服崩溃！请反馈至管理员解决。生存服将继续尝试启动。"
}
```

### 配置项说明

| 配置项                       | 类型     | 默认值                           | 说明                    |
| ------------------------- | ------ | ----------------------------- | --------------------- |
| `velocity_host`           | string | `127.0.0.1`                   | Velocity 服务器地址        |
| `velocity_port`           | int    | `25575`                       | Velocity RCON 端口      |
| `velocity_passwd`         | string | `password`                    | Velocity RCON 密码      |
| `lobby_host`              | string | `127.0.0.1`                   | 大厅服地址                 |
| `lobby_port`              | int    | `25575`                       | 大厅服 RCON 端口           |
| `lobby_passwd`            | string | `password`                    | 大厅服 RCON 密码           |
| `lobby_server`            | string | `lobby`                       | 大厅服在 Velocity 中的服务器名称 |
| `survival_server`         | string | `survival`                    | 生存服在 Velocity 中的服务器名称 |
| `survival_server_start`   | string | `生存服正在启动中...`                 | 生存服开始启动时向大厅服发送的消息     |
| `survival_server_startup` | string | `启动完成！正在将玩家返回至生存服...`         | 生存服启动完成时向大厅服发送的消息     |
| `survival_server_failure` | string | `生存服崩溃！请反馈至管理员解决。生存服将继续尝试启动。` | 生存服崩溃时向大厅服发送的消息       |

## 其他

初次开发插件有不熟练之处或不完善之处。若使用时有bug或其他建议，欢迎至Github插件源仓库处提交Issue。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [Cushion-of-Backup_v1.0.0.mcdr](https://github.com/HeTao-yz/Cushion-of-Backup/releases/tag/v1.0.0) | 1.0.0 | 2026/01/31 05:26:23 | 15.19KB | 31 | [下载](https://github.com/HeTao-yz/Cushion-of-Backup/releases/download/v1.0.0/Cushion-of-Backup_v1.0.0.mcdr) |

