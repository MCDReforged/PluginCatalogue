[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## console_command_api

### 基本信息

- 插件 ID: `console_command_api`
- 插件名: Console Command API
- 版本: 1.0.1
  - 元数据版本: 1.0.1
  - 发布版本: 1.0.1
- 总下载量: 50
- 作者: [Xc_Star](https://github.com/Xc-Star)
- 仓库: https://github.com/Xc-Star/console_command_api
- 仓库插件页: https://github.com/Xc-Star/console_command_api/tree/main
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 通过 HTTP API 执行控制台命令并获取响应

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [fastapi](https://pypi.org/project/fastapi) |  |
| [uvicorn](https://pypi.org/project/uvicorn) |  |
| [pydantic](https://pypi.org/project/pydantic) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.0.0 |

```
pip install fastapi uvicorn pydantic "mcdreforged>=2.0.0"
```

### 介绍

# Console Command API

[English](https://github.com/Xc-Star/console_command_api/tree/main/./README.md) | [简体中文](https://github.com/Xc-Star/console_command_api/tree/main/./README.zh_cn.md)

Console Command API 是一个 MCDReforged 插件，用于通过 HTTP API 执行命令并获取输出结果。

它同时支持两类命令：

- 以 `!!` 开头的命令会被当作 MCDR 命令执行
- 不以 `!!` 开头的命令会被当作 Minecraft 服务端控制台命令执行

## 功能

- 通过 HTTP 执行 MCDR 命令
- 通过 HTTP 执行 Minecraft 服务端控制台命令
- 在 HTTP 响应中返回捕获到的命令输出
- 使用 Bearer Token 进行鉴权
- 提供简单的健康检查接口

## 依赖

- 与当前 MCDR 运行环境兼容的 Python
- `mcdreforged>=2.0.0`
- `fastapi`
- `uvicorn`
- `pydantic`

## 配置

插件首次加载时会自动生成配置文件。

当前配置项如下：

```json
{
  "token": "",
  "timeout": 5.0,
  "idle_timeout": 0.2,
  "host": "0.0.0.0",
  "port": 8000
}
```

### 字段说明

- `token`：HTTP API 使用的 Bearer Token。如果为空，插件首次加载时会自动生成。
- `timeout`：等待命令输出的最长时间，单位为秒。
- `idle_timeout`：MCDR 命令输出收集时额外等待的静默窗口，单位为秒。
- `host`：HTTP 服务绑定地址。
- `port`：HTTP 服务监听端口。

## API

### 鉴权

所有接口都使用 Bearer Token：

```http
Authorization: Bearer <token>
```

### `GET /health`

返回插件当前健康状态。

示例响应：

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "status": "ok",
    "server_running": true
  }
}
```

### `POST /execute`

执行命令并返回捕获到的输出。

请求体：

```json
{
  "command": "!!MCDR plugin list"
}
```

### 命令路由规则

- `!!MCDR plugin list` -> 按 MCDR 命令执行
- `list` -> 按 Minecraft 服务端控制台命令执行

成功响应示例：

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "request_id": "2b0f0f34-2f0f-4d97-9e2f-123456789abc",
    "command": "!!MCDR plugin list",
    "command_type": "mcdr",
    "output": [
      "..."
    ],
    "output_text": "...",
    "timed_out": false
  }
}
```

错误响应示例：

```json
{
  "code": 401,
  "msg": "Invalid authentication token",
  "data": null
}
```

## 说明

- MCDR 命令通过自定义 `CommandSource` 和临时日志捕获来收集输出。
- Minecraft 服务端命令通过服务端输出中的开始/结束标记来截取响应。
- Minecraft 服务端命令要求游戏服务端已经处于运行状态。
- 为了避免并发请求之间的输出互相串台，插件会串行执行命令请求。

## 许可证

本项目使用 MIT License。详见 [LICENSE](https://github.com/Xc-Star/console_command_api/tree/main/./LICENSE)。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ConsoleCommandAPI-v1.0.1.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v1.0.1) | 1.0.1 | 2026/05/09 06:27:05 | 6.95KB | 41 | [下载](https://github.com/Xc-Star/console_command_api/releases/download/v1.0.1/ConsoleCommandAPI-v1.0.1.mcdr) |
| [ConsoleCommandAPI-v1.0.0.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v1.0.0) | 1.0.0 | 2026/05/08 16:06:16 | 6.96KB | 9 | [下载](https://github.com/Xc-Star/console_command_api/releases/download/v1.0.0/ConsoleCommandAPI-v1.0.0.mcdr) |

