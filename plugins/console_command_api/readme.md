**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## console_command_api

### Basic Information

- Plugin ID: `console_command_api`
- Plugin Name: Console Command API
- Version: 1.0.1
  - Metadata version: 1.0.1
  - Release version: 1.0.1
- Total downloads: 50
- Authors: [Xc_Star](https://github.com/Xc-Star)
- Repository: https://github.com/Xc-Star/console_command_api
- Repository plugin page: https://github.com/Xc-Star/console_command_api/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: Execute console commands via HTTP API and get responses

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [fastapi](https://pypi.org/project/fastapi) |  |
| [uvicorn](https://pypi.org/project/uvicorn) |  |
| [pydantic](https://pypi.org/project/pydantic) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.0.0 |

```
pip install fastapi uvicorn pydantic "mcdreforged>=2.0.0"
```

### Introduction

# Console Command API

[English](https://github.com/Xc-Star/console_command_api/tree/main/./README.md) | [简体中文](https://github.com/Xc-Star/console_command_api/tree/main/./README.zh_cn.md)

Console Command API is an MCDReforged plugin that exposes a small HTTP API for executing commands and reading their output.

It supports both command paths:

- Commands starting with `!!` are treated as MCDR commands
- Commands without `!!` are treated as Minecraft server console commands

## Features

- Execute MCDR commands over HTTP
- Execute Minecraft server console commands over HTTP
- Return captured command output in the HTTP response
- Bearer token authentication
- Simple health check endpoint

## Requirements

- Python environment compatible with your MCDR installation
- `mcdreforged>=2.0.0`
- `fastapi`
- `uvicorn`
- `pydantic`

## Configuration

The plugin will generate its config automatically on first load.

Current config fields:

```json
{
  "token": "",
  "timeout": 5.0,
  "idle_timeout": 0.2,
  "host": "0.0.0.0",
  "port": 8000
}
```

### Fields

- `token`: Bearer token used by the HTTP API. If empty, the plugin generates one automatically on first load.
- `timeout`: Maximum time in seconds to wait for command output.
- `idle_timeout`: Additional quiet window in seconds for MCDR command output collection.
- `host`: HTTP bind address.
- `port`: HTTP listen port.

## API

### Authentication

All endpoints use Bearer token authentication:

```http
Authorization: Bearer <token>
```

### `GET /health`

Returns the plugin health status.

Example response:

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

Executes a command and returns captured output.

Request body:

```json
{
  "command": "!!MCDR plugin list"
}
```

### Command routing

- `!!MCDR plugin list` -> executed as an MCDR command
- `list` -> executed as a Minecraft server console command

Example success response:

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

Example error response:

```json
{
  "code": 401,
  "msg": "Invalid authentication token",
  "data": null
}
```

## Notes

- MCDR commands are captured through a custom `CommandSource` plus temporary log capture.
- Minecraft server commands are captured from server console output by using start/end markers.
- Minecraft server commands require the game server to be running.
- To avoid mixed output between concurrent requests, command execution is serialized.

## License

This project is licensed under the MIT License. See [LICENSE](https://github.com/Xc-Star/console_command_api/tree/main/./LICENSE) for details.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ConsoleCommandAPI-v1.0.1.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v1.0.1) | 1.0.1 | 2026/05/09 06:27:05 | 6.95KB | 41 | [Download](https://github.com/Xc-Star/console_command_api/releases/download/v1.0.1/ConsoleCommandAPI-v1.0.1.mcdr) |
| [ConsoleCommandAPI-v1.0.0.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v1.0.0) | 1.0.0 | 2026/05/08 16:06:16 | 6.96KB | 9 | [Download](https://github.com/Xc-Star/console_command_api/releases/download/v1.0.0/ConsoleCommandAPI-v1.0.0.mcdr) |

