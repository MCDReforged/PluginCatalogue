**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## games_ai

### Basic Information

- Plugin ID: `games_ai`
- Plugin Name: GamesAI
- Version: 0.5.10
  - Metadata version: 0.5.10
  - Release version: 0.5.10
- Total downloads: 717
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

```
pip install openai requests
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
> Welcome to version 0.5.10! This release introduces **generic `extra_body` configuration** replacing the `thinking` boolean flag, enabling full control over API request parameters. See [What's New](#whats-new)

> [!IMPORTANT]
> **Breaking Change in 0.5.10**: The `thinking` boolean config has been replaced by a generic `extra_body` dict. If you were using `"thinking": true`, you must migrate to `"extra_body": {"thinking": {"type": "enabled"}}`. See [What's New](#1-extra_body--generic-api-parameter-configuration-breaking) for migration guide.

<details>
<summary>Table of Contents (click to expand)</summary>

- [GamesAI for MCDReforged](#gamesai-for-mcdreforged)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
    - [1.prefix](#1prefix)
    - [2.permission](#2permission)
    - [3.max\_history](#3max_history)
    - [4.all\_ai](#4all_ai)
    - [5.default\_ai](#5default_ai)
  - [Tools, Skills \& Custom Tools](#tools-skills--custom-tools)
    - [Tools](#tools)
    - [Skills](#skills)
    - [Custom Tools](#custom-tools)
  - [What's New](#whats-new)
    - [Version 0.5.10](#version-0510)
      - [1. `extra_body` — Generic API Parameter Configuration (BREAKING)](#1-extra_body--generic-api-parameter-configuration-breaking)
    - [Version 0.5.9](#version-059)
      - [1. System Message Refactoring](#1-system-message-refactoring)
      - [2. New `ai_read_all_data` Tool](#2-new-ai_read_all_data-tool)
      - [3. Real-Time Database Injection](#3-real-time-database-injection)
      - [4. Thinking Message Style](#4-thinking-message-style)
      - [5. Bug Fixes \& Stability](#5-bug-fixes--stability)
  - [Acknowledgements \& Disclaimer](#acknowledgements--disclaimer)
  - [Sponsorship \& Contributors](#sponsorship--contributors)
  - [License](#license)

</details>

## Installation

Run the following command in the MCDR console to install the plugin:

`!!MCDR plugin install games_ai`

---

Alternatively, get it from the [MCDR Plugin Repository](https://mcdreforged.com/plugin/games_ai) and place it in your plugin directory.

If you choose to install manually, install the Python packages `openai` and `requests` first:

```bash
pip install openai requests
```

## Usage

Type `!!gamesai` anywhere to display all available features of this plugin.

| Command                       | Description                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| `!!gamesai clear`             | Clear your own chat history. Chat history is unrelated to the public database.       |
| `!!gamesai clearall`          | Clear all players' chat history. Chat history is unrelated to the public database.   |
| `!!gamesai reload`            | Reload the plugin configuration file.                                                |
| `!!gamesai check`             | Check for plugin updates.                                                            |
| `!!gamesai speedtest [model]` | Test API server connection latency. If no model is specified, all models are tested. |

---

You can also use `!!ask` directly to ask the AI questions, chat, or ask it to do things for you.

| Command                         | Description                                                                                                                                                                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!ask <content>`               | Ask the AI a question, chat, or ask it to do something. `<content>` is what you want the AI to do or the question you want to ask.                                                                                          |
| `!!ask -m <model> <content>`    | Use a specific model to ask the AI a question, chat, or ask it to do something. `<model>` is the AI_ID or nickname of the model you want to use. `<content>` is what you want the AI to do or the question you want to ask. |
| `!!ask -n <content>`            | Ask the AI without using conversation history (current conversation is still saved).                                                                                                                                        |
| `!!ask -n -m <model> <content>` | Use a specific model without conversation history.                                                                                                                                                                          |

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

## Configuration

The default configuration file structure is as follows:

