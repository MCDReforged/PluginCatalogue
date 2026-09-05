[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## chest_scanner_lib

### 基本信息

- 插件 ID: `chest_scanner_lib`
- 插件名: ChestScannerLib
- 版本: 1.0.2
  - 元数据版本: 1.0.2
  - 发布版本: 1.0.2
- 总下载量: 46
- 作者: [YuShenLiu06](https://github.com/YuShenLiu06)
- 仓库: https://github.com/YuShenLiu06/mcdr-chest-scanner
- 仓库插件页: https://github.com/YuShenLiu06/mcdr-chest-scanner/tree/main
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: MCDReforged 库插件：通过玩家准星指向或指定坐标获取箱子内容，支持大箱子

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | * |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [hjson](https://pypi.org/project/hjson) | \>=3.1 |

```
pip install "hjson>=3.1"
```

### 介绍

# mcdr-chest-scanner

[English](https://github.com/YuShenLiu06/mcdr-chest-scanner/tree/main/README.md) | [中文](https://github.com/YuShenLiu06/mcdr-chest-scanner/tree/main/README_zh.md)

MCDReforged 库插件：通过玩家准星指向或指定坐标获取箱子内容，支持大箱子。

## 安装

在插件 `mcdreforged.plugin.json` 中声明依赖：

```json
{
  "dependencies": {
    "chest_scanner_lib": ">=0.1.0"
  }
}
```

## 依赖

| 依赖                                                                    | 类型                                  |
| --------------------------------------------------------------------- | ----------------------------------- |
| [MCDReforged](https://github.com/MCDReforged/MCDReforged) >=2.14.0    | 插件平台                                |
| [MinecraftDataAPI](https://github.com/Fallen-Breath/MinecraftDataAPI) | 玩家位置/朝向（仅 `find_targeted_chest` 需要） |
| [hjson](https://pypi.org/project/hjson/) >=3.1                        | Python 包（`pip install hjson`）       |

## API

所有函数成功返回 `({item_id: qty}, None)`，失败返回 `(None, error_code)`。

### 高级 API

#### `find_targeted_chest(server, player, max_distance=6.0)`

扫描玩家准星指向的箱子，含双联箱子合并。

```python
items, err = find_targeted_chest(server, "Steve")
if err:
    server.logger.warning(f"扫描失败: {err}")
```

#### `scan_chest_rcon(server, x, y, z)`

扫描指定坐标的箱子，含双联箱子合并。

```python
items, err = scan_chest_rcon(server, 10, 64, 20)
```

### 低级 API

| 函数                                                  | 返回值                            | 说明                                     |
| --------------------------------------------------- | ------------------------------ | -------------------------------------- |
| `detect_facing_type(server, x, y, z)`               | `(facing, type)` 或 `None`      | 通过 `execute if block` 探测箱子 block state |
| `read_double_chest(server, x, y, z, primary_items)` | `dict`                         | 检测 partner 半 + 合并 54 格                 |
| `expand_items(items, acc)`                          | `None`                         | 递归展开嵌套物品（潜影盒）到 `Counter`               |
| `parse_rcon_block_items(raw)`                       | `(list, None)` 或 `(None, err)` | 解析 RCON `data get block` 响应            |
| `parse_block_coords(raw)`                           | `(x, y, z)` 或 `None`           | 从 RCON 响应前缀提取坐标                        |

### 错误码

| 错误码                              | 含义              |
| -------------------------------- | --------------- |
| `no_rcon`                        | RCON 未运行或查询失败   |
| `no_api` / `no_pos`              | 无法获取玩家位置（仅准星模式） |
| `not_container`                  | 非容器方块           |
| `not_found`                      | 射线范围内无容器        |
| `empty`                          | 容器为空            |
| `parse_error` / `unknown_format` | SNBT 解析失败       |

## 实现方式

- **DDA 体素遍历**（Amanatides & Woo）— 准星射线逐格探测，不跳格不遗漏
- **双联箱子合并** — `execute if block` 探测 `type`/`facing`，自动合并 54 格
- **陷阱箱兼容** — `minecraft:chest` + `minecraft:trapped_chest`
- **SNBT 解析** — 提取自 MinecraftDataAPI 预处理 + hjson 宽松解析

## 许可

MIT

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [chest_scanner_lib-v1.0.2.mcdr](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/tag/v1.0.2) | 1.0.2 | 2026/08/15 02:45:25 | 8.94KB | 19 | [下载](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/download/v1.0.2/chest_scanner_lib-v1.0.2.mcdr) |
| [chest_scanner_lib-v1.0.1.mcdr](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/tag/v1.0.1) | 1.0.1 | 2026/08/14 15:18:05 | 8.92KB | 12 | [下载](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/download/v1.0.1/chest_scanner_lib-v1.0.1.mcdr) |
| [chest_scanner_lib-v1.0.0.mcdr](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/tag/v1.0.0) | 1.0.0 | 2026/08/08 05:33:10 | 8.9KB | 15 | [下载](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/download/v1.0.0/chest_scanner_lib-v1.0.0.mcdr) |

