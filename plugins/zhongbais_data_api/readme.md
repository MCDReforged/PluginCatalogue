**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## zhongbais_data_api

### Basic Information

- Plugin ID: `zhongbais_data_api`
- Plugin Name: zhongbaisDataAPI
- Version: 0.2.4
  - Metadata version: 0.2.4
  - Release version: 0.2.4
- Total downloads: 195
- Authors: [zhongbai233](https://github.com/zhongbai2333)
- Repository: https://github.com/zhongbai2333/zhongbais-Data-API
- Repository plugin page: https://github.com/zhongbai2333/zhongbais-Data-API/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: Polling /data command related APIs

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |

```
pip install mcdreforged
```

### Introduction

# zhongbais Data API

A MCDReforged–based player position retrieval and callback API. It encapsulates timed polling and callback mechanisms, making it easy for other plugins or scripts to uniformly access and subscribe to changes in player position, dimension, rotation, and more.

English | [简中](https://github.com/zhongbai2333/zhongbais-Data-API/tree/main/README_zh.md)

---

## Features

- **Timed Polling**: Automatically polls all online players’ NBT data via RCON at the configured interval
- **Callback System**: Built-in lists of callbacks let you subscribe to specific NBT fields or to player list changes

---

## Quick Start

```python
from mcdreforged.api.all import PluginServerInterface, new_thread
from zhongbais_data_api import zbDataAPI

def on_load(self, server: PluginServerInterface, old):
    # Listen for *all* NBT changes
    zbDataAPI.register_player_info_callback(self.on_player_update)
    # Or listen for specific NBT fields only:
    # zbDataAPI.register_player_info_callback(self.on_player_update, ['Pos', 'Dimension', ...])

    # Listen for player join/leave events
    zbDataAPI.register_player_list_callback(self.on_player_list_change)

def on_player_update(self, name: str, info: dict):
    """
    name: player’s name
    info: {
      "Pos": [...],         # position [x, y, z]
      "Rotation": [...],    # rotation [yaw, pitch]
      "Dimension": "...",   # dimension
      …                     # other fields as configured
    }
    """
    self.server.logger.info(f"[PlayerUpdate] {name} -> {info}")

def on_player_list_change(self, player: str, current_list: list):
    # player: name of the player who joined or left
    # current_list: list of all online players
    self.server.logger.info(f"[PlayerList] {player} changed, now: {current_list}")

# Manually trigger a data fetch (e.g. for testing)
zbDataAPI.refresh_getpos()
```

---

## Configuration

Only the bot detection related config is listed here; others can stay at their defaults:

- bot_keyword (bot keyword)
  - Used to detect and ignore bot player names.
  - Supports glob-style wildcards: `*`, `?`, `[]`.
  - If no wildcard is present, falls back to substring check (backward compatible with older versions).
  - Matching is case-insensitive.
  - Examples:
    - `bot_*`: matches names starting with `bot_`, e.g., `bot_alice`.
    - `*_bot`: matches names ending with `_bot`, e.g., `helper_bot`.
    - `Bot??Bot*`: matches `Bot` + any two chars + `Bot` + any suffix, e.g., `Bot12BotX`, `BotA3Bot_something`.

> Tip: To keep the old behavior where any name containing `bot_` is treated as a bot, set it to `bot_` (without wildcards).

---

## API Documentation

### `zbDataAPI.register_player_info_callback(func, list=[]) -> None`

Automatically delivers NBT data (position, dimension, rotation, etc.) for players.
If `list` is empty (default), listens to *all* players; otherwise, only to the specified NBT fields.

> **Parameters**
> 
> - `func(name: str, info: dict)`: callback function; `name` is the player’s name, `info` is a dict of the latest data.
> - `list: list` (optional): list of NBT field names to listen for, default `[]`.

---

### `zbDataAPI.get_player_list() -> list`

Returns the list of currently online player names.

```python
players = zbDataAPI.get_player_list()
```

---

### `zbDataAPI.register_player_list_callback(func) -> None`

Triggered when a player joins or leaves.

> **Parameters**
> 
> - `func(player: str, current_list: list)`: callback function; `player` is the name of the joined/left player, `current_list` is the updated list of online players.

---

### `zbDataAPI.refresh_getpos() -> None`

Manually triggers a data fetch, equivalent to the internal timed polling.

---

## Development & Contribution

1. Fork this repository
2. Create a branch `feature/xxx`
3. Commit your changes and open a Pull Request

Contributions, issues, and PRs are welcome to make this API even better!

---

## License

This project is licensed under GPLv3. See [LICENSE](https://github.com/zhongbai2333/zhongbais-Data-API/tree/main/./LICENSE) for details.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [zhongbaisDataAPI-v0.2.4.mcdr](https://github.com/zhongbai2333/zhongbais-Data-API/releases/tag/v0.2.4) | 0.2.4 | 2026/01/12 02:51:14 | 19.9KB | 20 | [Download](https://github.com/zhongbai2333/zhongbais-Data-API/releases/download/v0.2.4/zhongbaisDataAPI-v0.2.4.mcdr) |
| [zhongbaisDataAPI-v0.2.3.mcdr](https://github.com/zhongbai2333/zhongbais-Data-API/releases/tag/v0.2.3) | 0.2.3 | 2025/10/25 05:32:41 | 19.85KB | 24 | [Download](https://github.com/zhongbai2333/zhongbais-Data-API/releases/download/v0.2.3/zhongbaisDataAPI-v0.2.3.mcdr) |
| [zhongbaisDataAPI-v0.2.2.mcdr](https://github.com/zhongbai2333/zhongbais-Data-API/releases/tag/v0.2.2) | 0.2.2 | 2025/08/22 13:34:28 | 19.25KB | 47 | [Download](https://github.com/zhongbai2333/zhongbais-Data-API/releases/download/v0.2.2/zhongbaisDataAPI-v0.2.2.mcdr) |
| [zhongbaisDataAPI-v0.2.1.mcdr](https://github.com/zhongbai2333/zhongbais-Data-API/releases/tag/v0.2.1) | 0.2.1 | 2025/08/22 03:50:02 | 19.07KB | 23 | [Download](https://github.com/zhongbai2333/zhongbais-Data-API/releases/download/v0.2.1/zhongbaisDataAPI-v0.2.1.mcdr) |
| [zhongbaisDataAPI-v0.2.0.mcdr](https://github.com/zhongbai2333/zhongbais-Data-API/releases/tag/v0.2.0) | 0.2.0 | 2025/05/11 02:30:50 | 17.71KB | 30 | [Download](https://github.com/zhongbai2333/zhongbais-Data-API/releases/download/v0.2.0/zhongbaisDataAPI-v0.2.0.mcdr) |
| [zhongbaisDataAPI-v0.1.1.mcdr](https://github.com/zhongbai2333/zhongbais-Data-API/releases/tag/v0.1.1) | 0.1.1 | 2025/05/06 14:57:46 | 17.27KB | 25 | [Download](https://github.com/zhongbai2333/zhongbais-Data-API/releases/download/v0.1.1/zhongbaisDataAPI-v0.1.1.mcdr) |
| [zhongbaisDataAPI-v0.1.0.mcdr](https://github.com/zhongbai2333/zhongbais-Data-API/releases/tag/v0.1.0) | 0.1.0 | 2025/05/06 13:59:51 | 17.25KB | 26 | [Download](https://github.com/zhongbai2333/zhongbais-Data-API/releases/download/v0.1.0/zhongbaisDataAPI-v0.1.0.mcdr) |

