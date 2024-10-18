[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## where2go

### 基本信息

- 插件 ID: `where2go`
- 插件名: Where2go
- 版本: 0.2.5
  - 元数据版本: 0.2.5
  - 发布版本: 0.2.5
- 总下载量: 207
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

# 演示

![show](https://raw.githubusercontent.com/LazyAlienServer/Where2go/main/show.jpg)

# ToDo

- [ ] 将主世界和地狱的两个坐标点进行关联
- [ ] `!!wp add here/<player>`快速将玩家位置添加为坐标点

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [Where2go-v0.2.5.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.5) | 0.2.5 | 2024/09/27 16:16:38 | 23.17KB | 57 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.5/Where2go-v0.2.5.mcdr) |
| [Where2go-v0.2.4.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.4) | 0.2.4 | 2024/09/15 11:54:46 | 23.17KB | 36 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.4/Where2go-v0.2.4.mcdr) |
| [Where2go-v0.2.3.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.3) | 0.2.3 | 2024/08/31 14:58:18 | 23.16KB | 49 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.3/Where2go-v0.2.3.mcdr) |
| [Where2go-v0.2.2.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.2) | 0.2.2 | 2024/08/03 12:59:43 | 23.17KB | 37 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.2/Where2go-v0.2.2.mcdr) |
| [Where2go-v0.2.1.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.1) | 0.2.1 | 2024/07/30 06:17:13 | 23.21KB | 6 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.1/Where2go-v0.2.1.mcdr) |
| [Where2go-v0.2.0.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.2.0) | 0.2.0 | 2024/07/28 10:20:13 | 23.22KB | 7 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.2.0/Where2go-v0.2.0.mcdr) |
| [Where2go-v0.1.2.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.1.2) | 0.1.2 | 2024/07/24 08:54:35 | 22.19KB | 10 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.1.2/Where2go-v0.1.2.mcdr) |
| [Where2go-v0.1.1.mcdr](https://github.com/LazyAlienServer/Where2go/releases/tag/v0.1.1) | 0.1.1 | 2024/07/23 10:11:02 | 22.19KB | 5 | [下载](https://github.com/LazyAlienServer/Where2go/releases/download/v0.1.1/Where2go-v0.1.1.mcdr) |

