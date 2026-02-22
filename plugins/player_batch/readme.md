**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## player_batch

### Basic Information

- Plugin ID: `player_batch`
- Plugin Name: PlayerBatch
- Version: 1.0.6
  - Metadata version: 1.0.7
  - Release version: 1.0.6
- Total downloads: 349
- Authors: [Eason120806](https://github.com/Eason120806)
- Repository: https://github.com/Eason120806/player_batch-MCDR
- Repository plugin page: https://github.com/Eason120806/player_batch-MCDR/tree/main
- Labels: [`Tool`](/labels/tool/readme.md), [`Management`](/labels/management/readme.md)
- Description: MCDR Batch Bot Management Plugin

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# PlayerBatch - MCDR Fake Player Batch Operation Plugin

🎮 A MCDReforged-based plugin providing powerful Carpet fake player batch operation capabilities

![License](https://img.shields.io/badge/License-GPLv3-blue)
![MCDR](https://img.shields.io/badge/MCDR-2.1.0%2B-blue)

## 📦 Features

- **Batch Basic Operations**: Control multiple fake players to execute commands simultaneously
- **Smart Arrangement Generation**: Support linear/square formation generation
- **Initialization Sequence**: Customized generation + action execution + automatic cleanup process
- **Multi-dimensional Configuration**: Customizable naming rules and operation intervals
- **Permission Management**: Control command permissions through config file

## 🛠️ Installation

1. Ensure [MCDReforged] is installed
2. Download latest `PlayerBatch.pyz`
3. Place into MCDR's plugins directory
4. Restart MCDR server

## ⚙️ Configuration

Path: `config/player_batch.json`

```json
{
    "base_name": "bot_",
    "permission": 0,
    "interval": 1.0
}
```
## 🎯 Commands

### Basic Commands
```text
!!plb <name> <start> <end> <action>
!!playerbatch <name> <start> <end> <action>
```

### Linear Generation
```text
!!plb l <name> <start> <length> <direction> <interval>
!!playerbatch l <name> <start> <length> <direction> <interval>
```

### Square Formation Generation
```text
!!plb s <name> <start> <length> <width> <direction1> <direction2> <interval>
!!playerbatch s <name> <start> <length> <width> <direction1> <direction2> <interval>
```

### Initialization Sequence
```text
!!plb init <name> <start> <length> <interval1> <interval2> <x> <y> <z> <action>
!!playerbatch init <name> <start> <length> <interval1> <interval2> <x> <y> <z> <action>
```

### Stop command
```text
!!plb stop
!!playerbatch stop
```


## ⚠️ Notes

1. Requires Carpet Mod with fake player functionality
2. Interval settings affect server performance - configure reasonably
3. Fake player name format: Prefix + Custom name + Sequence number

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.6) | 1.0.6 | 2025/05/02 11:59:23 | 10.74KB | 174 | [Download](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.6/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.5) | 1.0.5 | 2025/05/02 09:59:45 | 10.68KB | 28 | [Download](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.5/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.4) | 1.0.4 | 2025/05/02 07:56:25 | 10.23KB | 26 | [Download](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.4/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.3) | 1.0.3 | 2025/04/30 17:24:58 | 10.2KB | 29 | [Download](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.3/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.2) | 1.0.2 | 2025/04/28 17:18:04 | 9.86KB | 31 | [Download](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.2/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.1) | 1.0.1 | 2025/04/25 10:51:49 | 3.23KB | 33 | [Download](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.1/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.0) | 1.0.0 | 2025/04/20 15:48:35 | 2.19KB | 28 | [Download](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.0/player_batch.pyz) |

