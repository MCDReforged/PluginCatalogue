**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## games_ai

### Basic Information

- Plugin ID: `games_ai`
- Plugin Name: GamesAI
- Version: 0.5.1
  - Metadata version: 0.5.1
  - Release version: 0.5.1
- Total downloads: 167
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

# GamesAI

English  |  [简体中文](https://github.com/PengZixuan30/Games_AI/tree/main//README.zh-CN.md)  |  [繁體中文](https://github.com/PengZixuan30/Games_AI/tree/main//README.zh-TW.md)

[Report an Issue](https://github.com/PengZixuan30/Games_AI/issues/new)  |  [Share an Idea](https://github.com/PengZixuan30/Games_AI/discussions/new/choose)

</div>

> [!NOTE]
> Welcome to version 0.5.1! This release introduces the prompt file feature — you can use `> xxx.md` in the `prompt` field of AI config to point to a prompt file. See [Configuration](#4all_ai). It also adds automatic error code detection and fixes some issues. See [What's New](#whats-new)

> [!IMPORTANT]
> Version 0.5.0 introduced custom tool support and created a `tools.py` file in the config folder. See [Custom Tools](#custom-tools). This version introduces the prompt file feature and creates a `prompt` folder in the config folder. See [Configuration](#4all_ai)

<details>
<summary>Table of Contents (click to expand)</summary>

- [GamesAI](#gamesai)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
    - [1.prefix](#1prefix)
    - [2.permission](#2permission)
    - [3.max\_history](#3max_history)
    - [4.all\_ai](#4all_ai)
    - [5.default\_ai](#5default_ai)
  - [Tools \& Custom Tools](#tools--custom-tools)
    - [Tools](#tools)
    - [Custom Tools](#custom-tools)
  - [What's New](#whats-new)
    - [1. Prompt File Support](#1-prompt-file-support)
    - [2. Automatic Error Code Detection](#2-automatic-error-code-detection)
  - [Acknowledgements \& Disclaimer](#acknowledgements--disclaimer)
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

<details>
<summary>

All `!!gamesai` Commands (click to expand)</summary>

| Command              | Description                                                                        |
| -------------------- | ---------------------------------------------------------------------------------- |
| `!!gamesai clear`    | Clear your own chat history. Chat history is unrelated to the public database.     |
| `!!gamesai clearall` | Clear all players' chat history. Chat history is unrelated to the public database. |
| `!!gamesai reload`   | Reload the plugin configuration file.                                              |
| `!!gamesai check`    | Check for plugin updates.                                                          |

</details>

---

You can also use `!!ask` directly to ask the AI questions, chat, or ask it to do things for you.

<details>
<summary>

All `!!ask` Commands (click to expand)</summary>

| Command                      | Description                                                                                                                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!ask <content>`            | Ask the AI a question, chat, or ask it to do something. `<content>` is what you want the AI to do or the question you want to ask.                                                                                          |
| `!!ask -m <model> <content>` | Use a specific model to ask the AI a question, chat, or ask it to do something. `<model>` is the AI_ID or nickname of the model you want to use. `<content>` is what you want the AI to do or the question you want to ask. |

</details>

---

Type `!!data` for information about database commands.

> [!TIP]
> The database is automatically created when upgrading to version 0.3.0 or above.

<details>
<summary>

All `!!data` Commands (click to expand)</summary>

| Command                      | Description                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| `!!data write <key> <value>` | Add a data entry to the public database. `<key>` must not contain spaces; `<value>` can be any string. |
| `!!data add <key> <value>`   | Append `<value>` to an existing key in the public database. Creates a new key if it does not exist.    |
| `!!data del <key>`           | Delete a data entry from the public database, regardless of whether the key exists.                    |
| `!!data read <key>`          | Read the value associated with a key from the public database.                                         |
| `!!data list`                | Read all entries in the public database.                                                               |
| `!!data list keys`           | Read all keys in the public database.                                                                  |

</details>

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
          "thinking": false
      }
    },
  "default_ai": "<Your AI ID>"
  }
```

---

Below is a brief introduction to each parameter:

<details>

<summary>Click to expand</summary>

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

The maximum number of conversation turns retained per player. Unrelated to the public database.

### 4.all_ai
Type: `dict`

Default: see file

All AI configuration entries, consisting of multiple sub-dictionaries. Each sub-dictionary represents one AI model, and its key serves as the plugin's internal AI_ID.

**prompt**: Use this option to write a system prompt for each AI. Use `> xxx.md` to point the prompt to the `config/games_ai/prompt/xxx.md` file (any file type is supported).

**ai_name**: Similar to `prefix`, but set per model. May include Minecraft formatting codes.

**base_url**, **ai_model**, **api_key**: Same as previous related configuration, but now set per model.

**thinking**: Enable or disable the model's thinking/reasoning mode. Defaults to `false` when omitted. Do not enable this for models that do not support a thinking mode — it may cause errors.

### 5.default_ai
Type: `str`

Default: `<Your AI ID>`

The model used when a player simply uses `!!ask`. Should be one of the keys in the `all_ai` dictionary (i.e. the plugin's internal AI_ID). An incorrect value will prevent `!!ask` from working properly.

</details>

## Tools & Custom Tools

### Tools
The GamesAI plugin provides many built-in tools, listed in the table below. If you want more tools, you can [submit a suggestion](https://github.com/PengZixuan30/Games_AI/issues/new) or use [Custom Tools](#custom-tools).

<details>
<summary>Click to view all built-in tools</summary>

|        Tool ID        |          Parameters          | Description                                                                                                                                                                                                                                                    |
| :-------------------: | :--------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  get_online_players   |             None             | Get the list of currently online players. Depends on the `online_player_api` plugin; automatically disabled if unavailable.                                                                                                                                    |
|  get_whitelist_name   |             None             | Get the complete server whitelist. Depends on the `whitelist_api` plugin; automatically disabled if unavailable.                                                                                                                                               |
|   add_to_whitelist    |            `name`            | Add a player to the whitelist. Depends on the `whitelist_api` plugin; automatically disabled if unavailable.                                                                                                                                                   |
| remove_from_whitelist |            `name`            | Remove a player from the whitelist. Depends on the `whitelist_api` plugin; automatically disabled if unavailable.                                                                                                                                              |
| search_minecraft_wiki |           `query`            | Let the AI search the Minecraft Wiki for more accurate answers.                                                                                                                                                                                                |
|      calculator       |         `expression`         | A simple mathematical expression calculator.                                                                                                                                                                                                                   |
|    item_caculator     | `expression`, `single_limit` | A mathematical expression calculator that converts results into Minecraft item notation (shulker boxes, stacks, items). Automatically adapts to stack size; defaults to 64 if not specified.                                                                   |
|      add_pos_pos      |  `name`, `pos`, `dimension`  | Add a waypoint at a specified location. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                                                                 |
|     add_pos_here      |            `name`            | Add a waypoint at the player's current location. Automatically disabled when executed from the console. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available. |
|      remove_pos       |            `name`            | Delete a waypoint. The `where2go` version automatically converts names to IDs. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                          |
|      search_pos       |            `name`            | Search for a waypoint. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                                                                                  |
|      get_all_pos      |             None             | Get a list of all waypoints. Depends on the `where2go` or `location_marker` plugin; prioritizes `where2go` when both are present; automatically disabled when neither is available.                                                                            |
|     ai_read_data      |            `key`             | Read a single entry from the database.                                                                                                                                                                                                                         |
|   ai_read_all_keys    |             None             | Get all keys from the database.                                                                                                                                                                                                                                |
|     ai_write_data     |        `key`, `value`        | Write a data entry to the database (overwrite mode).                                                                                                                                                                                                           |
|      ai_add_data      |        `key`, `value`        | Write a data entry to the database (append mode).                                                                                                                                                                                                              |
|      ai_del_data      |            `key`             | Delete a data entry from the database.                                                                                                                                                                                                                         |

</details>

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

### 1. Prompt File Support
You can now point AI prompts to external files. Use `> xxx.md` in the `prompt` field to reference the `config/games_ai/prompt/xxx.md` file.

### 2. Automatic Error Code Detection
When an error occurs while accessing the AI, the error code and cause are now automatically identified and displayed.

---

Additionally, this release fixes several issues.

## Acknowledgements & Disclaimer

Special thanks to the Wanghai Commune server for providing the foundation for testing this plugin.

All content generated by AI (LLM) models is unrelated to this plugin.

All consequences arising from custom tools are unrelated to this plugin.

## License

MIT License, Copyright (c) 2026 yello

<div align = "center">

---

[Back to Top](#gamesai)

</div>

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [GamesAI-v0.5.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.1) | 0.5.1 | 2026/05/16 14:33:47 | 37.42KB | 7 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.1/GamesAI-v0.5.1.mcdr) |
| [GamesAI-v0.5.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.0) | 0.5.0 | 2026/05/10 06:56:40 | 35.83KB | 6 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.0/GamesAI-v0.5.0.mcdr) |
| [GamesAI-v0.4.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.2) | 0.4.2 | 2026/05/02 14:47:09 | 23.1KB | 15 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.2/GamesAI-v0.4.2.mcdr) |
| [GamesAI-v0.4.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.1) | 0.4.1 | 2026/05/01 12:03:32 | 20.61KB | 14 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.1/GamesAI-v0.4.1.mcdr) |
| [GamesAI-v0.4.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.0) | 0.4.0 | 2026/04/26 05:25:45 | 20.0KB | 18 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.0/GamesAI-v0.4.0.mcdr) |
| [GamesAI-v0.3.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.2) | 0.3.2 | 2026/04/18 01:20:54 | 17.06KB | 31 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.2/GamesAI-v0.3.2.mcdr) |
| [GamesAI-v0.3.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.1) | 0.3.1 | 2026/04/12 06:15:12 | 14.82KB | 12 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.1/GamesAI-v0.3.1.mcdr) |
| [GamesAI-v0.3.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.0) | 0.3.0 | 2026/04/11 14:21:17 | 11.37KB | 16 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.0/GamesAI-v0.3.0.mcdr) |
| [GamesAI-v0.2.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.1) | 0.2.1 | 2026/04/04 04:27:04 | 8.45KB | 22 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.1/GamesAI-v0.2.1.mcdr) |
| [Game.sAI-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.0) | 0.2.0 | 2026/03/29 03:10:14 | 3.49KB | 26 | [Download](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.0/Game.sAI-v0.2.0.mcdr) |

