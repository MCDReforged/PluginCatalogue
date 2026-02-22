[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## uuid_api

### 基本信息

- 插件 ID: `uuid_api`
- 插件名: UUIDAPI
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 826
- 作者: [Andy Zhang](https://github.com/AnzhiZhang)
- 仓库: https://github.com/AnzhiZhang/MCDReforgedPlugins
- 仓库插件页: https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api
- 标签: [`API`](/labels/api/readme-zh_cn.md), [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: UUID API

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [requests](https://pypi.org/project/requests) |  |

```
pip install requests
```

### 介绍

# UUID API

> 玩家 UUID API

## 依赖的 Python 模块

- requests

## 使用方法

```python
get_uuid(name: str) -> UUID | None
```

未查到时返回 `None`。

示例：

```python
uuid_api = server.get_plugin_instance('uuid_api')
uuid = uuid_api.get_uuid('Steve')
server.logger.warning(uuid)
```

## 配置

### use_usercache

默认值: `true`

是否使用 `usercache.json` 文件中的数据做为缓存来获取玩家 UUID。

### override_online_mode

默认值: `false`

是否覆盖 `server.properties` 中的 `online-mode` 设置。

如果设置为 `true`，则插件将忽略 `server.properties` 中的在线模式设置，并使用插件配置中的 `override_online_mode_value`。

如果使用了 BungeeCord 或 Velocity 等代理服务器，并开启了正版验证, 或实际的 UUID 与 `server.properties` 中的 `online-mode` 并不匹配，设置该值确保插件正确处理在线模式。

### override_online_mode_value

默认值: `true`

如果 `override_online_mode` 设置为 `true`，则此值将决定插件是否认为服务器处于在线模式。

## 鸣谢

部分代码改编自 <https://github.com/gubaiovo/MCDR_uuid_api_remake>

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [UUIDAPI-v1.0.0.mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/tag/uuid_api-v1.0.0) | 1.0.0 | 2025/07/07 02:51:16 | 2.22KB | 151 | [下载](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/download/uuid_api-v1.0.0/UUIDAPI-v1.0.0.mcdr) |
| [UUIDAPI-v0.1.2.mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/tag/uuid_api-v0.1.2) | 0.1.2 | 2023/07/18 13:53:49 | 1.53KB | 302 | [下载](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/download/uuid_api-v0.1.2/UUIDAPI-v0.1.2.mcdr) |
| [UUIDAPI-v0.1.1.mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/tag/uuid_api-v0.1.1) | 0.1.1 | 2022/06/30 12:08:40 | 1.41KB | 221 | [下载](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/download/uuid_api-v0.1.1/UUIDAPI-v0.1.1.mcdr) |
| [UUIDAPI-v0.1.0.mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/tag/uuid_api-v0.1.0) | 0.1.0 | 2022/06/30 10:03:54 | 1.42KB | 152 | [下载](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/download/uuid_api-v0.1.0/UUIDAPI-v0.1.0.mcdr) |

