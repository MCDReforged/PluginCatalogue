**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## cushion_of_backup

### Basic Information

- Plugin ID: `cushion_of_backup`
- Plugin Name: Cushion of Backup
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 31
- Authors: [HeTao_yz](https://github.com/HeTao-yz)
- Repository: https://github.com/HeTao-yz/Cushion-of-Backup
- Repository plugin page: https://github.com/HeTao-yz/Cushion-of-Backup/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: 优化服务器回档/重启时的玩家处理逻辑，让玩家游戏体验连贯顺畅

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged ](https://pypi.org/project/mcdreforged ) | \>= 2.0.0 |
| [rcon](https://pypi.org/project/rcon) |  |

```
pip install "mcdreforged >= 2.0.0" rcon
```

### Introduction

# Cushion of Backup - Rollback Cushion

Optimizes the player handling logic during server rollbacks/restarts to provide players with a seamless and smooth gaming experience.

## Foreword

> Note: This plugin does not provide a new method for rollbacks. It is an improvement plugin for the rollback experience, built upon the existing rollback method that requires a server restart.

In multiplayer servers, rollbacks/restarts are inevitable. However, every rollback requires a server restart, forcing players to disconnect and return to the server list. Not only is the experience abruptly interrupted, but players also have to manually reconnect repeatedly, without knowing how long they must wait to rejoin...

The author wanted to change this commonly poor experience. Therefore, some improvements were attempted. We hope this plugin can bring an enhanced rollback experience to you or the server you are on.

## How It Optimizes

Demo Video: [Perhaps the Best Rollback Experience in Survival Technical Servers](https://www.bilibili.com/video/BV1kD6ABjEwc)

Under Velocity, when the survival server (main server) restarts, players will be transferred to the lobby server (can be any sub-server; 'lobby' is just a name, without special meaning; functionally, it serves as a temporary transfer server for players).

When the survival server successfully rolls back and is preparing to start, as well as after it starts successfully, prompt messages will be sent to the lobby server. Subsequently, players will automatically be returned to the survival server. This achieves a seamless and smooth gaming experience for players during the survival server's restart.

## Installation

### Prerequisites

- Requires a configured Velocity proxy, and the [Velocircon](https://modrinth.com/plugin/velocircon) plugin must be installed to enable and configure RCON control.

- Both the survival server and the lobby server are sub-servers of Velocity, and the lobby server must have RCON control enabled and configured.

- In the Velocity configuration file's `try` block, the survival server and lobby server need to be added.

### Note

**This plugin needs to be installed on the survival server (main server).**

## Configuration File

The plugin will automatically generate the configuration file `config/cushion_of_backup.json` upon first load.

```json
{
    "velocity_host": "127.0.0.1",
    "velocity_port": 25581,
    "velocity_passwd": "password123",
    "lobby_host": "127.0.0.1",
    "lobby_port": 25576,
    "lobby_passwd": "password123",
    "lobby_server": "lobby",
    "survival_server": "survival",
    "survival_server_start": "The survival server is starting up...",
    "survival_server_startup": "Startup complete! Returning players to the survival server...",
    "survival_server_failure": "The survival server crashed! Please report to an administrator. The survival server will continue attempting to start."
}
```

### Configuration Item Descriptions

| Configuration Item        | Type   | Default Value                                                                                                            | Description                                                                 |
| ------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| `velocity_host`           | string | `127.0.0.1`                                                                                                              | Velocity server address                                                     |
| `velocity_port`           | int    | `25575`                                                                                                                  | Velocity RCON port                                                          |
| `velocity_passwd`         | string | `password`                                                                                                               | Velocity RCON password                                                      |
| `lobby_host`              | string | `127.0.0.1`                                                                                                              | Lobby server address                                                        |
| `lobby_port`              | int    | `25575`                                                                                                                  | Lobby server RCON port                                                      |
| `lobby_passwd`            | string | `password`                                                                                                               | Lobby server RCON password                                                  |
| `lobby_server`            | string | `lobby`                                                                                                                  | Lobby server name in Velocity                                               |
| `survival_server`         | string | `survival`                                                                                                               | Survival server name in Velocity                                            |
| `survival_server_start`   | string | `The survival server is starting up...`                                                                                  | Message sent to the lobby server when the survival server begins starting   |
| `survival_server_startup` | string | `Startup complete! Returning players to the survival server...`                                                          | Message sent to the lobby server when the survival server finishes starting |
| `survival_server_failure` | string | `The survival server crashed! Please report to an administrator. The survival server will continue attempting to start.` | Message sent to the lobby server when the survival server crashes           |

## Other

This is the initial plugin development, and there may be unfamiliarities or imperfections. If you encounter bugs or have other suggestions while using it, welcome to submit an Issue at the plugin's source repository on GitHub.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [Cushion-of-Backup_v1.0.0.mcdr](https://github.com/HeTao-yz/Cushion-of-Backup/releases/tag/v1.0.0) | 1.0.0 | 2026/01/31 05:26:23 | 15.19KB | 31 | [Download](https://github.com/HeTao-yz/Cushion-of-Backup/releases/download/v1.0.0/Cushion-of-Backup_v1.0.0.mcdr) |

