**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## games_ai

### Basic Information

- Plugin ID: `games_ai`
- Plugin Name: GamesAI
- Version: 0.7.3
  - Metadata version: 0.7.3
  - Release version: 0.7.3
- Total downloads: 1438
- Authors: [yello](https://github.com/PengZixuan30)
- Repository: https://github.com/PengZixuan30/Games_AI
- Repository plugin page: https://github.com/PengZixuan30/Games_AI/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: This plugin allows you to use AI in the game

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [openai](https://pypi.org/project/openai) |  |
| [requests](https://pypi.org/project/requests) |  |
| [websockets](https://pypi.org/project/websockets) |  |

```
pip install openai requests websockets
```

### Introduction

<div align="center">

# GamesAI for MCDReforged

English  |  [简体中文](https://github.com/PengZixuan30/Games_AI/tree/main//README.zh-CN.md)  |  [繁體中文](https://github.com/PengZixuan30/Games_AI/tree/main//README.zh-TW.md)

[Report an Issue](https://github.com/PengZixuan30/Games_AI/issues/new)  |  [Share an Idea](https://github.com/PengZixuan30/Games_AI/discussions/new/choose)  |  [Join QQ Group](https://qm.qq.com/q/jDQQaUPNmw)

[Go to Fabric Version](https://github.com/PengZixuan30/GamesAI)

</div>

> [!NOTE]
> **GamesAI Plugin/Mod QQ Group: 849544707** — Join us to discuss issues, share feedback, and exchange prompt, skills, tools configurations!

> [!NOTE]
> Welcome to version 0.7.3! This release reworks the **message layout of a request**: there is only one system message now (the model's prompt + the skills list), the current time travels as a `user` message in front of the question and is re-injected periodically, the public data travels as an `assistant` message, and adjacent `user` messages are merged into one before sending — so models that accept a single leading system message only (Qwen3.5 and friends) work again, and the provider's prefix cache keeps hitting in long conversations. See [What's New](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/changelog.md#whats-new) for details.

<details>
<summary>Table of Contents (click to expand)</summary>

- [GamesAI for MCDReforged](#gamesai-for-mcdreforged)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Technical Documentation](#technical-documentation)
  - [The Role of AI in This Project](#the-role-of-ai-in-this-project)
  - [Acknowledgements \& Disclaimer](#acknowledgements--disclaimer)
  - [Sponsorship \& Contributors](#sponsorship--contributors)
  - [License](#license)

</details>

## Installation

Run the following command in the MCDR console to install the plugin:

`!!MCDR plugin install games_ai`

---

Alternatively, get it from the [MCDR Plugin Repository](https://mcdreforged.com/plugin/games_ai) and place it in your plugin directory.

If you choose to install manually, install the Python packages `openai`, `requests`, and `websockets` first:

```bash
pip install openai requests websockets
```

## Usage

Type `!!gamesai` anywhere to display all available features of this plugin.

| Command                              | Description                                                                                                                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!gamesai clear`                    | Clear your own chat history. Chat history is unrelated to the public database.                                                                                                |
| `!!gamesai clearall`                 | Clear all players' chat history. Chat history is unrelated to the public database.                                                                                            |
| `!!gamesai reload`                   | Reload the plugin configuration file. See [Hot Reload](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/hot-reload.md#hot-reload) for details.                   |
| `!!gamesai check`                    | Check for plugin updates and force-refresh the context-window table.                                                                                                          |
| `!!gamesai speedtest [model]`        | Test API server connection latency. If no model is specified, all models are tested.                                                                                          |
| `!!gamesai config get <key>`         | Read a configuration value.                                                                                                                                                   |
| `!!gamesai config set <key> <value>` | Update a configuration value (auto type-adapts; automatically triggers [Hot Reload](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/hot-reload.md#hot-reload)). |

---

You can also use `!!ask` directly to ask the AI questions, chat, or ask it to do things for you.

| Command                  | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!ask <content>`        | Ask the AI a question, chat, or ask it to do something. `<content>` is what you want the AI to do or the question you want to ask.                                                                                                                                                                                                                                                                        |
| `!!ask -n <content>`     | Ask the AI without using conversation history (current conversation is still saved).                                                                                                                                                                                                                                                                                                                      |
| `!!ask -f <content>`     | Force-ask without waiting: the request is merged into the round that is currently running (alias: `-forced`). See [AI Request Pipeline & Chat Mechanism](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#ai-request-pipeline--chat-mechanism).                                                                                                                       |
| `!!ask switch <model>`   | Switch the AI model for your current conversation (`<model>` is the AI_ID or nickname). The history is cleared and the old model summarizes it right before your next request, handing the summary to the new model. See [Summary Hand-off on Model Switch](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#summary-hand-off-on-model-switch).                       |
| `!!ask stop`             | Immediately stop everything you have in flight: your running round (tool calls included), a running `!!ask -n` request and a task you delegated to the bot. The interrupted step is deleted from the history and queued `!!ask -f` messages are discarded. See [Stopping a running round](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#stopping-a-running-round). |
| `!!ask context [player]` | Show the context usage: model and window source, how much of the window is used, how many tokens are left before compression, the per-round sizes and the cache-hit rate. Without a player name it shows your own. See [Context Inspection](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#context-inspection).                                                     |
| `!!ask context --all`    | Sum the context usage of every player on the server, grouped by model (models with zero usage are not listed); hover for the totals since the plugin was loaded. See [Context Inspection](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#context-inspection).                                                                                                       |
| `!!ask compact`          | Compress the older history right now, ignoring the compression triggers. It is performed by the preflight of your next question, so the command itself never blocks. See [Context Inspection](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#context-inspection).                                                                                                   |

---

Type `!!data` for information about database commands.

> [!TIP]
> The database is automatically created when upgrading to version 0.3.0 or above.

| Command                      | Description                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| `!!data write <key> <value>` | Add a data entry to the public database. `<key>` must not contain spaces; `<value>` can be any string. |
| `!!data add <key> <value>`   | Append `<value>` to an existing key in the public database. Creates a new key if it does not exist.    |
| `!!data del <key>`           | Delete a data entry from the public database, regardless of whether the key exists.                    |
| `!!data read <key>`          | Read the value associated with a key from the public database.                                         |
| `!!data list`                | Read all entries in the public database.                                                               |
| `!!data list keys`           | Read all keys in the public database.                                                                  |

---

## Technical Documentation

The technical details live in [`docs/en_us/`](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/) — how a request is built and kept inside the window, what every configuration key does, how tools and skills work, how the bot is driven, and what to do when something fails.

| Document                                                                                                    | Contents                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [AI Request Pipeline](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md) | Request chain, the stateless `!!ask -n`, the `!!ask switch` hand-off, `!!ask stop`, automatic context management, per-user state |
| [Configuration](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/configuration.md)             | Every key of `config.json`: `prefix`, `permission`, `all_ai` (incl. `context_window`), `default_ai`, `mineflayer_bot`            |
| [Tools](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/tools.md)                             | The 26 built-in tools, writing your own in `tools.py`, registering tools from your own plugin, permissions and visibility        |
| [Skills](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/skills.md)                           | What skills are for, the built-in ones, `skills.json`, letting the AI write them, registering them from your own plugin          |
| [Example](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/example.md)                         | A real server configuration end to end: config, six skills, 44 custom tools, a walkthrough round and the pitfalls                |
| [Mineflayer Bot](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/mineflayer-bot.md)           | Prerequisites, commands, how it works, supported actions, bot control tools                                                      |
| [Hot Reload](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/hot-reload.md)                   | Triggering a reload, what happens during one, following it from your plugin                                                      |
| [Troubleshooting](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/troubleshooting.md)         | `!!ask` errors, bot errors, logging & debugging                                                                                  |
| [Changelog](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/changelog.md)                     | Release notes of every published version                                                                                         |

> The same documents in other languages: [简体中文](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/) · [繁體中文](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_tw/).

---

## The Role of AI in This Project

GamesAI is an AI-powered plugin, and AI also plays an important role in how this project itself is maintained:

1. This README was originally typeset by the author (yello) and has since been fully revised by AI;
2. All translation files (`lang/*.yml`) are maintained by AI;
3. Logic checks before each release are performed by AI;
4. Issues reported for snapshot/development builds are investigated by AI;
5. GitHub issues and PRs are first triaged by AI before reaching the maintainer.

## Acknowledgements & Disclaimer

Special thanks to [WangHai Server](https://github.com/Wanghai-Server) for providing the foundation for testing this plugin.

Special thanks to [william-song-shy (William Song)](https://github.com/william-song-shy) for suggesting the `!!ask` no-history mode.

Special thanks to [ZhangZuoqian (张作乾)](https://github.com/ZhangZuoqian) for suggesting the `!!gamesai speedtest` command.

All content generated by AI (LLM) models is unrelated to this plugin.

All consequences arising from custom tools are unrelated to this plugin.

## Sponsorship & Contributors

Sponsorship address: [Afdian](https://ifdian.net/a/yello)

Those who sponsor GamesAI will appear in the following sponsor list (currently no sponsors):

| #   | Sponsor | Amount | Date |
| --- | ------- | ------ | ---- |
| -   | -       | -      | -    |

## License

MIT License, Copyright (c) 2026 yello

<div align = "center">

---

[Back to Top](#gamesai-for-mcdreforged)

</div>

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [GamesAI-v0.7.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.3) | 0.7.3 | 2026/10/02 03:12:51 | 271.5KB | 22 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.3/GamesAI-v0.7.3.mcdr) |
| [GamesAI-v0.7.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.2) | 0.7.2 | 2026/09/27 06:54:23 | 262.42KB | 15 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.2/GamesAI-v0.7.2.mcdr) |
| [GamesAI-v0.7.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.1) | 0.7.1 | 2026/09/11 17:30:38 | 158.52KB | 21 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.1/GamesAI-v0.7.1.mcdr) |
| [GamesAI-v0.7.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.0) | 0.7.0 | 2026/08/29 17:46:11 | 112.88KB | 26 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.0/GamesAI-v0.7.0.mcdr) |
| [GamesAI-v0.6.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.4) | 0.6.4 | 2026/08/22 05:15:46 | 112.68KB | 36 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.4/GamesAI-v0.6.4.mcdr) |
| [GamesAI-v0.6.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.3) | 0.6.3 | 2026/08/18 09:05:58 | 107.24KB | 33 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.3/GamesAI-v0.6.3.mcdr) |
| [GamesAI-v0.6.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.2) | 0.6.2 | 2026/08/10 12:54:37 | 101.42KB | 42 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.2/GamesAI-v0.6.2.mcdr) |
| [GamesAI-v0.6.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.1) | 0.6.1 | 2026/08/07 06:52:54 | 92.88KB | 33 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.1/GamesAI-v0.6.1.mcdr) |
| [GamesAI-v0.6.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.0) | 0.6.0 | 2026/08/06 05:28:15 | 90.59KB | 26 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.0/GamesAI-v0.6.0.mcdr) |
| [GamesAI-v0.5.11.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.11) | 0.5.11 | 2026/07/28 04:27:12 | 54.15KB | 33 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.11/GamesAI-v0.5.11.mcdr) |
| [GamesAI-v0.5.10.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.10) | 0.5.10 | 2026/07/22 07:03:08 | 52.39KB | 30 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.10/GamesAI-v0.5.10.mcdr) |
| [GamesAI-v0.5.9.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.9) | 0.5.9 | 2026/07/22 06:14:53 | 53.52KB | 6 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.9/GamesAI-v0.5.9.mcdr) |
| [GamesAI-v0.5.8.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.8) | 0.5.8 | 2026/07/21 03:22:17 | 51.09KB | 31 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.8/GamesAI-v0.5.8.mcdr) |
| [GamesAI-v0.5.7.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.7) | 0.5.7 | 2026/07/19 03:45:10 | 50.45KB | 34 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.7/GamesAI-v0.5.7.mcdr) |
| [GamesAI-v0.5.6.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.6) | 0.5.6 | 2026/07/14 11:32:49 | 54.39KB | 33 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.6/GamesAI-v0.5.6.mcdr) |
| [GamesAI-v0.5.5.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.5) | 0.5.5 | 2026/07/08 11:08:15 | 51.89KB | 41 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.5/GamesAI-v0.5.5.mcdr) |
| [GamesAI-v0.5.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.4) | 0.5.4 | 2026/06/05 16:23:44 | 43.34KB | 72 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.4/GamesAI-v0.5.4.mcdr) |
| [GamesAI-v0.5.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.3) | 0.5.3 | 2026/05/24 08:27:26 | 41.59KB | 61 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.3/GamesAI-v0.5.3.mcdr) |
| [GamesAI-v0.5.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.2) | 0.5.2 | 2026/05/24 03:31:00 | 39.75KB | 56 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.2/GamesAI-v0.5.2.mcdr) |
| [GamesAI-v0.5.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.1) | 0.5.1 | 2026/05/16 14:33:47 | 37.42KB | 65 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.1/GamesAI-v0.5.1.mcdr) |
| [GamesAI-v0.5.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.0) | 0.5.0 | 2026/05/10 06:56:40 | 35.83KB | 64 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.0/GamesAI-v0.5.0.mcdr) |
| [GamesAI-v0.4.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.2) | 0.4.2 | 2026/05/02 14:47:09 | 23.1KB | 79 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.2/GamesAI-v0.4.2.mcdr) |
| [GamesAI-v0.4.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.1) | 0.4.1 | 2026/05/01 12:03:32 | 20.61KB | 78 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.1/GamesAI-v0.4.1.mcdr) |
| [GamesAI-v0.4.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.0) | 0.4.0 | 2026/04/26 05:25:45 | 20.0KB | 81 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.0/GamesAI-v0.4.0.mcdr) |
| [GamesAI-v0.3.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.2) | 0.3.2 | 2026/04/18 01:20:54 | 17.06KB | 94 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.2/GamesAI-v0.3.2.mcdr) |
| [GamesAI-v0.3.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.1) | 0.3.1 | 2026/04/12 06:15:12 | 14.82KB | 78 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.1/GamesAI-v0.3.1.mcdr) |
| [GamesAI-v0.3.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.0) | 0.3.0 | 2026/04/11 14:21:17 | 11.37KB | 75 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.0/GamesAI-v0.3.0.mcdr) |
| [GamesAI-v0.2.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.1) | 0.2.1 | 2026/04/04 04:27:04 | 8.45KB | 83 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.1/GamesAI-v0.2.1.mcdr) |
| [Game.sAI-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.0) | 0.2.0 | 2026/03/29 03:10:14 | 3.49KB | 90 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.0/Game.sAI-v0.2.0.mcdr) |

