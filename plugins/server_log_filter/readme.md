**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## server_log_filter

### Basic Information

- Plugin ID: `server_log_filter`
- Plugin Name: Server Log Filter
- Version: 1.4.1
  - Metadata version: 1.4.1
  - Release version: 1.4.1
- Total downloads: 67
- Authors: [Pau1am](https://github.com/Pau1am)
- Repository: https://github.com/LifeSci-Craft/MCDR-ServerLogFilter
- Repository plugin page: https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Hide noisy server console lines from the MCDR console with configurable regex rules, without touching the server's own log file.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# MCDR-ServerLogFilter

**Language / 语言:** **English** | [简体中文](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/README.md)

> An MCDReforged plugin that hides noisy server console lines from the MCDR console, while leaving the server's own log file completely untouched.

[![MCDR](https://img.shields.io/badge/MCDReforged-%3E%3D2.15-blue)](https://mcdreforged.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/LICENSE)
[![Python](https://img.shields.io/badge/python-%3E%3D3.9-blue)](https://www.python.org/)

|           |                                                                               |
| --------- | ----------------------------------------------------------------------------- |
| Plugin ID | `server_log_filter`                                                           |
| Commands  | `!!logfilter` / `!!lf`                                                        |
| Requires  | MCDR **2.15.0+** (tested on 2.15.0 / 2.15.7 / 2.16.0; MC-version independent) |
| License   | MIT                                                                           |

> Building or modifying the plugin, or looking for the packaging and test docs? See [docs/DEVELOPMENT.md](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/docs/DEVELOPMENT.md).

## Contents

- [Features](#features)
- [Installation](#installation)
- [Commands](#commands)
- [Configuration](#configuration)
- [Notes](#notes)
- [License](#license)

## Features

- Filters server output with regex rules; a matching line is hidden from the **MCDR console only**, and the server's own `server/logs/latest.log` keeps every line
- Hiding the console echo is not discarding the line: the event is still dispatched, so other plugins and MCDR's own start / stop / join-leave detection are unaffected
- The default rule targets the Minecraft 26.3 "standing on air" spam (an upstream false positive; Mojira [MC-311474](https://bugs.mojang.com/browse/MC-311474) / [MC-311727](https://bugs.mojang.com/browse/MC-311727))
- Rules can be added or changed at any time; `!!logfilter test <text>` verifies one before you rely on it
- A rule that matches nothing for several sessions is reported once; rules with catastrophic backtracking are refused at load (skipped with a warning, the others keep working)
- A broken config file is backed up as `config.json.old` and rebuilt; new options are filled in after plugin upgrades, never overwriting your values
- English and Simplified Chinese; every command needs administrator permission

## Installation

1. Download `ServerLogFilter-vX.Y.Z.mcdr` from [Releases](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/../../releases), or build it yourself (see [docs/DEVELOPMENT.md](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/docs/DEVELOPMENT.md));
2. Drop it into the MCDR `plugins/` folder;
3. If MCDR is running, use `!!MCDR reload plugin server_log_filter`; if not, just start it;
4. The first load generates `config/server_log_filter/config.json`; the defaults work out of the box.

Running several backends? Put one copy in each; configurations are independent.

## Commands

`!!logfilter` and `!!lf` are completely interchangeable. **Every command needs MCDR administrator permission** (this is not the same as being op in the game: MCDR only reads its own `permission.yml`, and unlisted players default to `user`). Grant it in the MCDR console with `!!MCDR permission set <name> admin`.

| Command                              | Effect                                                                                                                                                   |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!logfilter` (= `!!logfilter help`) | Help page (each line is clickable in in-game chat)                                                                                                       |
| `!!logfilter list`                   | Status: active language and where it comes from, per-rule hits and idle streaks, number of skipped rules                                                 |
| `!!logfilter test <text>`            | Whether a line would be hidden, and which rule matches; pasting the whole console line works too (the `[time] [thread/level]:` prefix is stripped first) |
| `!!logfilter reload`                 | Re-read the config and apply it immediately, no restart needed; statistics for rules removed from the config are cleared as well                         |
| `!!logfilter reset`                  | Clear the idle-session counters and start observing again                                                                                                |

## Configuration

`config/server_log_filter/config.json` is generated on first load:

```json
{
    "language": "auto",
    "patterns": [
        "standing on air - force-sending blocks below"
    ],
    "log_matched_lines": false,
    "report_on_server_stop": true,
    "warn_about_stale_rules": true,
    "stale_rule_threshold": 3,
    "validate_patterns": true,
    "pattern_probe_timeout_ms": 25,
    "announce_config_upgrade": true,
    "announce_broken_config": true
}
```

<details><summary>Show options</summary>

| Key                        | Type       | Default   | Description                                                                                                                                                        |
| -------------------------- | ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `language`                 | `string`   | `"auto"`  | Message language. `auto` follows MCDR; `zh_cn` / `en_us` pin it (case and `-` / `_` are free; `zh_tw` resolves to `zh_cn`, anything missing falls back to `en_us`) |
| `patterns`                 | `string[]` | see above | Regex rules, matched against the **body** of each line (MCDR has already stripped the `[time] [thread/level]:` prefix). A match hides the line                     |
| `log_matched_lines`        | `bool`     | `false`   | Debug aid: write every hidden line to the MCDR log at INFO level                                                                                                   |
| `report_on_server_stop`    | `bool`     | `true`    | Log a summary of how many lines were hidden this run, on server stop                                                                                               |
| `warn_about_stale_rules`   | `bool`     | `true`    | Warn once when a rule has matched nothing for several sessions (only sessions that finished starting count)                                                        |
| `stale_rule_threshold`     | `int`      | `3`       | How many consecutive idle sessions before warning; `0` disables this reminder                                                                                      |
| `validate_patterns`        | `bool`     | `true`    | At load, probe each rule and refuse ones with catastrophic backtracking (skipped with a warning)                                                                   |
| `pattern_probe_timeout_ms` | `int`      | `25`      | Time budget for that check, in milliseconds; rarely needs changing                                                                                                 |
| `announce_config_upgrade`  | `bool`     | `true`    | Say which options were filled in after an upgrade                                                                                                                  |
| `announce_broken_config`   | `bool`     | `true`    | Say why a broken config was backed up and reset, and where the backup went                                                                                         |

</details>

**Matching uses `re.search` (substring match), not full match.** Writing `standing on air` matches the whole line, no `.*` needed. The flip side: `.` matches any character, so use `\.` for a literal dot.

**Adding rules:** append the log body to `patterns` (leave the other keys as they are), verify with `!!logfilter test <text>`, then run `!!logfilter reload`:

```json
{
    "patterns": [
        "standing on air - force-sending blocks below",
        "Ignoring chat session from .* due to missing Services public key"
    ]
}
```

A few notes:

- A rule that fails to compile is skipped with a warning in the log; the others keep working. To switch filtering off for a while, empty `patterns` and run `!!logfilter reload`.
- Idle statistics live in `state.json`, separate from your `config.json`; the plugin never edits your config file. Remove a rule from the config and its statistics are cleared on `reload`.
- A broken config is renamed to `config.json.old` before the defaults are rebuilt (one backup slot only). A file that is not UTF-8 (for example saved as ANSI) counts as broken too.
- The three notice switches (`warn_about_stale_rules`, `announce_config_upgrade`, `announce_broken_config`) only control the message: backing up, filling in and counting always keep running.
- Adding a language: copy `en_us.json` to `<code>.json` and translate the values; see `server_log_filter/lang/README.md`. No code changes needed.

## Notes

- Filtering happens entirely on the MCDR side, so it is independent of the MC version. The default rule only means something on MC 26.3; on other versions the plugin works as usual and the default rule simply never matches.
- Avoid overly broad rules (`.`, `.*`, `^`): the console can start looking like the server is not running. A warning is printed at load, and `!!logfilter list` flags them.
- For the complete raw log, always read `server/logs/latest.log`.

## License

[MIT](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/LICENSE)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ServerLogFilter-v1.4.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.4.1) | 1.4.1 | 2026/10/07 04:27:30 | 20.8KB | 7 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.4.1/ServerLogFilter-v1.4.1.mcdr) |
| [ServerLogFilter-v1.4.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.4.0) | 1.4.0 | 2026/10/04 13:08:49 | 19.3KB | 8 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.4.0/ServerLogFilter-v1.4.0.mcdr) |
| [ServerLogFilter-v1.3.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.3.0) | 1.3.0 | 2026/10/04 09:49:57 | 26.88KB | 4 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.3.0/ServerLogFilter-v1.3.0.mcdr) |
| [ServerLogFilter-v1.2.2.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.2.2) | 1.2.2 | 2026/10/04 08:54:14 | 25.14KB | 5 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.2.2/ServerLogFilter-v1.2.2.mcdr) |
| [ServerLogFilter-v1.2.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.2.1) | 1.2.1 | 2026/10/04 07:33:51 | 17.87KB | 3 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.2.1/ServerLogFilter-v1.2.1.mcdr) |
| [ServerLogFilter-v1.2.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.2.0) | 1.2.0 | 2026/10/04 06:42:18 | 19.21KB | 5 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.2.0/ServerLogFilter-v1.2.0.mcdr) |
| [ServerLogFilter-v1.1.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.1.1) | 1.1.1 | 2026/10/04 05:29:16 | 14.78KB | 6 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.1.1/ServerLogFilter-v1.1.1.mcdr) |
| [ServerLogFilter-v1.1.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.1.0) | 1.1.0 | 2026/10/04 05:12:28 | 27.8KB | 4 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.1.0/ServerLogFilter-v1.1.0.mcdr) |
| [ServerLogFilter-v1.0.2.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.0.2) | 1.0.2 | 2026/10/02 08:42:25 | 6.99KB | 8 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.0.2/ServerLogFilter-v1.0.2.mcdr) |
| [ServerLogFilter-v1.0.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.0.1) | 1.0.1 | 2026/10/01 12:54:16 | 4.73KB | 8 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.0.1/ServerLogFilter-v1.0.1.mcdr) |
| [ServerLogFilter-v1.0.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.0.0) | 1.0.0 | 2026/10/01 12:39:20 | 4.76KB | 9 | [Download](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.0.0/ServerLogFilter-v1.0.0.mcdr) |

