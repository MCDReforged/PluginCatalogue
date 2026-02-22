**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## unlock_recipe

### Basic Information

- Plugin ID: `unlock_recipe`
- Plugin Name: UnlockRecipe
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 64
- Authors: [uerhu](https://uerhu.cn)
- Repository: https://github.com/uerhu/MCDR-UnlockRecipe
- Repository plugin page: https://github.com/uerhu/MCDR-UnlockRecipe/tree/master
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Allow player uses !!recipe to unlock recipes

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# UnlockRecipe
[中文](https://github.com/uerhu/MCDR-UnlockRecipe/tree/master/README_cn.md)

---
## Introduction
* JEI, REI and other mods cannot view locked recipes when browsing recipes
* Use this plugin to unlock recipes for non-op players
---
## Command
* `!!recipe`unlock recipes for oneself（Only for player）
---
## Configuration
config.json （default configuration file）
```json5
{
    "permission": 1,  // player permission level
    "announce": true,  // whether to notify players when they enter the game
    "announce_once": true  // whether to notify only once
}
```
announced_players.json (record notified players)
```json5
{
  "announced_players": [
    "player1",
    "player2"
    ]
}
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [UnlockRecipe-1.0.0.mcdr](https://github.com/uerhu/MCDR-UnlockRecipe/releases/tag/1.0.0) | 1.0.0 | 2025/08/22 09:35:59 | 4.02KB | 64 | [Download](https://github.com/uerhu/MCDR-UnlockRecipe/releases/download/1.0.0/UnlockRecipe-1.0.0.mcdr) |

