**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## uuid_api_remake

### Basic Information

- Plugin ID: `uuid_api_remake`
- Plugin Name: UUID API Remake
- Version: 2.1.1
  - Metadata version: 2.1.0
  - Release version: 2.1.1
- Total downloads: 244
- Authors: [gubai](https://github.com/gubaiovo)
- Repository: https://github.com/gubaiovo/MCDR_uuid_api_remake
- Repository plugin page: https://github.com/gubaiovo/MCDR_uuid_api_remake/tree/main/uuid_api_remake
- Labels: [`API`](/labels/api/readme.md), [`Tool`](/labels/tool/readme.md)
- Description: Get UUID of players

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install mcdreforged requests
```

### Introduction

# UUID API REMAKE
本插件为UUID API重制版，[原作UUID API链接：https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api)

### 本插件uuid获取流程 (如果获取失败则执行下一步)：

1. 判断服务器正版/离线
2. (1). 正版：
   1. 读取 usercache.json，失败则下一步
   2. 调用 API
   (2). 离线
   1. 读取 offline_uuid.json，失败则下一步
   2. 本地计算 uuid，保存到 offline_uuid.json

### 配置文件

```json
{
    "online_api": "https://api.mojang.com/users/profiles/minecraft/{}",
    "mojang_online_mode_fallback": true,
    "permissions": {
        "help": 3,
        "get": 3
    }
}
```

**mojang_online_mode_fallback**: 当插件无法判断服务器正版/离线时，由该项决定使用正版/离线 uuid 获取方式  
**online_api**: 获取正版 uuid 的 API  
**permissions**: 权限管理，数值参考 [MCDReforgedPermissions](https://docs.mcdreforged.com/zh-cn/latest/permission.html)

### 命令

具体使用方法请参考 `!!uar help`

### API使用方法

获取玩家名对应的uuid：

```python
import uuid_api_remake

name = ... # str
uuid = uuid_api_remake.get_uuid(name)
print(uuid)
```

获取uuid对应的玩家名(获取范围为 `offline_uuid.json` 以及 `usercache.json`)

```python
import uuid_api_remake

uuid = ... # str
name = uuid_api_remake.get_name(uuid)
print(name)
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v2.1.1) | 2.1.1 | 2026/01/20 08:43:44 | 4.15KB | 20 | [Download](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v2.1.1/uuid_api_remake.mcdr) |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v2.1.0) | 2.1.0 | 2025/07/24 02:20:29 | 4.07KB | 87 | [Download](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v2.1.0/uuid_api_remake.mcdr) |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v2.0.0) | 2.0.0 | 2025/07/17 10:33:37 | 3.9KB | 35 | [Download](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v2.0.0/uuid_api_remake.mcdr) |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v1.1.0) | 1.1.0 | 2025/03/14 08:24:12 | 9.8KB | 69 | [Download](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v1.1.0/uuid_api_remake.mcdr) |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v1.0.0) | 1.0.0 | 2025/03/13 13:12:08 | 9.38KB | 33 | [Download](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v1.0.0/uuid_api_remake.mcdr) |