```json
{
  "prefix": "[GamesAI]",
  "permission": 3,
  "max_history": 10,
  "all_ai": {
      "<Your AI ID>":{
          "prompt": "You are a mature, reliable Minecraft bot tool named \"GamesAI\".",
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

---

Below is a brief introduction to each parameter:

### 1.prefix
Type: `str`

Default: `[GamesAI]`

The plugin name used as a prefix in replies. May include Minecraft formatting codes.

### 2.permission
Type: `int`

Default: `3`

The minimum permission level required to execute commands like `!!data`. See the [MCDR Permission Documentation](https://docs.mcdreforged.com/en/latest/permission.html).

### 3.max_history
Type: `int`

Default: `10`

The maximum number of conversation turns retained per player. Unrelated to the public database. Set to `0` to completely disable history.

### 4.all_ai
Type: `dict`

Default: see file

All AI configuration entries, consisting of multiple sub-dictionaries. Each sub-dictionary represents one AI model, and its key serves as the plugin's internal AI_ID.

**prompt**: Use this option to write a system prompt for each AI. Use `> xxx.md` to point the prompt to the `config/games_ai/prompt/xxx.md` file (any file type is supported).

**ai_name**: Similar to `prefix`, but set per model. May include Minecraft formatting codes.

**base_url**, **ai_model**, **api_key**: Same as previous related configuration, but now set per model.

**extra_body**: Please refer to your API provider's documentation for the `extra_body` parameter. For DeepSeek users migrating from the previous `thinking` option, use `{"thinking": {"type": "enabled"}}`. Defaults to `{}` (empty).

### 5.default_ai
Type: `str`

Default: `<Your AI ID>`

The model used when a player simply uses `!!ask`. Should be one of the keys in the `all_ai` dictionary (i.e. the plugin's internal AI_ID). An incorrect value will prevent `!!ask` from working properly.

## Tools, Skills & Custom Tools

### Tools
The GamesAI plugin provides many built-in tools, listed in the table below. If you want more tools, you can [submit a suggestion](https://github.com/PengZixuan30/Games_AI/issues/new) or use [Custom Tools](#custom-tools).

<details>
<summary>Click to view all built-in tools</summary>

|        Tool ID        |           Parameters           | Description                                                                                                                                                                                                                                                    |
| :-------------------: | :----------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  get_online_players   |              None              | Get the list of currently online players. Depends on the `online_player_api` plugin; automatically disabled if unavailable.                                                                                                                                    |
|  get_whitelist_name   |              None              | Get the complete server whitelist. Depends on the `whitelist_api` plugin; automatically disabled if unavailable.                                                                                                                                               |
|   add_to_whitelist    |             `name`             | Add a player to the whitelist. Depends on the `whitelist_api` plugin; automatically disabled if unavailable.                                                                                                                                                   |
| remove_from_whitelist |             `name`             | Remove a player from the whitelist. Depends on the `whitelist_api` plugin; automatically disabled if unavailable.                                                                                                                                              |
| search_minecraft_wiki |            `query`             | Let the AI search the Minecraft Wiki for more accurate answers.                                                                                                                                                                                                |
|      calculator       |          `expression`          | A simple mathematical expression calculator.                                                                                                                                                                                                                   |
|    item_caculator     |  `expression`, `single_limit`  | A mathematical expression calculator that converts results into Minecraft item notation (shulker boxes, stacks, items). Automatically adapts to stack size; defaults to 64 if not specified.                                                                   |
|      add_pos_pos      |   `name`, `pos`, `dimension`   | Add a waypoint at a specified location. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                                                                 |
|     add_pos_here      |             `name`             | Add a waypoint at the player's current location. Automatically disabled when executed from the console. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available. |
|      remove_pos       |             `name`             | Delete a waypoint. The `where2go` version automatically converts names to IDs. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                          |
|      search_pos       |             `name`             | Search for a waypoint. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                                                                                  |
|      get_all_pos      |              None              | Get a list of all waypoints. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                                                                            |
|     ai_read_data      |             `key`              | Read a single entry from the database.                                                                                                                                                                                                                         |
|   ai_read_all_keys    |              None              | Get all keys from the database.                                                                                                                                                                                                                                |
|   ai_read_all_data    |              None              | Read all key-value pairs from the database at once.                                                                                                                                                                                                            |
|     ai_write_data     |         `key`, `value`         | Write a data entry to the database (overwrite mode).                                                                                                                                                                                                           |
|      ai_add_data      |         `key`, `value`         | Write a data entry to the database (append mode).                                                                                                                                                                                                              |
|      read_skills      |            `skills`            | Read a registered skill instruction file to guide AI behavior for specific tasks.                                                                                                                                                                              |
|     write_skills      | `skills`, `summary`, `content` | Create or overwrite a skill file and register it in the skills index.                                                                                                                                                                                          |
|     modify_skills     | `skills`, `summary`, `content` | Modify an existing skill file and update its summary in the index.                                                                                                                                                                                             |
|     delete_skills     |            `skills`            | Delete a skill file and remove it from the skills index.                                                                                                                                                                                                       |
|   read_custom_tools   |              None              | Read the current content of the custom `tools.py` file.                                                                                                                                                                                                        |
|  modify_custom_tools  |            `tools`             | Replace the entire custom `tools.py` file with new code.                                                                                                                                                                                                       |
|  append_custom_tools  |            `tools`             | Append new tool code to the end of the custom `tools.py` file.                                                                                                                                                                                                 |
|     setting_timer     |           `duration`           | Pause execution for the specified number of seconds before continuing.                                                                                                                                                                                         |
|     reload_plugin     |              None              | Hot-reload the plugin to apply configuration, skills, and custom tools changes without losing chat history.                                                                                                                                                    |
|      ai_del_data      |             `key`              | Delete a data entry from the database.                                                                                                                                                                                                                         |

</details>

### Skills

The Skills system lets you write instruction files to guide how the AI handles specific tasks — such as whitelist management, fake player control, and more.

Skills files are stored in `config/games_ai/skills/` as Markdown (`.md`) files. To register a skill, edit `config/games_ai/skills/skills.json`. The following is an example configuration (`whitelist.md` and `player.md` are example filenames only — they are not built-in files):

```json
[
    {
        "file": "whitelist.md",
        "description": "Read this skill before managing the whitelist"
    },
    {
        "file": "player.md",
        "description": "Read this skill before controlling fake players"
    }
]
```

- **`file`** — the skill filename (relative to the `skills` folder).
- **`description`** — a short hint shown to the AI, explaining when to read this skill.

When a skill is registered, it appears in the AI's system prompt. The AI can then use the **`read_skills`** tool to read the full contents of any skill file before performing related tasks.

> [!TIP]
> GamesAI ships with two **built-in skills**: `skills_management.md` (how to manage skill files) and `custom_tools_management.md` (how to modify custom tools). The AI will automatically read these before modifying skills or tools.

> [!TIP]
> Skills are like SOPs (Standard Operating Procedures) for the AI — they ensure the AI follows the correct workflow every time.

### Custom Tools
Customize tools by editing the `config/games_ai/tools/tools.py` file.

Let's start by looking at the default content:

```python
from mcdreforged.command.command_source import CommandSource
from games_ai.games_ai_tool import register_tool

