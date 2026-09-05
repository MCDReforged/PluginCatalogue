**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## games_ai_extra

### Basic Information

- Plugin ID: `games_ai_extra`
- Plugin Name: GamesAI Extra
- Version: 0.2.0
  - Metadata version: 0.2.0
  - Release version: 0.2.0
- Total downloads: 32
- Authors: [yello](https://github.com/PengZixuan30), [man8in](https://github.com/man8in)
- Repository: https://github.com/PengZixuan30/Games_AI-Extra
- Repository plugin page: https://github.com/PengZixuan30/Games_AI-Extra/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Functional extension for GamesAI

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |
| [games_ai](/plugins/games_ai/readme.md) | \>=0.6.4 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [requests](https://pypi.org/project/requests) |  |
| [beautifulsoup4](https://pypi.org/project/beautifulsoup4) |  |

```
pip install requests beautifulsoup4
```

### Introduction

<div align="center">

# GamesAI Extra for MCDReforged

English  |  [简体中文](https://github.com/PengZixuan30/Games_AI-Extra/tree/main//README.zh-CN.md)  |  [繁體中文](https://github.com/PengZixuan30/Games_AI-Extra/tree/main//README.zh-TW.md)

[Report an Issue](https://github.com/PengZixuan30/Games_AI-Extra/issues/new)  |  [Share an Idea](https://github.com/PengZixuan30/Games_AI-Extra/discussions/new/choose)

</div>

> [!NOTE]
> **GamesAI Extra** is a functional extension for [GamesAI](https://github.com/PengZixuan30/Games_AI). It provides **Carpet fake player (bot) control** tools, **waypoint (location) management** tools, **Minecraft Wiki search** and **whitelist management** tools, allowing the AI to spawn/control fake players, manage waypoints, search the Minecraft Wiki and manage the whitelist on your Minecraft server.

> [!IMPORTANT]
> This plugin requires **GamesAI >= 0.6.4** to be installed and loaded first. GamesAI Extra follows the [Extension Plugin System](https://github.com/PengZixuan30/Games_AI#custom-tools-in-your-mcdr-plugin) — tools registered this way are identical to built-in tools.

<details>
<summary>Table of Contents (click to expand)</summary>

- [GamesAI Extra for MCDReforged](#gamesai-extra-for-mcdreforged)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Tools \& Skills](#tools--skills)
    - [Carpet Bot Control](#carpet-bot-control)
      - [Spawn \& Kill](#spawn--kill)
      - [Behavior Control](#behavior-control)
      - [Movement Control](#movement-control)
      - [Camera Control](#camera-control)
      - [Hotbar](#hotbar)
      - [Timed Actions](#timed-actions)
      - [Custom Commands](#custom-commands)
    - [Waypoint Management](#waypoint-management)
    - [Minecraft Wiki Search](#minecraft-wiki-search)
    - [Whitelist Management](#whitelist-management)
    - [Skills](#skills)
  - [Dependencies](#dependencies)
  - [What's New](#whats-new)
    - [Version 0.2.0](#version-020)
    - [Version 0.1.3](#version-013)
    - [Version 0.1.2](#version-012)
    - [Version 0.1.1](#version-011)
  - [License](#license)

</details>

## Installation

Run the following command in the MCDR console to install the plugin:

`!!MCDR plugin install games_ai_extra`

---

Alternatively, get it from the [MCDR Plugin Repository](https://mcdreforged.com/plugin/games_ai_extra) and place it in your plugin directory.

This plugin requires the Python packages `requests` and `beautifulsoup4`, which are declared in the plugin metadata and installed automatically when using `!!MCDR plugin install`. If you install a packed `.mcdr` file manually, make sure these packages are available in your Python environment.

## Configuration

The default configuration file (`config/games_ai_extra/config.json`) structure is as follows:

```json
{
    "carpet": true,
    "location_plguin": false,
    "where2go_plugin": true,
    "whitelist_api": true,
    "web_search": true
}
```

- **carpet**: Set to `true` to enable the Carpet fake player tools. Set to `false` to disable them.
- **location_plguin**: Set to `true` to enable waypoint management via the [Location Marker](https://mcdreforged.com/plugin/location_marker) MCDR plugin. Set to `false` to disable.
- **where2go_plugin**: Set to `true` to enable waypoint management via the [Where2Go](https://mcdreforged.com/plugin/where2go) MCDR plugin. Set to `false` to disable.
- **whitelist_api**: Set to `true` to enable whitelist management via the [WhitelistAPI](https://mcdreforged.com/plugin/whitelist_api) MCDR plugin. Set to `false` to disable.
- **web_search**: Set to `true` to enable the Minecraft Wiki search tool. Set to `false` to disable.

> [!TIP]
> `location_plguin` and `where2go_plugin` manage the same set of waypoint tools (`add_pos_pos`, `add_pos_here`, `remove_pos`, `search_pos`, `get_all_pos`). It is recommended to enable only **one** of them to avoid duplicate tool registrations. `where2go_plugin` is enabled by default.

After modifying the configuration, use `!!gamesai reload` to apply the changes.

## Tools & Skills

Once enabled, the following tools are automatically registered with GamesAI and can be called by the AI through `!!ask`.

### Carpet Bot Control

> 🤖 **Skill:** Read `carpet.md` before operating fake players. Call `read_skills("carpet.md")` to get complete instructions.

Fake player tools provided by the `carpet` module. Requires **fabric-carpet** mod installed on the server. `spawn_bot` and `kill_bot` additionally have `@register_bot_tool()`, making them available to the Mineflayer autonomous Bot controller.

#### Spawn & Kill

|    Tool     |            Parameters             | Description                                                                                                                                                                                                                                                                                                                               |
| :---------: | :-------------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spawn_bot` | `name`, `pos?`, `player?`, `dim?` | Spawn a fake player on the server. Specify `pos` (coordinates `[x, y, z]`) to spawn at a location, or `player` (username) to spawn next to a player. `pos` and `player` are mutually exclusive. Optionally specify `dim` (e.g. `minecraft:the_nether`) to spawn in a different dimension. If no location is given, spawns at world spawn. |
| `kill_bot`  |              `name`               | Remove (kill) a fake player. This operation is irreversible — use `spawn_bot` to recreate if needed.                                                                                                                                                                                                                                      |

#### Behavior Control

|     Tool     |          Parameters           | Description                                                                                                                                                                                                                                                                                                                                                             |
| :----------: | :---------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bot_action` | `name`, `action`, `interval?` | Make a fake player perform an action. Supported actions: `attack` (requires weapon), `use` (right-click target), `mine` (break block in front), `stop` (cancel all actions), `drop` (drop held item), `dropStack` (drop entire stack), `jump`, `sneak` (toggle), `swapHands`, `mount` (ride nearby entity), `dismount`. Optional `interval` in game ticks (default: 1). |

#### Movement Control

|    Tool    |     Parameters      | Description                                                                                                                                                              |
| :--------: | :-----------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bot_move` | `name`, `direction` | Make a fake player move continuously in a direction: `forward`, `backward`, `left`, or `right`. The bot keeps moving until you send a `stop` action or change direction. |

#### Camera Control

|    Tool    |    Parameters    | Description                                                                                                                                                                               |
| :--------: | :--------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bot_look` | `name`, `target` | Make a fake player look at a direction or coordinates. `target` can be a direction word (`north`, `south`, `east`, `west`, `up`, `down`) or coordinates (`"x y z"`, e.g. `"100 64 200"`). |

#### Hotbar

|     Tool     |   Parameters   | Description                                                                                                                        |
| :----------: | :------------: | ---------------------------------------------------------------------------------------------------------------------------------- |
| `bot_hotbar` | `name`, `slot` | Switch the fake player's selected hotbar slot (1–9). After switching, actions like attack/use/mine will use the item in that slot. |

#### Timed Actions

|        Tool        |          Parameters          | Description                                                                                                                                                                                                                                                                          |
| :----------------: | :--------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bot_timed_action` | `name`, `action`, `duration` | Make a fake player perform an action for a specified duration (in seconds), then automatically stop. Supports: `attack`, `use`, `mine`, `forward`, `backward`, `left`, `right`. Best suited for short operations (≤ 60s). Note: blocks the current AI conversation until time is up. |

#### Custom Commands

|     Tool      |    Parameters     | Description                                                                                                                                                                                            |
| :-----------: | :---------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bot_command` | `name`, `command` | Send a raw custom `/player` command for advanced operations not covered by the above tools. The command is automatically prefixed with `player <name>`. Requires familiarity with Carpet bot commands. |

### Waypoint Management

Waypoint tools are provided by either `location_plguin` (Location Marker) or `where2go_plugin` (Where2Go). Only one should be enabled at a time.

|      Tool      |         Parameters         | Description                                                                                                                                  |
| :------------: | :------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `add_pos_pos`  | `name`, `pos`, `dimension` | Add a waypoint at the specified coordinates. `pos` is `[x, y, z]`, `dimension` is the dimension (e.g. `overworld`, `the_nether`, `the_end`). |
| `add_pos_here` |           `name`           | Add a waypoint at the player's current location. Only works when called by a player (not console).                                           |
|  `remove_pos`  |           `name`           | Delete a waypoint by name. The Where2Go version supports fuzzy name matching.                                                                |
|  `search_pos`  |           `name`           | Search for a waypoint by name and return its details.                                                                                        |
| `get_all_pos`  |          _(none)_          | Get a list of all registered waypoints.                                                                                                      |

### Minecraft Wiki Search

|          Tool           | Parameters | Description                                                                                                                                                                                                                                                                |
| :---------------------: | :--------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_minecraft_wiki` |  `query`   | Search the Minecraft Wiki. Uses `minecraft.wiki` when the server language is English, otherwise `zh.minecraft.wiki`. Search pages return a list of result titles; exact matches return the (truncated) article content. Also registered for the Mineflayer Bot controller. |

### Whitelist Management

Whitelist tools are provided by the `whitelist_api` module and require the [WhitelistAPI](https://mcdreforged.com/plugin/whitelist_api) MCDR plugin.

|          Tool           | Parameters | Description                                                               |
| :---------------------: | :--------: | ------------------------------------------------------------------------- |
|  `get_whitelist_name`   |  _(none)_  | Get the list of all whitelisted players.                                  |
|   `add_to_whitelist`    |  `player`  | Add a player to the whitelist. Requires caller permission level ≥ 3.      |
| `remove_from_whitelist` |  `player`  | Remove a player from the whitelist. Requires caller permission level ≥ 3. |

### Skills

GamesAI Extra provides the following built-in skill, registered via `register_skills()`:

| Skill File  | Description                                                                                                                             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `carpet.md` | Guides the AI on how to properly spawn, control, and kill Carpet fake players (bots). Read this skill before any fake player operation. |

> [!TIP]
> Skills are like SOPs (Standard Operating Procedures) for the AI — they ensure the AI follows the correct workflow every time. The AI can read skill files using the `read_skills` tool.

## Dependencies

Each tool module requires its own server-side dependency to function:

| Module            | Required Dependency                                                           |
| ----------------- | ----------------------------------------------------------------------------- |
| `carpet`          | Server-side mod [fabric-carpet](https://github.com/gnembon/fabric-carpet)     |
| `location_plguin` | MCDR plugin [Location Marker](https://mcdreforged.com/plugin/location_marker) |
| `where2go_plugin` | MCDR plugin [Where2Go](https://mcdreforged.com/plugin/where2go)               |
| `whitelist_api`   | MCDR plugin [WhitelistAPI](https://mcdreforged.com/plugin/whitelist_api)      |
| `web_search`      | Python packages `requests` and `beautifulsoup4` (installed automatically)     |

If a required dependency is not installed, the corresponding tools will return an error message when called.

## What's New

### Version 0.2.0

- Added `web_search` module: `search_minecraft_wiki` tool for searching the Minecraft Wiki (English or Chinese wiki based on the server language), available to both the AI and the Mineflayer Bot controller
- Added `whitelist_api` module: `get_whitelist_name`, `add_to_whitelist` and `remove_from_whitelist` tools for whitelist management via the WhitelistAPI MCDR plugin (add/remove require permission level ≥ 3)
- All user-facing tool messages now use translation keys with built-in language files (`en_us`, `zh_cn`, `zh_tw`)
- Bumped GamesAI requirement to >= 0.6.4
- Added Python requirements `requests` and `beautifulsoup4` for the Wiki search tool

### Version 0.1.3

- Fixed some issues

### Version 0.1.2

- Added `@register_bot_tool()` decorator to `spawn_bot` and `kill_bot` for Mineflayer Bot support
- Registered `carpet.md` skill via `register_skills()` API
- Added `register_self()` support for automatic reload on `!!gamesai reload`
- Supports both extracted directory (dev) and packed `.mcdr` zip (distribution)

### Version 0.1.1

- Added waypoint management tools via `location_plguin` (Location Marker) and `where2go_plugin` (Where2Go) modules
- Added `@register_bot_tool()` decorator to `spawn_bot` and `kill_bot` for Mineflayer Bot support
- Each tool module can now be independently enabled/disabled via `config.json`
- Initial release with Carpet fake player control tools

## License

MIT License, Copyright (c) 2026 yello

<div align = "center">

---

[Back to Top](#gamesai-extra-for-mcdreforged)

</div>

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [GamesAIExtra-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI-Extra/releases/tag/0.2.0) | 0.2.0 | 2026/08/22 05:47:52 | 34.93KB | 7 | [Download](https://github.com/PengZixuan30/Games_AI-Extra/releases/download/0.2.0/GamesAIExtra-v0.2.0.mcdr) |
| [GamesAIExtra-v0.1.3.mcdr](https://github.com/PengZixuan30/Games_AI-Extra/releases/tag/0.1.3) | 0.1.3 | 2026/08/19 02:50:40 | 28.09KB | 7 | [Download](https://github.com/PengZixuan30/Games_AI-Extra/releases/download/0.1.3/GamesAIExtra-v0.1.3.mcdr) |
| [GamesAIExtra-v0.1.2.mcdr](https://github.com/PengZixuan30/Games_AI-Extra/releases/tag/0.1.2) | 0.1.2 | 2026/08/07 07:25:35 | 28.01KB | 18 | [Download](https://github.com/PengZixuan30/Games_AI-Extra/releases/download/0.1.2/GamesAIExtra-v0.1.2.mcdr) |

