**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## chest_scanner_lib

### Basic Information

- Plugin ID: `chest_scanner_lib`
- Plugin Name: ChestScannerLib
- Version: 1.0.2
  - Metadata version: 1.0.2
  - Release version: 1.0.2
- Total downloads: 46
- Authors: [YuShenLiu06](https://github.com/YuShenLiu06)
- Repository: https://github.com/YuShenLiu06/mcdr-chest-scanner
- Repository plugin page: https://github.com/YuShenLiu06/mcdr-chest-scanner/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: MCDReforged library: scan and read container contents via player crosshair or coordinates

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | * |

### Requirements

| Python package | Requirement |
| --- | --- |
| [hjson](https://pypi.org/project/hjson) | \>=3.1 |

```
pip install "hjson>=3.1"
```

### Introduction

# mcdr-chest-scanner

[English](https://github.com/YuShenLiu06/mcdr-chest-scanner/tree/main/README.md) | [中文](https://github.com/YuShenLiu06/mcdr-chest-scanner/tree/main/README_zh.md)

MCDReforged library plugin: retrieve chest contents by player's crosshair target or block coordinates, with double chest support.

## Install

Declare as dependency in your plugin's `mcdreforged.plugin.json`:

```json
{
  "dependencies": {
    "chest_scanner_lib": ">=0.1.0"
  }
}
```

## Dependencies

| Dependency                                                            | Type                                                 |
| --------------------------------------------------------------------- | ---------------------------------------------------- |
| [MCDReforged](https://github.com/MCDReforged/MCDReforged) >=2.14.0    | Plugin platform                                      |
| [MinecraftDataAPI](https://github.com/Fallen-Breath/MinecraftDataAPI) | Player position/rotation (for `find_targeted_chest`) |
| [hjson](https://pypi.org/project/hjson/) >=3.1                        | Python package (`pip install hjson`)                 |

## API

All functions return `({item_id: qty}, None)` on success or `(None, error_code)` on failure.

### High-level

#### `find_targeted_chest(server, player, max_distance=6.0)`

Scan the chest the player is looking at, with double chest merge.

```python
items, err = find_targeted_chest(server, "Steve")
if err:
    server.logger.warning(f"Scan failed: {err}")
```

#### `scan_chest_rcon(server, x, y, z)`

Scan chest at given coordinates, with double chest merge.

```python
items, err = scan_chest_rcon(server, 10, 64, 20)
```

### Low-level

| Function                                            | Returns                         | Description                                                    |
| --------------------------------------------------- | ------------------------------- | -------------------------------------------------------------- |
| `detect_facing_type(server, x, y, z)`               | `(facing, type)` or `None`      | Probe chest block state via `execute if block`                 |
| `read_double_chest(server, x, y, z, primary_items)` | `dict`                          | Detect partner half + merge 54 slots                           |
| `expand_items(items, acc)`                          | `None`                          | Recursively expand nested items (shulker boxes) into `Counter` |
| `parse_rcon_block_items(raw)`                       | `(list, None)` or `(None, err)` | Parse RCON `data get block` response                           |
| `parse_block_coords(raw)`                           | `(x, y, z)` or `None`           | Extract coordinates from RCON response prefix                  |

### Error codes

| Code                             | Meaning                                   |
| -------------------------------- | ----------------------------------------- |
| `no_rcon`                        | RCON not running or query failed          |
| `no_api` / `no_pos`              | Cannot get player position (raycast only) |
| `not_container`                  | Block is not a container                  |
| `not_found`                      | No container in raycast range             |
| `empty`                          | Container is empty                        |
| `parse_error` / `unknown_format` | SNBT parsing failed                       |

## Implementation

- **DDA voxel traversal** (Amanatides & Woo) — raycast visits every block, no gaps
- **Double chest merge** — `execute if block` probes `type`/`facing`, auto-merges 54 slots
- **Trapped chest support** — `minecraft:chest` + `minecraft:trapped_chest`
- **SNBT parsing** — extracted from MinecraftDataAPI preprocessing + hjson

## License

MIT

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [chest_scanner_lib-v1.0.2.mcdr](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/tag/v1.0.2) | 1.0.2 | 2026/08/15 02:45:25 | 8.94KB | 19 | [Download](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/download/v1.0.2/chest_scanner_lib-v1.0.2.mcdr) |
| [chest_scanner_lib-v1.0.1.mcdr](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/tag/v1.0.1) | 1.0.1 | 2026/08/14 15:18:05 | 8.92KB | 12 | [Download](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/download/v1.0.1/chest_scanner_lib-v1.0.1.mcdr) |
| [chest_scanner_lib-v1.0.0.mcdr](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/tag/v1.0.0) | 1.0.0 | 2026/08/08 05:33:10 | 8.9KB | 15 | [Download](https://github.com/YuShenLiu06/mcdr-chest-scanner/releases/download/v1.0.0/chest_scanner_lib-v1.0.0.mcdr) |

