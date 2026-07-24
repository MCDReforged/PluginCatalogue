**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## unified_handler

### Basic Information

- Plugin ID: `unified_handler`
- Plugin Name: Unified Handler
- Version: 0.2.1
  - Metadata version: 0.2.1
  - Release version: 0.2.1
- Total downloads: 40
- Authors: [Alex3236](https://github.com/Alex3236)
- Repository: https://github.com/alex3236/UnifiedHandler
- Repository plugin page: https://github.com/alex3236/UnifiedHandler/tree/master
- Labels: [`Handler`](/labels/handler/readme.md)
- Description: ✨ YAML-driven universal server handler, simple, easy to use, and extensible

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.13.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

[`中文`](https://github.com/alex3236/UnifiedHandler/tree/master/README.md) | **English**

# Unified Handler

A profile-driven server handler plugin for MCDReforged. One plugin, all server types. No more juggling a dozen handler plugins.

## What problem does it solve?

MCDR's plugin handler system has a couple of quirks:

- **Only one plugin handler can be active at a time.** If plugin A adds "command block support" and plugin B adds "chat prefix parsing" — you have to pick one.
- **Plugin handlers can't elegantly extend the current handler.** Want to tweak just one thing on top of ForgeHandler? You'd have to copy the entire thing.

Unified Handler fixes both with a simple **Base ⊕ Features** architecture.

## How it works

```
Handler = Base (server type, pick one) ⊕ Features (extras, stack as many as you like)
```

- **Base** tells the plugin what kind of server you're running. Built-in support for Vanilla, Forge, Bukkit, Velocity, Bedrock BDS, plus community forks like Cleanroom and Leaves.
- **Features** are stackable enhancements — **you can enable multiple features at once, in any combination**. Command block recognition, chat prefix parsing, subserver message routing — pick and choose like building blocks.

Everything is defined in **YAML profiles** — readable, editable, and upgrade-safe.

### Why not hooks / mixins?

Early on, this project considered exposing hooks so other plugins could inject logic during message processing. Ultimately we chose not to go that route:

- **More efficient.** Profiles are compiled once at load time into pre-processed regex structures. There's no runtime dispatching, no jumping between plugins, no dynamic callback lookup. Every log line matches directly against the compiled profile.

- **Easier to use.** Writing YAML has a much lower barrier than writing Python. No coding knowledge, no MCDR API familiarity needed — just write a few regex patterns that match your server's log format. The built-in profiles are living proof: the Cleanroom and Leaves adapters each took less than 20 lines of YAML.

- **One handler is enough.** MCDR only allows one plugin handler at a time. Base ⊕ Features already covers the vast majority of use cases. Instead of making multiple plugins coordinate at runtime, UnifiedHandler consolidates everything into a single, compile-time solution.

## Quick Start

> [!IMPORTANT]
> **Do not use alongside other handler plugins.** MCDR's behavior is undefined when multiple plugin handlers are present — there's no guarantee which one takes effect.
> If you already have other handler plugins installed, remove them first, then configure UnifiedHandler.

### 📦 Installation

Run in the MCDR console:

```
!!MCDR plugin install unified_handler
```

The plugin auto-generates `config/unified_handler/config.yml` and deploys built-in profiles — no manual reload needed.

Alternatively, drop the `.mcdr` file into the `plugins/` directory and reload MCDR.

### ⚙️ Configuration

> [!NOTE]  
> After configuration, run through the [Handler Verification Guide](https://github.com/alex3236/UnifiedHandler/tree/master/doc/handler_troubleshooting_en.md) to confirm everything is working.

Edit `config/unified_handler/config.yml`

<details open>
<summary><strong>✅ Case 1: MCDR's built-in handler covers your server</strong></summary>

[MCDR's built-in handlers](https://docs.mcdreforged.com/en/latest/configuration.html#handler) (Vanilla / Forge / Bukkit / Velocity, etc.) handle most cases. You just need some extensions (like Team prefix handling):

1. Keep the `handler` field in your MCDR config file
2. Set `base_handler` to `"auto"`
3. Add the features you want

```yaml
base_handler: "auto"

features:
  - chat_prefixes     # parse team/rank prefixes in player chat
  - commandblock      # stack as many as you like
```

</details>

<details>
<summary><strong>🔧 Case 2: MCDR's built-in handler can't handle your server</strong></summary>

For servers like BDS, Leaves, etc. — use the plugin's built-in profiles:

1. Set `base_handler` to the matching profile name
2. Add features as needed

```yaml
base_handler: "bedrock_bds"    # see "Built-in Profiles" below

features:
  - commandblock
```

If the built-in profiles aren't enough, you can always [write your own](https://github.com/alex3236/UnifiedHandler/tree/master/doc/custom_profile_en.md):

```yaml
base_handler: "my_custom_server"
```

</details>

Other config fields:

```yaml
command_prefix: "!!uh" # command prefix
admin_permission: 3    # permission level for UnifiedHandler commands
debug: false           # set to true to enable debug output
```

## Built-in Profiles

UnifiedHandler ships with profiles for common server setups. Thanks to the original plugin authors.

Since these haven't been fully tested on a live server, some profiles might have issues. If you find that any features aren't working as advertised during use, please report it in an Issue.

### Base

| Name            | File                     | For                        | Credits                                                                          |
| --------------- | ------------------------ | -------------------------- | -------------------------------------------------------------------------------- |
| `cleanroom`     | `base/cleanroom.yml`     | Cleanroom MC               | [`Cmmmmmm`](https://github.com/CmmmmmmLau/CleanroomHandler)                      |
| `leaves`        | `base/leaves.yml`        | LeavesMC                   | [`Mooling0602`](https://github.com/Mooling0602/LeavesHandler-MCDR)               |
| `lbs_subserver` | `base/lbs_subserver.yml` | Velocity subserver routing | [`Ra1ny_Yuki`](https://github.com/Lazy-Bing-Server/LBSVelocityHandler-MCDR)      |
| `bedrock_bds`   | `base/bedrock_bds.yml`   | Bedrock Dedicated Server   | [`Elec glacier`](https://github.com/Elec-Glacier/liteloader_handler), `jiangyan` |

### Features

| Name            | File                         | Does                                                  | Credits                                                                                                                         |
| --------------- | ---------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `commandblock`  | `features/commandblock.yml`  | `[@]` and `[Server]` output can trigger MCDR commands | [`Dainsleif`](https://github.com/Dainsleif233/MCDR-Commandblock-Handler)                                                        |
| `chat_prefixes` | `features/chat_prefixes.yml` | Parse `<[Team]Name>` and rank prefix chat formats     | [`DCS`](https://github.com/ayuan94/TitlePrefixHandler), [`Mooling0602`](https://github.com/Mooling0602/VanillaTeamHandler-MCDR) |

## Custom Profiles

Need to adapt a custom server? Just write a few lines of YAML. We provide a full [JSON Schema](https://github.com/alex3236/UnifiedHandler/tree/master/profile.schema.json) for autocompletion and validation.

Check out the [Custom Profile Guide](https://github.com/alex3236/UnifiedHandler/tree/master/doc/custom_profile_en.md).

## Contribute Your Profile

If your profile serves a general use case (a server adapter, a common feature enhancement), we welcome PRs. Before submitting:

- Place the file under `resources/builtin_profiles/base/` or `features/`
- Include `name`, `version`, `changelog`, and `description` fields
- If adapting an existing plugin's handler, credit the original author in the PR

## Commands

*All `!!uh` commands require admin permission.*

| Command               | Does                                           |
| --------------------- | ---------------------------------------------- |
| `!!uh`                | Show current Base and active Features          |
| `!!uh status`         | Same as above                                  |
| `!!uh reload`         | Reload config and profiles                     |
| `!!uh debug [on|off]` | Toggle debug output                            |
| `!!uh update`         | Update and overwrite outdated builtin profiles |

## Compatibility

- MCDReforged >= 2.13.0
- Zero MCDR core modifications

## License

[FreeBSD License](https://github.com/alex3236/UnifiedHandler/tree/master/LICENSE)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [UnifiedHandler-v0.2.1.mcdr](https://github.com/alex3236/UnifiedHandler/releases/tag/v0.2.1) | 0.2.1 | 2026/05/29 12:56:23 | 23.88KB | 40 | [Download](https://github.com/alex3236/UnifiedHandler/releases/download/v0.2.1/UnifiedHandler-v0.2.1.mcdr) |

