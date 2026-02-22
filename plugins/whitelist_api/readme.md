**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## whitelist_api

### Basic Information

- Plugin ID: `whitelist_api`
- Plugin Name: WhitelistAPI
- Version: 1.4.0
  - Metadata version: 1.4.0
  - Release version: 1.4.0
- Total downloads: 1862
- Authors: [Aimerny](https://github.com/Aimerny)
- Repository: https://github.com/Aimerny/MCDRPlugins
- Repository plugin page: https://github.com/Aimerny/MCDRPlugins/tree/main/src/whitelist_api
- Labels: [`API`](/labels/api/readme.md)
- Description: whitelist common api

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.6.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [watchdog](https://pypi.org/project/watchdog) | \>=5.0.2 |
| [pathlib](https://pypi.org/project/pathlib) | \>=1.0.1 |

```
pip install "watchdog>=5.0.2" "pathlib>=1.0.1"
```

### Introduction

# WhitelistAPI - 通用白名单API

---

# ⭐ 功能
**WhitelistAPI**适用于需要获取服务器白名单的场景.支持常见的白名单操作以及白名单玩家列表获取.
本插件会自动跟踪白名单文件`whitelist.json`的变化而自动同步列表,保证通过api调用得到的白名单列表是最新的

- [x] 获取白名单内所有成员
- [x] 获取白名单内所有成员的玩家名
- [x] 获取白名单内所有成员的uuid列表
- [x] 开启服务器白名单功能
- [x] 关闭服务器白名单功能
- [x] 添加正版玩家白名单
- [x] 添加离线玩家白名单
- [x] 移除玩家白名单
- [x] 根据服务器在线/离线自适应添加白名单

# 📌 依赖
| python依赖    | 版本     |
| ----------- | ------ |
| mcdreforged | ^2.6.0 |
| watchdog    | ^5.0.2 |

# ⌨️ 使用方式
示例代码
```python

def on_load(server, old):
    whitelist_api = server.get_plugin_instance('whitelist_api') # 通过MCDR获取API实例
    whitelist_api.get_whitelist()           # 获取白名单内所有成员
    whitelist_api.get_whitelist_uuids()     # 获取白名单内所有成员的uuid列表
    whitelist_api.get_whitelist_names()     # 获取白名单内所有成员的玩家名
    whitelist_api.add_player('Aimerny')     # 根据目标server的online-mode自适应添加白名单(仅限Java版)
    whitelist_api.add_offline_player('Aimerny')      # 添加离线玩家白名单(仅限Java版)
    whitelist_api.add_online_player('Aimerny')       # 添加正版玩家白名单(仅限Java版)
    whitelist_api.remove_player('Aimerny')           # 移除玩家白名单
    whitelist_api.enable_whitelist()        # 开启服务器白名单功能
    whitelist_api.disable_whitelist()       # 关闭服务器白名单功能

    # 如果需要为通过floodgate加入的玩家添加白名单
    whitelist_api.add_floodgate_player('Aimerny')
    whitelist_api.add_floodgate_player('Aimerny', '#')
```
# 🎾 使用此api的插件集合

1. [Offline Whitelist Reforged](https://github.com/Aimerny/MCDRPlugins/tree/main/src/whitelist_api/../offline_whitelist_reforged): 简单小巧的离线服白名单插件
2. [KookIn](https://github.com/Aimerny/MCDRPlugins/tree/main/src/whitelist_api/../kookin): Kook平台的MC机器人
3. [GUGUBot](https://github.com/LoosePrince/PF-GUGUBot): GUGUBot插件

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [WhitelistAPI-v1.4.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.4.0) | 1.4.0 | 2025/06/09 16:58:30 | 3.09KB | 811 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.4.0/WhitelistAPI-v1.4.0.mcdr) |
| [WhitelistAPI-v1.3.4.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.3.4) | 1.3.4 | 2025/02/06 07:04:09 | 3.05KB | 311 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.3.4/WhitelistAPI-v1.3.4.mcdr) |
| [WhitelistAPI-v1.3.3.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.3.3) | 1.3.3 | 2024/12/23 05:12:23 | 3.04KB | 235 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.3.3/WhitelistAPI-v1.3.3.mcdr) |
| [WhitelistAPI-v1.3.1.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.3.1) | 1.3.1 | 2024/12/20 08:18:02 | 3.0KB | 77 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.3.1/WhitelistAPI-v1.3.1.mcdr) |
| [WhitelistAPI-v1.3.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.3.0) | 1.3.0 | 2024/10/29 07:05:08 | 2.95KB | 108 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.3.0/WhitelistAPI-v1.3.0.mcdr) |
| [WhitelistAPI-v1.2.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.2.0) | 1.2.0 | 2024/10/16 15:01:26 | 2.92KB | 74 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.2.0/WhitelistAPI-v1.2.0.mcdr) |
| [WhitelistAPI-v1.1.1.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.1.1) | 1.1.1 | 2024/10/12 19:46:45 | 2.87KB | 58 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.1.1/WhitelistAPI-v1.1.1.mcdr) |
| [WhitelistAPI-v1.1.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.1.0) | 1.1.0 | 2024/10/07 15:16:10 | 2.87KB | 57 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.1.0/WhitelistAPI-v1.1.0.mcdr) |
| [WhitelistAPI-v1.0.1.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.0.1) | 1.0.1 | 2024/10/01 17:49:08 | 2.61KB | 61 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.0.1/WhitelistAPI-v1.0.1.mcdr) |
| [WhitelistAPI-v1.0.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.0.0) | 1.0.0 | 2024/09/26 15:30:57 | 2.61KB | 70 | [Download](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.0.0/WhitelistAPI-v1.0.0.mcdr) |

