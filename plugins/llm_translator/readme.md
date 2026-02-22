**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## llm_translator

### Basic Information

- Plugin ID: `llm_translator`
- Plugin Name: LLM_Translator
- Version: 1.4.0
  - Metadata version: 1.4.0
  - Release version: 1.4.0
- Total downloads: 52
- Authors: [HeTao_yz](https://github.com/HeTao-yz)
- Repository: https://github.com/HeTao-yz/llm-translator
- Repository plugin page: https://github.com/HeTao-yz/llm-translator/tree/main
- Labels: [`Tool`](/labels/tool/readme.md), [`Information`](/labels/information/readme.md)
- Description: 在游戏内使用大语言模型进行翻译。支持翻译玩家对话，游戏内木牌文字，讲台上的书籍内容。

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | \>=1.4.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged ](https://pypi.org/project/mcdreforged ) | \>= 2.0.0 |
| [openai](https://pypi.org/project/openai) |  |
| [nbtlib](https://pypi.org/project/nbtlib) |  |

```
pip install "mcdreforged >= 2.0.0" openai nbtlib
```

### Introduction

# LLM-Translator

> The development inspiration for this plugin comes from the MCDR plugin [SimpleTranslator - Plugin Repository - MCDReforged](https://mcdreforged.com/zh-CN/plugin/simple_translator)

Uses Large Language Models to provide in-game translation for player chat messages, sign text, and book content.
The plugin uses the `deepseek-chat` large language model for translation by default.

## Introduction

When players speak different languages on the server, this plugin can significantly improve communication. Supports synchronized forwarding of translated player chat messages across multiple servers. Using LLM translation offers higher accuracy and better adaptability compared to traditional machine translation.
Supports translating the following in-game:

- Player chat messages
- Text on Signs
- Book content on Lecterns

## Configuration

1. After the plugin is successfully loaded for the first time, a configuration file will be generated in the `/config/llm-translator/` folder.

2. The configuration file uses the `deepseek-chat` model for Chinese-English translation by default. If this meets your needs, simply enter your API key in the `api_key` field. Otherwise, please modify the configuration file as described below.

   ```json
   {
   "first_language": "zh_cn",
   "secondary_language": "en_us",
   "base_url": "https://api.deepseek.com",
   "model": "deepseek-chat",
   "api_key": "enter-your-api-key",
   "is_proxy_to_other_servers": false,
   "proxy_servers": [
       {
           "address": "127.0.0.1",
           "port": 25575,
           "password": ""
       },
       {
           "address": "127.0.0.1",
           "port": 25576,
           "password": ""
       }
   ]
   }
   ```

| Field Name                    | Data Type  | Default Value                | Description                                                         |
| ----------------------------- | ---------- | ---------------------------- | ------------------------------------------------------------------- |
| **first_language**            | string     | `"zh_cn"`                    | The primary language, usually the user's native or main language.   |
| **secondary_language**        | string     | `"en_us"`                    | The secondary language, the target language for translation.        |
| **base_url**                  | string     | `"https://api.deepseek.com"` | The base request URL for the API.                                   |
| **model**                     | string     | `"deepseek-chat"`            | The name of the language model to use.                              |
| **api_key**                   | string     | *No default*                 | The API access key.                                                 |
| **is_proxy_to_other_servers** | boolean    | `false`                      | Whether to forward translated chat messages to other servers.       |
| **proxy_servers**             | list[dict] | `[]`                         | List of target server configurations for forwarding. Requires RCON. |

**proxy_servers** RCON server configuration:

| Field Name   | Data Type | Default Value | Description                                            |
| ------------ | --------- | ------------- | ------------------------------------------------------ |
| **address**  | string    | `"127.0.0.1"` | The address of the target server.                      |
| **port**     | int       | *No default*  | The RCON port of the target server.                    |
| **password** | string    | `""`          | The RCON password for the target server (if required). |

### Configuration Notes

1. **Basic Setup**: Just fill in the `api_key` to use the default DeepSeek model for Chinese-English player chat translation.

2. **Other Language Pairs**: Modify `first_language` and `secondary_language` to support other language pairs.

3. **Multiple Model Support**: Change `base_url` and `model` to switch to other LLM providers.

4. **Chat Message Forwarding**: To forward translated player messages to other servers (typically used in setups like Velocity with multiple backend servers and pre-configured chat forwarding), set `is_proxy_to_other_servers` to `true` and configure the `proxy_servers` list.

## Usage

### Player Chat Translation

In the game chat, prefix your message with **`t` and a space** to translate it.

<img width="643" height="125" alt="image" src="https://github.com/user-attachments/assets/da3c74f2-e252-46b2-a826-114a121a9565" />

### Sign and Book Translation

*Book Content: The book must be placed on a Lectern to be translated.*

Use the command `!!tr <x> <y> <z>` to translate (the parameters <x> <y> <z> are the coordinates of the sign or the book on a lectern; you can use ~ to represent the current player's coordinates).

<img width="1754" height="978" alt="image" src="https://github.com/user-attachments/assets/927ded2c-4a81-4ec5-9912-1f06d806bc6e" /><img width="484" height="443" alt="image" src="https://github.com/user-attachments/assets/71e7b327-8e3c-4be4-98d2-d0e5a208bebd" /> <img width="1683" height="1375" alt="image" src="https://github.com/user-attachments/assets/419d5613-b0f6-4cd4-880e-2e3f3e065b30" />

## Other

This is my first time developing a plugin, so there might be imperfections or areas for improvement. If you encounter bugs or have suggestions while using it, please feel free to submit an Issue on the plugin's Github repository.


### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [LLM_Translator_v1.4.0.mcdr](https://github.com/HeTao-yz/llm-translator/releases/tag/v1.4.0) | 1.4.0 | 2025/12/09 15:29:28 | 9.5KB | 22 | [Download](https://github.com/HeTao-yz/llm-translator/releases/download/v1.4.0/LLM_Translator_v1.4.0.mcdr) |
| [LLM_Translator_v1.3.1.mcdr](https://github.com/HeTao-yz/llm-translator/releases/tag/v1.3.1) | 1.3.1 | 2025/11/27 05:42:59 | 7.09KB | 15 | [Download](https://github.com/HeTao-yz/llm-translator/releases/download/v1.3.1/LLM_Translator_v1.3.1.mcdr) |
| [llm-translator-v1.0.0.mcdr](https://github.com/HeTao-yz/llm-translator/releases/tag/v1.0.0) | 1.0.0 | 2025/11/24 15:00:48 | 5.63KB | 15 | [Download](https://github.com/HeTao-yz/llm-translator/releases/download/v1.0.0/llm-translator-v1.0.0.mcdr) |

