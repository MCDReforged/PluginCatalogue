**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## ollama_chat

### Basic Information

- Plugin ID: `ollama_chat`
- Plugin Name: OllamaChat
- Version: 1.0.0-pre2
  - Metadata version: 1.0.0-pre2
  - Release version: 1.0.0-pre2
- Total downloads: 20
- Authors: [xwwsdd](https://github.com/mcraftbbs)
- Repository: https://github.com/mcraftbbs/OllamaChat_MCDR
- Repository plugin page: https://github.com/mcraftbbs/OllamaChat_MCDR/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Let your server chat with AI using Ollama or OpenAI

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [uuid_api](/plugins/uuid_api/readme.md) | \>=0.1.2 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [openai](https://pypi.org/project/openai) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install mcdreforged openai requests
```

### Introduction

Some code writing techniques are inspired by reference: https://github.com/gubaiovo/MCDR_chat_with_ai
# OllamaChat

[The officially developed OllamaChat plugin MCDR version]

📜 LICENSE: **GNU GPLv3** [![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Minecraft server plugin for MCDReforged that enables players to chat with AI using either Ollama or OpenAI.

## 📦 Dependencies
- Main Dependency: [MCDReforged](https://github.com/MCDReforged/MCDReforged) v2.x
- *Required Dependency*: [uuid_api](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api) (GPLv3)

## Features
- Chat with AI in Minecraft.
- Supports both Ollama (local) and OpenAI (API) backends.
- Customizable AI label and setup prompts.
- View and reset chat history.

## Installation
1. Ensure [MCDReforged](https://github.com/MCDReforged/MCDReforged) is installed on your server.
2. Install required Python dependencies:
   ```bash
   pip install openai requests
   ```
3. Place the plugin files in the `plugins` folder of your MCDReforged server.
4. Restart the server to generate the default configuration.

## Commands
All commands are prefixed with `!!oc` and can only be used by players.

| Command               | Description             | Example        |
| --------------------- | ----------------------- | -------------- |
| `!!oc guide`          | Show this command guide | `!!oc guide`   |
| `!!oc records`        | View chat history       | `!!oc records` |
| `!!oc reset`          | Clear chat history      | `!!oc reset`   |
| `!!oc chat <message>` | Chat with the AI        | `!!oc chat Hi` |

## Support
- Report issues or suggest features on GitHub/[community server](https://chat.sarskin.cn/invite/iHgI6LTX)..

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ollama_chat.mcdr](https://github.com/mcraftbbs/OllamaChat_MCDR/releases/tag/1.0.0-pre2) | 1.0.0-pre2 | 2025/03/12 19:59:13 | 6.38KB | 17 | [Download](https://github.com/mcraftbbs/OllamaChat_MCDR/releases/download/1.0.0-pre2/ollama_chat.mcdr) |
| [ollama_chat.mcdr](https://github.com/mcraftbbs/OllamaChat_MCDR/releases/tag/1.0.0-pre1) | 1.0.0-pre1 | 2025/03/11 14:16:32 | 6.62KB | 3 | [Download](https://github.com/mcraftbbs/OllamaChat_MCDR/releases/download/1.0.0-pre1/ollama_chat.mcdr) |

