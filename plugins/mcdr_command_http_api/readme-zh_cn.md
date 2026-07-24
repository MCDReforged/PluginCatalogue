[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mcdr_command_http_api

### 基本信息

- 插件 ID: `mcdr_command_http_api`
- 插件名: MCDR Command HTTP API
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 86
- 作者: [Andy Zhang](https://github.com/AnzhiZhang)
- 仓库: https://github.com/AnzhiZhang/MCDReforgedPlugins
- 仓库插件页: https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/mcdr_command_http_api
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 提供 HTTP 调用 MCDR 命令的接口

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [fastapi_mcdr](/plugins/fastapi_mcdr/readme-zh_cn.md) | 2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

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

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MCDRCommandHTTPAPI-v1.0.0.mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/tag/mcdr_command_http_api-v1.0.0) | 1.0.0 | 2026/04/18 01:19:12 | 1.55KB | 86 | [下载](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/download/mcdr_command_http_api-v1.0.0/MCDRCommandHTTPAPI-v1.0.0.mcdr) |

