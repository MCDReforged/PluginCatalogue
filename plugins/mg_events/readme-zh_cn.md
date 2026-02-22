[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mg_events

### 基本信息

- 插件 ID: `mg_events`
- 插件名: MoreGameEvents
- 版本: 1.1.2
  - 元数据版本: 1.1.1
  - 发布版本: 1.1.2
- 总下载量: 1624
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/MoreGameEvents-MCDR
- 仓库插件页: https://github.com/Mooling0602/MoreGameEvents-MCDR/tree/main
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 向MCDR添加更多的游戏事件！

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |
| [online_player_api](/plugins/online_player_api/readme-zh_cn.md) | \>=1.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# MoreGameEvents-MCDR
向MCDR添加更多的游戏事件！

目前已经实现监听和派发玩家死亡和完成进度的事件，仅支持Java版高版本。

v1.0.0版本现已发布，保留了基础事件格式的兼容，并支持i18n，但原content部分进行了重构，无法兼容旧版本，对接此插件的消息互通类插件需要重新适配！

> [!CAUTION]
> 1.0.0和0.x版本完全不兼容，包括旧有的配置文件！
> 
> 如果你使用对接此插件的Im类插件，在相关插件发布适配更新以前，请继续使用0.3.1版本；如果你使用诸如返回死亡点（[DeathBack](https://mcdreforged.com/zh-CN/plugin/death_back)）的功能性插件，则可以直接更新

## 适用范围
各种Java版游戏服务端，非模组端支持最好

README和文档部分默认不会支持简体中文以外的其他语言，但欢迎PR

本插件理论上适合各种类型的服务端使用，包括带有各种第三方模组的服务器，只要服务端会在控制台严格按照指定的语言文件输出相关的事件信息。

注意：插件的死亡事件识别功能会和DieMessage及类似的BukkitAPI插件冲突，因为他们会修改服务端输出的死亡消息内容！

## 为什么需要此插件
- 为消息互通开发提供更丰富的游戏内事件信息
- 结合Minecraft Data API，为诸如“返回死亡点”等更丰富的玩法开发设计提供基础
- 其他（欢迎参与下游开发，或者为此项目做贡献！）

## 工作原理
将控制台输出的死亡、成就等提示消息，根据游戏的语言文件进行解析，并派发成相关事件供下游插件处理。

关于多语言和事件消息处理：见文档部分。

现在若服务端的语言和你的本地语言不同，插件会在解析完游戏事件后在控制台发送一条翻译后的事件消息以供参考，你需要将MCDR的语言设置为你的本地语言以使用此功能。

> [!CAUTION]
> 若服务端日志中存在游戏事件内容，但未触发此插件的日志，视为插件工作异常，请立即在此仓库发起Issue进行反馈以帮助解决问题！

## 文档（简易版）
插件在派发的事件中按以下固定的参数来提供有用的信息：
- player 玩家名（为字符串）
- event 事件类型（直接使用翻译键名称即字典key名，为字符串）
- content 事件内容（列表，下面i代表列表中的任意对象）
- i.locale 事件信息原始info输出的语言类型，如`"zh_cn"`
- i.raw 事件信息的原始info输出，如`"Steve被僵尸杀死了"`
- i.advancement 成就名称（仅在玩家成就事件中，不含字符颜色和中括号）
- i.killer 击杀者（杀死玩家的人或怪物），若没有则返回None（仅在玩家死亡事件中）
- i.weapon 击杀者使用的武器（参考上一条），若没有则返回None（仅在玩家死亡事件中）

然后，开发者可将需要的内容转发到需要的地方（例如消息互通转发到其他平台）或进行更多的插件开发。

简单示例：
```python
from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, prev_module):
    server.register_event_listener("PlayerDeathEvent", on_player_death) # 需要死亡事件时进行注册
    server.register_event_listener("PlayerAdvancementEvent", on_player_advancement) # 需要成就事件时进行注册

def on_player_death(server: PluginServerInterface, player, event, content):
    player: str = player
    event: str = event # 死亡类型（翻译键名称）
    for i in content:
        if i.locale == 'zh_cn': # 需要明确指定你要使用哪种语言
            killer = i.killer
            weapon = i.weapon
            transfer(i.raw) # 转发原版死亡消息文本

def on_player_advancement(server: PluginServerInterface, player, event, content):
    player: str = player # 玩家名
    event: str = event # 成就类型（翻译键名称）
    for i in content:
        if i.locale == 'zh_cn': # 需要明确指定你要使用哪种语言
            advancement = i.advancement
            transfer(i.raw) # 转发原版成就消息文本

# 成就消息文本默认匹配了原版的格式，使用了格式化代码
# 如果你要转发到外部Im平台，需要手动移除，或提醒用户修改此插件配置以禁用文本颜色

def transfer():
    pass # 实现你的转发逻辑
```

## 语言文件要求及适配指南
- 插件一般会内置最新正式版的游戏语言文件，开箱即用
- 互通服可以修改插件配置将语言文件的路径改到Geyser下，以便使用Geyser获取的语言文件，更新更及时
- 语言文件的文件名必须是合法的语言类型，如`zh_cn`
- 没有提供语言文件的语言类型，无法支持
- 你必须指定一个语言文件（大部分情况下为`en_us`）用于识别，且该文件的语言类型必须匹配服务端的日志输出
> 插件工作的基础

## 其他
插件的README和文档部分的文本内容风格需要改善，欢迎PR！

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MoreGameEvents-v1.1.2.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/1.1.2) | 1.1.2 | 2025/10/06 04:39:55 | 209.08KB | 493 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/1.1.2/MoreGameEvents-v1.1.2.mcdr) |
| [MoreGameEvents-v1.1.1.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/1.1.1) | 1.1.1 | 2025/08/18 04:58:49 | 194.74KB | 219 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/1.1.1/MoreGameEvents-v1.1.1.mcdr) |
| [MoreGameEvents-v1.1.0.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/1.1.0) | 1.1.0 | 2025/04/17 12:34:20 | 195.51KB | 348 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/1.1.0/MoreGameEvents-v1.1.0.mcdr) |
| [MoreGameEvents-v1.0.0.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/1.0.0) | 1.0.0 | 2025/04/03 08:55:38 | 194.34KB | 61 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/1.0.0/MoreGameEvents-v1.0.0.mcdr) |
| [MoreGameEvents-v0.3.1.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/0.3.1) | 0.3.1 | 2025/01/06 06:57:18 | 200.1KB | 286 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/0.3.1/MoreGameEvents-v0.3.1.mcdr) |
| [MoreGameEvents-v0.3.0.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/0.3.0) | 0.3.0 | 2025/01/06 06:50:10 | 200.09KB | 30 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/0.3.0/MoreGameEvents-v0.3.0.mcdr) |
| [MoreGameEvents-v0.2.3.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/0.2.3) | 0.2.3 | 2024/12/22 14:13:30 | 198.84KB | 54 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/0.2.3/MoreGameEvents-v0.2.3.mcdr) |
| [MoreGameEvents-v0.2.2.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/0.2.2) | 0.2.2 | 2024/12/11 13:48:39 | 199.36KB | 45 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/0.2.2/MoreGameEvents-v0.2.2.mcdr) |
| [MoreGameEvents-v0.2.1.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/0.2.1) | 0.2.1 | 2024/12/10 13:06:24 | 209.82KB | 28 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/0.2.1/MoreGameEvents-v0.2.1.mcdr) |
| [MoreGameEvents-v0.2.0.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/0.2.0) | 0.2.0 | 2024/12/07 14:54:44 | 209.97KB | 28 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/0.2.0/MoreGameEvents-v0.2.0.mcdr) |
| [MoreGameEvents-v0.1.0.mcdr](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/tag/0.1.0) | 0.1.0 | 2024/11/30 10:32:24 | 198.2KB | 32 | [下载](https://github.com/Mooling0602/MoreGameEvents-MCDR/releases/download/0.1.0/MoreGameEvents-v0.1.0.mcdr) |

