[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## games_ai_extra

### 基本信息

- 插件 ID: `games_ai_extra`
- 插件名: GamesAI Extra
- 版本: 0.2.0
  - 元数据版本: 0.2.0
  - 发布版本: 0.2.0
- 总下载量: 32
- 作者: [yello](https://github.com/PengZixuan30), [man8in](https://github.com/man8in)
- 仓库: https://github.com/PengZixuan30/Games_AI-Extra
- 仓库插件页: https://github.com/PengZixuan30/Games_AI-Extra/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: GamesAI的功能性扩展

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |
| [games_ai](/plugins/games_ai/readme-zh_cn.md) | \>=0.6.4 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [requests](https://pypi.org/project/requests) |  |
| [beautifulsoup4](https://pypi.org/project/beautifulsoup4) |  |

```
pip install requests beautifulsoup4
```

### 介绍

<div align="center">

# GamesAI Extra for MCDReforged

[English](https://github.com/PengZixuan30/Games_AI-Extra/tree/main//README.md)  |  简体中文  |  [繁體中文](https://github.com/PengZixuan30/Games_AI-Extra/tree/main//README.zh-TW.md)

[反馈问题](https://github.com/PengZixuan30/Games_AI-Extra/issues/new)  |  [反馈想法](https://github.com/PengZixuan30/Games_AI-Extra/discussions/new/choose)

</div>

> [!NOTE]
> **GamesAI Extra** 是 [GamesAI](https://github.com/PengZixuan30/Games_AI) 的功能性扩展插件。它为 AI 提供了 **Carpet 假人（Bot）控制**工具、**路径点（坐标）管理**工具、**Minecraft Wiki 搜索**与**白名单管理**工具，允许 AI 在你的 Minecraft 服务器上生成、控制假人、管理路径点、搜索 Wiki 以及管理白名单。

> [!IMPORTANT]
> 此插件需要 **GamesAI >= 0.6.4** 已安装并先加载。GamesAI Extra 遵循[扩展插件系统](https://github.com/PengZixuan30/Games_AI#在自己的mcdr插件中自定义工具)——以此方式注册的工具与内置工具完全相同。

<details>
<summary>目录（点击展开）</summary>

- [GamesAI Extra for MCDReforged](#gamesai-extra-for-mcdreforged)
  - [安装](#安装)
  - [配置](#配置)
  - [工具与Skills](#工具与skills)
    - [Carpet 假人控制](#carpet-假人控制)
      - [生成与移除](#生成与移除)
      - [行为控制](#行为控制)
      - [移动控制](#移动控制)
      - [视角控制](#视角控制)
      - [快捷栏](#快捷栏)
      - [限时动作](#限时动作)
      - [自定义指令](#自定义指令)
    - [路径点管理](#路径点管理)
    - [Minecraft Wiki 搜索](#minecraft-wiki-搜索)
    - [白名单管理](#白名单管理)
    - [Skills](#skills)
  - [依赖说明](#依赖说明)
  - [本次更新](#本次更新)
    - [Version 0.2.0](#version-020)
    - [Version 0.1.3](#version-013)
    - [Version 0.1.2](#version-012)
    - [Version 0.1.1](#version-011)
  - [许可证](#许可证)

</details>

## 安装

在 MCDR 控制台中使用以下命令安装插件：

`!!MCDR plugin install games_ai_extra`

---

或者从 [MCDR 插件仓库](https://mcdreforged.com/plugin/games_ai_extra) 获取并放置到你的插件目录中。

此插件需要 Python 包 `requests` 和 `beautifulsoup4`，它们已在插件元数据中声明，通过 `!!MCDR plugin install` 安装时会自动安装。若手动放置打包后的 `.mcdr` 文件，请确保你的 Python 环境中已安装这些包。

## 配置

默认配置文件（`config/games_ai_extra/config.json`）结构如下：

```json
{
    "carpet": true,
    "location_plguin": false,
    "where2go_plugin": true,
    "whitelist_api": true,
    "web_search": true
}
```

- **carpet**：设为 `true` 启用 Carpet 假人工具；设为 `false` 禁用。
- **location_plguin**：设为 `true` 启用基于 [Location Marker](https://mcdreforged.com/plugin/location_marker) MCDR 插件的路径点管理；设为 `false` 禁用。
- **where2go_plugin**：设为 `true` 启用基于 [Where2Go](https://mcdreforged.com/plugin/where2go) MCDR 插件的路径点管理；设为 `false` 禁用。
- **whitelist_api**：设为 `true` 启用基于 [WhitelistAPI](https://mcdreforged.com/plugin/whitelist_api) MCDR 插件的白名单管理；设为 `false` 禁用。
- **web_search**：设为 `true` 启用 Minecraft Wiki 搜索工具；设为 `false` 禁用。

> [!TIP]
> `location_plguin` 和 `where2go_plugin` 提供的是同一套路径点工具（`add_pos_pos`、`add_pos_here`、`remove_pos`、`search_pos`、`get_all_pos`）。建议只启用**其中一个**，避免工具重复注册。默认启用 `where2go_plugin`。

修改配置后，使用 `!!gamesai reload` 使更改生效。

## 工具与Skills

启用后，以下工具会自动注册到 GamesAI 中，AI 可通过 `!!ask` 调用。

### Carpet 假人控制

> 🤖 **技能：** 操作假人之前务必阅读 `carpet.md`。调用 `read_skills("carpet.md")` 获取完整说明。

假人控制工具由 `carpet` 模块提供。需要服务端安装 **fabric-carpet** 模组。`spawn_bot` 和 `kill_bot` 额外注册了 `@register_bot_tool()`，可供 Mineflayer 自主 Bot 控制器调用。

#### 生成与移除

|     工具      |               参数               | 用途                                                                                                                                                     |
| :---------: | :----------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `spawn_bot` | `name`、`pos?`、`player?`、`dim?` | 在服务器中生成一个假人。可指定 `pos`（坐标 `[x, y, z]`）在特定位置生成，或指定 `player`（玩家名）在某玩家身边生成。`pos` 与 `player` 互斥。可选指定 `dim`（如 `minecraft:the_nether`）在特定维度生成。不指定位置时在世界出生点生成。 |
| `kill_bot`  |             `name`             | 移除（杀死）一个假人。此操作不可逆——如需重新使用请用 `spawn_bot` 重新生成。                                                                                                          |

#### 行为控制

|      工具      |             参数              | 用途                                                                                                                                                                                                                          |
| :----------: | :-------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bot_action` | `name`、`action`、`interval?` | 控制假人执行动作。支持的动作：`attack`（攻击，需手持武器）、`use`（右键目标）、`mine`（挖掘面前方块）、`stop`（停止所有动作）、`drop`（丢弃手中物品）、`dropStack`（丢弃整组物品）、`jump`（跳跃）、`sneak`（切换潜行）、`swapHands`（交换左右手）、`mount`（骑乘附近实体）、`dismount`（下马）。可选 `interval` 为游戏刻（tick）间隔（默认 1）。 |

#### 移动控制

|     工具     |         参数         | 用途                                                                                            |
| :--------: | :----------------: | --------------------------------------------------------------------------------------------- |
| `bot_move` | `name`、`direction` | 让假人持续向某个方向移动：`forward`（前进）、`backward`（后退）、`left`（向左）、`right`（向右）。假人会一直移动，直到发送 `stop` 动作或改变方向。 |

#### 视角控制

|     工具     |       参数        | 用途                                                                                                       |
| :--------: | :-------------: | -------------------------------------------------------------------------------------------------------- |
| `bot_look` | `name`、`target` | 控制假人看向某个方向或坐标。`target` 可以是方向词（`north`、`south`、`east`、`west`、`up`、`down`）或坐标（`"x y z"`，如 `"100 64 200"`）。 |

#### 快捷栏

|      工具      |      参数       | 用途                                            |
| :----------: | :-----------: | --------------------------------------------- |
| `bot_hotbar` | `name`、`slot` | 切换假人当前选中的快捷栏格子（1~9）。切换后攻击/使用/挖掘等操作将使用对应格子的物品。 |

#### 限时动作

|         工具         |             参数             | 用途                                                                                                                            |
| :----------------: | :------------------------: | ----------------------------------------------------------------------------------------------------------------------------- |
| `bot_timed_action` | `name`、`action`、`duration` | 让假人执行一个限时动作，到达指定秒数后自动停止。支持：`attack`、`use`、`mine`、`forward`、`backward`、`left`、`right`。适合短时间操作（建议 ≤ 60 秒）。注意：会阻塞当前 AI 对话直到时间到达。 |

#### 自定义指令

|      工具       |        参数        | 用途                                                                                                |
| :-----------: | :--------------: | ------------------------------------------------------------------------------------------------- |
| `bot_command` | `name`、`command` | 向假人发送一条原始自定义 `/player` 指令，用于上述工具无法覆盖的高级操作。命令会自动补全为 `player <name> <command>` 格式。需要了解 Carpet 假人指令。 |

### 路径点管理

路径点工具由 `location_plguin`（Location Marker）或 `where2go_plugin`（Where2Go）提供。同一时间只需启用其中一个。

|       工具       |            参数            | 用途                                                                                      |
| :------------: | :----------------------: | --------------------------------------------------------------------------------------- |
| `add_pos_pos`  | `name`、`pos`、`dimension` | 在指定坐标添加一个路径点。`pos` 为 `[x, y, z]`，`dimension` 为维度（如 `overworld`、`the_nether`、`the_end`）。 |
| `add_pos_here` |          `name`          | 在玩家当前位置添加一个路径点。仅玩家调用时有效（控制台无法使用）。                                                       |
|  `remove_pos`  |          `name`          | 按名称删除一个路径点。Where2Go 版本支持名称模糊匹配。                                                         |
|  `search_pos`  |          `name`          | 按名称搜索路径点并返回详细信息。                                                                        |
| `get_all_pos`  |          _（无）_           | 获取所有已注册的路径点列表。                                                                          |

### Minecraft Wiki 搜索

|           工具            |   参数    | 用途                                                                                                                             |
| :---------------------: | :-----: | ------------------------------------------------------------------------------------------------------------------------------ |
| `search_minecraft_wiki` | `query` | 搜索 Minecraft Wiki。服务器语言为英文时使用 `minecraft.wiki`，否则使用 `zh.minecraft.wiki`。搜索结果页返回标题列表，精确匹配时返回（截断后的）条目正文。同时注册为 Mineflayer Bot 工具。 |

### 白名单管理

白名单工具由 `whitelist_api` 模块提供，需要 [WhitelistAPI](https://mcdreforged.com/plugin/whitelist_api) MCDR 插件。

|           工具            |    参数    | 用途                         |
| :---------------------: | :------: | -------------------------- |
|  `get_whitelist_name`   |  _（无）_   | 获取所有白名单玩家列表。               |
|   `add_to_whitelist`    | `player` | 将一名玩家添加到白名单。需要发起者权限等级 ≥ 3。 |
| `remove_from_whitelist` | `player` | 将一名玩家从白名单移除。需要发起者权限等级 ≥ 3。 |

### Skills

GamesAI Extra 通过 `register_skills()` 提供以下内置技能：

| 技能文件        | 描述                                            |
| ----------- | --------------------------------------------- |
| `carpet.md` | 指导 AI 如何正确生成、控制和移除 Carpet 假人。操作假人之前务必读取此技能文件。 |

> [!TIP]
> Skills 就像 AI 的「标准作业程序 (SOP)」——确保 AI 每次都遵循正确的工作流程。AI 可使用 `read_skills` 工具读取技能文件。

## 依赖说明

每个工具模块需要对应的服务端依赖才能正常工作：

| 模块                | 所需依赖                                                                      |
| ----------------- | ------------------------------------------------------------------------- |
| `carpet`          | 服务端模组 [fabric-carpet](https://github.com/gnembon/fabric-carpet)           |
| `location_plguin` | MCDR 插件 [Location Marker](https://mcdreforged.com/plugin/location_marker) |
| `where2go_plugin` | MCDR 插件 [Where2Go](https://mcdreforged.com/plugin/where2go)               |
| `whitelist_api`   | MCDR 插件 [WhitelistAPI](https://mcdreforged.com/plugin/whitelist_api)      |
| `web_search`      | Python 包 `requests` 和 `beautifulsoup4`（自动安装）                              |

如果未安装对应依赖，调用相关工具时将返回错误提示。

## 本次更新

### Version 0.2.0

- 新增 `web_search` 模块：`search_minecraft_wiki` 工具，用于搜索 Minecraft Wiki（根据服务器语言自动选择英文或中文 Wiki），AI 与 Mineflayer Bot 均可调用
- 新增 `whitelist_api` 模块：`get_whitelist_name`、`add_to_whitelist`、`remove_from_whitelist` 三个白名单管理工具，基于 WhitelistAPI MCDR 插件（添加/移除需要权限等级 ≥ 3）
- 所有面向用户的工具消息改用翻译键，内置 `en_us`、`zh_cn`、`zh_tw` 语言文件
- GamesAI 依赖要求提升至 >= 0.6.4
- 新增 Python 依赖 `requests` 和 `beautifulsoup4`（Wiki 搜索工具所需）

### Version 0.1.3

- 修复了一些问题

### Version 0.1.2

- 为 `spawn_bot` 和 `kill_bot` 添加 `@register_bot_tool()` 装饰器，支持 Mineflayer Bot 调用
- 通过 `register_skills()` API 注册 `carpet.md` 技能文件
- 添加 `register_self()` 支持，`!!gamesai reload` 时自动重载
- 支持解压目录（开发模式）和打包 `.mcdr` zip（分发模式）两种运行方式

### Version 0.1.1

- 新增路径点管理工具，支持 `location_plguin`（Location Marker）和 `where2go_plugin`（Where2Go）模块
- 为 `spawn_bot` 和 `kill_bot` 添加 `@register_bot_tool()` 装饰器，支持 Mineflayer Bot 调用
- 各工具模块可通过 `config.json` 独立启用/禁用
- 首个正式版本，包含 Carpet 假人控制工具

## 许可证

MIT License, Copyright (c) 2026 yello

<div align = "center">

---

[回到顶部](#gamesai-extra-for-mcdreforged)

</div>

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [GamesAIExtra-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI-Extra/releases/tag/0.2.0) | 0.2.0 | 2026/08/22 05:47:52 | 34.93KB | 7 | [下载](https://github.com/PengZixuan30/Games_AI-Extra/releases/download/0.2.0/GamesAIExtra-v0.2.0.mcdr) |
| [GamesAIExtra-v0.1.3.mcdr](https://github.com/PengZixuan30/Games_AI-Extra/releases/tag/0.1.3) | 0.1.3 | 2026/08/19 02:50:40 | 28.09KB | 7 | [下载](https://github.com/PengZixuan30/Games_AI-Extra/releases/download/0.1.3/GamesAIExtra-v0.1.3.mcdr) |
| [GamesAIExtra-v0.1.2.mcdr](https://github.com/PengZixuan30/Games_AI-Extra/releases/tag/0.1.2) | 0.1.2 | 2026/08/07 07:25:35 | 28.01KB | 18 | [下载](https://github.com/PengZixuan30/Games_AI-Extra/releases/download/0.1.2/GamesAIExtra-v0.1.2.mcdr) |

