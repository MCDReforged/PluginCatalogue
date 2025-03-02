**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## pcc

### Basic Information

- Plugin ID: `pcc`
- Version: *Data fetching failed*
- Total downloads: N/A
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/pcc_mcdr
- Repository plugin page: https://github.com/kmcsr/pcc_mcdr/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

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

*Data fetching failed*

