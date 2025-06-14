**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## hat

### Basic Information

- Plugin ID: `hat`
- Plugin Name: Hat
- Version: 1.1.5
  - Metadata version: 1.1.5
  - Release version: 1.1.5
- Total downloads: 520
- Authors: [shuangshun](https://github.com/shuangshun)
- Repository: https://github.com/shuangshun/Hat
- Repository plugin page: https://github.com/shuangshun/Hat/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Equip the item in your hand on your head

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | * |

### Requirements

| Python package | Requirement |
| --- | --- |
| [nbtlib](https://pypi.org/project/nbtlib) | \>=2.0.4 |

```
pip install "nbtlib>=2.0.4"
```

### Introduction

# Hat

[![](https://img.shields.io/github/v/release/shuangshun/Hat)](https://github.com/shuangshun/Hat/releases)
[![](https://shields.io/github/downloads/shuangshun/Hat/total)](https://github.com/MrXiaoM/shuangshun/Hat)
[![](https://img.shields.io/github/stars/shuangshun/Hat)](https://github.com/shuangshun/Hat)

**English** | [中文](https://github.com/shuangshun/Hat/tree/main/README_zh_cn.md)

Provides a command `!!hat`, allowing players to wear items on their head

---

## Usage

- Install the plugin and all required dependencies
- Hold any item in your hand and enter the `!!hat` command in the game

## Configuration Explanation

- `permission` sets the minimum permission level required to use the `!!hat` command
> Only integer values are allowed. For details, please refer to [Permission Overview](https://docs.mcdreforged.com/en/latest/permission.html#overview)

- `cooldown` sets the cooldown time for using the `!!hat` command (unit: seconds)

```json5
{
    "permission": 1, // Default is 1, regular player
    "cooldown": 3 // Default is 3 seconds
}
```

------

> [!Note]
> Notice! This plugin is only applicable for [1.17+](https://minecraft.wiki/w/Commands/item#History)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [Hat-v1.1.5.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.5) | 1.1.5 | 2025/05/02 07:10:41 | 4.05KB | 127 | [Download](https://github.com/shuangshun/Hat/releases/download/v1.1.5/Hat-v1.1.5.mcdr) |
| [Hat-v1.1.4.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.4) | 1.1.4 | 2025/01/22 12:44:46 | 3.63KB | 200 | [Download](https://github.com/shuangshun/Hat/releases/download/v1.1.4/Hat-v1.1.4.mcdr) |
| [Hat-v1.1.3.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.3) | 1.1.3 | 2025/01/21 14:34:27 | 3.63KB | 12 | [Download](https://github.com/shuangshun/Hat/releases/download/v1.1.3/Hat-v1.1.3.mcdr) |
| [Hat-v1.1.2.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.2) | 1.1.2 | 2025/01/17 15:06:08 | 3.4KB | 32 | [Download](https://github.com/shuangshun/Hat/releases/download/v1.1.2/Hat-v1.1.2.mcdr) |
| [Hat-v1.1.1.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.1) | 1.1.1 | 2025/01/11 10:48:48 | 3.4KB | 43 | [Download](https://github.com/shuangshun/Hat/releases/download/v1.1.1/Hat-v1.1.1.mcdr) |
| [Hat-v1.1.0.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.0) | 1.1.0 | 2024/12/29 04:18:30 | 3.4KB | 54 | [Download](https://github.com/shuangshun/Hat/releases/download/v1.1.0/Hat-v1.1.0.mcdr) |
| [Hat-v1.0.2.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.0.2) | 1.0.2 | 2024/12/01 04:41:12 | 3.43KB | 52 | [Download](https://github.com/shuangshun/Hat/releases/download/v1.0.2/Hat-v1.0.2.mcdr) |

