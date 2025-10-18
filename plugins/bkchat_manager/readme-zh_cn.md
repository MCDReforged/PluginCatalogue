[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## bkchat_manager

### 基本信息

- 插件 ID: `bkchat_manager`
- 插件名: BukkitChatManager
- 版本: 0.3.0
  - 元数据版本: 0.3.0
  - 发布版本: 0.3.0
- 总下载量: 235
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/BukkitChatManager-MCDR
- 仓库插件页: https://github.com/Mooling0602/BukkitChatManager-MCDR/tree/main
- 标签: [`信息`](/labels/information/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 接管BukkitAPI服务端的游戏内聊天。

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
在MCDR接管BukkitAPI服务端的游戏内聊天。

## 依赖
- BukkitAPI 插件：[PlayerLog](https://github.com/Mooling0602/BukkitChatManager-MCDR/blob/main/extra/PlayerLog-1.1.jar)
> 已附加到MCDR插件中，MCDR启动或重载此插件时会自动更新或加载，你可能需要重启服务器以使其生效！

## 用法
从Release中安装此MCDR插件，如果出现问题，请确认依赖是否已经正常加载，有报错请反馈到Issues！

## 配置
配置文件位于`config/bkchat_manager/config.json`，你可以在里面修改聊天消息的格式等。

其中，`%player%`表示玩家名；`%message%`表示聊天消息内容或玩家执行的指令内容；`%src_prefix%`表示指令源。

## 注意事项
和类似的BukkitAPI插件冲突，请不要使用这些同类型的插件。

另外，如果有和依赖中作用相同的替代品插件，此MCDR插件可无缝迁移到其他类型的服务端上；Mohist等支持BukkitAPI的混合端也可以使用。

插件有内置专门的服务端处理器，强烈建议启用，同时启用后无法使用其他的服务端处理器，否则会冲突。

## 更新内容
### 历史日志
- `v0.2.1` 对内置的Bukkit插件依赖进行了更新，添加了客户端聊天拦截的动态控制功能，非生产环境下可以使用/chatmsg on|off进行调试，生产环境下请禁止普通玩家的playerlog.chatmsg权限（将于后续优化）！
- `v0.3.0` 更新了兼容模式（compatibility_mode），你可以通过安装此插件并启用聊天兼容模式的方式，使MCDR本身和MCDR的大部分按规范开发的插件，可以兼容各种会修改聊天内容并影响服务端聊天相关日志输出的Bukkit服务端插件如VentureChat等！

### 计划中

经过测试的服务端：Mohist、Paper、Leaves
> 极低版本的服务端尚未测试，理论上支持1.12及以上的所有Bukkit服务端。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BukkitChatManager-v0.3.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.3.0) | 0.3.0 | 2025/02/06 13:41:06 | 21.15KB | 76 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.3.0/BukkitChatManager-v0.3.0.mcdr) |
| [BukkitChatManager-v0.2.1.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.2.1) | 0.2.1 | 2025/02/05 14:17:30 | 8.38KB | 31 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.2.1/BukkitChatManager-v0.2.1.mcdr) |
| [BukkitChatManager-v0.2.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.2.0) | 0.2.0 | 2024/11/22 12:06:32 | 18.83KB | 38 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.2.0/BukkitChatManager-v0.2.0.mcdr) |
| [BukkitChatManager-v0.1.0.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.1.0) | 0.1.0 | 2024/11/17 10:28:30 | 17.35KB | 29 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.1.0/BukkitChatManager-v0.1.0.mcdr) |
| [BukkitChatManager-v0.0.2.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.0.2) | 0.0.2 | 2024/10/31 10:53:39 | 14.35KB | 34 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.0.2/BukkitChatManager-v0.0.2.mcdr) |
| [BukkitChatManager-v0.0.1.mcdr](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/tag/0.0.1) | 0.0.1 | 2024/10/31 09:44:40 | 1.31KB | 27 | [下载](https://github.com/Mooling0602/BukkitChatManager-MCDR/releases/download/0.0.1/BukkitChatManager-v0.0.1.mcdr) |

