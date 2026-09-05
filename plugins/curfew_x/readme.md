**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## curfew_x

### Basic Information

- Plugin ID: `curfew_x`
- Plugin Name: CurfewX
- Version: 0.1.2
  - Metadata version: 0.1.2
  - Release version: 0.1.2
- Total downloads: 34
- Authors: [River_tao](https://github.com/Rivertao1)
- Repository: https://github.com/Rivertao1/CurfewX
- Repository plugin page: https://github.com/Rivertao1/CurfewX/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Keep a Minecraft server offline during configurable curfew hours

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.7 \<3.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# CurfewX

[简体中文](https://github.com/Rivertao1/CurfewX/tree/main/README.md) | English

CurfewX is an MCDReforged plugin that keeps a Minecraft server offline during configurable curfew hours. It warns online players before curfew, gracefully stops the server, and starts it again when curfew ends. Only servers stopped by CurfewX are started automatically.

CurfewX targets MCDReforged 2.15.7 and uses only public MCDR server-control APIs. It requires no Forge mod and works with `forge_handler` as well as other correctly configured MCDR server handlers.

## Installation

1. Download the latest `CurfewX-v*.mcdr` from GitHub Releases.
2. Put it in the MCDR `plugins/` directory.
3. Run `!!MCDR reload plugin`, or restart MCDR.
4. On first load, CurfewX creates `config/curfew_x/config.yml` and `config/curfew_x/state.json`.

The default timezone is `Asia/Shanghai`, with curfew active every day from `00:00` to `08:00`.

## Configuration

Default configuration:

```yaml
timezone: Asia/Shanghai

schedule:
  every_day:
    - 00:00-08:00

reminders:
  minutes:
    - 60
    - 30
    - 10
    - 5
  seconds:
    - 30
    - 10
    - 9
    - 8
    - 7
    - 6
    - 5
    - 4
    - 3
    - 2
    - 1

shutdown:
  warning_after_seconds: 120
  warning_interval_seconds: 300
  force_kill_after_seconds: 3600

messages:
  prefix: "[CurfewX]"
  minutes_remaining: "距离服务器宵禁还有 {value} 分钟"
  seconds_remaining: "距离服务器宵禁还有 {value} 秒"
  shutdown_now: "宵禁开始，服务器正在关闭"
  colors:
    prefix: green
    countdown_text: yellow
    countdown_value: red
    shutdown_text: red
```

In-game broadcasts use MCDR structured text, so the prefix, countdown text, countdown value, and shutdown text can be colored independently. A color may be a standard Minecraft color name such as `green`, `yellow`, `red`, or `gold`, or a hexadecimal RGB value such as `#55FF55`. Countdown templates must keep the `{value}` placeholder, which uses the `countdown_value` color.

Schedules may also be configured per weekday, with multiple intervals per day and intervals that cross midnight:

```yaml
schedule:
  monday:
    - 00:00-08:00
  friday:
    - 00:00-08:00
    - 23:30-24:00
  saturday:
    - 00:00-09:00
```

Supported weekday keys are `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, and `sunday`. Intervals under `every_day` apply to every day and are merged with weekday-specific intervals. Remove `every_day` when every weekday should use independent rules.

Run `!!cfx reload` after editing the configuration. If validation fails, CurfewX keeps the currently active valid configuration and reports the error in both the command response and MCDR log.

## Commands and permissions

Every command requires MCDR `admin` permission level 3 or higher. The MCDR console has `owner` permission and remains available while the Minecraft server is offline.

| Command                  | Description                                                        |
| ------------------------ | ------------------------------------------------------------------ |
| `!!cfx` / `!!cfx status` | Show scheduler, server, and pardon status                          |
| `!!cfx help`             | Show the plugin command reference                                  |
| `!!cfx pardon <minutes>` | Temporarily suspend curfew and start the server if needed          |
| `!!cfx pardon cancel`    | Cancel a pardon; during curfew, stop after a 10-second countdown   |
| `!!cfx enable`           | Enable scheduling; during curfew, stop after a 10-second countdown |
| `!!cfx disable`          | Disable scheduling and start a server stopped by CurfewX           |
| `!!cfx reload`           | Validate and reload the configuration                              |

`!!curfew` is the full command alias and supports the same subcommands as `!!cfx`.

Pardon expiration is persisted. If the configured curfew is still active when a pardon expires, the server is stopped. Otherwise, it remains online.

## Shutdown and recovery policy

- CurfewX first asks MCDR to stop the server gracefully so Minecraft can save and exit normally.
- After 120 seconds, CurfewX reports an error to the MCDR console and log, then repeats it every 300 seconds.
- After 3600 seconds, it invokes MCDR's `kill()` API to terminate the server process group.
- Forced termination can lose unsaved data or damage a world. It is only a last resort, and all three timeouts are configurable.
- CurfewX only starts servers it stopped itself. It does not restart manually stopped or crashed servers during open hours.
- If another MCDR command starts the server during curfew, CurfewX asks it to stop again. Public APIs cannot cancel process creation, so a Forge process might run briefly.
- `state.json` stores ownership, pardon, and force-kill timing state. Editing or deleting it manually is not recommended.

## Development

The project uses [uv](https://docs.astral.sh/uv/) and pins its development interpreter to Python 3.11.15 through `.python-version`. The plugin source remains compatible with Python 3.9 and later, matching MCDReforged 2.15.7.

```bash
uv sync
uv run pytest -q
uv run ruff check .
mkdir -p dist
uv run mcdreforged pack -o dist
```

## License

CurfewX is released under the [MIT License](https://github.com/Rivertao1/CurfewX/tree/main/LICENSE).

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [CurfewX-v0.1.2.mcdr](https://github.com/Rivertao1/CurfewX/releases/tag/v0.1.2) | 0.1.2 | 2026/08/15 01:06:30 | 16.98KB | 14 | [Download](https://github.com/Rivertao1/CurfewX/releases/download/v0.1.2/CurfewX-v0.1.2.mcdr) |
| [CurfewX-v0.1.1.mcdr](https://github.com/Rivertao1/CurfewX/releases/tag/v0.1.1) | 0.1.1 | 2026/08/12 04:43:19 | 15.64KB | 14 | [Download](https://github.com/Rivertao1/CurfewX/releases/download/v0.1.1/CurfewX-v0.1.1.mcdr) |
| [CurfewX-v0.1.0.mcdr](https://github.com/Rivertao1/CurfewX/releases/tag/v0.1.0) | 0.1.0 | 2026/08/11 06:51:25 | 15.34KB | 6 | [Download](https://github.com/Rivertao1/CurfewX/releases/download/v0.1.0/CurfewX-v0.1.0.mcdr) |

