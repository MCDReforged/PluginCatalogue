**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## clear_player_data

### Basic Information

- Plugin ID: `clear_player_data`
- Plugin Name: player_data_clearer
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 48
- Authors: [tch](https://github.com/god-what-is-that)
- Repository: https://github.com/god-what-is-that/mcdr-player-data-clearer
- Repository plugin page: https://github.com/god-what-is-that/mcdr-player-data-clearer/tree/main/player_data_clearer
- Labels: [`Management`](/labels/management/readme.md), [`Tool`](/labels/tool/readme.md)
- Description: 清除指定UUID的玩家数据

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [uuid_api_remake](/plugins/uuid_api_remake/readme.md) | \>=2.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [pyyaml](https://pypi.org/project/pyyaml) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install pyyaml requests
```

### Introduction

# mcdr-player-data-clearer
依赖uuid_api_remake插件。  
在配置文件中添加你需要删除的玩家数据位置以及后缀。默认会删除world/playerdata/uuid.dat+dat_old、advancements/uuid.json、stats/uuid.json。  
!!cpd uuid [uuid], 清除指定UUID的玩家数据。  
!!cpd playerid [playerid], 清除指定玩家数据。  
!!cpd clean [day]，清除多少天没修改的玩家数据。不是查的usercache.json，是直接查world的playerdata的修改日期。

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [player_data_clearer-v1.0.0.mcdr](https://github.com/god-what-is-that/mcdr-player-data-clearer/releases/tag/1.0.0) | 1.0.0 | 2025/07/17 14:08:04 | 4.86KB | 48 | [Download](https://github.com/god-what-is-that/mcdr-player-data-clearer/releases/download/1.0.0/player_data_clearer-v1.0.0.mcdr) |

