[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## bkchat_manager

### 基本信息

- 插件 ID: `bkchat_manager`
- 插件名: BukkitChatManager
- 版本: 0.3.1
  - 元数据版本: 0.3.1
  - 发布版本: 0.3.1
- 总下载量: 324
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/BukkitChatManager-MCDR
- 仓库插件页: https://github.com/Mooling0602/BukkitChatManager-MCDR/tree/main/src
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 接管BukkitAPI服务端的游戏内聊天。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.15.0 |
| [packaging](https://pypi.org/project/packaging) |  |
| [psutil](https://pypi.org/project/psutil) |  |

```
pip install "mcdreforged>=2.15.0" packaging psutil
```

### 介绍

# BukkitChatManager-MCDR

在 MCDR 接管服务端内的游戏聊天。

> 目前支持 BukkitAPI，但你也可以接入到其他服务端中。
> 
> 由于历史遗留原因，插件名称将继续保留“bukkit”字样。

## 依赖
- BukkitAPI 插件：[PlayerLog](https://github.com/Mooling0602/PlayerLog-Bukkit)

> 此 MCDR 插件会自动管理安装，你可能需要重启服务器以完成重载。

## 用法

从 Release 中安装此MCDR插件，如果出现问题，请确认依赖是否已经正常加载，有报错请反馈到 Issues！

## 配置

配置文件位于 `config/bkchat_manager/config.json`，你可以在里面修改聊天消息的格式等。

其中，`%player%` 表示玩家名；`%message%` 表示聊天消息内容或玩家执行的指令内容；`%src_prefix%` 表示指令源。

## 注意事项

和类似的 BukkitAPI 插件冲突，请不要使用这些同类型的插件。

> 其他服务端同理，不再赘述。

另外，如果有和依赖中作用相同的替代品插件，此 MCDR 插件可无缝迁移到其他类型的服务端上；Mohist等支持 BukkitAPI 的混合端也可以使用。

> 自 v0.4.0 版本起，需要修改配置文件才能使用未经验证的服务端插件。

插件自 v0.4.0 版本起不再需要定制的服务端处理器，你可以根据需要来自行配置。

经过测试的服务端：Mohist、Paper、Leaves、Folia、Luminol（已停止维护）

> 极低版本的服务端尚未测试，理论上支持 1.13 及以上的所有 Bukkit 服务端。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BukkitChatManager-v0.3.1.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.3.1) | 0.3.1 | 2026/07/14 12:55:50 | 4.65KB | 8 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.3.1/BukkitChatManager-v0.3.1.mcdr) |
| [BukkitChatManager-v0.3.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.3.0) | 0.3.0 | 2025/02/06 13:41:06 | 21.15KB | 96 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.3.0/BukkitChatManager-v0.3.0.mcdr) |
| [BukkitChatManager-v0.2.1.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.2.1) | 0.2.1 | 2025/02/05 14:17:30 | 8.38KB | 45 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.2.1/BukkitChatManager-v0.2.1.mcdr) |
| [BukkitChatManager-v0.2.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.2.0) | 0.2.0 | 2024/11/22 12:06:32 | 18.83KB | 50 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.2.0/BukkitChatManager-v0.2.0.mcdr) |
| [BukkitChatManager-v0.1.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.1.0) | 0.1.0 | 2024/11/17 10:28:30 | 17.35KB | 43 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.1.0/BukkitChatManager-v0.1.0.mcdr) |
| [BukkitChatManager-v0.0.2.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.0.2) | 0.0.2 | 2024/10/31 10:53:39 | 14.35KB | 44 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.0.2/BukkitChatManager-v0.0.2.mcdr) |
| [BukkitChatManager-v0.0.1.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.0.1) | 0.0.1 | 2024/10/31 09:44:40 | 1.31KB | 38 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.0.1/BukkitChatManager-v0.0.1.mcdr) |

