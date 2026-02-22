[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## easybot_mcdr

### 基本信息

- 插件 ID: `easybot_mcdr`
- 插件名: EasyBot
- 版本: 1.2.1
  - 元数据版本: 1.2.1
  - 发布版本: 1.2.1
- 总下载量: 729
- 作者: [MiuxuE](https://github.com/easybot-team)
- 仓库: https://github.com/easybot-team/easybot-mcdr
- 仓库插件页: https://github.com/easybot-team/easybot-mcdr/tree/main
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一款集消息同步、自定义命令、绑定管理、高级权限控制、群组互动、自定义模板支持以及自定义插件支持等全方位功能于一体的服务器管理工具，全方位优化游戏社区体验!

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [websockets](https://pypi.org/project/websockets) | \>=14.2 |
| [requests](https://pypi.org/project/requests) | ~=2.32.3 |

```
pip install "websockets>=14.2" requests~=2.32.3
```

### 介绍

# EasyBot 机器人插件

> 一款支持全方位功能于一体的服务器管理工具，全方位优化游戏社区体验!
> 目前功能包括消息同步、自定义命令、绑定管理、高级权限控制、群组互动、自定义模板支持以及自定义插件支持等

## 文档

[点我查看](https://docs.inectar.cn/docs/easybot/quick_start/plugin/mcdr/install_mcdr)

## 开发环境

- `Python`: `3.12.8`
- `MCDR`: `2.14.5`

## 适用服务器

> 得益于 MCDR 的工作机制, 你可以在绝大部分服务器上使用 EasyBot。

## 兼容性

`EasyBot_MCDR`是`EasyBot`插件的一个分支,由于实现原理不同,他的特性与功能与`EasyBot-Bukkit`有所不同。


| 特性             | 原因                             |
| -------------- | ------------------------------ |
| 死亡同步           | ❌ 不同服务器实现原理不同,无法稳定判断死亡原因       |
| PlaceholderAPI | ⚠ 不完全支持: 目前只支持 `%player_name%` |

| 特性       | MCDR 解决方案 |
| -------- | --------- |
| 消息同步     | ✅ 支持      |
| 进入退出通知   | ✅ 支持      |
| 强制绑定     | ✅ 支持      |
| 使用命令绑定账号 | ✅ 支持      |
| 命令模式消息同步 | ✅ 支持      |
| 热重载      | ✅ 支持      |
| 执行命令     | ✅ 支持      |
| 绑定时执行命令  | ✅ 支持      |
| 联动原版白名单  | ✅ 支持      |
| 解绑时执行命令  | ✅ 支持      |

## PlaceholderAPI?

PlaceholderAPI 是一个用于 `Bukkit/Spigot` 服务器端的 API，它提供了许多占位符。  
在MCDR中`EasyBot`只实现了`%player_name%`

### 未来计划

> ⚠ 此功能正在开发

检测到服务器安装了PlaceholderAPI 时, 使用RCON执行解析变量。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [EasyBot-MCDR-v1.2.1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.2.1) | 1.2.1 | 2026/01/01 03:00:34 | 40.01KB | 53 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.2.1/EasyBot-MCDR-v1.2.1.mcdr) |
| [EasyBot-v1.2.0-release.1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.2.0-release.1) | 1.2.0-release.1 | 2025/12/06 13:16:49 | 32.59KB | 35 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.2.0-release.1/EasyBot-v1.2.0-release.1.mcdr) |
| [EasyBot-v1.1.7-release.2.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.7-release.2) | 1.1.7-release.2 | 2025/11/22 10:30:17 | 31.05KB | 28 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.7-release.2/EasyBot-v1.1.7-release.2.mcdr) |
| [EasyBot-v1.1.7-release.1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.7-release.1) | 1.1.7-release.1 | 2025/11/22 08:10:50 | 30.63KB | 7 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.7-release.1/EasyBot-v1.1.7-release.1.mcdr) |
| [EasyBot-MCDR-v1.1.7.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.7) | 1.1.7-release1 | 2025/10/24 14:11:59 | 26.77KB | 55 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.7/EasyBot-MCDR-v1.1.7.mcdr) |
| [EasyBot-MCDR.V1.1.6Fix.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/V1.1.6) | 1.1.6 | 2025/10/01 12:49:06 | 27.26KB | 53 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/V1.1.6/EasyBot-MCDR.V1.1.6Fix.mcdr) |
| [EasyBot-MCDR.V1.1.4.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.4) | 1.1.4 | 2025/07/26 10:44:52 | 25.3KB | 93 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.4/EasyBot-MCDR.V1.1.4.mcdr) |
| [EasyBot-MCDR.V1.1.3pre1.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.3-pre1) | 1.1.3 | 2025/06/10 12:06:02 | 24.14KB | 113 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.3-pre1/EasyBot-MCDR.V1.1.3pre1.mcdr) |
| [easybot_mcdr_V1.1.0.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.1.0) | 1.1.0 | 2025/05/06 12:10:08 | 21.94KB | 90 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.1.0/easybot_mcdr_V1.1.0.mcdr) |
| [EasyBot-v1.0.4.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.0.4) | 1.0.4 | 2025/03/26 09:17:07 | 19.11KB | 108 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.0.4/EasyBot-v1.0.4.mcdr) |
| [EasyBot-v1.0.3.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.0.3) | 1.0.3 | 2025/03/23 11:44:45 | 17.72KB | 45 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.0.3/EasyBot-v1.0.3.mcdr) |
| [EasyBot-v1.0.2.mcdr](https://github.com/easybot-team/easybot-mcdr/releases/tag/v1.0.2) | 1.0.2 | 2025/03/16 15:59:16 | 17.15KB | 49 | [下载](https://github.com/easybot-team/easybot-mcdr/releases/download/v1.0.2/EasyBot-v1.0.2.mcdr) |

