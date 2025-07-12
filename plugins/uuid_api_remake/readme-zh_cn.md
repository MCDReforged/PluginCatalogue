[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## uuid_api_remake

### 基本信息

- 插件 ID: `uuid_api_remake`
- 插件名: UUID API Remake
- 版本: 1.1.0
  - 元数据版本: 1.1.0
  - 发布版本: 1.1.0
- 总下载量: 53
- 作者: [gubai](https://github.com/gubaiovo)
- 仓库: https://github.com/gubaiovo/MCDR_uuid_api_remake
- 仓库插件页: https://github.com/gubaiovo/MCDR_uuid_api_remake/tree/main/uuid_api_remake
- 标签: [`API`](/labels/api/readme-zh_cn.md), [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 获取玩家的UUID

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install mcdreforged requests
```

### 介绍

# UUID API REMAKE
本插件为UUID API重制版，[原作UUID API链接：https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api)

本插件使用了原api获取 正版/离线服务器 uuid 的所有代码

### 重制版额外特性：

1. 增加更多命令，便于管理uuid。
2. 所有已获取的 uuid 存放到 `uuid.json` 数据文件中统一管理。
3. 增加 `get_name(uuid)` 函数，可以由uuid获取玩家名。(获取范围为 `uuid.json` `usercache.json`)

### 本插件uuid获取流程 (如果获取失败则执行下一步)：

1. 读取插件数据文件 `uuid.json`
2. 读取  `usercache.json` ，若读取成功，存放到 `uuid.json`
3. 调用原api，若获取成功，存放到 `uuid.json`
4. 使用 `玩家名+时间戳` 的哈希值(sha256)的前50位作为伪uuid，存放到 `uuid.json`

### 配置文件

```json
{
    "mojang_online_mode": true,
    "online_api": "https://api.mojang.com/users/profiles/minecraft/",
    "use_offline_api": true,
    "offline_api": "http://tools.glowingmines.eu/convertor/nick/"
}
```

**mojang_online_mode**: 服务器是否为正版服务器，若为true则使用正版api获取uuid

**online_api**: 正版api地址，默认为 `https://api.mojang.com/users/profiles/minecraft/`

**use_offline_api**: 是否使用离线api获取uuid，默认为true。当mojang_online_mode为false时，该项生效。

**offline_api**: 离线api地址，默认为 `http://tools.glowingmines.eu/convertor/nick/`

**注**：请保证配置文件中该四项完整。如果使用了自定义api，请注意不要忘记最后的 `/`

### 命令

除了 `!!uar` `!!uar help` ，其他命令只能在控制台使用

具体使用方法请参考  `!!uar` 或 `!!uar help`

### API使用方法

获取玩家名对应的uuid：

```python
import uuid_api_remake

name = ... # str
uuid = uuid_api_remake.get_uuid(name)
print(uuid)
```

获取uuid对应的玩家名(获取范围为 `uuid.json` `usercache.json`)

```python
import uuid_api_remake

uuid = ... # str
name = uuid_api_remake.get_name(uuid)
print(name)
```

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v1.1.0) | 1.1.0 | 2025/03/14 08:24:12 | 9.8KB | 43 | [下载](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v1.1.0/uuid_api_remake.mcdr) |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v1.0.0) | 1.0.0 | 2025/03/13 13:12:08 | 9.38KB | 10 | [下载](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v1.0.0/uuid_api_remake.mcdr) |

