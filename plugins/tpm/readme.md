**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## tpm

### Basic Information

- Plugin ID: `tpm`
- Plugin Name: TpManager
- Version: 0.5.0
  - Metadata version: 0.5.0
  - Release version: 0.5.0
- Total downloads: 1439
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/tpmanager_mcdr
- Repository plugin page: https://github.com/kmcsr/tpmanager_mcdr/tree/master
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: A Minecraft teleport manager

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.3.0 |
| [kpi](/plugins/kpi/readme.md) | ~1.4.6 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction


- English
- [中文](https://github.com/kmcsr/tpmanager_mcdr/tree/master/README_zh.MD)

# Tp Manager

*If it's useful, please give a star :)*

## Feature

- Teleport between players
- In game warp points

## TODO

- Linking with login_proxy?

## Dependencies

| ID                                       | Release Link                                 |
| ---------------------------------------- | -------------------------------------------- |
| [kpi](https://github.com/kmcsr/kpi_mcdr) | <https://github.com/kmcsr/kpi_mcdr/releases> |

## Commands

> [!TIP]
> Some other plugins also registered `!!tp` as root command. To avoid conflict, you also can use `!!tpm` to replace `!!tp`

| Command format         | Introduction                                  |
| ---------------------- | --------------------------------------------- |
| `!!tp help`            | Show help message, aka `!!tp`                 |
| `!!tp pos <x> <y> <z>` | Teleport to `<x>`, `<y>`, `<z>`               |
| `!!tp ask <name>`      | Send an teleport request, aka `!!tpa`         |
| `!!tp askhere <name>`  | Send an teleport request to here, aka `!!tph` |
| `!!tp accept`          | Accept the teleport request                   |
| `!!tp reject`          | Reject the teleport request                   |
| `!!tp cancel`          | Cancel your teleport request                  |

## Config files

#### tpm/config.json

```javascript
{
    "minimum_permission_level": { // Command permissions
        "pos": 2,
        "ask": 1,
        "askhere": 1,
        "accept": 1,
        "reject": 0,
        "cancel": 0
    },
    "teleport_cooldown": 60, // in sec, the minimum teleport operation interval
    "teleport_expiration": 10, // in sec, the teleport request expiration
    "teleport_commands": [ // Command list for teleport players
        "say Teleporting {src} to {dst} ...",
        "tp {src} {dst}",
    ],
    "teleport_xyz_command": "tp {name} {x} {y} {z}" // Command for teleport position
}
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [TpManager-v0.5.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.5.0) | 0.5.0 | 2024/09/07 16:34:52 | 18.75KB | 199 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.5.0/TpManager-v0.5.0.mcdr) |
| [TpManager-v0.4.6.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.6) | 0.4.6 | 2024/03/09 21:53:20 | 17.01KB | 326 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.6/TpManager-v0.4.6.mcdr) |
| [TpManager-v0.4.5.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.5) | 0.4.5 | 2024/02/27 04:59:38 | 17.0KB | 36 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.5/TpManager-v0.4.5.mcdr) |
| [TpManager-v0.4.4.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.4) | 0.4.4 | 2024/02/05 00:16:45 | 17.02KB | 41 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.4/TpManager-v0.4.4.mcdr) |
| [TpManager-v0.4.3.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.3) | 0.4.3 | 2024/02/03 02:35:34 | 17.01KB | 50 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.3/TpManager-v0.4.3.mcdr) |
| [TpManager-v0.4.2.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.2) | 0.4.2 | 2024/02/03 02:33:06 | 17.01KB | 47 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.2/TpManager-v0.4.2.mcdr) |
| [TpManager-v0.4.1.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.1) | 0.4.1 | 2024/02/03 00:52:34 | 17.0KB | 48 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.1/TpManager-v0.4.1.mcdr) |
| [TpManager-v0.4.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.0) | 0.4.0 | 2024/02/03 00:35:46 | 17.0KB | 54 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.0/TpManager-v0.4.0.mcdr) |
| [TpManager-v0.3.4.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.4) | 0.3.4 | 2023/05/21 16:56:38 | 16.74KB | 299 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.4/TpManager-v0.3.4.mcdr) |
| [TpManager-v0.3.3.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.3) | 0.3.3 | 2023/02/26 17:42:05 | 16.63KB | 91 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.3/TpManager-v0.3.3.mcdr) |
| [TpManager-v0.3.2.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.2) | 0.3.2 | 2023/02/26 16:53:28 | 16.64KB | 28 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.2/TpManager-v0.3.2.mcdr) |
| [TpManager-v0.3.1.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.1) | 0.3.1 | 2023/02/26 16:52:51 | 16.65KB | 23 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.1/TpManager-v0.3.1.mcdr) |
| [TpManager-v0.3.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.0) | 0.3.0 | 2023/02/26 05:48:16 | 16.69KB | 26 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.0/TpManager-v0.3.0.mcdr) |
| [TpManager-v0.2.1.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.2.1) | 0.2.1 | 2022/11/28 02:31:44 | 16.41KB | 109 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.2.1/TpManager-v0.2.1.mcdr) |
| [TpManager-v0.2.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.2.0) | 0.2.0 | 2022/11/27 22:43:52 | 16.41KB | 29 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.2.0/TpManager-v0.2.0.mcdr) |
| [TpManager-v0.1.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.1.0) | 0.1.0 | 2022/11/27 19:00:42 | 16.18KB | 33 | [Download](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.1.0/TpManager-v0.1.0.mcdr) |
