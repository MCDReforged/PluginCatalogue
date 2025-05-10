[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## division

### 基本信息

- 插件 ID: `division`
- 插件名: Division
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 27
- 作者: [bzyyyyyyyy](https://github.com/bzyyyyyyyy)
- 仓库: https://github.com/bzyyyyyyyy/MCDR-Division
- 仓库插件页: https://github.com/bzyyyyyyyy/MCDR-Division/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`信息`](/labels/information/readme-zh_cn.md)
- 描述: 玩家分组和留言

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [online_player_api](/plugins/online_player_api/readme-zh_cn.md) | * |
| [player_ip_logger](/plugins/player_ip_logger/readme-zh_cn.md) | * |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.1.0 |
| [requests](https://pypi.org/project/requests) | \>=2.30.0 |
| [pytz](https://pypi.org/project/pytz) | \>=2023.3 |
| [redis](https://pypi.org/project/redis) | \>=3.5.3 |
| [rejson](https://pypi.org/project/rejson) | \>=0.5.6 |

```
pip install "mcdreforged>=2.1.0" "requests>=2.30.0" "pytz>=2023.3" "redis>=3.5.3" "rejson>=0.5.6"
```

### 介绍

![MCDR-Division](https://socialify.git.ci/bzyyyyyyyy/MCDR-Division/image?custom_description=%E4%B8%80%E4%B8%AA%E6%94%AF%E6%8C%81%E5%B0%86%E7%8E%A9%E5%AE%B6%E5%88%86%E7%BB%84%26%E5%90%91%E7%BB%84%2F%E7%8E%A9%E5%AE%B6%E7%95%99%E8%A8%80%E7%9A%84%E6%8F%92%E4%BB%B6&description=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F63280128&name=1&owner=1&pattern=Floating+Cogs&theme=Light)

# MCDR-Division
---------

**中文** | [English](https://github.com/bzyyyyyyyy/MCDR-Division/tree/master/./README_en.md)

一个支持将玩家分组&向组/玩家留言的插件

## 功能

- **玩家分组**：支持创建多个不同的组，玩家可以同时进入多个组，支持一键将所有玩家加入组。
- **发送留言**：玩家可以自由地向组或者玩家留言，支持 MC 的[颜色代码](https://zh.minecraft.wiki/w/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)，以及自动将网址转换为可被点击的文字。
- **查看留言**：每次玩家上线时，将会显示留给该玩家和该玩家进入的组的留言，可选以日期顺序或以组顺序排列。
- **多种存储方式**：插件支持使用 JSON 或 [Redis](https://redis.io/) 存储组、玩家以及留言信息。
- **多服共享信息**：使用 [Redis](https://redis.io/) 存储信息支持多个服共享组、玩家以及留言信息。
- **权限设置**：根据MCDR权限限制玩家加入组、退出组、删除留言、删除组的操作。
- **自定义颜色**：支持自定义插件中的组或玩家的颜色，不限于MC自带的16种颜色。
- **最近在线时间显示**：插件将根据最近在线时间对玩家进行排序，并根据此顺序显示玩家列表。
- **时区检测**：插件将根据玩家的ip获取该玩家的时区，并根据时区显示所有插件记录的时间。
- **流畅交互**：大部分操作都能通过点击文字执行。

## 依赖

需要 `v2.1.0` 以上的 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)

需要 [OnlinePlayerAPI](https://mcdreforged.com/zh-CN/plugin/online_player_api)，[Player IP Logger](https://mcdreforged.com/zh-CN/plugin/player_ip_logger)

Python 包要求：见 [requirements.txt](https://github.com/bzyyyyyyyy/MCDR-Division/tree/master/requirements.txt)

## 命令格式说明

`!!div` 显示帮助信息

`!!div search <keyword> [<page>]` 搜索组/玩家，返回所有匹配项

`!!div list [<page>]` 显示所有组

`!!div ids [<page>]` 显示所有玩家

`!!div info <group/player_id>` 显示组/玩家的信息

`!!div make <group> [<perm>] [<color>]` 创建一个新组

`!!div join <group> [<player_id>]` 加入组/让玩家加入组

`!!div leave <group> [<player_id>]` 离开组/让玩家离开组

`!!div perm <group> <perm>` 更改组的使用权限

`!!div color <group> <color>` 更改组的颜色

`!!div send <group/player_id> <msg>` 向组/玩家留言

`!!div edit <group/player_id> <lineNo.> <msg>` 修改组/玩家的第 `<lineNo.>` 行留言

`!!div del <group/player_id> <lineNo.>` 删除组/玩家的第 `<lineNo.>` 行留言

`!!div del <group/player_id>` 删除组

`!!div confirm` 再次确认是否删除组/留言

`!!div place <group> <pos>` 更改组的显示位置

`!!div check [time/group]` 查看留给自己的言，可选以日期顺序或以组顺序排列

`!!div <keyword> [<page>]` 同 `!!div search`

## 配置文件说明

路径：`config/division/config.json`

#### item_per_page

默认值：`10`

使用 `!!div list <page>` ， `!!div list <page>` 或 `!!div search <keyword> <page>` 后

每一页显示的指令堆数量

#### default_perm

默认值：`1`

使用 `!!div make <group> [<perm>] [<color>]` 不输入 `[<perm>]` 时，默认的权限值

#### default_color

默认值：`"white"`

使用 `!!div make <group> [<perm>] [<color>]` 不输入 `[<color>]` 时，默认的颜色

#### default_sender

默认值：`"server"`

非玩家（如：服务器终端）使用插件时默认的 id

示例：

1. 非玩家使用 `!!div send <group/player_id> <msg>` 时，插件将会把 `server` 储存为发送者

2. 非玩家使用 `!!div join <group>` 时，插件会让 `server` 加入组

3. 非玩家使用 `!!div check [time/group]` 时，插件会显示留给 `server` 的言

#### default_check_mode

默认值：`"time"`

在玩家上线，或者使用 `!!div check` 后，默认的留言排列顺序

| 值       | 含义          |
| ------- | ----------- |
| `time`  | 优先以时间顺序排列留言 |
| `group` | 优先以组的顺序排列留言 |


#### perm_to_modify_all

默认值：`1`

玩家使用 `!!div join <group> All` 或 `!!div leave <group> All` 所需要的权限

#### msg_for_new_player

默认值：`""`

新玩家加入服务器时由插件留给玩家个人的言

#### redis_ip

默认值：`""`

Redis 服务端的ip地址

如果不为 `""` 则使用 Redis 存储组、玩家以及留言信息（示例：`"127.0.0.1"` ）

如果为 `""` 则使用 JSON 存储组、玩家以及留言信息

#### redis_port

默认值：`6379`

Redis 服务端的端口

#### redis_db

默认值：`1`

Redis 服务端的数据库索引

#### redis_password

默认值：`""`

Redis 服务端的密码

## 颜色格式

以下是可以输入参数 `<color>` 的值：

- [MC 颜色](https://zh.minecraft.wiki/w/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)（示例：`white` ， `black`）
- RGB 代码（示例：`00AAFF` ， `0x00AAFF` ， `#00AAFF`）

## 转义符

由于玩家无法在游戏内输入符号 `§` 导致无法使用MC的颜色代码

此插件提供了 `$` 作为转义符

即当玩家在留言时使用 `$` 时，插件会将其转换为符号 `§`

而当玩家需要输入符号 `$` 时，输入 `$$` 即可

## 网址转换

插件会将所有以 `http` 开头，以空格结尾的内容识别为网址

并将其转换为可以被点击的文字

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [Division-v1.0.0.mcdr](https://github.com/bzyyyyyyyy/MCDR-Division/releases/tag/v1.0.0) | 1.0.0 | 2024/12/22 06:12:49 | 59.96KB | 27 | [下载](https://github.com/bzyyyyyyyy/MCDR-Division/releases/download/v1.0.0/Division-v1.0.0.mcdr) |