@register_tool(description="My Custom Tool")
def my_custom_tool(source: CommandSource, ai_prefix: str):
    return "Tool execution completed"
```

> [!IMPORTANT]
> The `from games_ai.games_ai_tool import register_tool` import and the `@register_tool` decorator above the function definition **must** be present.

> [!TIP]
> In version 0.5.7+, the AI can autonomously **read, modify, and append** the custom tools file using the `read_custom_tools`, `modify_custom_tools`, and `append_custom_tools` tools. Just ask the AI to add a new tool for you — it will read the current file, write the new code, and reload the plugin.

As you can see, the structure is very simple.

Now I'll show you how to build a real tool. Let's use searching `baidu.com` as an example.

<details>

<summary>Click to expand</summary>

The best way to understand how to implement a Baidu search is to look at the built-in `search_minecraft_wiki` tool in the GamesAI source code:

```python
@register_tool(description="Search Minecraft Wiki for relevant information. Do not use this method to search for non-Minecraft content. If the search results page is returned, you can browse that page first and then perform a more precise query.", tr_key="searching_minecraft_wiki", parameters={
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "The search term, e.g. the name of an item, mob, or game mechanic."
        }
    },
    "required": ["query"]
})
def search_minecraft_wiki(source: CommandSource, ai_prefix: str, query: str):
    source.reply(f'{ai_prefix}{source.get_server().rtr("games_ai.tools.searching_minecraft_wiki", query=query)}')
    lang = source.get_server().get_mcdr_language()
    if lang == "en_us":
        search_url = f"https://minecraft.wiki/?search={query}"
    else:
        search_url = f"https://zh.minecraft.wiki/?search={query}"
    response = requests.get(search_url)
    if response.status_code == 200:
        return f"Search results for {query}:\n{response.content.decode('utf-8')}"
    else:
        return "Unable to access Minecraft Wiki for searching."
