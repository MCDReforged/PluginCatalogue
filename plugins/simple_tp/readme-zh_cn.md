[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## simple_tp

### 基本信息

- 插件 ID: `simple_tp`
- 插件名: Simple TP
- 版本: 1.3.3
  - 元数据版本: 1.3.3
  - 发布版本: 1.3.3
- 总下载量: 367
- 作者: [PairZhu](https://github.com/PairZhu)
- 仓库: https://github.com/PairZhu/SimpleTP-MCDR
- 仓库插件页: https://github.com/PairZhu/SimpleTP-MCDR/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 一个简单的传送插件，用于创建传送点并实现EssentialsX的传送功能。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | * |
| [mg_events](/plugins/mg_events/readme-zh_cn.md) | \>=1.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.7 |
| [readerwriterlock](https://pypi.org/project/readerwriterlock) | ==1.0.9 |

```
pip install "mcdreforged>=2.14.7" readerwriterlock==1.0.9
```

### 介绍

# SimpleTP
[English](https://github.com/PairZhu/SimpleTP-MCDR/tree/master/README.md) | **简体中文**

一个简单的传送插件，用于创建传送点并实现EssentialsX的传送功能。

## 预览
![help](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README.zh/1757132558004.png)
![list](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README.zh/1757133070580.png)
![back](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README.zh/1757133504026.png)

## 特点
- 支持个人传送点，玩家可以创建和管理自己的传送点，仅对自己可见
- 支持全局传送点（公共传送点），所有玩家可见，适用于公共区域
- 可配置插件启用的维度，支持Mod中的异维度世界（暮色森林、永恒星光等）
- 支持死亡后返回死亡位置和回到传送前的位置
- 支持大部分命令的点击操作，方便快捷
- easytp语法糖，自动识别传送目标，优先级为`个人传送点 > 公共传送点 > 玩家`
- 支持完善的命令参数补全，可以使用Tab键补全传送点名称和玩家名称（需要配合插件 [command_suggest](https://mcdreforged.com/zh-CN/plugin/command_suggest) 使用）

## 命令
下文以默认前缀"!!stp"为例，实际使用时请根据配置文件中的前缀进行调整。
- !!stp help 查看帮助信息

预览命令请查看 [语言文件](https://github.com/PairZhu/SimpleTP-MCDR/tree/master/./lang/zh_cn.yml) 中的 help 部分。



## 配置文件
配置文件位于`config/SimpleTP/config.json`
- **prefix**: 命令前缀，默认为`!!stp`
- **back_on_death**: 是否在玩家死亡后自动记录位置，默认为`true`
- **save_interval**: 定时保存传送点数据的间隔时间，单位为秒，默认为`30`秒
- **permissions**: 权限配置
- **worlds**: 支持的维度列表（支持Mod中的异维度世界），默认为`["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]`，不在此列表中的维度将无法使用传送功能，如要禁用某个维度的传送功能，将其从列表中移除即可。
- **extra_dimensions**: ***仅 1.16以前的 Minecraft 版本需要配置此项***，配置格式为`{<dimension_id>: "<dimension_name>"}`，例如`{0: "minecraft:overworld", 1: "minecraft:the_nether", 2: "minecraft:the_end"}`。此配置用于支持旧版 Minecraft 中Mod中的异维度世界。
- **easy_tp**: 是否启用 easytp 语法糖，默认为`true`。

### 权限配置
- **back**: 使用`!!stp back`命令的权限
- **tpa**: 使用`!!stp tpa`命令的权限
- **tpahere**: 使用`!!stp tpahere`命令的权限
- **tp**: 使用`!!stp tp <player>`命令的权限
- **tphere**: 使用`!!stp tphere <player>`命令的权限
- **personal_waypoint**: 设置/删除 个人传送点相关命令的权限
- **global_waypoint**: 设置/删除 全局传送点相关命令的权限
- **cross_world_tp**: 跨维度传送的权限

## 依赖插件
- **minecraft_data_api**: 用于获取玩家信息
- **mg_events**: 用于监听玩家死亡事件

## 常见问题
- **点击传送按钮没有反应**
  MCDR对高版本MC的点击执行支持有问题，需要安装 [LetMeClickAndSendForServer](https://github.com/Fallen-Breath/LetMeClickAndSendForServer)(服务端) 或 [LetMeClickAndSend](https://github.com/Fallen-Breath/LetMeClickAndSend)(客户端)。
- **有时死亡后back指令无法回到上一个位置**
  一些Mod的死亡消息比较特殊，可能无法被mg_events监听到。需要手动在mg_events的语言文件中添加对应的死亡消息。例如 [永恒星光](https://www.curseforge.com/minecraft/mc-mods/eternal-starlight) Mod 中，玩家在以太中死亡需要在 `config/mg_events/lang/zh_cn.json` 中添加 `"death.attack.ether": "%1$s飘然而去",`, 在 `config/mg_events/lang/en_us.json` 中添加 `"death.attack.ether": "%1$s drifts away"`。
- **日志输出Player {player} is in a dimension not enabled in config: {dimension}**
  这表示玩家处于一个未在配置文件中启用的维度。请检查 `config/SimpleTP/config.json` 中的 `worlds` 配置，确保包含了此维度。
- **日志输出Player {player} is in an unknown dimension with ID {dimension}**
  服务端 Minecraft 版本为 1.16 以前且安装了异维度 Mod 时，可能会出现此错误。请检查 `config/SimpleTP/config.json` 中的 `extra_dimensions` 配置，确保包含了此维度。维度ID可以通过 `/data get entity <player> Dimension` 命令获取。

## TODO
如有更多功能需求或对某个计划中的功能有兴趣，可以在 issues 中提出🚀
按照优先级排序：
- [x] 支持传送点的点击操作
- [x] back 命令支持往返传送
- [x] 传送点记录玩家的维度（下界、主世界、末地）
- [x] 是否允许跨维度传送配置
- [x] 定时保存传送点数据（防崩溃丢失）
- [x] tp/tphere 功能
- [x] tpa/tpahere 功能
- [x] 多语言支持
- [x] 帮助信息
- [ ] 传送点记录玩家的朝向
- [ ] 添加传送点的描述信息
- [ ] 传送冷却配置
- [ ] 传送点的最大数量限制配置
- [ ] 传送点的名称长度限制配置
- [ ] 传送点安全检测，如传送点在危险位置则提示确认或传送到附近安全位置
- [ ] 传送代价配置 (消耗自定义的物品或经验)(基础消耗+距离消耗)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [SimpleTP-v1.3.3.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.3) | 1.3.3 | 2025/09/10 05:48:09 | 15.97KB | 121 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.3/SimpleTP-v1.3.3.mcdr) |
| [SimpleTP-v1.3.2.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.2) | 1.3.2 | 2025/09/06 10:11:37 | 15.92KB | 29 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.2/SimpleTP-v1.3.2.mcdr) |
| [SimpleTP-v1.3.1.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.1) | 1.3.1 | 2025/09/04 09:31:42 | 15.87KB | 16 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.1/SimpleTP-v1.3.1.mcdr) |
| [SimpleTP-v1.3.0.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.0) | 1.3.0 | 2025/09/03 04:22:54 | 15.81KB | 17 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.0/SimpleTP-v1.3.0.mcdr) |
| [SimpleTP-v1.2.1.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.2.1) | 1.2.1 | 2025/08/26 08:49:38 | 9.59KB | 37 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.2.1/SimpleTP-v1.2.1.pyz) |
| [SimpleTP-v1.2.0.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.2.0) | 1.2.0 | 2025/08/09 10:07:57 | 9.41KB | 43 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.2.0/SimpleTP-v1.2.0.pyz) |
| [SimpleTP-v1.1.4.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.4) | 1.1.4 | 2025/08/03 05:03:13 | 6.69KB | 33 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.4/SimpleTP-v1.1.4.pyz) |
| [SimpleTP-v1.1.3.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.3) | 1.1.3 | 2025/08/02 18:35:33 | 6.53KB | 18 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.3/SimpleTP-v1.1.3.pyz) |
| [SimpleTP-v1.1.2.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.2) | 1.1.2 | 2025/08/02 18:27:15 | 6.47KB | 15 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.2/SimpleTP-v1.1.2.pyz) |
| [SimpleTP-v1.1.1.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.1) | 1.1.1 | 2025/08/02 14:28:38 | 6.15KB | 15 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.1/SimpleTP-v1.1.1.pyz) |
| [SimpleTP-v1.0.0.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.0.0) | 1.0.0 | 2025/08/01 03:41:47 | 4.16KB | 23 | [下载](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.0.0/SimpleTP-v1.0.0.pyz) |

