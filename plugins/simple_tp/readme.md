**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## simple_tp

### Basic Information

- Plugin ID: `simple_tp`
- Plugin Name: Simple TP
- Version: 1.1.1
  - Metadata version: 1.1.1
  - Release version: 1.1.1
- Total downloads: 8
- Authors: [PairZhu](https://github.com/PairZhu)
- Repository: https://github.com/PairZhu/SimpleTP-MCDR
- Repository plugin page: https://github.com/PairZhu/SimpleTP-MCDR/tree/master
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: A simple teleport plugin aiming to match and extend EssentialsX teleport features.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | * |
| [mg_events](/plugins/mg_events/readme.md) | \>=1.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | ==2.14.7 |
| [readerwriterlock](https://pypi.org/project/readerwriterlock) | ==1.0.9 |

```
pip install mcdreforged==2.14.7 readerwriterlock==1.0.9
```

### Introduction

# SimpleTP
**English** | [简体中文](https://github.com/PairZhu/SimpleTP-MCDR/tree/master/README.zh.md)

A simple teleport plugin aiming to match and extend EssentialsX teleport features.

## Preview
![Teleport Button](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README/1754023706691.png)
![Delete Button](https://raw.githubusercontent.com/PairZhu/SimpleTP-MCDR/master/image/README/1754125441339.png)

## Features and Commands
The following examples use the default prefix "!!stp". Adjust according to your configuration file.

### Personal Waypoints
Players can create and manage their own waypoints, which are only visible to themselves.
- **Create Personal Waypoint**: `!!stp setp <name>`
- **Teleport to Personal Waypoint**: `!!stp tpp <name>`
- **Delete Personal Waypoint**: `!!stp delp <name>`
- **List All Personal Waypoints** (clickable for teleport): `!!stp listp`

### Global Waypoints (Public Waypoints)
Global waypoints are visible to all players and suitable for public areas.
- **Create Global Waypoint**: `!!stp setg <name>`
- **Teleport to Global Waypoint**: `!!stp tpg <name>`
- **Delete Global Waypoint**: `!!stp delg <name>`
- **List All Global Waypoints** (clickable for teleport): `!!stp listg`

### Other Commands
- **List All Waypoints** (personal and global): `!!stp list`
- **Return to Last Location**: `!!stp back` (available after teleporting or upon death)

## Configuration File
The configuration file is located at `config/SimpleTP/config.json`
- **prefix**: Command prefix, default is `!!stp`
- **back_on_death**: Whether to automatically record the position upon player death, default is `true`
- **save_interval**: Interval for scheduled saving of waypoint data, in seconds, default is `30` seconds
- **permissions**: Permission configuration
- **worlds**: List of supported dimensions (including mod dimensions), default is `["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]`. Teleportation will not work in dimensions not in this list. To disable teleportation in a dimension, simply remove it from the list.

### Permission Configuration
- **back**: Permission to use `!!stp back` command
- **tpa**: Permission to use `!!stp tpa` command
- **tpahere**: Permission to use `!!stp tpahere` command
- **tp**: Permission to use `!!stp tp <player>` command
- **tphere**: Permission to use `!!stp tphere <player>` command
- **tp_xyz**: Permission to use `!!stp tp <x> <y> <z>` command
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

## TODO
Sorted by priority:
- [x] Support clickable waypoints
- [x] `back` command supports round-trip teleportation
- [x] Record player's dimension in waypoints (Nether, Overworld, End)
- [x] Configuration for cross-dimension teleportation
- [x] Scheduled saving of waypoint data (to prevent loss on crash)
- [ ] `tp`/`tphere` functionality
- [ ] `tpa`/`tpahere` functionality
- [ ] Add help information
- [ ] Record player's orientation in waypoints
- [ ] Add description information for waypoints
- [ ] Teleport cooldown configuration
- [ ] Maximum number of waypoints configuration
- [ ] Waypoint name length limit configuration
- [ ] Waypoint safety check, prompting confirmation or teleporting to nearby safe location if the waypoint is in a dangerous position
- [ ] Teleport cost configuration (consume custom items or experience) (base cost + distance cost)
- [ ] Multi-language support
- [ ] More feature requests can be submitted in issues🚀

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [SimpleTP-v1.1.1.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.1.1) | 1.1.1 | 2025/08/02 14:28:38 | 6.15KB | 1 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.1.1/SimpleTP-v1.1.1.pyz) |
| [SimpleTP-v1.0.0.pyz](https://github.com/PairZhu/SimpleTP-MCDR/releases/tag/v1.0.0) | 1.0.0 | 2025/08/01 03:41:47 | 4.16KB | 7 | [Download](https://github.com/PairZhu/SimpleTP-MCDR/releases/download/v1.0.0/SimpleTP-v1.0.0.pyz) |