```

Let's start by looking at the tool registration. `description` is like a system prompt — it's mandatory and is provided to the AI. `tr_key` is an internal identifier; you do **not** need to include it when writing external `tools.py`. `parameters` defines the arguments the AI should pass in. You can decide whether to include it based on your actual needs. `properties` lists all the input parameters, and `required` specifies which are mandatory. Make sure `properties` and the function's parameter list correspond one-to-one.

For example:

```python
@register_tool(description="Search Baidu")
```

However, searching Baidu obviously requires a search term, so:

```python
@register_tool(description="Search Baidu", parameters={
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "The search term"
        }
    },
    "required": ["query"]
})
```

Great — you now know how to register a tool! Next, write the function definition:

```python
def search_baidu(source: CommandSource, ai_prefix: str, query: str):
```

In the code above, the `source` and `ai_prefix` parameters **must** be included because they are always passed in.

Then write the function body:

```python
def search_baidu(source: CommandSource, ai_prefix: str, query: str):
    ...
    return ...
```

The function body can contain any operations you need. Just remember to always `return` a result — otherwise the AI won't be able to process the output properly.

Complete `tools.py` example:

```python
import requests
from games_ai.games_ai_tool import register_tool

@register_tool(
    description="Use Baidu to search for information on the internet. Use this tool when you need real-time info, news, encyclopedia knowledge, etc.",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The keyword or question to search for on Baidu"
            }
        },
        "required": ["query"]
    }
)
def search_baidu(source, ai_prefix: str, query: str):
    source.reply(f'{ai_prefix}Searching Baidu: {query}...')

    try:
        url = "https://www.baidu.com/s"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, params={"wd": query}, headers=headers, timeout=10)

        if response.status_code != 200:
            return f"Baidu search failed, HTTP status code: {response.status_code}"

        # Extract plain text from page (strip HTML tags)
        import re
        text = response.text
        # Remove script and style tag contents
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        # Collapse extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        # Truncate long content (keep first 3000 characters, suitable for AI context)
        max_len = 3000
        if len(text) > max_len:
            text = text[:max_len] + "\n...(content truncated)"

        return f"Baidu search results for 「{query}」:\n{text}"

    except requests.Timeout:
        return "Baidu search request timed out. Please try again later."
    except Exception as e:
        return f"Baidu search error: {str(e)}"
