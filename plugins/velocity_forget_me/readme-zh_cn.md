[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## velocity_forget_me

### 基本信息

- 插件 ID: `velocity_forget_me`
- 插件名: Velocity Forget Me
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 4
- 作者: tanh_Heng
- 仓库: https://github.com/LazyAlienServer/VelocityForgetMe
- 仓库插件页: https://github.com/LazyAlienServer/VelocityForgetMe/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 玩家因连接异常在加入服务器后立即断开时，清除 RememberMe 中该服务器的记录。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.2.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# Velocity Forget Me

中文 | [English](https://github.com/LazyAlienServer/VelocityForgetMe/tree/main/./README_en.md)

一个基于 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 和 [RememberMe](https://github.com/ActualPlayer/RememberMe) 的 Velocity 辅助插件。当玩家连接到某个后端服务器后，在短时间内因连接错误断开时，删除文件记录，避免玩家下次登录时被再次传送到故障服务器。

## 特性

- 支持自定义连接日志正则表达式。
- 以“玩家 + 服务器”作为 session 标识。
  - 同一玩家连接不同服务器时，session 互不覆盖、互不影响。
- 默认将三秒内的同服务器连接/断开视为一次立即断开。
- 仅当以下条件全部满足时删除记录：
  - 玩家存在对应的连接 session；
  - 连接服务器与断开服务器相同；
  - 断开时间不超过配置的时间窗口；
  - UUID 查询成功；
  - RememberMe 文件内容与该服务器名相同。

## 依赖

- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) `>=2.2.0`
- 能访问 PlayerDB API 的网络环境。

## 限制

- 暂不计划支持 [VelocityRememberServer](https://github.com/TISUnion/VelocityRememberServer)，也许你应该尝试一下 [RememberMe](https://github.com/ActualPlayer/RememberMe) 作为更“新”的替代品？
- 仅支持文件形式的 RememberMe 记录，不支持 LuckPerms `last-server` 元数据。
- 玩家连接后没有对应断开事件时，session 会保留在内存中，直到对应 session 收到断开事件、插件卸载或 MCDR 重载插件。
- UUID 查询依赖外部 PlayerDB 服务；查询失败时不会删除记录。

## 效果

```
[Server] [23:38:45 INFO]: [server connection] tanh_Heng -> survival has connected
[Server] [23:38:45 INFO]: [server connection] tanh_Heng -> creative has disconnected
[Server] [23:38:45 INFO]: [connected player] tanh_Heng (/223.64.14.141:10642) has disconnected
[Server] [23:38:45 INFO]: [server connection] tanh_Heng -> survival has disconnected
[MCDR] [23:38:45] [Thread-48 (process)/INFO] [velocity_forget_me]: Removed RememberMe record for tanh_Heng after an early disconnect
```
tanh_Heng 下次进入 velocity 群组时，将不会加入 survival 服务器。

## 配置文件

默认配置：

```json
{
    "record_directory": "plugins/rememberme",
    "disconnect_window_seconds": 3.0,
    "connection_regex": "^\\[server connection\\]\\s*(?P<player>[A-Za-z0-9_]{1,16})\\s*->\\s*(?P<server>\\S+)\\s+has\\s+(?P<action>connected|disconnected)$",
    "uuid_api_url": "https://playerdb.co/api/player/minecraft/{player}",
    "uuid_api_timeout_seconds": 5.0,
    "uuid_cache_seconds": 3600.0
}
```

### 配置项

**record_directory** `str` | 默认值 `plugins/rememberme`
- RememberMe 记录目录。相对路径相对于 MCDR 配置中的 `working_directory`。

**disconnect_window_seconds** `float` | 默认值 `3.0`
- 必须大于 `0`。玩家从连接到断开的最长时间。超过该时间的断开事件不会删除 RememberMe 记录。

**connection_regex** `str`
- 默认值

   ```
   ^\\[server connection\\]\\s*(?P<player>[A-Za-z0-9_]{1,16})\\s*->\\s*(?P<server>\\S+)\\s+has\\s+(?P<action>connected|disconnected)$
   ```
- 用于匹配 `Info.content`，必须包含命名捕获组 `player`（玩家名）、`server`（服务器名）和 `action`（`connected` 或 `disconnected`）。默认匹配以下日志：

  ```text
  [server connection] Steve -> lobby has connected
  [server connection] Steve -> lobby has disconnected
  ```

- MCDR 已经移除了时间戳和线程前缀，因此正则只需要匹配 `Info.content`，不需要匹配完整原始日志行。

**uuid_api_url** `str` | 默认值 `https://playerdb.co/api/player/minecraft/{player}`
- 必须是包含 `{player}` 的 HTTP(S) URL 模板。

**uuid_api_timeout_seconds** `float` | 默认值 `5.0`
- 必须大于 `0`。UUID 网络查询超时时间。

**uuid_cache_seconds** `float` | 默认值 `3600.0`
- 必须大于等于 `0`。按玩家名缓存在线 UUID 的时间。该缓存只用于减少 API 请求，不会改变 session 的服务器隔离规则。

## RememberMe 文件要求

插件假定每个玩家的记录文件为：

```text
<record_directory>/<uuid>.txt
```

文件内容应为保存的服务器名，例如：

```text
lobby
```

删除前会要求：

```text
连接服务器 == 断开服务器 == 文件内容
```

如果文件内容是 `survival`，但本次 session 来自 `lobby`，插件会保留文件。

## 日志

插件不会为每一条成功的连接和断开输出日志。

常见日志包括：

- `INFO`：成功删除记录；
- `WARNING`：配置错误、UUID 查询失败、服务器不匹配或文件内容不匹配；
- `ERROR`：读取或删除文件失败、处理过程中出现未预期异常；
- `DEBUG`：记录文件不存在或文件在删除前消失。

成功删除时的日志类似：

```text
Removed RememberMe record for Player after an early disconnect
```

## 配置错误处理

插件使用 MCDR 原生配置加载：

- 配置文件不存在时，MCDR 使用默认值生成配置；
- 配置文件读取失败或配置值无效时，插件输出 `WARNING` 并禁用全部处理；
- 插件不会使用一份未经验证的配置继续运行；
- 修改配置后需要重新加载插件。

## 开发文档

实现流程、session 隔离、事件顺序和线程模型见 [开发文档](https://github.com/LazyAlienServer/VelocityForgetMe/tree/main/./docs/development.md)。

*本插件使用AI辅助完成。*

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [VelocityForgetMe-v1.0.0.mcdr](https://github.com/LazyAlienServer/VelocityForgetMe/releases/tag/v1.0.0) | 1.0.0 | 2026/08/05 16:11:13 | 18.73KB | 4 | [下载](https://github.com/LazyAlienServer/VelocityForgetMe/releases/download/v1.0.0/VelocityForgetMe-v1.0.0.mcdr) |

