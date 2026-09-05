**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## batch_bot_spawn

### Basic Information

- Plugin ID: `batch_bot_spawn`
- Plugin Name: BatchBotSpawn
- Version: 0.2.0
  - Metadata version: 0.2.0
  - Release version: 0.2.0
- Total downloads: 31
- Authors: [oneIdler](https://github.com/oneIdler)
- Repository: https://github.com/SDK-Minecraft-Server/BatchBotSpawn
- Repository plugin page: https://github.com/SDK-Minecraft-Server/BatchBotSpawn/tree/release
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: A plugin for batch managing Carpet fake players

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.0.0 |

```
pip install "mcdreforged>=2.0.0"
```

### Introduction

# BatchBotSpawn

English | [简体中文](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/tree/release/README.md)

A MCDR plugin for **batch managing Carpet fake players**, with customizable name prefix/suffix, online status detection, command throttling and spawn result verification, making it fast and convenient to spawn bots, drop items and kick bots offline.

---

## 💡 Inspiration

This project is inspired by [Walkersifolia/FastBotSpawn](https://github.com/Walkersifolia/FastBotSpawn).

---

## ✨ Features

- **Batch spawn**: spawn bots by an index range, with customizable name prefix and suffix.
- **Smart skip**: automatically detects and skips bots that are already online.
- **Command throttling**: batch commands are sent one by one with a configurable interval to avoid flooding the server command queue.
- **Result verification**: optionally waits and reports how many bots actually came online after spawning.
- **Offline skip**: `drop` / `kill` only target online bots to avoid server errors.
- **Flexible config**: set the max bot count per operation, default count, send interval, etc., persisted to disk.
- **Online list**: `!!b list` shows online bots matching the current naming rule; click to fill in the kill command.
- **Multi-language**: built-in Chinese (zh_CN) and English (en_US) command interface.

---

## 📦 Dependencies

- **MCDR** ≥ 2.0.0
- **Carpet Mod** (installed on the server, provides the `/player` command)
- **minecraft_data_api** (optional but recommended. When installed, the online player list is queried accurately via `/list`; otherwise the plugin tracks players through MCDR join/leave events, and players already online before the server starts may not be recognized)

---

## 🚀 Installation

1. Put the plugin folder into the MCDR `plugins` directory.
2. It is recommended to install `minecraft_data_api` as well.
3. Restart MCDR or run `!!MCDR reload plg` to load the plugin.

---

## 🔧 Commands

All commands start with `!!b` and are player-only (console is not supported). `pre / suf / limit / def_num / clear` are config commands and require **admin** permission or above.

| Command                        | Description                                       | Example               |
| ------------------------------ | ------------------------------------------------- | --------------------- |
| `!!b pre <prefix>`             | Set bot name prefix (keep consistent with Carpet) | `!!b pre bot_`        |
| `!!b suf <suffix>`             | Set bot name suffix (keep consistent with Carpet) | `!!b suf _fake`       |
| `!!b limit <number>`           | Set max bot count per operation                   | `!!b limit 20`        |
| `!!b def_num <number>`         | Set default spawn count (must be ≤ limit)         | `!!b def_num 5`       |
| `!!b clear`                    | Clear prefix and suffix settings                  | `!!b clear`           |
| `!!b spawn [name] [min] [max]` | Spawn bots in batch (default 1~def_num)           | `!!b spawn test 1 10` |
| `!!b drop [name] [min] [max]`  | Make bots drop all items (default 1~def_num)      | `!!b drop test 1 5`   |
| `!!b kill [name] [min] [max]`  | Kick bots offline (default 1~def_num)             | `!!b kill test 1 5`   |
| `!!b list [name]`              | List online bots matching the naming rule         | `!!b list test`       |

> **Argument notes**:
> - `[name]`, `[min]` and `[max]` are all optional, combined as follows:
>   - No arguments: operates on the default range `1~def_num`;
>   - 1 number: operates on that single index;
>   - 2 numbers: operates on that index range;
>   - With `name` placed first: 1 number = a single index for that name, 2 numbers = an index range for that name.
> - `[name]` must be 1-16 letters, digits or underscores, and the final bot name (`prefix + name/index + suffix`) must not exceed 16 characters.

---

## ⚙️ Configuration

The config file is located at `config/batch_bot_spawn/config.json` (auto-generated on first run, also editable via in-game commands).

```json
{
  "prefix": "bot_",
  "suffix": "",
  "limit": 10,
  "def_num": 10,
  "interval": 0.05,
  "verify": true,
  "verify_delay": 2.0
}
```

| Key            | Default | Description                                                 |
| -------------- | ------- | ----------------------------------------------------------- |
| `prefix`       | `""`    | Bot name prefix                                             |
| `suffix`       | `""`    | Bot name suffix                                             |
| `limit`        | `10`    | Max bot count per operation (shared by spawn/drop/kill)     |
| `def_num`      | `10`    | Default spawn count, clamped to `limit` on load             |
| `interval`     | `0.05`  | Interval in seconds between commands, 0 disables throttling |
| `verify`       | `true`  | Whether to verify the actual online count after spawn       |
| `verify_delay` | `2.0`   | Seconds to wait before verification                         |

> Tip: `prefix` / `suffix` must match the actual names used by Carpet's `player` command, otherwise `list` cannot match correctly.

---

## 🧪 Development & Testing

Run the unit tests (requires a Python environment with MCDR installed):

```bash
python -m unittest discover -s tests -v
```

Build the release package:

```bash
python -m mcdreforged pack -i . -o releases
```

---

## 📄 License

This project is open-sourced under the [MIT License](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/tree/release/LICENSE).

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [BatchBotSpawn-v0.2.0.mcdr](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/releases/tag/v0.2.0) | 0.2.0 | 2026/08/01 12:09:33 | 9.17KB | 31 | [Download](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/releases/download/v0.2.0/BatchBotSpawn-v0.2.0.mcdr) |

