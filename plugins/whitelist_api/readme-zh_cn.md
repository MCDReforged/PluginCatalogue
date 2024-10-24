[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## whitelist_api

### 基本信息

- 插件 ID: `whitelist_api`
- 插件名: WhitelistAPI
- 版本: 1.2.0
  - 元数据版本: 1.2.0
  - 发布版本: 1.2.0
- 总下载量: 58
- 作者: [Aimerny](https://github.com/Aimerny)
- 仓库: https://github.com/Aimerny/MCDRPlugins
- 仓库插件页: https://github.com/Aimerny/MCDRPlugins/tree/main/src/whitelist_api
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 通用的白名单API

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.6.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [watchdog](https://pypi.org/project/watchdog) | \>=5.0.2 |

```
pip install "watchdog>=5.0.2"
```

### 介绍

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
    whitelist_api.add_player('Aimerny')     # 根据目标server的online-mode自适应添加白名单
    whitelist_api.add_offline_player('Aimerny')      # 添加离线玩家白名单
    whitelist_api.add_online_player('Aimerny')       # 添加正版玩家白名单
    whitelist_api.remove_player('Aimerny')           # 移除玩家白名单
    whitelist_api.enable_whitelist()        # 开启服务器白名单功能
    whitelist_api.disable_whitelist()       # 关闭服务器白名单功能
```
# 🎾 使用此api的插件集合

1. [Offline Whitelist Reforged](https://github.com/Aimerny/MCDRPlugins/tree/main/src/whitelist_api/../offline_whitelist_reforged): 简单小巧的离线服白名单插件
2. [KookIn](https://github.com/Aimerny/MCDRPlugins/tree/main/src/whitelist_api/../kookin): Kook平台的MC机器人

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [WhitelistAPI-v1.2.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.2.0) | 1.2.0 | 2024/10/16 15:01:26 | 2.92KB | 15 | [下载](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.2.0/WhitelistAPI-v1.2.0.mcdr) |
| [WhitelistAPI-v1.1.1.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.1.1) | 1.1.1 | 2024/10/12 19:46:45 | 2.87KB | 6 | [下载](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.1.1/WhitelistAPI-v1.1.1.mcdr) |
| [WhitelistAPI-v1.1.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.1.0) | 1.1.0 | 2024/10/07 15:16:10 | 2.87KB | 7 | [下载](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.1.0/WhitelistAPI-v1.1.0.mcdr) |
| [WhitelistAPI-v1.0.1.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.0.1) | 1.0.1 | 2024/10/01 17:49:08 | 2.61KB | 10 | [下载](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.0.1/WhitelistAPI-v1.0.1.mcdr) |
| [WhitelistAPI-v1.0.0.mcdr](https://github.com/Aimerny/MCDRPlugins/releases/tag/whitelist_api-v1.0.0) | 1.0.0 | 2024/09/26 15:30:57 | 2.61KB | 20 | [下载](https://github.com/Aimerny/MCDRPlugins/releases/download/whitelist_api-v1.0.0/WhitelistAPI-v1.0.0.mcdr) |

