[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## chunk_backup

### 基本信息

- 插件 ID: `chunk_backup`
- 插件名: Chunk Backup
- 版本: 2.0.3
  - 元数据版本: 2.0.3
  - 发布版本: 2.0.3
- 总下载量: 1564
- 作者: [FRUITS_CANDY](https://github.com/FRUITS-CANDY), [Bexerlmao](https://github.com/Bexerlmao)
- 仓库: https://github.com/Passion-Never-Dissipate/Chunk_BackUp
- 仓库插件页: https://github.com/Passion-Never-Dissipate/Chunk_BackUp/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一个以区块为单位备份或回档的MCDR插件

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.1 |
| [candy_tools](/plugins/candy_tools/readme-zh_cn.md) | \>=1.0.2 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.15.1 |

```
pip install "mcdreforged>=2.15.1"
```

### 介绍

# Chunk Backup —— 区块备份插件，v2.0.0 焕新登场！

[![MCDReforged](https://img.shields.io/badge/MCDReforged-≥2.15.1-blue)](https://mcdreforged.com)
[![Minecraft](https://img.shields.io/badge/Minecraft-1.16--26.1-green)]()
[![GitHub release](https://img.shields.io/github/v/release/Passion-Never-Dissipate/Chunk_BackUp)]()

> ⚠️ **警告**  
> **v2.0.0 是一次完全重写的大版本升级，与旧版 v1.x 不兼容！**  
> 旧版备份数据**无法直接在新版中使用**，请务必阅读下方的「升级指南」.

> 如果你正在使用插件的2.0.0-2.0.2版本，请立刻升级插件至2.0.3，然后删除插件旧的配置文件重新生成，否则备份回档可能出现问题!!!!

> 具体问题见：[26.1版本及以上服务端生成的配置文件错误](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/issues/4) [空区域文件导致读取错误，路径误用导致权限错误](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/issues/5)

> 💡 **提示**
> - 当前版本支持 Minecraft 1.16以后的所有正式版，并自动适配26.1前后的新世界存储结构。
> - 需要 MCDReforged **≥2.15.1** 和 **必须的前置插件** [candy_tools](https://github.com/Passion-Never-Dissipate/candy_tools) **≥1.0.2**（缺少它将导致插件无法正常工作）。
> - 建议将服务端编码设为 UTF-8（详见配置说明）。
> - 遇到问题先检查插件是否为最新版，并确认配置文件是否正确。
> - 若发现问题或有改进建议，欢迎提交 Issue 或 PR，也可加入交流群：**417086159**。

---

## 📌 新版简介

**Chunk Backup** 是一款以 **区块（chunk）** 为最小单位的 Minecraft 服务器备份插件。它只备份你指定的区块范围，而不是整个世界，从而大幅节省存储空间和操作时间。

**v2.0.0 是一次脱胎换骨的重构**，我们重写了命令系统、任务调度、备份格式和错误处理，带来了更可靠、更易用的体验：

- **全新命令树**：相较于以前复杂且难以理解的命令，新版本命令更容易理解，直观，功能更多。
- **任务队列与确认机制**：所有耗时操作（备份、回档、删除）均进入队列，支持 `!!cb confirm` 和 `!!cb abort`，告别误操作。
- **智能版本适配**：自动识别服务端版本，配置文件自动切换26.1版本前后的存储结构（`dimensions/minecraft/...`）。
- **玩家数据备份**：拥有Carpet Mod时，备份时自动收集选区内的玩家数据，回档时可选择一并恢复。
- **完整操作日志**：每次危险任务都会生成日志，可追溯任务状态、执行者和结果。
- **备份索引文件**：每个备份目录下生成 `index.json`，明确记录备份范围与外部区块，确保可恢复性。

---

## 🚀 主要特性

### 🧩 区块级精确操作
- 支持三种选区方式：
  - **半径模式**：以玩家所在区块为中心，备份 `2×半径+1` 边长的正方形区域（最小为单个区块）。
  - **两点模式**：通过两个世界坐标确定矩形范围，自动转换为区块坐标。
  - **维度模式**：备份整个维度的所有区域文件（如主世界、下界、末地）。

### 📦 智能处理超大区块
- 当区块数据超过 **1020 KiB** 时，自动将其内容存储为外部文件（`c.x.z.mcc`），区域文件中仅保留标记。
- 备份与恢复时自动处理这些外部文件，完美兼容原版机制。

### 👤 玩家数据备份（需 Carpet Mod 和 candy_tools）
- 在安装 Carpet Mod 且启用 candy_tools 插件的情况下，备份时会自动备份选区内玩家的物品栏，坐标，成就等数据。
- 回档时可选择 **同时恢复玩家数据**（需添加 `-d` 参数），确保玩家进度与区块同步。
- 玩家数据独立存储，与区块备份分开管理，灵活可控。

### 🔄 智能版本适配
- 自动检测 Minecraft 服务端版本，配置文件自动切换26.1版本前后的存储结构（`dimensions/minecraft/...`）。
- 无需手动修改配置文件，插件自动切换路径规则。

### 🛡️ 安全可靠的任务管理
- **任务队列**：所有耗时操作作为独立任务运行，避免阻塞服务器主线程。
- **确认与中断**：
  - `!!cb confirm` 确认危险操作，`!!cb abort` 随时中止等待中的任务。
  - 重型任务（如回档）与轻型任务分离，互不干扰。
- **自动回滚保护**：回档前自动创建“回档前备份”（overwrite），若回档失败，插件会自动尝试恢复到此状态，最大限度保护存档。

### 📜 完整日志追溯
- 每次备份、回档、删除操作都会生成详细日志，保存最近 **100 条** 记录。
- 通过 `!!cb log list` 和 `!!cb log show` 可查看任务状态、执行者、执行时间及结果。
- 日志文件以 JSON 格式存储，便于外部分析。

### 🗂️ 备份索引文件
- 每个备份目录下都会生成 `index.json`，明确记录：
  - 备份类型（全区域/部分区块）
  - 包含的区块范围
  - 外部区块列表（若有）
- **重要提示**：每个备份目录下的 `info.json` 文件存储了该备份的所有元数据（日期、注释、维度等），是备份有效的核心标识。**切勿手动删除或修改**，否则该备份将被视为无效，无法用于回档。

### ⚡ 高性能并发处理
- 使用线程池并行处理多个区域的区块导出/合并操作。
- 支持配置最大并发线程数（`max_workers`），在性能与资源占用间取得平衡。

### 🌍 多维度支持
- 配置文件支持自定义多个维度，每个维度可指定：
  - 世界文件夹名称
  - 区域文件夹路径（支持多个，如 `region`、`entities`、`poi`）
  - 维度描述和整数 ID（用于命令输入）
- 开箱即支持主世界、下界、末地，也可轻松添加其他模组维度。

### 🎮 人性化命令设计
- 基于 MCDReforged 原生命令节点构建，支持 **Tab 补全** 和 **参数提示**。
- 提供详细的指令帮助，输入 `!!cb help <指令>` 即可查看用法示例。
- 支持 `-s`（静态备份）、`-d`（回档时恢复玩家数据）、`-c`（跳过确认）等便捷参数。

---

## 📦 安装

1. **确保已安装前置插件**：`candy_tools` 是必须的前置插件，缺少它将导致 Chunk Backup 无法正常工作。请先安装 [candy_tools](https://github.com/Passion-Never-Dissipate/candy_tools) **≥1.0.2**。
2. **安装 Chunk Backup**：你可以通过以下任意一种方式安装：
   - **推荐：使用 MCDR 插件管理器**  
     在游戏内或控制台执行命令：  
     `!!MCDR plugin install chunk_backup`  
     插件管理器将自动下载并安装最新版本。
   - **手动安装**  
     从 [GitHub Releases](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases) 页面下载最新版本的插件（`.mcdr` 或源码包），放入 MCDR 的 `plugins` 文件夹。
3. 启动/重启 MCDR，插件会自动生成配置文件 `config/chunk_backup/config.json`。
4. 根据需要修改配置文件（详见下文「配置」），然后输入 `!!cb reload` 重载。

> ⚠️ **注意**
> - 若你的服务端使用 Spigot/Paper 等多世界文件夹结构，请确保在配置中为每个维度正确设置 `world_name` 和 `region_folder`。
> - 如果服务端输出乱码，请参考 [MCDR 文档](https://docs.mcdreforged.com/zh-cn/latest/configuration.html#handler) 设置正确的处理器（handler）和 UTF-8 编码。

---

## ⚙️ 配置

配置文件位于 `config/chunk_backup/config.json`。首次运行插件时会自动生成默认配置，请根据实际情况修改。

### 根字段

| 字段                  | 类型     | 默认值                 | 说明                                     |
| ------------------- | ------ | ------------------- | -------------------------------------- |
| `server_root`       | string | `"./server"`        | 服务端文件夹路径                               |
| `storage_root`      | string | `"./cb_files"`      | 插件数据存储根目录                              |
| `log_storage`       | string | `"logs"`            | 日志存储子目录（相对于 `storage_root`）            |
| `static_storage`    | string | `"static_storage"`  | 静态备份存储子目录                              |
| `dynamic_storage`   | string | `"dynamic_storage"` | 动态备份存储子目录                              |
| `overwrite_storage` | string | `"overwrite"`       | 回档前自动备份存放目录                            |
| `max_workers`       | int    | `4`                 | 文件操作的最大并发线程数                           |
| `ensure_no_carpet`  | bool   | `false`             | 是否强制在未安装 Carpet Mod 时仍尝试玩家数据备份（可能导致错误） |
| `config_version`    | string | 插件版本                | 配置文件版本（自动管理，请勿手动修改）                    |
| `minecraft_version` | string | 自动检测                | 上次备份时的 Minecraft 版本，用于路径自动升级           |

### 命令配置（`command`）

#### `command.prefix`
- 类型：string
- 默认值：`"!!cb"`
- 说明：插件指令的前缀，修改后需重载生效。

#### `command.permission`
权限级别字典，控制各子命令的访问权限。数值含义参考 [MCDR 权限系统](https://mcdreforged.readthedocs.io/zh_CN/latest/permission.html)。默认值如下：

```json
{
    "root": 0,
    "make": 1,
    "pmake": 1,
    "dmake": 1,
    "back": 2,
    "restore": 2,
    "del": 2,
    "list": 0,
    "show": 0,
    "log": 1,
    "help": 0,
    "confirm": 1,
    "abort": 1,
    "reload": 3
}
```

#### `command.confirm_time_wait`
- 类型：字符串（带单位的时间，如 `"60s"`）
- 默认值：`"60s"`
- 说明：执行危险操作时等待确认的超时时间。

#### `command.restore_countdown_sec`
- 类型：int
- 默认值：`10`
- 说明：回档前服务器关闭倒计时的秒数。

### 服务端配置（`server`）

#### `server.turn_off_auto_save`
- 类型：bool
- 默认值：`true`
- 说明：备份时是否自动关闭自动保存（`save-off`），完成后重新开启。

#### `server.commands`
Minecraft 命令模板，用于执行特定操作。可修改以适应非原版服务端。

- `get_entity_data`: 默认 `"data get entity {name} {path}"`，获取实体数据。
- `save_all_worlds`: 默认 `"save-all flush"`，保存世界。
- `auto_save_off`: 默认 `"save-off"`，关闭自动保存。
- `auto_save_on`: 默认 `"save-on"`，开启自动保存。

#### `server.data_getter_regex`
正则表达式字典，用于解析 `data get entity` 命令的返回结果。默认包含：

- `crood_getter`: 匹配坐标输出。
- `dimension_getter`: 匹配维度输出。

如果修改了服务端语言或输出格式，可能需要调整这些正则。

#### `server.saved_world_regex`
- 类型：字符串列表
- 默认值：`["Saved the game", "Saved the world"]`
- 说明：匹配世界保存完成时的控制台输出，用于确认保存操作完成。

#### `server.save_world_max_wait`
- 类型：字符串（带单位的时间）
- 默认值：`"10min"`
- 说明：等待世界保存完成的最大超时时间。

### 备份配置（`backup`）

#### `backup.dimension`
维度配置字典，键为维度名（如 `"minecraft:overworld"`），值为对象，包含：

- `integer_id` (int): 用于命令中输入的数字 ID，必须唯一。
- `world_name` (string): 世界文件夹名称（相对于 `server_root`）。
- `description` (string): 维度描述（仅用于显示）。
- `region_folder` (list of string): 区域文件夹路径列表，相对于 `world_name`。通常包含 `region`、`entities`、`poi`。插件会自动根据 Minecraft 版本调整路径，但也可手动设置。

默认包含主世界、下界、末地。

#### `backup.player_data`
玩家数据文件路径配置，用于备份和恢复玩家相关文件。格式为字典，键为文件扩展名（如 `".json"`），值为文件夹列表。默认值会根据 Minecraft 版本自动切换（旧版与 26.1+ 路径不同）。

#### `backup.max_dynamic_slot`
- 类型：int
- 默认值：`10`
- 说明：动态备份最大槽位数，超过上限时自动删除最旧备份。

#### `backup.max_static_slot`
- 类型：int
- 默认值：`50`
- 说明：静态备份最大槽位数，超过上限时阻止新备份创建。

#### `backup.max_chunk_length`
- 类型：int
- 默认值：`320`
- 说明：允许备份的区块矩形最大边长（区块个数），用于限制过大范围。

---

## 📌 添加自定义维度

Chunk Backup 支持任意 Minecraft 维度（包括模组维度，如暮色森林、地狱、末地等）。你只需在配置文件中正确添加维度信息，即可对该维度执行备份与回档操作。

### 1. 获取维度的合法名称

在添加维度前，你需要知道该维度在游戏中的内部名称。有两种常用方法：

- **F3 调试屏幕**  
  在游戏中按下 F3 键，打开调试屏幕。在左上角可以看到当前所在维度的信息，例如 `twilightforest:twilight_forest`。

  ![F3 调试屏幕示例](https://raw.githubusercontent.com/Passion-Never-Dissipate/Chunk_BackUp/main/images/before_use1.png)  
  *（图片仅为示意，请以实际游戏内显示为准）*

- **使用 `/data get entity` 命令**  
  执行指令 `/data get entity <玩家名> Dimension`，控制台会返回当前维度的名称。例如：
  ```
  /data get entity Steve Dimension
  ```
  返回结果中会包含维度名，如 `"twilightforest:twilight_forest"`。

  ![命令示例](https://raw.githubusercontent.com/Passion-Never-Dissipate/Chunk_BackUp/main/images/before_use2.png)

### 2. 维度配置结构

在配置文件 `config/chunk_backup/config.json` 中，找到 `backup.dimension` 字段。它是一个字典，**键为维度名**（如 `"minecraft:overworld"`），值为一个对象，包含以下字段：

| 字段              | 类型     | 说明                                                                                                                                                                         |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `integer_id`    | int    | 用于命令中输入的整数 ID，**必须唯一**（不能与其他维度重复）。建议使用自定义的负整数或大整数以避免与原版冲突。                                                                                                                 |
| `world_name`    | string | 该维度所在的世界文件夹名称（相对于 `server_root`）。对于单世界服务端，通常为 `"world"`；对于多世界服务端，可能为其他名称。                                                                                                  |
| `description`   | string | 维度的描述信息（仅用于显示，不影响功能）。                                                                                                                                                      |
| `region_folder` | list   | 区域文件夹路径列表，相对于 `world_name`。通常需要包含 `region`、`entities`、`poi` 这三个子文件夹的路径（注意：在 Minecraft 26.1 版本后，路径可能变为 `dimensions/minecraft/overworld/region` 等，插件会自动适配，但如果你手动设置，请确保路径正确）。 |

### 3. 确定 `region_folder` 路径

`region_folder` 中的路径需要指向该维度下存储区域文件（`.mca`）的目录。
- 对于 **原版单世界服务端**，各维度的路径通常是固定的：
  - 主世界：`region`、`entities`、`poi`（直接位于世界文件夹下）
  - 下界：`DIM-1/region`、`DIM-1/entities`、`DIM-1/poi`
  - 末地：`DIM1/region`、`DIM1/entities`、`DIM1/poi`
- 对于 **模组维度**（如暮色森林），路径通常形如 `dimensions/<modid>/<dimension>/region` 等。你可以通过查看服务端文件夹结构来确定。

**提示**：插件会自动根据 Minecraft 版本切换路径规则（26.1 版本前后路径不同）。如果你不确定，可以先留空让插件自动生成默认值，然后根据实际情况微调。

### 4. 完整示例：添加暮色森林维度

假设你的服务器安装了暮色森林模组，其维度名为 `twilightforest:twilight_forest`，世界文件夹为 `world`，区域文件位于 `dimensions/twilightforest/twilight_forest/` 下。则配置如下：

```json
"backup": {
    "dimension": {
        "minecraft:overworld": {
            "integer_id": 0,
            "world_name": "world",
            "description": "主世界",
            "region_folder": [
                "region",
                "entities",
                "poi"
            ]
        },
        "minecraft:the_nether": {
            "integer_id": -1,
            "world_name": "world",
            "description": "下界",
            "region_folder": [
                "DIM-1/region",
                "DIM-1/entities",
                "DIM-1/poi"
            ]
        },
        "minecraft:the_end": {
            "integer_id": 1,
            "world_name": "world",
            "description": "末地",
            "region_folder": [
                "DIM1/region",
                "DIM1/entities",
                "DIM1/poi"
            ]
        },
        "twilightforest:twilight_forest": {
            "integer_id": -2,
            "world_name": "world",
            "description": "暮色森林",
            "region_folder": [
                "dimensions/twilightforest/twilight_forest/region",
                "dimensions/twilightforest/twilight_forest/entities",
                "dimensions/twilightforest/twilight_forest/poi"
            ]
        }
    },
    // ... 其他备份配置
}
```

### 5. 注意事项

- **`integer_id` 必须唯一**：不能与已有维度重复。建议使用负整数或 100 以上的整数，以避免与未来 Minecraft 版本新增维度冲突。
- **路径准确性**：如果 `region_folder` 路径错误，插件将无法找到对应的区域文件，导致备份失败。请务必检查服务端文件夹结构，确保路径正确。
- **多世界服务端**：如果你的服务端使用 Spigot/Paper 等多世界服务端，不同维度可能位于不同的世界文件夹中，此时 `world_name` 应设置为对应的世界文件夹名称（例如 `world_nether`、`world_the_end` 或自定义名称）。
- **修改后重载**：每次修改配置文件后，都需要在游戏或控制台执行 `!!cb reload` 使更改生效。

---

通过以上步骤，你可以轻松地将任何自定义维度纳入 Chunk Backup 的管理范围，享受精确的区块备份与恢复功能。

## 🎮 指令帮助

所有指令均以插件前缀（默认 `!!cb`）开头。支持 Tab 补全，输入 `!!cb help` 查看总览，`!!cb help <指令>` 查看详细用法。

### 通用选项

| 选项                | 含义                                      |
| ----------------- | --------------------------------------- |
| `-s`, `--static`  | 操作静态备份（不自动轮换）                           |
| `-d`, `--data`    | 回档时同时恢复玩家数据（需 Carpet Mod 和 candy_tools） |
| `-c`, `--confirm` | 跳过二次确认，直接执行                             |

### 备份指令

| 指令                                              | 说明                                                                |
| ----------------------------------------------- | ----------------------------------------------------------------- |
| `!!cb make <半径> [<注释>]`                         | 以玩家所在区块为中心，备份边长为 `2*半径+1` 的区块区域。**玩家数据会自动备份（若安装 Carpet）**，无需额外参数。 |
| `!!cb pmake <x1> <z1> <x2> <z2> in <维度> [<注释>]` | 备份两个坐标点所确定的矩形区块范围。                                                |
| `!!cb dmake <维度列表> [<注释>]`                      | 备份整个维度的所有区域文件（支持逗号分隔多个维度，如 `0,-1,1`）。                             |

### 回档指令

| 指令                   | 说明                        |
| -------------------- | ------------------------- |
| `!!cb back [<备份ID>]` | 回档到指定备份（不指定 ID 则使用最新的备份）。 |
| `!!cb restore`       | 撤销上一次回档，恢复到回档前状态。         |

### 管理指令

| 指令                  | 说明                                   |
| ------------------- | ------------------------------------ |
| `!!cb list [<页数>]`  | 列出备份列表。                              |
| `!!cb show <备份ID>`  | 显示指定备份的详细信息（添加 `-d` 可查看玩家数据列表）。      |
| `!!cb del <备份ID范围>` | 删除指定备份（支持单个ID、逗号分隔、连字符范围，如 `1,3-5`）。 |
| `!!cb del all`      | 删除当前类型（动态/静态）的所有备份。                  |

### 日志指令

| 指令                      | 说明                       |
| ----------------------- | ------------------------ |
| `!!cb log list [<页数>]`  | 显示日志列表。                  |
| `!!cb log show [<日志名>]` | 显示指定日志的详细内容（不指定则显示最新日志）。 |

### 帮助与确认

| 指令                 | 说明            |
| ------------------ | ------------- |
| `!!cb help [<指令>]` | 显示帮助信息。       |
| `!!cb confirm`     | 确认当前等待中的危险操作。 |
| `!!cb abort`       | 中止当前等待中的操作。   |
| `!!cb reload`      | 重载插件配置。       |

---

## 📋 示例

### 1. 备份当前区块（半径0）到静态备份，并附带注释
```
!!cb make 0 --static 保存出生点建筑
```
（玩家数据会自动备份，无需 `-d`）

### 2. 备份主世界和下界的所有区域（维度0和-1）
```
!!cb dmake 0,-1 备份全主世界和下界
```

### 3. 恢复第3个备份，同时恢复玩家数据
```
!!cb back 3 -d
```

### 4. 删除动态备份中ID为1、2、5到10的备份
```
!!cb del 1,2,5-10
```

### 5. 查看日志列表第2页
```
!!cb log list 2
```

### 6. 显示最新日志详情
```
!!cb log show
```

---

## ⚠️ 升级指南（从 v1.x 迁移到 v2.0.0）

由于 v2.0.0 完全重构了备份格式和存储结构，旧版备份**无法直接兼容**。请按照以下步骤安全升级：

1. **备份你的世界和旧版插件数据**（包括 `cb_multi`、`cb_static` 等文件夹）。
2. 卸载旧版插件（删除旧版`.mcdr` 文件）。
3. 安装新版插件和 `candy_tools` 插件，启动 MCDR 生成默认配置。
4. 根据你的需求重新配置 `config.json`（特别是维度设置）。
5. **重要**：如果你有重要的旧版备份需要保留，建议先用旧版插件将备份恢复到世界，然后用新版插件重新备份这些区域。
6. **关于自定义备份**：新版插件暂时不支持旧版的自定义备份（custom）功能。我们计划在未来版本中开发一个功能更强大、更易于使用的自定义备份系统，敬请期待。当前版本仅支持区块级备份和区域级备份。
7. 开始使用新版插件。

> ⚠️ **注意**：新版配置字段与旧版完全不同，请勿直接复制旧版配置文件。

---

## ❓ 常见问题

### Q1：为什么备份时提示“没有玩家数据”？
A：你需要安装 [Carpet Mod](https://www.curseforge.com/minecraft/mc-mods/carpet) 并确保其正常工作，同时安装 [candy_tools](https://github.com/Passion-Never-Dissipate/candy_tools) 插件。另外，只有选区内的在线玩家才会被备份。

### Q2：备份文件存储在什么位置？
A：动态备份位于 `./cb_files/dynamic_storage/`，静态备份位于 `./cb_files/static_storage/`，回档前备份位于 `./cb_files/overwrite/`，日志位于 `./cb_files/logs/`。

### Q3：如何添加模组维度（如暮色森林）？
A：在配置文件的 `backup.dimension` 中添加新条目，指定一个唯一的 `integer_id` 和正确的 `region_folder` 路径。路径需相对于该维度的世界文件夹（通常为 `world` 或自定义世界名）。例如：
```json
"twilightforest:twilight_forest": {
    "integer_id": -2,
    "world_name": "world",
    "description": "暮色森林",
    "region_folder": [
        "dimensions/twilightforest/twilight_forest/region",
        "dimensions/twilightforest/twilight_forest/entities",
        "dimensions/twilightforest/twilight_forest/poi"
    ]
}
```

### Q4：为什么回档时玩家数据没有恢复？
A：需要在回档命令中添加 `-d` 参数，如 `!!cb back 3 -d`。同时确保备份时已经收集了玩家数据（即有在线玩家在选区内）。

### Q5：如何取消正在等待确认的操作？
A：输入 `!!cb abort` 即可中止当前任务。

---

## 🙏 鸣谢

本插件在开发过程中参考并使用了 [Prime Backup](https://github.com/TISUnion/PrimeBackup) 的部分代码，特此感谢 Prime Backup 的作者及 TISUnion 组织。Prime Backup 是一个优秀的 Minecraft 备份插件，为我们提供了宝贵的思路和代码参考。

---

## 🤝 贡献与反馈

- 项目地址：[GitHub](https://github.com/Passion-Never-Dissipate/Chunk_BackUp)
- 反馈 Issue：[Issues](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/issues)
- 交流 QQ 群：**417086159**

如果你喜欢这个插件，欢迎给个 Star ⭐，也欢迎提交 PR 一起改进！

---

> 💡 最后提醒：**备份文件夹内的文件请不要手动移动或修改**，否则可能导致备份失效。

> 祝使用愉快！


### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [Chunk_BackUp-v2.0.3.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v2.0.3) | 2.0.3 | 2026/07/23 15:36:42 | 98.67KB | 13 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v2.0.3/Chunk_BackUp-v2.0.3.mcdr) |
| [Chunk_BackUp-v2.0.2.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v2.0.2) | 2.0.2 | 2026/03/13 17:51:26 | 98.58KB | 204 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v2.0.2/Chunk_BackUp-v2.0.2.mcdr) |
| [Chunk_BackUp-v2.0.1.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v2.0.1) | 2.0.1 | 2026/03/12 14:13:09 | 98.41KB | 58 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v2.0.1/Chunk_BackUp-v2.0.1.mcdr) |
| [Chunk_BackUp-v2.0.0.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v2.0.0) | 2.0.0 | 2026/03/12 04:22:38 | 98.41KB | 57 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v2.0.0/Chunk_BackUp-v2.0.0.mcdr) |
| [Chunk_BackUp-v1.3.8.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.8) | 1.3.8 | 2025/08/28 13:20:18 | 48.98KB | 306 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.8/Chunk_BackUp-v1.3.8.mcdr) |
| [Chunk_BackUp-v1.3.7.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.7) | 1.3.7 | 2025/08/06 17:16:34 | 48.97KB | 88 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.7/Chunk_BackUp-v1.3.7.mcdr) |
| [Chunk_BackUp-v1.3.6.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.6) | 1.3.6 | 2025/07/27 13:43:18 | 48.9KB | 83 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.6/Chunk_BackUp-v1.3.6.mcdr) |
| [Chunk_BackUp-v1.3.5.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.5) | 1.3.5 | 2025/07/26 03:06:12 | 49.01KB | 49 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.5/Chunk_BackUp-v1.3.5.mcdr) |
| [Chunk_BackUp-v1.3.4.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.4) | 1.3.4 | 2025/04/12 13:28:44 | 48.88KB | 235 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.4/Chunk_BackUp-v1.3.4.mcdr) |
| [Chunk_BackUp-v1.3.3.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.3) | 1.3.3 | 2025/04/11 14:11:57 | 47.76KB | 37 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.3/Chunk_BackUp-v1.3.3.mcdr) |
| [Chunk_BackUp-v1.3.2.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.2) | 1.3.2 | 2025/04/10 14:50:47 | 47.79KB | 38 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.2/Chunk_BackUp-v1.3.2.mcdr) |
| [Chunk_BackUp-v1.3.1.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.3.1) | 1.3.1 | 2025/04/10 08:39:34 | 47.69KB | 49 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.3.1/Chunk_BackUp-v1.3.1.mcdr) |
| [Chunk_BackUp-v1.2.3.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.2.3) | 1.2.3 | 2025/03/14 14:21:17 | 39.51KB | 74 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.2.3/Chunk_BackUp-v1.2.3.mcdr) |
| [Chunk_BackUp-v1.2.2.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.2.2) | 1.2.2 | 2025/03/13 06:41:58 | 39.34KB | 44 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.2.2/Chunk_BackUp-v1.2.2.mcdr) |
| [Chunk_BackUp-v1.2.1.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.2.1) | 1.2.1 | 2025/03/12 23:15:31 | 39.64KB | 48 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.2.1/Chunk_BackUp-v1.2.1.mcdr) |
| [Chunk_BackUp-v1.2.0.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.2.0) | 1.2.0 | 2025/03/11 07:33:36 | 38.96KB | 55 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.2.0/Chunk_BackUp-v1.2.0.mcdr) |
| [Chunk_BackUp-v1.1.1.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.1.1) | 1.1.1 | 2025/03/10 08:29:59 | 37.47KB | 40 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.1.1/Chunk_BackUp-v1.1.1.mcdr) |
| [Chunk_BackUp-v1.1.0.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.1.0) | 1.1.0 | 2025/03/09 12:20:39 | 34.43KB | 46 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.1.0/Chunk_BackUp-v1.1.0.mcdr) |
| [Chunk_BackUp-v1.0.0.mcdr](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/tag/v1.0.0) | 1.0.0 | 2025/03/08 15:46:23 | 33.37KB | 40 | [下载](https://github.com/Passion-Never-Dissipate/Chunk_BackUp/releases/download/v1.0.0/Chunk_BackUp-v1.0.0.mcdr) |

