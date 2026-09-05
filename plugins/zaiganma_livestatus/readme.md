**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## zaiganma_livestatus

### Basic Information

- Plugin ID: `zaiganma_livestatus`
- Plugin Name: ZaiGanMa (LiveStatus)
- Version: 1.1.1
  - Metadata version: 1.1.1
  - Release version: 1.1.1
- Total downloads: 67
- Authors: [man8in](https://github.com/man8in)
- Repository: https://github.com/man8in/zaiganma-livestatus
- Repository plugin page: https://github.com/man8in/zaiganma-livestatus/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Allows players to set their own status tags and display them in the chat box and TAB list

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | \>=1.6.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

<div align="center">

# ZaiGanMa (LiveStatus) for MCDReforged

[简体中文](https://github.com/man8in/zaiganma-livestatus/tree/main//README.zh-CN.md)  |  [繁體中文](https://github.com/man8in/zaiganma-livestatus/tree/main//README.zh-TW.md)

[Report an Issue](https://github.com/man8in/zaiganma-livestatus/issues)  |  [Share an Idea](https://github.com/man8in/zaiganma-livestatus/discussions)

</div>

> [!NOTE]
> **ZaiGanMa (LiveStatus)** is a lightweight MCDR plugin that allows players to set their own status tags and display them in the chat box and TAB list. Based on Minecraft's native Team mechanism.

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [HTTP API](#-http-api)
- [Configuration](#configuration)
- [Supported Colors](#supported-colors)
- [License](#license)

## ✨ Features

- ✅ Set/clear manual status (`!!zgm set / clear`)
- ✅ Set status color (`!!zgm color`)
- ✅ **Preset status** - visible offline, auto-apply on join (`!!zgm preset / pending / cancel_pending`)
- ✅ Query any player's status (**supports offline players**) (`!!zgm <player>`)
- ✅ **Status history** with privacy control (`!!zgm history`)
- ✅ Status library management (`!!zgm lib`)
- ✅ Random status suggestion (`!!zgm suggest`)
- ✅ **HTTP API** for external program integration
- ✅ Auto-detect bots (`bot_` prefix)
- ✅ Admin config panel (`!!zgm config`)

## Installation

Run the following command in the MCDR console:

```
!!MCDR plugin install zaiganma_livestatus
```

Alternatively, download the `.mcdr` file from the [Releases page](https://github.com/man8in/zaiganma-livestatus/releases) and place it in your `plugins` folder.

## Dependencies

| Dependency         | Version  | Required   |
| ------------------ | -------- | ---------- |
| MCDR               | >= 2.0.0 | ✅ Yes      |
| minecraft_data_api | >= 1.6.0 | ✅ Yes      |
| uuid_api           | >= 1.0.0 | ❌ Optional |

> [!TIP]
> `uuid_api` is optional. If installed, it improves offline-player UUID resolution; the plugin degrades gracefully without it.

## Usage

| Command                              | Description                                         |
| ------------------------------------ | --------------------------------------------------- |
| `!!zgm`                              | View your own status                                |
| `!!zgm <player>`                     | View another player's status (**supports offline**) |
| `!!zgm set <text>`                   | Set your status                                     |
| `!!zgm clear`                        | Clear your status                                   |
| `!!zgm color <color>`                | Set status color                                    |
| `!!zgm clib`                         | View available colors                               |
| `!!zgm preset <text>`                | Set preset status (auto-apply on next join)         |
| `!!zgm pending`                      | Check your preset status                            |
| `!!zgm cancel_pending`               | Cancel your preset status                           |
| `!!zgm history [player]`             | View status history (self if empty)                 |
| `!!zgm history privacy <true/false>` | Set history privacy                                 |
| `!!zgm lib`                          | View status library (click to use)                  |
| `!!zgm lib add <text>`               | Add status to library                               |
| `!!zgm lib remove <text>`            | Remove status from library                          |
| `!!zgm lib reload`                   | Reload status library from file                     |
| `!!zgm lib reset`                    | Reset status library to default (admin only)        |
| `!!zgm suggest`                      | Get a random status suggestion                      |
| `!!zgm config`                       | View configuration panel (admin only)               |

> [!TIP]
> Click on any status in `!!zgm lib`, `!!zgm clib`, `!!zgm suggest`, or `!!zgm config` to automatically fill the command into your chat bar, then press Enter to confirm.

## 🔌 HTTP API

ZaiGanMa includes a built-in HTTP API server that allows external programs (such as QQ bots, web panels, mobile apps, etc.) to read and write player status via HTTP requests.

The API server starts automatically with the plugin — no extra setup required. When the plugin loads successfully, the MCDR log will show:

```
[ZaiGanMa] API 服务器已启动 http://0.0.0.0:8123
```

| Item          | Value                                |
| ------------- | ------------------------------------ |
| Base URL      | `http://<your-server-IP>:8123`       |
| GET endpoint  | `/api/status/get?uuid=<player-UUID>` |
| POST endpoint | `/api/status/set`                    |

> The listen address and port are controlled by `api_host` / `api_port` in the [Configuration](#configuration) section.

### 1️⃣ GET /api/status/get?uuid=<player-UUID>

Query the current status of a specified player.

Request example:

```bash
curl "http://127.0.0.1:8123/api/status/get?uuid=069a79f4-44e9-4726-a5be-fca90e38aaf5"
```

Success response:

```json
{
  "success": true,
  "data": {
    "name": "man8in",
    "status": "Mining",
    "color": "gold",
    "has_pending": false,
    "updated_at": 1723705800
  }
}
```

| Field       | Type    | Description                            |
| ----------- | ------- | -------------------------------------- |
| name        | string  | Player name                            |
| status      | string  | Current status text                    |
| color       | string  | Status color name                      |
| has_pending | boolean | Whether a pending preset status exists |
| updated_at  | integer | Status update timestamp                |

Failure response:

```json
{
  "success": false,
  "error": "Player not found"
}
```

### 2️⃣ POST /api/status/set

Set a player's status.

Request format:

```
POST http://<your-server-IP>:8123/api/status/set
Content-Type: application/json
```

Request parameters:

| Parameter | Type    | Required | Default | Description                                    |
| --------- | ------- | -------- | ------- | ---------------------------------------------- |
| uuid      | string  | ✅ Yes    | -       | Player UUID                                    |
| name      | string  | ✅ Yes    | -       | Player name                                    |
| status    | string  | ✅ Yes    | -       | Status text                                    |
| color     | string  | ❌ No     | white   | Color name                                     |
| pending   | boolean | ❌ No     | true    | true = preset status, false = immediate effect |

Request example (preset status):

```bash
curl -X POST http://127.0.0.1:8123/api/status/set \
  -H "Content-Type: application/json" \
  -d '{"uuid":"069a79f4-44e9-4726-a5be-fca90e38aaf5","name":"man8in","status":"Going to eat","color":"yellow","pending":true}'
```

Success response:

```json
{
  "success": true,
  "message": "Status set successfully",
  "pending": true
}
```

Request example (immediate effect):

```bash
curl -X POST http://127.0.0.1:8123/api/status/set \
  -H "Content-Type: application/json" \
  -d '{"uuid":"069a79f4-44e9-4726-a5be-fca90e38aaf5","name":"man8in","status":"Mining","color":"gold","pending":false}'
```

Failure response:

```json
{
  "success": false,
  "error": "Missing uuid"
}
```

### 🔒 Security Recommendations

> [!WARNING]
> The API has **no authentication by default**. If you expose it to the public network, configure security measures based on your actual needs.

**1. Restrict listen address**

If you only need local access (e.g., a QQ bot running on the same machine as MCDR), change `api_host` to `127.0.0.1` — only programs on the local machine can then access the API.

**2. Change the default port**

Avoid using the default port to reduce the risk of being scanned (e.g., `38123`).

**3. Firewall restrictions**

Use a firewall (e.g., iptables, ufw) to restrict access to specific IPs:

```bash
# Only allow 192.168.1.100 to access port 8123
ufw allow from 192.168.1.100 to any port 8123
```

**4. Add token authentication (advanced)**

For more advanced security control, add Token authentication in the API handler yourself. Add the following at the beginning of the `StatusAPIHandler` class:

```python
API_TOKEN = "your_secret_token_here"

def do_GET(self):
    token = self.headers.get('Authorization', '').replace('Bearer ', '')
    if token != self.API_TOKEN:
        self._send_json(401, {'error': 'Unauthorized'})
        return
    # ... original code
```

### 💻 Integration Examples

**Python (QQ bot):**

```python
import requests

API_BASE = "http://127.0.0.1:8123"

def get_player_status(uuid):
    resp = requests.get(f"{API_BASE}/api/status/get", params={"uuid": uuid})
    return resp.json()

def set_player_status(uuid, name, status, color="white", pending=True):
    resp = requests.post(f"{API_BASE}/api/status/set", json={
        "uuid": uuid,
        "name": name,
        "status": status,
        "color": color,
        "pending": pending
    })
    return resp.json()
```

**JavaScript (Node.js):**

```javascript
const axios = require('axios');

const API_BASE = 'http://127.0.0.1:8123';

async function getPlayerStatus(uuid) {
    const resp = await axios.get(`${API_BASE}/api/status/get`, { params: { uuid } });
    return resp.data;
}

async function setPlayerStatus(uuid, name, status, color = 'white', pending = true) {
    const resp = await axios.post(`${API_BASE}/api/status/set`, {
        uuid,
        name,
        status,
        color,
        pending
    });
    return resp.data;
}
```

### ❓ FAQ

**Q1: API request returns 404?**

Incorrect URL path or the API server is not running. Check that the MCDR log shows `[ZaiGanMa] API 服务器已启动 http://...` and that the request URL path is correct (case-sensitive).

**Q2: Returns `{"success": false, "error": "Player not found"}`?**

No player record for that UUID in the database. The player needs to have set a status at least once to have a record.

**Q3: How to get a player's UUID?**

- Use `!!zgm` in-game or query history (may be displayed depending on server configuration)
- Use the uuid_api plugin:

```python
uuid_api = server.get_plugin_instance('uuid_api')
uuid = uuid_api.get_uuid('man8in')
```

- Or query the database directly:

```bash
sqlite3 config/zaiganma_livestatus/zaigamma.db "SELECT uuid, name FROM player_status;"
```

**Q4: API didn't change after modifying config?**

Reload the plugin:

```
!!MCDR reload ZaiGanMa
```

**Q5: Can the API be accessed cross-origin?**

Yes. The API adds `Access-Control-Allow-Origin: *` to the response headers, supporting cross-origin requests.

## Configuration

The plugin generates config.json on first run:

| Key                      | Type    | Default | Description                                                             |
| ------------------------ | ------- | ------- | ----------------------------------------------------------------------- |
| show_status              | boolean | true    | Master switch for status display                                        |
| default_status           | string  | 在线      | Default status text                                                     |
| max_length               | integer | 8       | Max status text length                                                  |
| allow_color              | boolean | true    | Allow custom colors                                                     |
| manual_status_timeout    | integer | 180     | Manual status timeout (minutes, 0 = forever)                            |
| api_host                 | string  | 0.0.0.0 | HTTP API bind address                                                   |
| api_port                 | integer | 8123    | HTTP API port                                                           |
| library_entry_max_length | integer | 8       | Max status library entry length                                         |
| op_permission_level      | integer | 3       | Permission level for admin commands (config panel, library reset, etc.) |

## Supported Colors

black, dark_blue, dark_green, dark_aqua, dark_red, dark_purple, gold, gray, dark_gray, blue, green, aqua, red, light_purple, yellow, white

Also supports hex colors like `#FF6B6B`.

## License

MIT

## Author

man8in — [GitHub](https://github.com/man8in)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ZaiGanMa.LiveStatus.-v1.1.1.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.1.1) | 1.1.1 | 2026/08/29 06:08:22 | 14.11KB | 4 | [Download](https://github.com/man8in/zaiganma-livestatus/releases/download/1.1.1/ZaiGanMa.LiveStatus.-v1.1.1.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.1.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.1.0) | 1.1.0 | 2026/08/16 08:06:02 | 14.23KB | 16 | [Download](https://github.com/man8in/zaiganma-livestatus/releases/download/1.1.0/ZaiGanMa.LiveStatus.-v1.1.0.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.2.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.2) | 1.0.2 | 2026/08/06 07:32:13 | 8.7KB | 20 | [Download](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.2/ZaiGanMa.LiveStatus.-v1.0.2.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.1.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.1) | 1.0.1 | 2026/08/04 18:16:46 | 9.12KB | 13 | [Download](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.1/ZaiGanMa.LiveStatus.-v1.0.1.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.0) | 1.0.0 | 2026/08/04 06:41:52 | 7.73KB | 14 | [Download](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.0/ZaiGanMa.LiveStatus.-v1.0.0.mcdr) |

