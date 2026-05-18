**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mcdr_command_http_api

### Basic Information

- Plugin ID: `mcdr_command_http_api`
- Plugin Name: MCDR Command HTTP API
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 22
- Authors: [Andy Zhang](https://github.com/AnzhiZhang)
- Repository: https://github.com/AnzhiZhang/MCDReforgedPlugins
- Repository plugin page: https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/mcdr_command_http_api
- Labels: [`API`](/labels/api/readme.md)
- Description: Provide an interface for calling MCDR commands via HTTP

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [fastapi_mcdr](/plugins/fastapi_mcdr/readme.md) | 2.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# MCDR Command HTTP API

> 提供 HTTP 调用 MCDR 命令的接口

## 依赖

| 插件 | 版本 |
| - | - |
| [fastapi_mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/fastapi_mcdr) | \>=2.0.0 |

## 配置

配置文件路径：`config/mcdr_command_http_api/config.json`

| 配置项 | 默认值 | 说明 |
| - | - | - |
| `token` | 随机生成 | 接口鉴权 Token，首次加载时自动生成 |

## 接口

所有接口均挂载在 `/mcdr_command_http_api` 路径下。

### 鉴权

请求时需在 HTTP Header 中携带 Bearer Token：

```http
Authorization: Bearer <token>
```

### POST /mcdr_command_http_api/execute

在 MCDR 命令系统中执行一条命令。

#### 请求体

```json
{
  "command": "!!MCDR status"
}
```

| 字段 | 类型 | 说明 |
| - | - | - |
| `command` | `string` | 要执行的 MCDR 命令 |

#### 响应

```json
{
  "status": "ok",
  "command": "!!MCDR status"
}
```

#### 错误码

| 状态码 | 说明 |
| - | - |
| `401` | Token 无效 |

## 在线调试

启动 MCDR 后访问 `http://<服务器IP>:8080/mcdr_command_http_api/docs` 可使用 Swagger UI 在线测试接口。

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MCDRCommandHTTPAPI-v1.0.0.mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/tag/mcdr_command_http_api-v1.0.0) | 1.0.0 | 2026/04/18 01:19:12 | 1.55KB | 22 | [Download](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/download/mcdr_command_http_api-v1.0.0/MCDRCommandHTTPAPI-v1.0.0.mcdr) |