```

</details>

## What's New

### Version 0.5.10

#### 1. `extra_body` — Generic API Parameter Configuration (BREAKING)

The previous `thinking` boolean configuration option has been replaced with a generic `extra_body` dictionary. Please refer to your API provider's documentation for available options.

> [!WARNING]
> **Breaking Change**: If you were using `"thinking": true`, you must now migrate as shown below:
> 
> ```json
> // Before (0.5.9)
> { "thinking": true }
> 
> // After (0.5.10) — for DeepSeek users
> { "extra_body": { "thinking": { "type": "enabled" } } }
> ```
> 
> For other API providers, consult their documentation for the correct `extra_body` format.

### Version 0.5.9

#### 1. System Message Refactoring

The system prompt sent to the AI has been restructured into **four independent messages**:

1. **Current time & language** — the current server time and MCDR language setting
2. **AI prompt** — the model-specific system prompt configured in `all_ai`
3. **Registered skills** — the list of currently registered skills (including built-in ones)
4. **Database content** — the current public database data

This separation improves compatibility with models that have strict requirements on system message formatting (e.g., DeepSeek), and makes the prompt structure cleaner and more maintainable.

#### 2. New `ai_read_all_data` Tool

A new built-in tool `ai_read_all_data` has been added, allowing the AI to read all key-value pairs from the public database in a single call. Previously, the AI had to first call `ai_read_all_keys` to get all keys, then call `ai_read_data` for each key — now it can retrieve everything at once.

#### 3. Real-Time Database Injection

The current public database content is now automatically injected into the system message on every `!!ask` request. This means the AI always has up-to-date knowledge of the database without needing to call any tools first, improving response quality for data-related queries.

#### 4. Thinking Message Style

The "Thinking..." status message now uses Minecraft gray formatting (`§7...§r`), making it visually distinct from the AI's actual response.

#### 5. Bug Fixes & Stability

- Fixed `ai_read_all_data` returning a non-string value (`list[tuple]`) that caused HTTP 400 errors on DeepSeek and other strict API implementations. Tool call results now always return properly formatted strings.

## Acknowledgements & Disclaimer

Special thanks to the Wanghai Commune server for providing the foundation for testing this plugin.

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
| [GamesAI-v0.5.10.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.10) | 0.5.10 | 2026/07/22 07:03:08 | 52.39KB | 10 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.10/GamesAI-v0.5.10.mcdr) |
| [GamesAI-v0.5.9.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.9) | 0.5.9 | 2026/07/22 06:14:53 | 53.52KB | 2 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.9/GamesAI-v0.5.9.mcdr) |
| [GamesAI-v0.5.8.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.8) | 0.5.8 | 2026/07/21 03:22:17 | 51.09KB | 11 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.8/GamesAI-v0.5.8.mcdr) |
| [GamesAI-v0.5.7.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.7) | 0.5.7 | 2026/07/19 03:45:10 | 50.45KB | 15 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.7/GamesAI-v0.5.7.mcdr) |
| [GamesAI-v0.5.6.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.6) | 0.5.6 | 2026/07/14 11:32:49 | 54.39KB | 16 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.6/GamesAI-v0.5.6.mcdr) |
| [GamesAI-v0.5.5.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.5) | 0.5.5 | 2026/07/08 11:08:15 | 51.89KB | 18 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.5/GamesAI-v0.5.5.mcdr) |
| [GamesAI-v0.5.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.4) | 0.5.4 | 2026/06/05 16:23:44 | 43.34KB | 48 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.4/GamesAI-v0.5.4.mcdr) |
| [GamesAI-v0.5.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.3) | 0.5.3 | 2026/05/24 08:27:26 | 41.59KB | 35 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.3/GamesAI-v0.5.3.mcdr) |
| [GamesAI-v0.5.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.2) | 0.5.2 | 2026/05/24 03:31:00 | 39.75KB | 30 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.2/GamesAI-v0.5.2.mcdr) |
| [GamesAI-v0.5.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.1) | 0.5.1 | 2026/05/16 14:33:47 | 37.42KB | 46 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.1/GamesAI-v0.5.1.mcdr) |
| [GamesAI-v0.5.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.0) | 0.5.0 | 2026/05/10 06:56:40 | 35.83KB | 42 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.0/GamesAI-v0.5.0.mcdr) |
| [GamesAI-v0.4.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.2) | 0.4.2 | 2026/05/02 14:47:09 | 23.1KB | 52 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.2/GamesAI-v0.4.2.mcdr) |
| [GamesAI-v0.4.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.1) | 0.4.1 | 2026/05/01 12:03:32 | 20.61KB | 51 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.1/GamesAI-v0.4.1.mcdr) |
| [GamesAI-v0.4.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.0) | 0.4.0 | 2026/04/26 05:25:45 | 20.0KB | 53 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.0/GamesAI-v0.4.0.mcdr) |
| [GamesAI-v0.3.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.2) | 0.3.2 | 2026/04/18 01:20:54 | 17.06KB | 69 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.2/GamesAI-v0.3.2.mcdr) |
| [GamesAI-v0.3.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.1) | 0.3.1 | 2026/04/12 06:15:12 | 14.82KB | 52 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.1/GamesAI-v0.3.1.mcdr) |
| [GamesAI-v0.3.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.0) | 0.3.0 | 2026/04/11 14:21:17 | 11.37KB | 49 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.0/GamesAI-v0.3.0.mcdr) |
| [GamesAI-v0.2.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.1) | 0.2.1 | 2026/04/04 04:27:04 | 8.45KB | 57 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.1/GamesAI-v0.2.1.mcdr) |
| [Game.sAI-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.0) | 0.2.0 | 2026/03/29 03:10:14 | 3.49KB | 61 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.0/Game.sAI-v0.2.0.mcdr) |

