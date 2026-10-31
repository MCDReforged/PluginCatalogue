**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## games_ai

### Basic Information

- Plugin ID: `games_ai`
- Plugin Name: GamesAI
- Version: 0.8.1
  - Metadata version: 0.8.1
  - Release version: 0.8.1
- Total downloads: 1533
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
> Welcome to version 0.8.1! This release adds **cross-server linking**: several MCDR instances form one cluster over WebSocket, one of them becomes the hub that owns the AI, the conversation history and the public database, and the others join as clients that forward their players' commands (the cluster-wide ones they run themselves); tools stay per instance -- every request carries the asking instance's local tool schemas. The Mineflayer bot joins the cluster as a client as well, instead of listening on a port of its own. See [the cross-server guide](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/cross-server.md). Every conversation is also **stored** (in a `chat_history` table of the same database file as `!!data`), so a reload, an update, a restart or removing the plugin no longer loses it, and a user's assistant can hand one message to another user's conversation with the new `send_message_to_player_ai` tool. The newest additions keep a stopped round's history (`!!ask stop`) and let an operator clear one player's history by name (`!!gamesai clear <name>`). **0.8.1 fixes the 0.8.0 self-updater**: an instance on 0.8.0 or 0.8.0-SNAPSHOT must install this release by hand once (`!!MCDR plugin install -U -y games_ai`), after which self-updates work again.

<details>
<summary>Table of Contents (click to expand)</summary>

