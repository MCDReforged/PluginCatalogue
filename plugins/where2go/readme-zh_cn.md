[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## where2go

### 基本信息

- 插件 ID: `where2go`
- 插件名: Where2go
- 版本: 0.3.0
  - 元数据版本: 0.3.0
  - 发布版本: 0.3.0
- 总下载量: 931
- 作者: [tanh_Heng](https://github.com/tanhHeng)
- 仓库: https://github.com/LazyAlienServer/Where2go
- 仓库插件页: https://github.com/LazyAlienServer/Where2go/tree/main
- 标签: [`信息`](/labels/information/readme-zh_cn.md)
- 描述: 一个功能强大的位置插件，包含共享坐标点、查询玩家位置等功能

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.6.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# Where2go
一个功能强大的位置插件，包含共享坐标点、查询玩家位置等功能

需要`Python >= 3.10`

# 功能

*README中指令全部按照默认配置文件书写，指令前缀可通过配置文件更改*

## 共享坐标点

`!!wp add <xaero-waypoint>` 添加Xaero坐标点

在Xaero地图中分享坐标点后，插件可**自动识别**。点击临时坐标点后方的`[+]`即可添加。若两个坐标点距离过近，插件会进行提示，以防重复添加。

`!!wp remove <id>` 移除坐标点

`!!wp list [page]` 列出所有的坐标点。`page`为可选项，不填则默认为`1`

`!!wp search <name>` 按照坐标点名称`name`搜索坐标点

`!!wp info <id>` 查看id为`id`的坐标点详情

## 更先进的!!here与!!vris

`!!here` 广播自身位置。若100m内有坐标点，则同时提示"附近的坐标点"

`!!vris <player>` 查询玩家`player`位置。若该玩家100m内有坐标点，则同时提示"附近的坐标点"

此功能用于快速辨别玩家位置，如玩家位于全物品附近。同时在部分情况下可以快速找到该玩家附近的地狱门

## 更”智能“的查询

聊天发送`XXX在哪`即可快速查询坐标点`XXX`或玩家`XXX`的位置

## 演示

![show](https://raw.githubusercontent.com/LazyAlienServer/Where2go/main/show.jpg)

## 配置文件

### xaero

**click_event_format** `str`

- 添加Xaero坐标点的按钮格式。可选：
  + `"simple"`：样式为`[+X]`，简易模式，不支持**Xaero's Minimap v24.6.0及以上**的版本。
  + `"compatible"`：样式为`[+X#]`，兼容模式。点击`+X`部分可以让旧版本Xaero直接添加坐标点，点击`#`部分可以通过玩家发送坐标点信息的方式，让客户端Xaero识别到坐标点分享信息，出现`[add]`按钮，点击`[add]`即可添加坐标点。

*我们暂不清楚Xaero's Minimap v24.6+的坐标点添加文本格式是什么样的。如果你知晓新的格式，请通过issue反馈*

### command

**waypoints** `str`
- 坐标点相关指令的指令前缀

**whereis** `str`
- 查询玩家位置的指令前缀

**here** `str`
- 发送自身位置的指令

**fastsearch_regex** `str`
- 快速询问的正则匹配。如果你想要支持英文，可以改成像这样：`[wW]here ((is)|(are)|(r)) (?P<name>\w+)\??`

**fastsearch_prompt** `str`
- 快速询问在MCDR的`!!help`界面显示的命令帮助

### player_api

获取玩家位置等指令、识别指令回显相关。一般服务端无需更改。

###

# ToDo

- [ ] 将主世界和地狱的两个坐标点进行关联
- [ ] `!!wp add here/<player>`快速将玩家位置添加为坐标点

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [Where2go-v0.3.0.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.3.0) | 0.3.0 | 2025/03/19 13:55:21 | 23.42KB | 270 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.3.0/Where2go-v0.3.0.mcdr) |
| [Where2go-v0.2.5.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.5) | 0.2.5 | 2024/09/27 16:16:38 | 23.17KB | 360 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.5/Where2go-v0.2.5.mcdr) |
| [Where2go-v0.2.4.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.4) | 0.2.4 | 2024/09/15 11:54:46 | 23.17KB | 59 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.4/Where2go-v0.2.4.mcdr) |
| [Where2go-v0.2.3.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.3) | 0.2.3 | 2024/08/31 14:58:18 | 23.16KB | 70 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.3/Where2go-v0.2.3.mcdr) |
| [Where2go-v0.2.2.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.2) | 0.2.2 | 2024/08/03 12:59:43 | 23.17KB | 60 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.2/Where2go-v0.2.2.mcdr) |
| [Where2go-v0.2.1.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.1) | 0.2.1 | 2024/07/30 06:17:13 | 23.21KB | 26 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.1/Where2go-v0.2.1.mcdr) |
| [Where2go-v0.2.0.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.0) | 0.2.0 | 2024/07/28 10:20:13 | 23.22KB | 30 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.0/Where2go-v0.2.0.mcdr) |
| [Where2go-v0.1.2.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.1.2) | 0.1.2 | 2024/07/24 08:54:35 | 22.19KB | 30 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.1.2/Where2go-v0.1.2.mcdr) |
| [Where2go-v0.1.1.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.1.1) | 0.1.1 | 2024/07/23 10:11:02 | 22.19KB | 26 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.1.1/Where2go-v0.1.1.mcdr) |

