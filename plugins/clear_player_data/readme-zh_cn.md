[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## clear_player_data

### 基本信息

- 插件 ID: `clear_player_data`
- 插件名: player_data_clearer
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 48
- 作者: [tch](https://github.com/god-what-is-that)
- 仓库: https://github.com/god-what-is-that/mcdr-player-data-clearer
- 仓库插件页: https://github.com/god-what-is-that/mcdr-player-data-clearer/tree/main/player_data_clearer
- 标签: [`管理`](/labels/management/readme-zh_cn.md), [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 清除指定UUID的玩家数据

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [uuid_api_remake](/plugins/uuid_api_remake/readme-zh_cn.md) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [pyyaml](https://pypi.org/project/pyyaml) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install pyyaml requests
```

### 介绍

# mcdr-player-data-clearer
依赖uuid_api_remake插件。  
在配置文件中添加你需要删除的玩家数据位置以及后缀。默认会删除world/playerdata/uuid.dat+dat_old、advancements/uuid.json、stats/uuid.json。  
!!cpd uuid [uuid], 清除指定UUID的玩家数据。  
!!cpd playerid [playerid], 清除指定玩家数据。  
!!cpd clean [day]，清除多少天没修改的玩家数据。不是查的usercache.json，是直接查world的playerdata的修改日期。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [player_data_clearer-v1.0.0.mcdr](https://github.com/god-what-is-that/mcdr-player-data-clearer/releases/tag/1.0.0) | 1.0.0 | 2025/07/17 14:08:04 | 4.86KB | 48 | [下载](https://github.com/god-what-is-that/mcdr-player-data-clearer/releases/download/1.0.0/player_data_clearer-v1.0.0.mcdr) |

