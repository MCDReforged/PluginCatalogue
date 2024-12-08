[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## bkchat_manager

### 基本信息

- 插件 ID: `bkchat_manager`
- 插件名: BukkitChatManager
- 版本: 0.2.0
  - 元数据版本: 0.2.0
  - 发布版本: 0.2.0
- 总下载量: 24
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/BukkitChatManager-MCDR
- 仓库插件页: https://github.com/Mooling0602/BukkitChatManager-MCDR/tree/main
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 接管BukkitAPI服务端的游戏内聊天

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [strip_ansi](https://pypi.org/project/strip_ansi) |  |

```
pip install strip_ansi
```

### 介绍

# BukkitChatManager-MCDR
---
- [en_US]

Manage chat in game for BukkitAPI servers in MCDR.

## Dependency
- BukkitAPI Plugin: [PlayerLog](https://github.com/Mooling0602/BukkitChatManager-MCDR/blob/main/extra/PlayerLog-1.0-SNAPSHOT.jar)

## Usage
Install need BukkitAPI plugin in **Dependency** first,
> Install this to disable server sent chat messages to clients by default, then the MCDR plugin can manage these messages after.

then install this MCDR plugin from release.

## Configuration
Located in `config/bkchat_manager/config.json`, default config is written by zh_CN, you can edit it to feat your language.

Among them, `%player%` represents the playername; `%message%` represents the chat content or commands player executed; `%src_prefix%` represents the command source, e.g. `MCDR`, `Server`.

## NOTE
Conflicts with similar BukkitAPI chat management plugins, please do not use these same type of plugins!

---
- [zh_CN]

在MCDR接管BukkitAPI服务端的游戏内聊天。

## 依赖
- BukkitAPI 插件：[PlayerLog](https://github.com/Mooling0602/BukkitChatManager-MCDR/blob/main/extra/PlayerLog-1.0-SNAPSHOT.jar)

## 用法
先安装**依赖**部分中的BukkitAPI插件，
> 以禁止服务端默认地向客户端发送聊天消息，然后此MCDR插件就可以接管这些消息并进行处理。

然后从Release中安装此MCDR插件。

## 配置
配置文件位于`config/bkchat_manager/config.json`，你可以在里面修改聊天消息的格式等。

其中，`%player%`表示玩家名；`%message%`表示聊天消息内容或玩家执行的指令内容；`%src_prefix%`表示指令源。

## 注意事项
和类似的BukkitAPI插件冲突，请不要使用这些同类型的插件。

另外，如果有和依赖中作用相同的替代品插件，此MCDR插件可无缝迁移到其他类型的服务端上；Mohist等支持BukkitAPI的混合端也可以使用。

经过测试的服务端：Mohist、Paper

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BukkitChatManager-v0.2.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.2.0) | 0.2.0 | 2024/11/22 12:06:32 | 18.83KB | 7 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.2.0/BukkitChatManager-v0.2.0.mcdr) |
| [BukkitChatManager-v0.1.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.1.0) | 0.1.0 | 2024/11/17 10:28:30 | 17.35KB | 4 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.1.0/BukkitChatManager-v0.1.0.mcdr) |
| [BukkitChatManager-v0.0.2.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.0.2) | 0.0.2 | 2024/10/31 10:53:39 | 14.35KB | 9 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.0.2/BukkitChatManager-v0.0.2.mcdr) |
| [BukkitChatManager-v0.0.1.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.0.1) | 0.0.1 | 2024/10/31 09:44:40 | 1.31KB | 4 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.0.1/BukkitChatManager-v0.0.1.mcdr) |

