**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## uuid_api_remake

### Basic Information

- Plugin ID: `uuid_api_remake`
- Plugin Name: UUID API Remake
- Version: 1.1.0
  - Metadata version: 1.1.0
  - Release version: 1.1.0
- Total downloads: 53
- Authors: [gubai](https://github.com/gubaiovo)
- Repository: https://github.com/gubaiovo/MCDR_uuid_api_remake
- Repository plugin page: https://github.com/gubaiovo/MCDR_uuid_api_remake/tree/main/uuid_api_remake
- Labels: [`API`](/labels/api/readme.md), [`Tool`](/labels/tool/readme.md)
- Description: Get UUID of players

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install mcdreforged requests
```

### Introduction

# UUID API REMAKE
This plugin is a remade version of the UUID API. [Original UUID API link: https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/uuid_api)

This plugin utilizes all code from the original API for obtaining UUIDs in **premium/offline** servers.

### Additional Features in the Remake:

1. Added more commands for easier UUID management.
2. All obtained UUIDs are stored and centrally managed in the `uuid.json` data file.
3. Added the `get_name(uuid)` function to retrieve player names from UUIDs (sourced from `uuid.json` and `usercache.json`).

### UUID Retrieval Workflow (proceeds to next step if failed):

1. Read the plugin data file `uuid.json`.
2. Read `usercache.json`. If successful, store results in `uuid.json`.
3. Call the original API. If successful, store results in `uuid.json`.
4. Generate a pseudo-UUID using the SHA-256 hash of `playername + timestamp`, take the first 50 bits, and store it in `uuid.json`.

### Configuration

```json
{
    "mojang_online_mode": true,
    "online_api": "https://api.mojang.com/users/profiles/minecraft/",
    "use_offline_api": true,
    "offline_api": "http://tools.glowingmines.eu/convertor/nick/"
}
```
**mojang_online_mode**: Indicates whether the server is an official (authenticated) server. When set to true, it uses the official Mojang API to obtain UUIDs

**online_api**: The endpoint URL for the official authentication API. Defaults to `https://api.mojang.com/users/profiles/minecraft/`

**use_offline_api**: Determines whether to use offline API for UUID retrieval. This setting becomes active only when mojang_online_mode is set to false. Defaults to true

**offline_api**: Offline API URL, defaults to `http://tools.glowingmines.eu/convertor/nick/`

**Note**: Ensure these four configuration items remain complete in the file. If using custom APIs, please remember to include the trailing `/`

### Commands

Except for `!!uar` and `!!uar help`, all other commands can only be used in the **console**.

For detailed usage, run `!!uar` or `!!uar help`.

### API Usage

**Obtain UUID from player name:**

```python
import uuid_api_remake

name = ... # str
uuid = uuid_api_remake.get_uuid(name)
print(uuid)
```

**Obtain player name from UUID (sourced from `uuid.json` and `usercache.json`):**

```python
import uuid_api_remake

uuid = ... # str
name = uuid_api_remake.get_name(uuid)
print(name)
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v1.1.0) | 1.1.0 | 2025/03/14 08:24:12 | 9.8KB | 43 | [Download](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v1.1.0/uuid_api_remake.mcdr) |
| [uuid_api_remake.mcdr](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/tag/v1.0.0) | 1.0.0 | 2025/03/13 13:12:08 | 9.38KB | 10 | [Download](https://github.com/gubaiovo/MCDR_uuid_api_remake/releases/download/v1.0.0/uuid_api_remake.mcdr) |

