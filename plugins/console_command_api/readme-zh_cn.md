[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## console_command_api

### 基本信息

- 插件 ID: `console_command_api`
- 插件名: Console Command API
- 版本: 2.1.0
  - 元数据版本: 2.1.0
  - 发布版本: 2.1.0
- 总下载量: 63
- 作者: [Xc_Star](https://github.com/Xc-Star)
- 仓库: https://github.com/Xc-Star/console_command_api
- 仓库插件页: https://github.com/Xc-Star/console_command_api/tree/main
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 通过 WebSocket 执行控制台命令并获取响应 (v2)

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [websockets](https://pypi.org/project/websockets) | ==12.0 |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.0.0 |

```
pip install websockets==12.0 "mcdreforged>=2.0.0"
```

### 介绍

# Console Command API

[English](https://github.com/Xc-Star/console_command_api/tree/main/./README.md) | [简体中文](https://github.com/Xc-Star/console_command_api/tree/main/./README.zh_cn.md)

Console Command API 是一个 MCDReforged 插件，通过 WebSocket API 执行命令并获取输出结果。多个 MCDR 服务器可以连接到同一个中央 WS Server，实现统一的命令执行与**获取执行结果**。

## 功能

- 通过 WebSocket 执行 MCDR 命令（以 `!!` 开头）
- 通过 WebSocket 执行 Minecraft 服务端控制台命令
- 在响应中返回结构化的命令输出
- Bearer Token 鉴权
- 通过唯一的 `server_name` 支持多个 MCDR 服务器
- 连接断开时自动重连
- 命令串行执行，防止输出混乱

## 从 v1 升级

### v2 新特性

| 特性  | v1    | v2                 |
| --- | ----- | ------------------ |
| 协议  | HTTP  | WebSocket          |
| 重连  | 需手动重启 | 自动重连               |
| 架构  | 独立插件  | 插件 + 集中式 WS Server |

### 如何选择：
- v2版本是为了服务多子服的服务器的。
- 如果需要连接的子服多，则会导致服务器占用大量端口，不易于管理。
- v2版本将多服务器的通信改为统一到[cca_client](https://github.com/Xc-Star/cca_cilent)进行统一到转发
- 对于单个服务器推荐使用v1，简单易上手。
- 当然多子服选择v1也是没问题的。

### 不兼容变更

- **不再独立运行**: v2 需要配合 [cca_client](https://github.com/Xc-Star/cca_client) 使用
- **配置格式变化**: `config.json` 结构已更改
- **需要 Token**: 插件和 cca_client 必须使用相同的 Token

### 升级步骤

1. 安装并启动 [cca_client](https://github.com/Xc-Star/cca_client)
2. 从 cca_client 控制台复制生成的 Token , 或前往
3. 更新插件 `config.json`，填入 Token 和 cca_client 地址
4. 移除任何 v1 的配置或依赖

## 安装

### 前置要求

- 与 MCDR 运行环境兼容的 Python
- `mcdreforged>=2.0.0`
- `websockets>=12.0`

### 推荐方法

1. 使用MCDR插件官网提供的安装方式：
2. 在MCDR运行时执行 `!!MCDR plugin install console_command_api`命令
3. 然后执行`!!MCDR plugin load console_command_api`则会加载插件与生成配置文件

### 手动安装

1. 前往插件的[Github](https://github.com/Xc-Star/console_command_api)页
2. 在Releases中下载你需要的版本
3. 将插件放入MCDR的plugins目录中
4. 如果你是v2，请执行`pip install websockets`。如果你是v1，请执行`pip install fastapi uvicorn pydantic`

## 配置

### config.json

插件首次加载时自动生成此文件。

```json
{
  "token": "your-shared-token",
  "timeout": 5.0,
  "idle_timeout": 0.2,
  "ws_url": "ws://127.0.0.1:8001/ws",
  "server_name": "default",
  "auto_reconnect": true,
  "reconnect_interval": 5.0
}
```

| 字段                   | 类型     | 默认值                    | 说明                                   |
| -------------------- | ------ | ---------------------- | ------------------------------------ |
| `token`              | string | (空)                    | Bearer Token。**必须与 WS Server 配置一致。** |
| `timeout`            | float  | 5.0                    | 等待命令输出的最长时间（秒）。                      |
| `idle_timeout`       | float  | 0.2                    | MCDR 命令输出收集的静默窗口（秒）。                 |
| `ws_url`             | string | ws://127.0.0.1:8001/ws | WebSocket 服务器地址。                     |
| `server_name`        | string | default                | 本 MCDR 服务器的唯一标识符。                    |
| `auto_reconnect`     | bool   | true                   | 连接断开时自动重连。                           |
| `reconnect_interval` | float  | 5.0                    | 重连间隔基数（秒）。                           |

### 配置注意事项

1. **Token 同步**: 插件 Token 必须与 WS Server Token 完全一致。如果不一致，WS Server 会以 code 1008 拒绝连接。

2. **server_name 唯一性**: 连接到同一 WS Server 的每个 MCDR 服务器必须使用不同的 `server_name`。客户端通过此名称路由命令。

3. **超时调整**: 如果命令执行时间较长，请增大 `timeout`。`idle_timeout` 有助于捕获多行输出。

## WebSocket API

完整的 API 由 [cca_client](https://github.com/Xc-Star/cca_client) 提供。请参阅其文档获取完整的 API 参考。

### 快速参考

**命令请求:**
```json
{
  "type": "command",
  "request_id": "uuid-string",
  "command": "!!MCDR plugin list",
  "server_name": "server_1"
}
```

**命令路由:**
- 以 `!!` 开头的命令 → 作为 MCDR 命令执行
- 不以 `!!` 开头的命令 → 作为 Minecraft 服务端控制台命令执行

## 故障排查

### "Invalid token" 错误

1. 确保 WS Server 的 Token 不为空
2. 确认插件的 `token` 与 WS Server 的 `token` 一致
3. 重启 WS Server 并记录新生成的 Token

### 命令超时

- 在插件配置中增大 `timeout`
- 检查 Minecraft 服务器是否响应正常

### 无法捕获输出

- MCDR 命令：检查 `idle_timeout` 是否足够大
- MC 服务端命令：确保服务器正在运行且未冻结

## 许可证

MIT 许可证。详见 [LICENSE](https://github.com/Xc-Star/console_command_api/tree/main/./LICENSE)。

## 相关链接

- [cca_client](https://github.com/Xc-Star/cca_client) - WS Server 组件
- [MCDReforged](https://github.com/MCDReforged/MCDReforged) - MCDR框架

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ConsoleCommandAPI-v2.1.0.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v2.1.0) | 2.1.0 | 2026/09/02 07:43:41 | 8.48KB | 11 | [下载](https://github.com/Xc-Star/console_command_api/releases/download/v2.1.0/ConsoleCommandAPI-v2.1.0.mcdr) |
| [ConsoleCommandAPI-v1.0.1.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v1.0.1) | 1.0.1 | 2026/05/09 06:27:05 | 6.95KB | 52 | [下载](https://github.com/Xc-Star/console_command_api/releases/download/v1.0.1/ConsoleCommandAPI-v1.0.1.mcdr) |

