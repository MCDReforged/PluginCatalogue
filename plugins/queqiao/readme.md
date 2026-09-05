**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## queqiao

### Basic Information

- Plugin ID: `queqiao`
- Plugin Name: QueQiao
- Version: 1.0.1
  - Metadata version: 1.0.1
  - Release version: 1.0.1
- Total downloads: 23
- Authors: [LonelySail](https://github.com/Lonely-Sails)
- Repository: https://github.com/Minecraft-UniBot/QueQiao.MCDReforged
- Repository plugin page: https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/tree/master
- Labels: [`API`](/labels/api/readme.md)
- Description: QueQiao V2 protocol bridge plugin supporting forward/reverse WebSocket connections for message exchange between Minecraft and external systems

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |
| [mg_events](/plugins/mg_events/readme.md) | * |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | * |
| [online_player_api](/plugins/online_player_api/readme.md) | * |

### Requirements

| Python package | Requirement |
| --- | --- |
| [websockets](https://pypi.org/project/websockets) | \>=12.0 |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0 |
| [psutil](https://pypi.org/project/psutil) | \>=5.9 |

```
pip install "websockets>=12.0" "PyYAML>=6.0" "psutil>=5.9"
```

### Introduction

# QueQiao MCDR

A MCDReforged plugin bridging the **QueQiao V2 protocol**, supporting both forward WebSocket (client) and reverse WebSocket (server) connection modes for real-time message exchange between a Minecraft server and external systems (e.g. NoneBot / QueQiao server).

## 📖 Compatible Projects

This plugin follows the QueQiao V2 protocol and can interoperate with:

- [UniBot](https://github.com/MineJPGcraft/UniBot) — A cross-platform Minecraft bot; this plugin serves as its MCDR endpoint
- [nonebot-adapter-minecraft](https://github.com/17TheWord/nonebot-adapter-minecraft) — A NoneBot adapter for Minecraft that communicates with this plugin via the QueQiao protocol
- [QueQiao](https://github.com/17TheWord/QueQiao) — The official QueQiao protocol implementation

## ✨ Features

### Connection
- 🔌 **Dual-mode WebSocket**: client mode actively connects to the QueQiao server; server mode passively waits for QueQiao clients
- 🔁 **Auto-reconnect** (client mode): configurable reconnect interval and max retry count
- 🔥 **Hot reload**: `!!queqiao reload` reloads config and reuses the existing connection without restarting the server

### API Handling (QueQiao → MCDR)
| API                 | Description                                                |
| ------------------- | ---------------------------------------------------------- |
| `broadcast`         | Broadcast a message to the game                            |
| `send_private_msg`  | Send a private message to a specific player                |
| `send_title`        | Send a title/subtitle (configurable fade-in/stay/fade-out) |
| `send_actionbar`    | Send an ActionBar message                                  |
| `send_rcon_command` | Execute a RCON command and return the result               |
| `get_status`        | Query server status (CPU/memory/players/MOTD, etc.)        |

### Game Event Forwarding (MCDR → QueQiao)
| Event                 | Source                                                                                 |
| --------------------- | -------------------------------------------------------------------------------------- |
| Player join / quit    | MCDR built-in events                                                                   |
| Player chat / command | MCDR `USER_INFO` event                                                                 |
| Player death          | [MoreGameEvents](https://mcdreforged.com/en/plugin/mg_events) `PlayerDeathEvent`       |
| Player advancement    | [MoreGameEvents](https://mcdreforged.com/en/plugin/mg_events) `PlayerAdvancementEvent` |

## 📦 Installation

### Option 1: Download the .mcdr package
Download `QueQiao-vX.X.X.mcdr` from [Releases](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/releases) and drop it into the MCDR `plugins/` directory.

### Option 2: From source
```bash
git clone https://github.com/Minecraft-UniBot/QueQiao.MCDReforged.git
cd QueQiao.MCDReforged
uv sync
```
Use the whole directory as a Directory Plugin, or pack it yourself:
```bash
uv run python -m mcdreforged pack
```

## 🎮 Commands

| Command            | Permission | Description                                                     |
| ------------------ | ---------- | --------------------------------------------------------------- |
| `!!queqiao`        | 2          | Show help                                                       |
| `!!queqiao status` | 2          | View connection status (mode, players, CPU, memory, MOTD, etc.) |
| `!!queqiao reload` | 2          | Reload config and reconnect                                     |

## 📋 Dependencies

### Runtime
- **MCDReforged** >= 2.15.0
- **Python** >= 3.12

### Python packages
- `websockets` >= 16.0
- `PyYAML` >= 6.0
- `psutil` >= 5.9

### MCDR plugin dependencies
| Plugin                                                                     | Usage                             | Required                                                 |
| -------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------- |
| [MoreGameEvents](https://mcdreforged.com/en/plugin/mg_events)              | Player death & advancement events | ✅                                                        |
| [Minecraft Data API](https://mcdreforged.com/en/plugin/minecraft_data_api) | Player coords, health, XP level   | ✅                                                        |
| [online_player_api](https://mcdreforged.com/en/plugin/online_player_api)   | Online player list                | ⚠️ Optional (falls back to MCDR built-in API if missing) |

## �📄 License

[MIT](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/tree/master/docs/./LICENSE)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [QueQiao-v1.0.1.mcdr](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/releases/tag/v1.0.1) | 1.0.1 | 2026/08/02 23:46:22 | 21.32KB | 23 | [Download](https://github.com/Minecraft-UniBot/QueQiao.MCDReforged/releases/download/v1.0.1/QueQiao-v1.0.1.mcdr) |

