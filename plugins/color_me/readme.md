**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## color_me

### Basic Information

- Plugin ID: `color_me`
- Plugin Name: ColorMe
- Version: 1.1.0
  - Metadata version: 1.1.0
  - Release version: 1.1.0
- Total downloads: 114
- Authors: [Apricityx_](https://github.com/Apricityx)
- Repository: https://github.com/Apricityx/ColorMe
- Repository plugin page: https://github.com/Apricityx/ColorMe/tree/master
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Players can change their name color by themselves!

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | ~=2.15.7 |

```
pip install mcdreforged~=2.15.7
```

### Introduction

[[中文]](https://github.com/Apricityx/ColorMe/tree/master/introduction/./introduction-zh_cn.md) | [English]

### ColorMe

A simple plugin that lets players choose their own name color:

```
!!color <color>
```

It works by making players join one of 16 vanilla scoreboard teams, one per chat color.
Both Minecraft 1.12.x and 1.13+ are supported.

After enabling the plugin, initialize the teams once:

```
!!color install
```

When you no longer need the plugin, remove the teams:

```
!!color uninstall
```

Other commands: `!!color list` lists the colors. `install` and `uninstall` require
MCDReforged permission level 2 (helper) or higher.

Note: a player can only be in one team, so this plugin may conflict with other systems
that use vanilla teams for prefix/suffix/permissions.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ColorMe-v1.1.0.mcdr](https://github.com/Apricityx/ColorMe/releases/tag/v1.1.0) | 1.1.0 | 2026/09/13 04:53:35 | 15.42KB | 8 | [Download](https://github.com/Apricityx/ColorMe/releases/download/v1.1.0/ColorMe-v1.1.0.mcdr) |
| [ColorMe-v1.1.0.mcdr](https://github.com/Apricityx/ColorMe/releases/tag/1.1.0) | 1.1.0 | 2026/09/13 04:54:52 | 15.42KB | 13 | [Download](https://github.com/Apricityx/ColorMe/releases/download/1.1.0/ColorMe-v1.1.0.mcdr) |
| [ColorMe-v1.0.2.mcdr](https://github.com/Apricityx/ColorMe/releases/tag/1.0.2) | 1.0.2 | 2025/10/28 15:14:00 | 17.83KB | 93 | [Download](https://github.com/Apricityx/ColorMe/releases/download/1.0.2/ColorMe-v1.0.2.mcdr) |

