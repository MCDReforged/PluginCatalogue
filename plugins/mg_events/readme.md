**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mg_events

### Basic Information

- Plugin ID: `mg_events`
- Version: *Data fetching failed*
- Total downloads: N/A
- Authors: [Mooling0602](https://github.com/Mooling0602)
- Repository: https://github.com/Mooling0602/MoreGameEvents-MCDR
- Repository plugin page: https://github.com/Mooling0602/MoreGameEvents-MCDR/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

### Introduction

# MoreGameEvents-MCDR
向MCDR添加更多的游戏事件！

目前已经实现监听和派发玩家死亡和完成进度的事件，仅支持Java版。

## 适用范围
各种Java版游戏服务端，非模组端支持最好

README和文档部分默认不会支持简体中文和英文以外的其他语言，但欢迎PR

本插件理论上适合各种类型的服务端使用，包括带有各种第三方模组的服务器，只要服务端会在控制台严格按照指定的语言文件输出相关的事件信息。

注意：插件的死亡事件识别功能会和DieMessage及类似的BukkitAPI插件冲突，因为他们会修改服务端输出的死亡消息内容！

## 为什么需要此插件
- 为消息互通开发提供更丰富的游戏内事件信息
- 结合Minecraft Data API，为诸如“返回死亡点”等更丰富的玩法开发设计提供基础
- 其他（欢迎参与下游开发，或者为此项目做贡献！）

## 工作原理
将控制台输出的死亡、成就等提示消息，根据游戏的语言文件进行解析，并派发成相关事件供下游插件处理。

因此，本插件仅为没有任何实际功能的API，并不能用于直接实现“死亡播报”等功能，需要用户配合开发者开发的下游插件使用。

## 文档（简易版，已存档，不再更新，适用于v0.x）
考虑到多语言支持，插件并不会直接将识别到的info翻译成中文或类似操作，而是在派发的事件中提供以下内容：
- player 玩家名
- event 事件类型（直接使用翻译键名称即key）
- content 事件内容（字典）
- [1]content.lang 事件信息原始info输出的语言类型，你可以据此判断是否需要进行二次翻译
- content.raw 事件信息的原始info输出，如“Steve被僵尸杀死了”
- content.advancement 成就名称（仅成就事件，暂未实现）
- content.death.killer 击杀者（杀死玩家的人或怪物），若没有则返回None
- content.death.weapon 击杀者使用的武器（参考上一条），若没有则返回None

然后，开发者可二次处理这些信息，并将其转发到需要的地方（例如消息互通转发到其他平台）或进行其他的插件开发。

只需要：
```python
from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, prev_module):
    server.register_event_listener("PlayerDeathEvent", on_player_death) # 需要死亡事件时进行注册
    server.register_event_listener("PlayerAdvancementEvent", on_player_advancement) # 需要成就事件时进行注册

def on_player_death(server: PluginServerInterface, player, event, content):
    player: str = player
    event: str = event # 死亡类型（翻译键名称）
    killer: str = content.death.killer # 击杀者，玩家或怪物名称
    weapon: str = content.death.weapon # 击杀者所用武器（保留了中括号）
    # 由于几乎所有服务端都默认输出英文日志，因此需要进行二次开发，使用event对整个死亡消息进行翻译以及翻译killer（若击杀者为怪物）
    # 本人已开发了一个适用于此的插件，开源后将在下方给出链接以供参考
    # 链接：https://github.com/Mooling0602/DeathTips-MCDR
    # 你也可以自行处理这些
    if content.lang == "zh_cn":
        transfer(content.raw) # 当语言区域为简体中文时，下游无需处理，直接转发使用

# 于 v0.2.0 添加
def on_player_advancement(server: PluginServerInterface, player, event, content):
    player: str = player # 玩家名
    event: str = event # 成就类型（翻译键名称）
    advancement: str = content.advancement # 成就内容（保留了中括号）
    if content.lang == "zh_cn":
        transfer(content.raw) # 当语言区域为简体中文时，下游无需处理，直接转发使用

def transfer():
    pass # 实现你的转发逻辑
```

### 备注
[1] 理论上这一部分可以支持输出中文log的服务端，但是这可能导致其他MCDR插件和MCDR本体无法正常解析服务器日志内容，故不推荐启用服务端的中文或其他语言log

## 语言文件要求及适配指南（已存档，不再更新）
- 仅对本插件而言，要求raw_lang（一般为英文，为服务端输出的所用的语言文件）
- 对据本插件进行了二次开发的插件的用户而言，要求raw_lang和tr_lang（用于翻出译文的语言文件，需和raw_lang严格对应），如果两个文件不相同的话
> tr_lang在下游插件使用，需要开发者支持
- 插件将原生支持Geyser互通服，如果检测到Geyser的语言文件路径，会自动使用（最开箱即用的一集）
- 服务端和其中安装的Mod应该含有raw_lang，你必须将这些分散的语言文件合成为一个，并存放在插件的配置目录中
- 客户端和其中安装的Mod应该同时含有raw_lang和tr_lang，你必须将分散的tr_lang合成为一个，并存放在下游插件的配置目录中
- 如果找不到tr_lang（例如Mod没有完成汉化等情况），你大概需要自行翻译或者放弃翻译
- 如果你运行的模组服，准备完这些，待下游插件开发完成后即可使用

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

*Data fetching failed*

