**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## division

### Basic Information

- Plugin ID: `division`
- Plugin Name: Division
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 27
- Authors: [bzyyyyyyyy](https://github.com/bzyyyyyyyy)
- Repository: https://github.com/bzyyyyyyyy/MCDR-Division
- Repository plugin page: https://github.com/bzyyyyyyyy/MCDR-Division/tree/master
- Labels: [`Tool`](/labels/tool/readme.md), [`Information`](/labels/information/readme.md)
- Description: Grouping players and leaving messages

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [online_player_api](/plugins/online_player_api/readme.md) | * |
| [player_ip_logger](/plugins/player_ip_logger/readme.md) | * |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.1.0 |
| [requests](https://pypi.org/project/requests) | \>=2.30.0 |
| [pytz](https://pypi.org/project/pytz) | \>=2023.3 |
| [redis](https://pypi.org/project/redis) | \>=3.5.3 |
| [rejson](https://pypi.org/project/rejson) | \>=0.5.6 |

```
pip install "mcdreforged>=2.1.0" "requests>=2.30.0" "pytz>=2023.3" "redis>=3.5.3" "rejson>=0.5.6"
```

### Introduction

![MCDR-Division](https://socialify.git.ci/bzyyyyyyyy/MCDR-Division/image?description=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F63280128&name=1&owner=1&pattern=Floating+Cogs&theme=Light)

# MCDR-Division
---------

[中文](https://github.com/bzyyyyyyyy/MCDR-Division/tree/master/./README.md) | **English**

A plugin that supports dividing player into groups & leaving messages for groups / players

## Features

- **Player Grouping**: Supports creating multiple groups. Players can join multiple groups. Supports adding all players to one group in a time.
- **Leaving Messages**: Players can leave messages to any groups or players. Supports MC [color codes](https://minecraft.wiki/w/Formatting_codes). And automatically convert urls into clickable text.
- **Checking Messages**: The plugin will display all the messages leaved for the player and the groups the player is in, whenever the player joins the server.
- **Multiple storage modes**: The plugin supports using JSON or [Redis](https://redis.io/) to store informations of groups, players, and messages.
- **Sharing Info Between Multiple Servers**: By using [Redis](https://redis.io/), the plugin supports sharing informations of groups, players, and messages between multiple servers.
- **Permision Setting**: The operations of joining groups, leaving groups, deleting messages or deleting groups would be limited by MCDR permissions.
- **Custom Color**: Supports customizing colors of groups and players in the plugin. Can be colors other than 16 MC built-in colors.
- **Latest Online Time**: The plugin will sort players according to their latest online time, and display them according to this order.
- **Time Zone Detection**: The plugin will get the time zone of the player based on its ip, and display the time based on the time zone.
- **Smooth Interaction**: Most actions can be performed by clicking texts

## Requirements

Needs `v2.1.0` + [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)

Needs [OnlinePlayerAPI](https://mcdreforged.com/zh-CN/plugin/online_player_api), [Player IP Logger](https://mcdreforged.com/zh-CN/plugin/player_ip_logger)

Python package requirements: See [requirements.txt](https://github.com/bzyyyyyyyy/MCDR-Division/tree/master/requirements.txt)

## Command

`!!div` Display help message

`!!div search <keyword> [<page>]` Search for groups/players. It gives back all items that matches

`!!div list [<page>]` Display groups

`!!div ids [<page>]` Display players

`!!div info <group/player_id>` Display information of the group/player

`!!div make <group> [<perm>] [<color>]` Make a new group

`!!div join <group> [<player_id>]` Join the group/make the player join the group

`!!div leave <group> [<player_id>]` Leave the group/make the player leave the group

`!!div perm <group> <perm>` Change the permission level of the group

`!!div color <group> <color>` Change the color of the group

`!!div send <group/player_id> <msg>` Leave message for the group/player

`!!div edit <group/player_id> <lineNo.> <msg>` Change the message at `<lineNo.>` of the group/player

`!!div del <group/player_id> <lineNo.>` Delete the message at `<lineNo.>` of the group/player

`!!div del <group/player_id>` Delete the group

`!!div confirm` Use after deleting to confirm the execution

`!!div place <group> <pos>` Change the position of the group

`!!div check [time/group]` Check the messages people have left for you, can be in time order or group order

`!!div <keyword> [<page>]` Same to `!!div search`

## Config file explaination

Path: `config/division/config.json`

#### item_per_page

Default: `10`

After using `!!div list <page>` ,  `!!div list <page>` or `!!div search <keyword> <page>`

the limit of items showing on each page

#### default_perm

Default: `1`

After using `!!div make <group> [<perm>] [<color>]` with out giving `[<perm>]` , the default permission entered

#### default_color

Default: `"white"`

After using `!!div make <group> [<perm>] [<color>]` with out giving `[<color>]` , the default color entered

#### default_sender

Default: `"server"`

The default id for operations from non-players (such as the terminal)

Example:

1. When a non-player useing `!!div send <group/player_id> <msg>` , the plugin will store `server` as the sender

2. When a non-player useing `!!div join <group>` , the plugin will make `server` join the group

3. When a non-player useing `!!div check [time/group]` , the plugin will display messages left for `server`

#### default_check_mode

Default: `"time"`

After a player joins the server, or using `!!div check` , the default order of displaying messages

| Value   | Explanation                           |
| ------- | ------------------------------------- |
| `time`  | Display messages in time order first  |
| `group` | Display messages in group order first |


#### perm_to_modify_all

Default: `1`

The permission of using `!!div join <group> All` or `!!div leave <group> All`

#### msg_for_new_player

Default: `""`

The message leaved for new players by the plugin

#### redis_ip

Default: `""`

Ip of the Redis server

If it's not `""` , then use Redis to store informations of groups, players, and messages (Example: `"127.0.0.1"` )

If it's `""` then use JSON to store informations of groups, players, and messages

#### redis_port

Default: `6379`

Port of the Redis server

#### redis_db

Default: `1`

Index of the database of the Redis server

#### redis_password

Default: `""`

Password of the Redis server

## Color Format

Here are the values you can enter for the parameter `<color>` :

- [MC color](https://minecraft.wiki/w/Formatting_codes) (Example: `white` ,  `black`)
- RGB code (Example: `00AAFF` ,  `0x00AAFF` ,  `#00AAFF`)

## Escape Character

Cause players cannot type the symbol `§` in MC which made them cannot use the color code

This plugin offers `$` as an escape character

When a player uses `$` when leaving a message, the plugin automatically converts it to the symbol `§`

When the player needs to enter the symbol `$`, enter `$$`

## URL Convert

The plugin will recognize anything that starts with `http` and ends with a space as a URL

And convert it to clickable text

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [Division-v1.0.0.mcdr](https://github.com/bzyyyyyyyy/MCDR-Division/releases/tag/v1.0.0) | 1.0.0 | 2024/12/22 06:12:49 | 59.96KB | 27 | [Download](https://github.com/bzyyyyyyyy/MCDR-Division/releases/download/v1.0.0/Division-v1.0.0.mcdr) |

