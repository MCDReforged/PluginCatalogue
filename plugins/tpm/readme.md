**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## tpm

### Basic Information

- Plugin ID: `tpm`
- Version: *Data fetching failed*
- Total downloads: N/A
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/tpmanager_mcdr
- Repository plugin page: https://github.com/kmcsr/tpmanager_mcdr/tree/master
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

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

*Data fetching failed*

