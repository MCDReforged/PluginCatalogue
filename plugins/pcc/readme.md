**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## pcc

### Basic Information

- Plugin ID: `pcc`
- Plugin Name: ProxiedChatConnection
- Version: 0.3.5
  - Metadata version: 0.3.5
  - Release version: 0.3.5
- Total downloads: 713
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/pcc_mcdr
- Repository plugin page: https://github.com/kmcsr/pcc_mcdr/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Allows you send MCDR commands privately with autocomplete feature

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.14.0 |
| [kpi](/plugins/kpi/readme.md) | ~1.5.1 |
| [loginproxy](/plugins/loginproxy/readme.md) | ~0.9.0 |
| [packet_parser](/plugins/packet_parser/readme.md) | ~0.0.3 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction


- English
- [中文](https://github.com/kmcsr/pcc_mcdr/tree/main/README_zh.MD)

# PCC

A MCDR plugin allows you send MCDR commands privately.  
It also support to autocomplete MCDR commands in game without any mods install in the client.

Require `enable_packet_proxy` set to `true` in `loginproxy/config.json`

Does not support Minecraft earier than 1.19.2.

Tested version: 1.19.2, 1.21.1

## Dependencies

| ID                                                      | Release Link                                         |
| ------------------------------------------------------- | ---------------------------------------------------- |
| [kpi](https://github.com/kmcsr/kpi_mcdr)                | <https://github.com/kmcsr/kpi_mcdr/releases>         |
| [loginproxy](https://github.com/kmcsr/login_proxy_mcdr) | <https://github.com/kmcsr/login_proxy_mcdr/releases> |

## Usage

This plugin will register MCDR commands to Minecraft command tree after player login,
You can use `/!!` as the prefix to be able to autocomplete MCDR commands.

PCC assume all the texts that starts with `!!` or `/!!` is MCDR commands. The commands that not begin with `!!` will not be proxied by PCC.

## Options

### `register_vanilla_command`

When enabling, PCC will register a dynamic command node which is called `<!!MCDR-command>` to autocomlete MCDR commands that sent in Minecraft command form.  
Enabled by default

### `proxy_mcdr_chat_command`

When enabling, PCC will proxy MCDR commands which sent in chat form, and prevent it from being send to the Minecraft server.
This might cause some plugins cannot parse its commands.  
Enabled by default

### `chat_preview_suggestion`

When enabling, PCC will request the clients send its chat preview to this plugin, which make PCC be able to parse MCDR commands and returns suggestions.  
Disabled by default


### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ProxiedChatConnection-v0.3.5.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.5) | 0.3.5 | 2025/04/23 15:46:25 | 17.76KB | 337 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.5/ProxiedChatConnection-v0.3.5.mcdr) |
| [ProxiedChatConnection-v0.3.4.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.4) | 0.3.4 | 2025/04/15 16:34:15 | 17.76KB | 49 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.4/ProxiedChatConnection-v0.3.4.mcdr) |
| [ProxiedChatConnection-v0.3.3.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.3) | 0.3.3 | 2025/03/10 15:15:32 | 17.77KB | 110 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.3/ProxiedChatConnection-v0.3.3.mcdr) |
| [ProxiedChatConnection-v0.3.2.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.2) | 0.3.2 | 2025/02/08 04:57:20 | 17.04KB | 66 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.2/ProxiedChatConnection-v0.3.2.mcdr) |
| [ProxiedChatConnection-v0.3.1.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.1) | 0.3.1 | 2025/02/07 23:55:48 | 16.87KB | 28 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.1/ProxiedChatConnection-v0.3.1.mcdr) |
| [ProxiedChatConnection-v0.3.0.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.0) | 0.3.0 | 2025/02/07 15:37:44 | 18.95KB | 27 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.0/ProxiedChatConnection-v0.3.0.mcdr) |
| [ProxiedChatConnection-v0.2.0.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.2.0) | 0.2.0 | 2025/02/06 23:23:54 | 18.27KB | 68 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.2.0/ProxiedChatConnection-v0.2.0.mcdr) |
| [ProxiedChatConnection-v0.1.0.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.1.0) | 0.1.0 | 2025/02/06 20:30:55 | 17.54KB | 28 | [Download](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.1.0/ProxiedChatConnection-v0.1.0.mcdr) |

