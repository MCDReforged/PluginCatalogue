**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## bot_kikai

### Basic Information

- Plugin ID: `bot_kikai`
- Plugin Name: BotKikai
- Version: 0.2.0
  - Metadata version: 0.2.0
  - Release version: 0.2.0
- Total downloads: 74
- Authors: [Jerry_FaGe](https://github.com/Jerry-FaGe), [RayanceKing](https://github.com/RayanceKing)
- Repository: https://github.com/Jerry-FaGe/MCDR-BotKikai
- Repository plugin page: https://github.com/Jerry-FaGe/MCDR-BotKikai/tree/master
- Labels: [`Tool`](/labels/tool/readme.md), [`Management`](/labels/management/readme.md)
- Description: 适用于 MCDR 的将假人存储至列表并提供指令映射，便捷放置，操作界面等功能的插件。

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | \>=1.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# MCDR-BotKikai（Bot機械）

适用于 [MCDR](https://github.com/Fallen-Breath/MCDReforged) 的将假人存储至列表并提供指令映射，便捷放置，操作界面等功能的插件。
需要安装前置插件 [MinecraftDataAPI](https://github.com/MCDReforged/MinecraftDataAPI) 。

> 君は道具ではなく、その名が似合う人になろんだ

此插件本意是为了方便记性不好记不住每个机器的挂机假人名字和英文不好的玩家，使其可以用中文操作某机器对应的假人（觉得聊天框中文不好打的甚至可以用拼音）。

假如你有一台刷沙机, 开关在 [0, 64, 0] 的位置。本插件可以实现让你在世界的任何位置输入指令 `!!bk 刷沙机 use` 都可以随时在指定位置召唤假人以开关这台刷沙机（顺便挂机）。

```Minecraft
!!bk: 显示本帮助信息
!!bk list [online|offline]: 显示假人列表，可筛选在线或离线
!!bk reload: 重载插件配置
!!bk add <name> <kikai>: 使用当前玩家参数添加一个名为<name>用于<kikai>的假人
!!bk add <name> <kikai> <dim> <pos> <facing>: 使用自定义参数添加一个名为<name>用于<kikai>的假人
!!bk del <kikai>: 从假人列表移除用于<kikai>的假人
!!bk <kikai>: 输出一个可点击的界面，自动根据假人是否在线改变选项
!!bk <kikai> spawn: 召唤一个用于<kikai>的假人
!!bk <kikai> kill: 干掉用于<kikai>的假人
!!bk <kikai> where: 假人发光两分钟并输出坐标
!!bk <kikai> use: 假人右键一次
!!bk <kikai> huse <interval>: 假人持续右键，后接正整数可控制间隔 gt
!!bk <kikai> atk: 假人左键一次
!!bk <kikai> hatk <interval>: 假人持续左键, 后接正整数可控制间隔 gt
!!bk <kikai> stop: 假人停止一切动作
```

## 功能补充
* 参数中的 `<kikai>` 指红石机械，`<name>` 指假人的真实名字。

  如果想让 `SandBot` 控制 `刷沙机`，则 `<name>` 为 `SandBot`，`<kikai>` 为 `刷沙机`。

  假人器械映射，顾名思义，`!!bk SandBot spawn` 和 `!!bk 刷沙机 spawn` 的运作效果是一样的，其他指令同理。

  `<name>` 应该为 MC 中所存在的玩家名。

* 本插件支持MCDR的权限系统，可以在 `utils.py` 文件修改使用指令的权限等级。

  默认的权限配置为：
  * user 及以上组可以操作假人 (spawn, use ,kill)
  * admin 及以上组可以操作假人列表 (add, remove)

* `!!bk list`: 输出一个类似下面的界面，不带参数可以显示本插件储存的所有假人，带上 `online/offline` 参数可以单独显示当前在线或离线的假人，可以通过点击进行操作。
  ```Minecraft
  ----------- Jerry_FaGe 在线 -----------
  此假人用于: 发哥, 开发者, test
  [下线] [停止] [报点] [右键] [持续右键] [左键] [持续左键] 

  ----------- SandBot 在线 -----------
  此假人用于: 刷沙机, shuashaji
  [下线] [停止] [报点] [右键] [持续右键] [左键] [持续左键] 

  ----------- Stonebot 离线 -----------
  此假人用于: 刷石机, shuashiji
  [上线] [报点] [右键] [持续右键] [左键] [持续左键]
  ```
* `!!bk reload`: 重载 [config.json](https://github.com/Jerry-FaGe/MCDR-BotKikai/blob/master/config.json) 配置文件，用于用户修改配置。配置文件详见下文 **关于配置文件**。

* `!!bk add <name> <kikai>`: 使用玩家当前的维度，坐标，朝向添加一个假人。也就是说如果玩家用准星指着开关使用此指令后，召唤出的假人可以直接 use 开关。如果想修改当前存在的假人信息可以直接重新 add ，只要假人名字一样新 add 的信息会覆盖旧的。

  **注:** 由于 carpet 本身原因，假人无法 use 拉杆（也不一定，我在新版本测试是能用的），如果机器的开关是拉杆形式的请自行替换成音符盒式或其他支持假人 use 的方式。

* `!!bk add <name> <kikai> <dim> <pos> <facing>`: 使用指令中的自定义参数添加一个假人，可用作挂机点等对假人朝向没有要求的场景。

* `!!bk <kikai>`: 输出一个可点击的界面，自动根据假人是否在线改变选项
  * 假人在线:
    ```Minecraft
    ----------- SandBot 在线 -----------
    用于: 刷沙机, shuashaji
    维度: minecraft:overworld
    坐标: [-2.439826988598193, 7.0, -5.05480960268401]
    朝向: [180.59103, 29.550417]
    [下线] [停止] [报点] [右键] [持续右键] [左键] [持续左键]
    ```
  * 假人离线:
    ```Minecraft
    ----------- Stonebot 离线 -----------
    用于: 刷石机, shuashiji
    维度: minecraft:overworld
    坐标: [4.589996529809662, 7.0, -4.426900981652432]
    朝向: [-214.02008, 31.20023]
    [上线] [报点] [右键] [持续右键] [左键] [持续左键]
    ```

## 关于配置文件

配置文件 [config.json](https://github.com/Jerry-FaGe/MCDR-BotKikai/blob/master/config.json) 是一个json格式文件。它一般储存在 `MCDR/config/bot_kikai` 文件夹下，如果想实现上文中的效果，它的格式应该如下：

```JSON
{
    "Jerry_FaGe": {
        "nicknames": ["Jerry_FaGe", "发哥", "开发者", "test"],
        "dimension": "minecraft:overworld",
        "position": [0, 70, 0],
        "facing": [0, 0]
    },
    "SandBot": {
        "nicknames": ["SandBot", "刷沙机"],
        "dimension": "minecraft:overworld",
        "position": [-2.439826988598193, 7.0, -5.05480960268401],
        "facing": [180.59103, 29.550417]
    },
    "Stonebot": {
        "nicknames": ["Stonebot", "刷石机"],
        "dimension": "minecraft:overworld",
        "position": [4.589996529809662, 7.0, -4.426900981652432],
        "facing": [-214.02008, 31.20023]
    }
}
```

除了使用`add`, `del`指令操作假人列表外，用户还可以根据配置文件的格式自行增删改，改完之后去游戏中执行`!!bk reload`即可更新修改后的假人列表。

## 声明

本插件实现的功能只要是装了 Carpet Mod 能召唤假人的服务端都可以实现，即便是这样也仍有可能引发争议。烦请想装本插件的腐竹实装前务必了解下成员们的意愿。

特别感谢 [AnzhiZhang](https://github.com/AnzhiZhang) 的 [Bot](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/bot) 插件提供的部分逻辑。

TODO:
- [x] 分开显示离线和在线假人
- [ ] 修复部分操作下指令无反馈
- [ ] 将权限配置文件化

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [BotKikai-v0.2.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.2.0) | 0.2.0 | 2025/08/15 11:52:11 | 20.35KB | 10 | [Download](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.2.0/BotKikai-v0.2.0.mcdr) |
| [BotKikai-v0.1.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.1.0) | 0.1.0 | 2025/07/14 08:14:12 | 20.18KB | 64 | [Download](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.1.0/BotKikai-v0.1.0.mcdr) |

