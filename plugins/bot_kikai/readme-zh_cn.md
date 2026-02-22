[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## bot_kikai

### 基本信息

- 插件 ID: `bot_kikai`
- 插件名: BotKikai
- 版本: 0.5.0
  - 元数据版本: 0.5.0
  - 发布版本: 0.5.0
- 总下载量: 418
- 作者: [Jerry_FaGe](https://github.com/Jerry-FaGe), [RayanceKing](https://github.com/RayanceKing)
- 仓库: https://github.com/Jerry-FaGe/MCDR-BotKikai
- 仓库插件页: https://github.com/Jerry-FaGe/MCDR-BotKikai/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 使用中文名称即可将假人精准召唤到任意位置，支持多种动作。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | \>=1.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# MCDR-BotKikai（Bot機械）

一个基于 [MCDR](https://github.com/Fallen-Breath/MCDReforged) 的 Minecraft 假人管理插件，专注于简化 [Carpet](https://github.com/gnembon/fabric-carpet) 假人的管理和操作。

> 君は道具ではなく、その名が似合う人になろんだ

## 📝 简介

本插件旨在解决以下问题：

- 记不住每个机器的假人名字？
- 不习惯输入英文指令？
- 想在家里快速开关远处、其他维度的机器？

只需为每个假人设置中文别名，就能通过简单的中文名字来操控它们。比如，对于一个叫 `SandBot` 的假人，你可以给它起个别名叫"刷沙机"，这样 `!!bk SandBot spawn` 和 `!!bk 刷沙机 spawn` 的效果是完全一样的！也就是说你不需要记住哪个假人控制哪个机器，只需要确认你想开关哪个机器。

你可以在世界的任意位置输入指令 `!!bk 刷沙机 use` 即可让假人 `SandBot` 自动在刷沙机处上线，并右键开关来开启刷沙机（顺便挂机）。

> 上古版本的[介绍视频](https://www.bilibili.com/video/BV1Rf4y1C776) By: [Nachuan川川](https://space.bilibili.com/107251863)

## 🚀 特性

- 支持假人别名系统（中文、拼音等都可以）
- 方便的假人位置和朝向记录
- 交互式的操作界面
- 支持假人前后缀
- 支持权限管理
- 配置文件热重载

## ⚙️ 依赖

- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) >= 2.0.0
- [MinecraftDataAPI](https://github.com/Fallen-Breath/MinecraftDataAPI) >= 1.1.0
- Minecraft 服务端需要安装 [Carpet](https://github.com/gnembon/fabric-carpet) 模组

## 📖 命令说明

基础命令（可于配置文件中自定义）：

```minecraft
!!bk
```

所有可用命令：

| 命令                                             | 说明              | 权限等级  |
| ---------------------------------------------- | --------------- | ----- |
| !!bk                                           | 显示帮助信息          | 所有人   |
| !!bk list [online|offline]                     | 显示假人列表，可筛选在线或离线 | 所有人   |
| !!bk reload                                    | 重载插件配置          | admin |
| !!bk add <name\> <kikai\>                      | 使用当前玩家位置添加假人    | admin |
| !!bk add <name\> <kikai\> [dim] [pos] [facing] | 使用自定义参数添加假人     | admin |
| !!bk del <kikai\>                              | 删除指定假人          | admin |
| !!bk <kikai\>                                  | 显示假人详细信息和操作界面   | user  |

假人操作命令：

| 命令                               | 说明                | 权限等级 |
| -------------------------------- | ----------------- | ---- |
| !!bk <kikai\> spawn              | 在对应位置生成假人         | user |
| !!bk <kikai\> kill               | 移除假人              | user |
| !!bk <kikai\> where              | 显示假人位置（会让假人发光2分钟） | user |
| !!bk <kikai\> use                | 假人右键一次            | user |
| !!bk <kikai\> huse [<interval\>] | 假人持续右键，可选间隔时间（gt） | user |
| !!bk <kikai\> atk                | 假人左键一次            | user |
| !!bk <kikai\> hatk [<interval\>] | 假人持续左键，可选间隔时间（gt） | user |
| !!bk <kikai\> stop               | 停止假人的所有动作         | user |

## ⚡ 快速上手

1. 为刷沙机添加一个假人并设置位置：

    ```minecraft
    !!bk add SandBot 刷沙机
    ```

   玩家站在期望的位置和朝向执行此命令，假人的位置和朝向会被自动记录。

   你也可以手动指定位置（不建议，挺麻烦的）：

    ```minecraft
    !!bk add SandBot 刷沙机 minecraft:overworld 0 64 0 -154.43 3.90
    ```

2. 使用假人：

    ```minecraft
    !!bk 刷沙机           # 显示假人信息和操作界面
    !!bk 刷沙机 spawn     # 召唤假人到记录的位置
    !!bk 刷沙机 use       # 让假人右键一次
    !!bk 刷沙机 hatk 12   # 让假人每 12gt 左键一次
    !!bk 刷沙机 stop      # 让假人停止动作
    !!bk 刷沙机 kill      # 让假人下线
    ```

## ⚙️ 配置文件

插件会在 `MCDR/config/bot_kikai` 目录下创建两个配置文件：

1. `config.json` - 插件基础配置：

    ```json
    {
        "prefix_short": "!!bk",
        "spawn_max_wait_time": 10.0,
        "spawn_check_interval": 0.5,
        "bot_name_prefix": "",
        "bot_name_suffix": "",
        "permission": {
            "bot": 1,
            "list": 3
        }
    }
    ```

   配置项说明：

   - prefix_short: 命令前缀
   - spawn_max_wait_time: 等待假人生成的最大时间（秒）
   - spawn_check_interval: 检查假人是否生成的间隔（秒）
   - bot_name_prefix: 在 Carpet 中设置的假人前缀
   - bot_name_suffix: 在 Carpet 中设置的假人后缀
   - permission.bot: 操作假人的最低权限等级
   - permission.list: 管理假人的最低权限等级

2. `bots.json` - 假人数据：

    ```json
    {
        "SandBot": {
            "nicknames": ["SandBot", "刷沙机", "shuashaji"],
            "dimension": "minecraft:overworld",
            "position": [-2.44, 7.0, -5.05],
            "facing": [180.59, 29.55]
        }
    }
    ```

   配置项说明：

   - nicknames: 假人的所有别名列表
   - dimension: 假人所在维度
   - position: 假人的位置坐标 [x, y, z]
   - facing: 假人的朝向角度 [水平角, 垂直角]

## 🔒 权限系统

插件使用 MCDR 的[权限](https://docs.mcdreforged.com/zh-cn/latest/permission.html#permission-file)系统，默认配置：

- 假人操作权限（spawn、use、kill 等）：需要 user 及以上权限
- 假人管理权限（add、remove 等）：需要 admin 及以上权限

权限等级对应关系：

- guest = 0
- user = 1
- helper = 2
- admin = 3
- owner = 4

## 📝 注意事项

- **关于前后缀配置**：
  - 如果服务器开启了假人前后缀，请务必在本插件配置文件中配置相同的前后缀，以防止预期之外的情况发生；
  - 如果服务器没有开启假人前后缀，您依然可以配置本插件的前后缀，这样由本插件创建的假人都会带有配置的前后缀。
- **关于命令点击执行**：
  - 自 Minecraft 1.19.1-rc1 起，由于游戏安全性更新，点击聊天框中的命令按钮将无法直接执行非 `/` 开头的命令
  - 这影响了 MCDR 插件的交互体验，包括本插件在内的绝大部分插件都改用了 `suggest_command`（命令建议）模式
  - 点击命令按钮后，命令会被填充到聊天框中，需要玩家手动按回车执行
  - 这也带来了一个好处：对于类似 `!!bk <kikai> huse [间隔gt]` 这样需要自定义参数的命令，玩家可以在发送前修改参数
  - 具体详见 [MCDReforged #203](https://github.com/MCDReforged/MCDReforged/issues/203)
- 对于某些版本的 Carpet 模组，假人可能无法操作拉杆，建议替换成音符盒式开关或其他支持假人右键的方式。

## ⚠️ 声明

本插件实现的功能只要是装了 Carpet Mod 能召唤假人的服务端都可以实现，即便是这样也仍有可能引发**不香草**争议。烦请想装本插件的腐竹实装前务必了解下成员们的意愿。

## 🤝 致谢

- 感谢 [Fallen_Breath](https://github.com/Fallen-Breath) 开发的 [MCDR](https://github.com/Fallen-Breath/MCDReforged) 框架
- 感谢 [Carpet](https://github.com/gnembon/fabric-carpet) 模组提供的假人功能
- 感谢 [AnzhiZhang](https://github.com/AnzhiZhang) 的 [Bot](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/bot) 插件提供的灵感

## 📄 开源协议

[GPL-3.0 License](https://github.com/Jerry-FaGe/MCDR-BotKikai/tree/master/LICENSE)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BotKikai-v0.5.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.5.0) | 0.5.0 | 2025/09/03 08:49:34 | 21.75KB | 193 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.5.0/BotKikai-v0.5.0.mcdr) |
| [BotKikai-v0.4.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.4.0) | 0.4.0 | 2025/08/29 09:58:15 | 21.61KB | 33 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.4.0/BotKikai-v0.4.0.mcdr) |
| [BotKikai-v0.3.1.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.3.1) | 0.3.1 | 2025/08/21 10:00:20 | 20.7KB | 34 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.3.1/BotKikai-v0.3.1.mcdr) |
| [BotKikai-v0.3.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.3.0) | 0.3.0 | 2025/08/20 09:42:58 | 20.54KB | 26 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.3.0/BotKikai-v0.3.0.mcdr) |
| [BotKikai-v0.2.1.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.2.1) | 0.2.1 | 2025/08/18 08:27:53 | 20.37KB | 24 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.2.1/BotKikai-v0.2.1.mcdr) |
| [BotKikai-v0.2.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.2.0) | 0.2.0 | 2025/08/15 11:52:11 | 20.35KB | 27 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.2.0/BotKikai-v0.2.0.mcdr) |
| [BotKikai-v0.1.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.1.0) | 0.1.0 | 2025/07/14 08:14:12 | 20.18KB | 81 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.1.0/BotKikai-v0.1.0.mcdr) |

