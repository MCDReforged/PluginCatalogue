**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## console_command_api

### Basic Information

- Plugin ID: `console_command_api`
- Plugin Name: Console Command API
- Version: 2.1.0
  - Metadata version: 2.1.0
  - Release version: 2.1.0
- Total downloads: 63
- Authors: [Xc_Star](https://github.com/Xc-Star)
- Repository: https://github.com/Xc-Star/console_command_api
- Repository plugin page: https://github.com/Xc-Star/console_command_api/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: Execute console commands via WebSocket and get responses (v2)

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [websockets](https://pypi.org/project/websockets) | ==12.0 |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.0.0 |

```
pip install websockets==12.0 "mcdreforged>=2.0.0"
```

### Introduction

# Console Command API

[English](https://github.com/Xc-Star/console_command_api/tree/main/./README.md) | [简体中文](https://github.com/Xc-Star/console_command_api/tree/main/./README.zh_cn.md)

Console Command API is an MCDReforged plugin that provides a WebSocket API for executing commands and retrieving their output. Multiple MCDR servers can connect to a single central WS Server, enabling unified command execution and **output retrieval**.

## Features

- Execute MCDR commands (starting with `!!`) over WebSocket
- Execute Minecraft server console commands over WebSocket
- Return structured command output in responses
- Bearer token authentication
- Support multiple MCDR servers via unique `server_name` identifier
- Auto-reconnection on connection loss
- Command serialization to prevent mixed output

## Migration from v1

### What's New in v2

| Feature      | v1                      | v2                             |
| ------------ | ----------------------- | ------------------------------ |
| Protocol     | HTTP                    | WebSocket                      |
| Reconnection | Manual restart required | Automatic reconnection         |
| Architecture | Standalone plugin       | Plugin + centralized WS Server |

### Which Version to Choose

- v2 is designed for servers with multiple sub-servers.
- With many sub-servers, v1 would consume many ports and be hard to manage.
- v2 centralizes multi-server communication through [cca_client](https://github.com/Xc-Star/cca_client) for unified routing.
- For single-server setups, v1 is recommended - simpler and easier to use.
- Of course, v1 can also work with multiple servers.

### Breaking Changes

- **No longer standalone**: v2 requires [cca_client](https://github.com/Xc-Star/cca_client)
- **Configuration format changed**: `config.json` structure has been updated
- **Token required**: Plugin and cca_client must share the same token

### Upgrade Steps

1. Install and start [cca_client](https://github.com/Xc-Star/cca_client)
2. Copy the generated token from cca_client console, or go to
3. Update plugin `config.json` with the token and cca_client address
4. Remove any v1 configurations or dependencies

## Installation

### Prerequisites

- Python environment compatible with your MCDR installation
- `mcdreforged>=2.0.0`
- `websockets>=12.0`

### Recommended Method

1. Use the installation method from the MCDR plugin website:
2. Run `!!MCDR plugin install console_command_api` in MCDR
3. Then run `!!MCDR plugin load console_command_api` to load the plugin and generate the config file

### Manual Installation

1. Go to the plugin's [GitHub](https://github.com/Xc-Star/console_command_api) page
2. Download your desired version from Releases
3. Place the plugin in MCDR's plugins directory
4. For v2, run `pip install websockets`. For v1, run `pip install fastapi uvicorn pydantic`

## Configuration

### config.json

The plugin auto-generates this file on first load.

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

| Field                | Type   | Default                | Description                                            |
| -------------------- | ------ | ---------------------- | ------------------------------------------------------ |
| `token`              | string | (empty)                | Bearer token. **Must match WS Server config.**         |
| `timeout`            | float  | 5.0                    | Max seconds to wait for command output.                |
| `idle_timeout`       | float  | 0.2                    | Quiet window (seconds) for MCDR output collection.     |
| `ws_url`             | string | ws://127.0.0.1:8001/ws | WebSocket server URL.                                  |
| `server_name`        | string | default                | Unique identifier for this MCDR server.                |
| `auto_reconnect`     | bool   | true                   | Auto-reconnect on connection loss.                     |
| `reconnect_interval` | float  | 5.0                    | Base interval (seconds) between reconnection attempts. |

### Configuration Notes

1. **Token Synchronization**: Plugin token must match WS Server token exactly. If they differ, the WS Server will reject the connection with code 1008.

2. **server_name Uniqueness**: Each MCDR server connected to the same WS Server must have a unique `server_name`. Clients use this to route commands.

3. **Timeout Tuning**: Increase `timeout` if your commands take longer to execute. `idle_timeout` helps capture multi-line outputs.

## WebSocket API

The complete API is provided by [cca_client](https://github.com/Xc-Star/cca_client). Please refer to its documentation for the full API reference.

### Quick Reference

**Command Request:**
```json
{
  "type": "command",
  "request_id": "uuid-string",
  "command": "!!MCDR plugin list",
  "server_name": "server_1"
}
```

**Command Routing:**
- Commands starting with `!!` → Executed as MCDR commands
- Commands without `!!` → Executed as Minecraft server console commands

## Troubleshooting

### "Invalid token" errors

1. Ensure WS Server token is not empty
2. Verify plugin `token` matches WS Server `token`
3. Restart WS Server and note the new generated token

### Command timeout

- Increase `timeout` in plugin config
- Check if the Minecraft server is responsive

### No output captured

- For MCDR commands: Check if `idle_timeout` is large enough
- For MC server commands: Ensure server is running and not frozen

## License

MIT License. See [LICENSE](https://github.com/Xc-Star/console_command_api/tree/main/./LICENSE) for details.

## Related Links

- [cca_client](https://github.com/Xc-Star/cca_client) - WS Server component
- [MCDReforged](https://github.com/MCDReforged/MCDReforged) - MCDR framework

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ConsoleCommandAPI-v2.1.0.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v2.1.0) | 2.1.0 | 2026/09/02 07:43:41 | 8.48KB | 11 | [Download](https://github.com/Xc-Star/console_command_api/releases/download/v2.1.0/ConsoleCommandAPI-v2.1.0.mcdr) |
| [ConsoleCommandAPI-v1.0.1.mcdr](https://github.com/Xc-Star/console_command_api/releases/tag/v1.0.1) | 1.0.1 | 2026/05/09 06:27:05 | 6.95KB | 52 | [Download](https://github.com/Xc-Star/console_command_api/releases/download/v1.0.1/ConsoleCommandAPI-v1.0.1.mcdr) |

