**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## simple_tp

### Basic Information

- Plugin ID: `simple_tp`
- Plugin Name: Simple TP
- Version: 1.3.3
  - Metadata version: 1.3.3
  - Release version: 1.3.3
- Total downloads: 545
- Authors: [PairZhu](https://github.com/PairZhu)
- Repository: https://github.com/PairZhu/SimpleTP-MCDR
- Repository plugin page: https://github.com/PairZhu/SimpleTP-MCDR/tree/master
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: A simple teleportation plugin designed to create waypoints and implement the teleportation features of EssentialsX.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | * |
| [mg_events](/plugins/mg_events/readme.md) | \>=1.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.7 |
| [readerwriterlock](https://pypi.org/project/readerwriterlock) | ==1.0.9 |

```
pip install "mcdreforged>=2.14.7" readerwriterlock==1.0.9
```

### Introduction

# SimpleTP
**English** | [简体中文](https://github.com/PairZhu/SimpleTP-MCDR/tree/master/README.zh.md)

A simple teleportation plugin designed to create waypoints and implement the teleportation features of EssentialsX.

## Preview
![help](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README/1757133291389.png)
![list](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README/1757133317304.png)
![back](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README/1757133375310.png)

## Features
- Support for personal waypoints that players can create and manage, visible only to themselves
- Support for global waypoints (public waypoints) visible to all players, suitable for public areas
- Configurable enabled dimensions with support for modded dimensions (like Twilight Forest, Eternal Starlight, etc.)
- Support for returning to death location and previous location before teleporting
- Most commands support clickable operations for convenience
- Easytp syntax sugar: `stp xxx` is equivalent to `stp tpp/tpg/tp/tpa xxx`, automatically recognizing waypoints and players, with priority `Personal Waypoint > Global Waypoint > Player`
- Support for comprehensive command argument completion, allowing the use of the Tab key to complete waypoint names and player names (requires the [command_suggest](https://mcdreforged.com/en/plugin/command_suggest) plugin)

## Commands
The following examples use the default prefix "!!stp". Adjust according to your configuration file.
- !!stp help View help information

Preview commands can be found in the [language file](https://github.com/PairZhu/SimpleTP-MCDR/tree/master/./lang/en_us.yml) under the help section.

## Configuration File
The configuration file is located at `config/SimpleTP/config.json`
- **prefix**: Command prefix, default is `!!stp`
- **back_on_death**: Whether to automatically record the position upon player death, default is `true`
- **save_interval**: Interval for scheduled saving of waypoint data, in seconds, default is `30` seconds
- **permissions**: Permission configuration
- **worlds**: List of supported dimensions (including mod dimensions), default is `["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]`. Teleportation will not work in dimensions not in this list. To disable teleportation in a dimension, simply remove it from the list.
- **extra_dimensions**: ***Only required for Minecraft versions before 1.16***, configuration format is `{<dimension_id>: "<dimension_name>"}`, for example `{0: "minecraft:overworld", 1: "minecraft:the_nether", 2: "minecraft:the_end"}`. This configuration is used to support mod dimensions in older Minecraft versions.
- **easy_tp**: Whether to enable easytp syntax sugar, default is `true`.

### Permission Configuration
- **back**: Permission to use `!!stp back` command
- **tpa**: Permission to use `!!stp tpa` command
- **tpahere**: Permission to use `!!stp tpahere` command
- **tp**: Permission to use `!!stp tp <player>` command
- **tphere**: Permission to use `!!stp tphere <player>` command
- **personal_waypoint**: Permission to set/delete personal waypoint related commands
- **global_waypoint**: Permission to set/delete global waypoint related commands
- **cross_world_tp**: Permission for cross-dimension teleportation

## Dependencies
- **minecraft_data_api**: Used for retrieving player information
- **mg_events**: Used for listening to player death events

## Common Issues
- **Clickable Teleport Button Not Responding**
  MCDR has issues with click execution support in higher MC versions. Install [LetMeClickAndSendForServer](https://github.com/Fallen-Breath/LetMeClickAndSendForServer) (server-side) or [LetMeClickAndSend](https://github.com/Fallen-Breath/LetMeClickAndSend) (client-side).
- **Sometimes `back` Command Doesn't Return to Previous Location After Death**
  Some mod death messages are special and may not be detected by mg_events. You need to manually add corresponding death messages in mg_events language files. For example, for the [Eternal Starlight](https://www.curseforge.com/minecraft/mc-mods/eternal-starlight) mod, when players die in the Ether, add `"death.attack.ether": "%1$s drifts away"` to `config/mg_events/lang/en_us.json`, and `"death.attack.ether": "%1$s飘然而去"` to `config/mg_events/lang/zh_cn.json`.
- **Log Shows "Player {player} is in a dimension not enabled in config: {dimension}"**
  This indicates the player is in a dimension not enabled in the configuration. Check the `worlds` configuration in `config/SimpleTP/config.json` to ensure the dimension is included.
- **Log Shows "Player {player} is in an unknown dimension with ID {dimension}"**
  This error may occur when the server Minecraft version is before 1.16 and mod dimensions are installed. Check the `extra_dimensions` configuration in `config/SimpleTP/config.json` to ensure the dimension is included. You can get the dimension ID using the `/data get entity <player> Dimension` command.

## TODO
If you have more feature requests or are interested in any planned features, feel free to raise them in the issues section 🚀
Sorted by priority:
- [x] Support clickable waypoints
- [x] `back` command supports round-trip teleportation
- [x] Record player's dimension in waypoints (Nether, Overworld, End)
- [x] Configuration for cross-dimension teleportation
- [x] Scheduled saving of waypoint data (to prevent loss on crash)
- [x] `tp`/`tphere` functionality
- [x] `tpa`/`tpahere` functionality
- [x] Multi-language support
- [x] Help information
- [ ] Record player's orientation in waypoints
- [ ] Add description information for waypoints
- [ ] Teleport cooldown configuration
- [ ] Maximum number of waypoints configuration
- [ ] Waypoint name length limit configuration
- [ ] Waypoint safety check, prompting confirmation or teleporting to nearby safe location if the waypoint is in a dangerous position
- [ ] Teleport cost configuration (consume custom items or experience) (base cost + distance cost)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [SimpleTP-v1.3.3.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.3) | 1.3.3 | 2025/09/10 05:48:09 | 15.97KB | 265 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.3/SimpleTP-v1.3.3.mcdr) |
| [SimpleTP-v1.3.2.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.2) | 1.3.2 | 2025/09/06 10:11:37 | 15.92KB | 32 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.2/SimpleTP-v1.3.2.mcdr) |
| [SimpleTP-v1.3.1.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.1) | 1.3.1 | 2025/09/04 09:31:42 | 15.87KB | 19 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.1/SimpleTP-v1.3.1.mcdr) |
| [SimpleTP-v1.3.0.mcdr](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.3.0) | 1.3.0 | 2025/09/03 04:22:54 | 15.81KB | 20 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.3.0/SimpleTP-v1.3.0.mcdr) |
| [SimpleTP-v1.2.1.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.2.1) | 1.2.1 | 2025/08/26 08:49:38 | 9.59KB | 39 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.2.1/SimpleTP-v1.2.1.pyz) |
| [SimpleTP-v1.2.0.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.2.0) | 1.2.0 | 2025/08/09 10:07:57 | 9.41KB | 48 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.2.0/SimpleTP-v1.2.0.pyz) |
| [SimpleTP-v1.1.4.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.4) | 1.1.4 | 2025/08/03 05:03:13 | 6.69KB | 36 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.4/SimpleTP-v1.1.4.pyz) |
| [SimpleTP-v1.1.3.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.3) | 1.1.3 | 2025/08/02 18:35:33 | 6.53KB | 22 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.3/SimpleTP-v1.1.3.pyz) |
| [SimpleTP-v1.1.2.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.2) | 1.1.2 | 2025/08/02 18:27:15 | 6.47KB | 18 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.2/SimpleTP-v1.1.2.pyz) |
| [SimpleTP-v1.1.1.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.1) | 1.1.1 | 2025/08/02 14:28:38 | 6.15KB | 19 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.1/SimpleTP-v1.1.1.pyz) |
| [SimpleTP-v1.0.0.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.0.0) | 1.0.0 | 2025/08/01 03:41:47 | 4.16KB | 27 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.0.0/SimpleTP-v1.0.0.pyz) |

