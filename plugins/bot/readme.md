**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## bot

### Basic Information

- Plugin ID: `bot`
- Version: *Data fetching failed*
- Total downloads: N/A
- Authors: [Andy Zhang](https://github.com/AnzhiZhang)
- Repository: https://github.com/AnzhiZhang/MCDReforgedPlugins
- Repository plugin page: https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/bot
- Labels: [`Tool`](/labels/tool/readme.md), [`Management`](/labels/management/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

### Introduction

# Bot

[简体中文](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/bot/readme_cn.md)

> The best carpet bot manager!

## Dependencies

- [MinecraftDataAPI](https://github.com/MCDReforged/MinecraftDataAPI)
- [MoreCommandNodes](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/bot/../more_command_nodes)

## Usage

`!!bot` View help

`!!bot list [--index <index>] [filters]` Show bot list

`!!bot spawn <name>` Spawn bot

`!!bot kill <name>` Kill bot

`!!bot action <name> [index]` Execute bot action(s)

`!!bot tags` View available tags

`!!bot tags <tag> spawn/kill` Spawn/kill bot(s) with tag

`!!bot info <name>` View bot info

`!!bot save <name> [position] [facing] [dimension]` Save bot

`!!bot del <name>` Delete saved bot

`!!bot config <name> <option> <value>` Config bot

### Workflow

```mermaid
sequenceDiagram
    participant Player/Console
    participant Online Bots
    participant Saved Bots

    Player/Console-->>Online Bots: !!bot spawn (player)
    Saved Bots-->>Online Bots: !!bot spawn
    Online Bots-->>Online Bots: !!bot kill
    Online Bots-->>Saved Bots: !!bot save
    Player/Console-->>Saved Bots: !!bot save [location]
    Saved Bots-->>Saved Bots: !!bot del
```

### list

**--index \<index\>**: Page number, e.g. `--index 1`, default is 0

**--online**: Show online bots

**--saved**: Show saved bots

**--tag \<tag\>**: Filter by tag

### spawn

Spawn bot

```mermaid
flowchart TD
    start([spawn])
    is_saved{Saved?}
    is_player{Running by Player?}

    start --> is_saved
    is_saved -->|Yes| spawn1(Spawn at Saved Location)
    is_saved -->|No| is_player
    is_player -->|Yes| spawn2(Spawn at player's Location)
    is_player -->|No| error1([Not Saved Error])
```

### kill

Kill bot

### action

Execute bot action(s)

When `index` is specified, execute specific action(s) instead of all actions

### tags

View available tags and spawn/kill bot(s) with tag

`!!bot tags` View available tags

`!!bot tags <tag> spawn` Spawn bot(s) with tag

`!!bot tags <tag> kill` Kill bot(s) with tag

### info

View bot info

### save

Save bot

```mermaid
flowchart TD
    start([save])
    with_location{Has Location?}
    online{Online or Saved?}
    is_player{Running by Player?}

    start --> with_location
    with_location -->|Yes| save3(Save at Input Location)
    with_location -->|No| online

    online -->|Yes| save1(Save at Bot's Location)
    online -->|No| is_player
    is_player -->|Yes| save2(Save at player's location)
    is_player -->|No| error1([Bot Not Exists])
```

### del

Delete saved bot

After deletion, the bot will be backed up to the `botBin.json` file in the data directory. If you delete it by mistake, you can use it for manual recovery.

### config

Config bot

### Full Command Tree

```mermaid
flowchart LR
    start(!!bot)

    start --> list(list)
    list --> list_index["--index &lt;index&gt;"]
    list --> list_online[--online]
    list --> list_saved[--saved]
    list --> list_tag["--tag &lt;tag&gt;"]

    start --> spawn(spawn)
    spawn --> spawn_name("&lt;name&gt;")

    start --> kill(kill)
    kill --> kill_name("&lt;name&gt;")

    start --> action(action)
    action --> action_name("&lt;name&gt;")
    action_name --> action_name_index["&lt;index&gt;"]

    start --> tags(tags)
    tags --> tags_tag["&lt;tag&gt;"]
    tags_tag --> tags_tag_spawn(spawn)
    tags_tag --> tags_tag_kill(kill)

    start --> info(info)
    info --> info_name("&lt;name&gt;")

    start --> save(save)
    save --> save_name("&lt;name&gt;")
    save_name --> save_name_position["&lt;position&gt;"]
    save_name_position --> save_name_position_facing["&lt;facing&gt;"]
    save_name_position_facing --> save_name_position_facing_dimension["&lt;dimension&gt;"]

    start --> del(del)
    del --> del_name("&lt;name&gt;")

    start --> config(config)
    config --> config_name("&lt;name&gt;")
    config_name --> config_name_name("name &lt;newName&gt;")
    config_name --> config_name_position("position &lt;position&gt;")
    config_name --> config_name_facing("facing &lt;facing&gt;")
    config_name --> config_name_dimension("dimension &lt;dimension&gt;")
    config_name --> config_name_comment("comment &lt;comment&gt;")
    config_name --> config_name_actions(actions)
    config_name --> config_name_tags(tags)
    config_name --> config_name_autoLogin("autoLogin &lt;autoLogin&gt;")
    config_name --> config_name_autoRunActions("autoRunActions &lt;autoRunActions&gt;")
    config_name --> config_name_autoUpdate("autoUpdate &lt;autoUpdate&gt;")

    config_name_actions --> config_name_actions_append("append &lt;action&gt;")
    config_name_actions --> config_name_actions_insert("insert &lt;index&gt; &lt;action&gt;")
    config_name_actions --> config_name_actions_delete("delete &lt;index&gt")
    config_name_actions --> config_name_actions_edit("edit &lt;index&gt; &lt;action&gt;")
    config_name_actions --> config_name_actions_clear(clear)

    config_name_tags --> config_name_tags_append["append &lt;tag&gt;"]
    config_name_tags --> config_name_tags_insert["insert &lt;index&gt; &lt;tag&gt;"]
    config_name_tags --> config_name_tags_delete["delete &lt;index&gt"]
    config_name_tags --> config_name_tags_edit["edit &lt;index&gt; &lt;tag&gt;"]
    config_name_tags --> config_name_tags_clear[clear]
```

## Config

### gamemode

Default: `survival`

Game mode of bot

### force_gamemode

Default: `false`

Forcing all bots to use the game mode configured by `gamemode`, if `false`, only saved bots will use the game mode configured by `gamemode`.

### name_prefix

Default: `bot_`

Prefix of bot name

### name_suffix

Default: None

Suffix of bot name

### post_join_delay

Default: `0`

Delay time (seconds) for processing after bot joined. If you are using a non-vanilla server, you may need to adjust this value.

### permissions

Minimum permission to use corresponding command

## FastAPI MCDR

The plugin supports the [FastAPI MCDR](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/bot/../fastapi_mcdr) plugin (>=2.0.0). After installing the FastAPI MCDR plugin, the plugin will automatically register endpoints. You can view the API definition through FastAPI.

Python packages required:

```text
pydantic>=2.0
```

You can use this feature to implement external control, such as a web page for managing bots:

![webpage to manage bots](https://github.com/user-attachments/assets/508689c3-a7d0-4280-ac3d-e9812d32c289)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

*Data fetching failed*