- [GamesAI for MCDReforged](#gamesai-for-mcdreforged)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
    - [1. First start: let the plugin install what it needs](#1-first-start-let-the-plugin-install-what-it-needs)
    - [2. Configure an AI](#2-configure-an-ai)
    - [3. Check the connection and ask the first question](#3-check-the-connection-and-ask-the-first-question)
    - [4. Where the conversation lives (and how to clear it)](#4-where-the-conversation-lives-and-how-to-clear-it)
    - [5. Give the AI abilities: tools and skills (optional)](#5-give-the-ai-abilities-tools-and-skills-optional)
    - [6. Let it drive a Mineflayer bot (optional)](#6-let-it-drive-a-mineflayer-bot-optional)
    - [7. Link several instances into a cluster (optional)](#7-link-several-instances-into-a-cluster-optional)
    - [8. Everyday maintenance](#8-everyday-maintenance)
    - [Command reference](#command-reference)
  - [Technical Documentation](#technical-documentation)
  - [The Role of AI in This Project](#the-role-of-ai-in-this-project)
  - [Acknowledgements \& Disclaimer](#acknowledgements--disclaimer)
  - [Sponsorship \& Contributors](#sponsorship--contributors)
  - [License](#license)

</details>

## Installation

Run the following command in the MCDR console to install the plugin:

`!!MCDR plugin install games_ai`

Requirements: Python 3.12 or newer and MCDReforged 2.15.0 or newer (the manifest declares `mcdreforged >= 2.15.0`; MCDR runs the plugin on its own interpreter). Node.js 18+ with npm is needed only when you enable the Mineflayer bot.

---

Alternatively, get it from the [MCDR Plugin Repository](https://mcdreforged.com/plugin/games_ai) and place it in your plugin directory.

If you choose to install manually, the plugin takes care of its Python packages itself: on the first start it looks for `openai`, `requests` and `websockets`, installs whatever is missing with pip (the machine's own pip configuration first, the Aliyun PyPI mirror as a second attempt) and reloads itself when that worked. You only have to step in when both attempts fail -- the log then prints the exact command to run, in the `python -m pip` form:

```bash
python -m pip install openai requests websockets
```

`!!MCDR plugin install games_ai` cannot pre-install anything either: the package list lives inside the plugin (`games_ai/requirements.txt`), and MCDR only reads a `requirements.txt` at the plugin root before loading it. Every install route therefore starts with the packages missing, and the plugin repairs them itself on the first start (see [PIM](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/pim.md)); use the manual command above only when both pip attempts fail, and run `!!MCDR plugin reload games_ai` afterwards to bring the plugin back.

Coming from an older release needs no manual config edit: the old `mineflayer_bot.websocket.url` is migrated to the top-level `websocket.uri` on the first load. In a cluster, a node running an older build cannot obey the hub's update order, so install the new build by hand once on every instance (`!!MCDR plugin install -U -y games_ai`). Only the hub needs a reachable port, and a `wss://` uri can only be a client.

GamesAI maintains itself: the plugin updates its own file (cluster-aware, verified download, rollback on failure) and repairs its own Python packages. Both are described in [PIM: the plugin's own installer](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/pim.md).

## Quick Start

### 1. First start: let the plugin install what it needs

Put the plugin into `plugins/` and start the server (if it is already installed, `!!MCDR plugin reload games_ai` is enough). On the first start it checks its three Python packages (`openai`, `requests`, `websockets`) and installs whatever is missing with pip -- the machine's own pip configuration first, the Aliyun PyPI mirror as a second attempt -- then reloads itself:

```text
Installing the missing Python package(s) with pip: ...
[deps] ...
Dependencies installed; reloading the plugin...
Dependencies are ready; the plugin is fully loaded again (openai, requests, websockets)
```

While that runs, the plugin is loaded but idle: it registers no command and starts neither the bot nor the cross-server link. If both attempts fail, the log prints `Could not install: ...` together with the command to run by hand (`python -m pip install openai requests websockets`); run it, then `!!MCDR plugin reload games_ai`. See [PIM: the Python package manager](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/pim.md#the-python-package-manager) and [Missing Python Packages](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/troubleshooting.md#missing-python-packages).

### 2. Configure an AI

Open `config/games_ai/config.json` (created on the first start) and fill in one `all_ai` entry plus `default_ai`:

```json
{
  "all_ai": {
    "<Your AI ID>": {
      "prompt": "You are a mature, reliable Minecraft assistant.",
      "ai_name": "[GamesAI]",
      "base_url": "<Your API Base URL>",
      "ai_model": "<Your AI Model>",
      "api_key": "<Your API Key>",
      "extra_body": {}
    }
  },
  "default_ai": "<Your AI ID>"
}
```

- `all_ai` holds one entry per model; the key you choose is the plugin's internal AI ID.
- `base_url`, `ai_model` and `api_key` are your provider's OpenAI-compatible endpoint, model name and key.
- `ai_name` is what the AI prefixes its answers with (Minecraft formatting codes work).
- `extra_body` is passed to the provider untouched -- for a thinking model, for example `{"thinking": {"type": "enabled"}}`.
- `default_ai` must be exactly one of the `all_ai` keys: it is the model a plain `!!ask` uses.
- Optional `context_window` overrides the window that [automatic context management](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#automatic-context-management) uses for that model.

Keep long prompts out of the file by writing `"prompt": "> my_prompt.md"`: the text is then read from `config/games_ai/prompt/my_prompt.md`.

Apply the change with `!!gamesai reload`. `!!gamesai config get <key>` and `!!gamesai config set <key> <value>` handle simple top-level keys, but `config set` refuses the complex `all_ai` and `mineflayer_bot` blocks and does not resolve dotted keys, so edit those in the file. Every key is documented in [Configuration](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/configuration.md#3all_ai).

### 3. Check the connection and ask the first question

`!!gamesai speedtest` asks every configured model at `<base_url>/models` and prints the latency (`!!gamesai speedtest <model>` tests a single one). Then simply talk to it:

```text
!!ask Hello! Are you there?
```

`!!ask` is open to every player. Around it: `!!ask -n <content>` answers without the conversation history, `!!ask -f <content>` (alias `--forced`) merges the question into the round that is already running, `!!ask switch <model>` hands the conversation to another model (the old one summarizes it first), `!!ask stop` stops everything you have in flight and **keeps what the round already wrote**, and `!!ask context [player]` / `!!ask context --all` show how much context is in use. See [AI Request Pipeline](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#context-inspection) and [Stopping a running round](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#stopping-a-running-round).

### 4. Where the conversation lives (and how to clear it)

Every conversation is written into a `chat_history` table of `config/games_ai/database/public_database.db` -- the same file as `!!data`, a separate table -- after every finished round, and restored on every plugin load. A reload, an update, a restart or removing the plugin therefore no longer loses it.

`!!gamesai clear` deletes your own conversation; `!!gamesai clear <name>` deletes another player's (it needs the configured `permission` level and stops that player's running round first); `!!gamesai clearall` deletes all of them (also permission-gated). See [Conversation persistence](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#conversation-persistence).

### 5. Give the AI abilities: tools and skills (optional)

The plugin ships 27 built-in tools (world queries, public data, skills, the bot). Which ones a request is offered depends on the player's MCDR permission level and the configured `permission`, so a low-level player never sees the administrative ones at all.

- **Your own tools**: `config/games_ai/tools/tools.py` is created on the first start with a `@register_tool` skeleton. Add your functions there and run `!!gamesai reload`. See [Tools](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/tools.md#2-custom-tools-in-toolspy).
- **Skills**: `config/games_ai/skills/skills.json` indexes the skill files the AI reads with `read_skills`; the AI can also write and maintain them itself. See [Skills](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/skills.md#3-adding-your-own-skills).

### 6. Let it drive a Mineflayer bot (optional)

Node.js 18+ and npm have to be installed on the server machine. Then set the credentials and start it:

```text
!!aibot set username <Minecraft account name>
!!aibot set password <password>
!!aibot set auth microsoft
!!aibot join
```

`!!aibot leave` stops it again. In `config.json` the same settings live under `mineflayer_bot`: `enabled`, `cycle_interval` (how often the autonomous controller decides, 15 seconds by default) and `bot.username` / `bot.password` / `bot.auth` (`microsoft`, `mojang` or `offline`). The bot joins the cluster as a client instead of listening on a port of its own, and the server address is read from `server.properties`. Credentials are only read when the Node process (re)starts, so change them with `!!aibot set` and restart (`!!aibot leave`, then `!!aibot join`); `!!gamesai config set` refuses the whole `mineflayer_bot` block. See [Mineflayer Bot](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/mineflayer-bot.md#commands).

### 7. Link several instances into a cluster (optional)

One instance becomes the **hub** (it owns the AI, the conversation history and the public database) and the others join it as **clients** that forward their players' commands; tools stay with each instance. Point every instance at the hub in the `websocket` block of `config.json`:

```json
{
  "websocket": {
    "uri": "ws://<hub address>:8080",
    "force_server": false,
    "name": ""
  }
}
```

An instance that finds a GamesAI hub at that address becomes a client; one that finds nothing (and can bind the address) becomes the hub, while `force_server` insists on the hub role. Enrolment is per node: on the hub, `!!gamesai node pending` lists the waiting names and `!!gamesai node token <name>` issues a token; that instance joins with `!!gamesai node claim <token>`. `websocket.name` is derived from the instance directory when it is left empty. Cluster updates are ordered by the hub -- nodes first, hub last. The remaining keys (`allow_app_id`, `token_ttl_hours`, `auto_enroll`, `identity_file`) are documented in [Configuration §6](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/configuration.md#6websocket); the full picture is in [Cross-server Linking](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/cross-server.md#enrolment-one-token-per-instance) and [Cluster updates](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/cross-server.md#cluster-updates).

### 8. Everyday maintenance

- `!!gamesai reload` re-reads the configuration, the skills and the tools and restarts the bot when needed; the cross-server link keeps running. Changes to `websocket.*` need `!!MCDR plugin reload games_ai` (or `!!gamesai node claim` / `node forget`, which rebuild the link), because the link is built on load. See [Hot Reload](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/hot-reload.md#triggering-a-hot-reload).
- `!!gamesai check` looks for a new release and refreshes the context-window table; in a cluster the hub coordinates it. The plugin updates its own file (verified download, rollback on failure) and repairs its own Python packages -- see [PIM](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/pim.md).
- `!!gamesai debug` toggles the full request log; `!!gamesai debug thread` lists the threads the plugin owns.
- `!!data` manages the public key/value database the AI can read.
- Something broken? [Troubleshooting](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/troubleshooting.md) lists the log lines and what to do about them.

---

### Command reference

Type `!!gamesai` for the in-game feature list (`!!gamesai node …` for cluster enrolment, `!!aibot …` for the bot); the tables below cover the most used commands.

| Command                                                                 | Description                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!gamesai clear`                                                       | Clear your own chat history. It is stored in its own table of the public database file, and this deletes your row. `!!gamesai clear <name>` clears one other player's history instead and requires the configured `permission` level; a round that player still has in flight is stopped first.                 |
| `!!gamesai clearall`                                                    | Clear all players' chat history (the stored rows included).                                                                                                                                                                                                                                                     |
| `!!gamesai reload`                                                      | Reload the configuration, the skills and the tools and restart the bot; the cross-server link keeps running. See [Hot Reload](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/hot-reload.md#hot-reload) for details.                                                                              |
| `!!gamesai check`                                                       | Check for plugin updates and force-refresh the context-window table. In a cluster this is executed on the hub, which starts an update round: the nodes install first, the hub last (see [Cross-server Linking](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/cross-server.md#cluster-updates)). |
| `!!gamesai speedtest [model]`                                           | Test API server connection latency. If no model is specified, all models are tested.                                                                                                                                                                                                                            |
| `!!gamesai config get <key>`                                            | Read a configuration value.                                                                                                                                                                                                                                                                                     |
| `!!gamesai config set <key> <value>`                                    | Update a configuration value (auto type-adapts; automatically triggers [Hot Reload](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/hot-reload.md#hot-reload)).                                                                                                                                   |
| `!!gamesai node <pending|token|list|revoke|rotate|claim|status|forget>` | Cluster enrolment and node management; see [Cross-server Linking](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/cross-server.md#enrolment-one-token-per-instance).                                                                                                                              |
| `!!aibot join | leave`                                                  | Start or stop the Mineflayer bot; `!!aibot set <key> <value>` edits the bot credentials and reloads. See [Mineflayer Bot](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/mineflayer-bot.md).                                                                                                     |

---

You can also use `!!ask` directly to ask the AI questions, chat, or ask it to do things for you.

| Command                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!ask <content>`        | Ask the AI a question, chat, or ask it to do something. `<content>` is what you want the AI to do or the question you want to ask.                                                                                                                                                                                                                                                                                                                                                             |
| `!!ask -n <content>`     | Ask the AI without using conversation history (current conversation is still saved).                                                                                                                                                                                                                                                                                                                                                                                                           |
| `!!ask -f <content>`     | Force-ask without waiting: the request is merged into the round that is currently running (alias: `--forced`). See [AI Request Pipeline & Chat Mechanism](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#ai-request-pipeline--chat-mechanism).                                                                                                                                                                                                           |
| `!!ask switch <model>`   | Switch the AI model for your current conversation (`<model>` is the AI_ID or nickname). The history is cleared and the old model summarizes it right before your next request, handing the summary to the new model. See [Summary Hand-off on Model Switch](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#summary-hand-off-on-model-switch).                                                                                                            |
| `!!ask stop`             | Immediately stop everything you have in flight: your running round (tool calls included), a running `!!ask -n` request and a task you delegated to the bot. **What the round already wrote stays in the history** -- only a tool call whose result never arrived is dropped; queued `!!ask -f` messages are kept and merged by your next round. See [Stopping a running round](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#stopping-a-running-round). |
| `!!ask context [player]` | Show the context usage: model and window source, how much of the window is used, how many tokens are left before compression, the per-round sizes and the cache-hit rate. Without a player name it shows your own. See [Context Inspection](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#context-inspection).                                                                                                                                          |
| `!!ask context --all`    | Sum the context usage of every player on the server, grouped by model (models with zero usage are not listed); hover for that model's totals since those conversations were created (they survive a reload and a restart). See [Context Inspection](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#context-inspection).                                                                                                                                  |
| `!!ask compact`          | Compress the older history right now, ignoring the compression triggers. It is performed by the preflight of your next question, so the command itself never blocks. See [Context Inspection](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md#context-inspection).                                                                                                                                                                                        |

---

Type `!!data` for information about database commands.

> [!TIP]
> The database is created automatically on the first start -- no upgrade step is needed.

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

| Document                                                                                                    | Contents                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AI Request Pipeline](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/ai-request-pipeline.md) | Request chain, the stateless `!!ask -n`, the `!!ask switch` hand-off, `!!ask stop`, automatic context management, per-user state                                                                                                                                    |
| [Configuration](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/configuration.md)             | Every key of `config.json`: `prefix`, `permission`, `all_ai` (incl. `context_window`), `default_ai`, `mineflayer_bot`, `websocket` (`uri`, `force_server`, `allow_app_id`, `name`, `token_ttl_hours`, `auto_enroll`, `identity_file`) and the self-update behaviour |
| [Tools](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/tools.md)                             | The 27 built-in tools, writing your own in `tools.py`, registering tools from your own plugin, permissions and visibility                                                                                                                                           |
| [Skills](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/skills.md)                           | What skills are for, the built-in ones, `skills.json`, letting the AI write them, registering them from your own plugin                                                                                                                                             |
| [Example](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/example.md)                         | A real server configuration end to end: config, six skills, 44 custom tools, a walkthrough round and the pitfalls                                                                                                                                                   |
| [Mineflayer Bot](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/mineflayer-bot.md)           | Prerequisites, commands, how it works, supported actions, bot control tools                                                                                                                                                                                         |
| [Hot Reload](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/hot-reload.md)                   | Triggering a reload, what happens during one, following it from your plugin                                                                                                                                                                                         |
| [Cross-server Linking](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/cross-server.md)       | Cluster roles, per-node enrolment, command routing, cluster updates, tool scope                                                                                                                                                                                     |
| [PIM](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/pim.md)                                 | The plugin's own installer: self-update and Python package repair                                                                                                                                                                                                   |
| [Troubleshooting](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/troubleshooting.md)         | `!!ask` errors, bot errors, logging & debugging                                                                                                                                                                                                                     |
| [Testing](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/testing.md)                         | Installing pytest, running the whole suite, one module or one test by name, what each part of `tests/` holds, and what a run needs                                                                                                                                  |
| [Architecture](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/architecture.md)               | The package tree by role, how the parts may depend on each other, the dependency gate, and where a new module goes                                                                                                                                                  |
| [Changelog](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/changelog.md)                     | Release notes of recent releases                                                                                                                                                                                                                                    |

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
| [GamesAI-v0.8.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.8.1) | 0.8.1 | 2026/10/25 03:20:06 | 652.71KB | 31 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.8.1/GamesAI-v0.8.1.mcdr) |
| [GamesAI-v0.8.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.8.0) | 0.8.0 | 2026/10/24 16:12:33 | 648.16KB | 9 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.8.0/GamesAI-v0.8.0.mcdr) |
| [GamesAI-v0.7.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.3) | 0.7.3 | 2026/10/02 03:12:51 | 271.5KB | 31 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.3/GamesAI-v0.7.3.mcdr) |
| [GamesAI-v0.7.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.2) | 0.7.2 | 2026/09/27 06:54:23 | 262.42KB | 16 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.2/GamesAI-v0.7.2.mcdr) |
| [GamesAI-v0.7.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.1) | 0.7.1 | 2026/09/11 17:30:38 | 158.52KB | 25 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.1/GamesAI-v0.7.1.mcdr) |
| [GamesAI-v0.7.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.0) | 0.7.0 | 2026/08/29 17:46:11 | 112.88KB | 29 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.0/GamesAI-v0.7.0.mcdr) |
| [GamesAI-v0.6.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.4) | 0.6.4 | 2026/08/22 05:15:46 | 112.68KB | 37 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.4/GamesAI-v0.6.4.mcdr) |
| [GamesAI-v0.6.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.3) | 0.6.3 | 2026/08/18 09:05:58 | 107.24KB | 34 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.3/GamesAI-v0.6.3.mcdr) |
| [GamesAI-v0.6.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.2) | 0.6.2 | 2026/08/10 12:54:37 | 101.42KB | 44 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.2/GamesAI-v0.6.2.mcdr) |
| [GamesAI-v0.6.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.1) | 0.6.1 | 2026/08/07 06:52:54 | 92.88KB | 35 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.1/GamesAI-v0.6.1.mcdr) |
| [GamesAI-v0.6.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.0) | 0.6.0 | 2026/08/06 05:28:15 | 90.59KB | 27 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.0/GamesAI-v0.6.0.mcdr) |
| [GamesAI-v0.5.11.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.11) | 0.5.11 | 2026/07/28 04:27:12 | 54.15KB | 35 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.11/GamesAI-v0.5.11.mcdr) |
| [GamesAI-v0.5.10.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.10) | 0.5.10 | 2026/07/22 07:03:08 | 52.39KB | 31 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.10/GamesAI-v0.5.10.mcdr) |
| [GamesAI-v0.5.9.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.9) | 0.5.9 | 2026/07/22 06:14:53 | 53.52KB | 6 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.9/GamesAI-v0.5.9.mcdr) |
| [GamesAI-v0.5.8.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.8) | 0.5.8 | 2026/07/21 03:22:17 | 51.09KB | 32 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.8/GamesAI-v0.5.8.mcdr) |
| [GamesAI-v0.5.7.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.7) | 0.5.7 | 2026/07/19 03:45:10 | 50.45KB | 36 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.7/GamesAI-v0.5.7.mcdr) |
| [GamesAI-v0.5.6.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.6) | 0.5.6 | 2026/07/14 11:32:49 | 54.39KB | 34 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.6/GamesAI-v0.5.6.mcdr) |
| [GamesAI-v0.5.5.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.5) | 0.5.5 | 2026/07/08 11:08:15 | 51.89KB | 44 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.5/GamesAI-v0.5.5.mcdr) |
| [GamesAI-v0.5.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.4) | 0.5.4 | 2026/06/05 16:23:44 | 43.34KB | 73 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.4/GamesAI-v0.5.4.mcdr) |
| [GamesAI-v0.5.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.3) | 0.5.3 | 2026/05/24 08:27:26 | 41.59KB | 61 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.3/GamesAI-v0.5.3.mcdr) |
| [GamesAI-v0.5.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.2) | 0.5.2 | 2026/05/24 03:31:00 | 39.75KB | 58 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.2/GamesAI-v0.5.2.mcdr) |
| [GamesAI-v0.5.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.1) | 0.5.1 | 2026/05/16 14:33:47 | 37.42KB | 66 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.1/GamesAI-v0.5.1.mcdr) |
| [GamesAI-v0.5.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.0) | 0.5.0 | 2026/05/10 06:56:40 | 35.83KB | 66 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.0/GamesAI-v0.5.0.mcdr) |
| [GamesAI-v0.4.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.2) | 0.4.2 | 2026/05/02 14:47:09 | 23.1KB | 79 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.2/GamesAI-v0.4.2.mcdr) |
| [GamesAI-v0.4.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.1) | 0.4.1 | 2026/05/01 12:03:32 | 20.61KB | 80 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.1/GamesAI-v0.4.1.mcdr) |
| [GamesAI-v0.4.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.0) | 0.4.0 | 2026/04/26 05:25:45 | 20.0KB | 82 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.0/GamesAI-v0.4.0.mcdr) |
| [GamesAI-v0.3.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.2) | 0.3.2 | 2026/04/18 01:20:54 | 17.06KB | 95 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.2/GamesAI-v0.3.2.mcdr) |
| [GamesAI-v0.3.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.1) | 0.3.1 | 2026/04/12 06:15:12 | 14.82KB | 79 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.1/GamesAI-v0.3.1.mcdr) |
| [GamesAI-v0.3.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.0) | 0.3.0 | 2026/04/11 14:21:17 | 11.37KB | 77 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.0/GamesAI-v0.3.0.mcdr) |
| [GamesAI-v0.2.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.1) | 0.2.1 | 2026/04/04 04:27:04 | 8.45KB | 87 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.1/GamesAI-v0.2.1.mcdr) |
| [Game.sAI-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.0) | 0.2.0 | 2026/03/29 03:10:14 | 3.49KB | 94 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.0/Game.sAI-v0.2.0.mcdr) |

