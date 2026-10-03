**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## server_log_filter

### Basic Information

- Plugin ID: `server_log_filter`
- Plugin Name: Server Log Filter
- Version: 1.0.2
  - Metadata version: 1.0.2
  - Release version: 1.0.2
- Total downloads: 14
- Authors: [Pau1am](https://github.com/Pau1am)
- Repository: https://github.com/Pau1am/MCDR-ServerLogFilter
- Repository plugin page: https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main
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

**Language / 语言:** **English** | [简体中文](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/README.md)

An MCDReforged plugin that **hides noisy server console lines from the MCDR console while leaving the server's own log file completely untouched.**

[![MCDR](https://img.shields.io/badge/MCDReforged-%3E%3D2.15-blue)](https://mcdreforged.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/LICENSE)
[![Python](https://img.shields.io/badge/python-%3E%3D3.9-blue)](https://www.python.org/)

---

## Why

MCDR echoes every line the server prints to its console. That is usually exactly what you want — but some server versions repeatedly print lines that carry no useful information at all, for example Minecraft 26.3:

```
[Server thread/INFO]: Player Steve standing on air - force-sending blocks below
```

This is an INFO line from the new "ghost block" auto-repair mechanism added in 26.3. It is a known **false positive** (Mojira [MC-311474](https://bugs.mojang.com/browse/MC-311474) / [MC-311727](https://bugs.mojang.com/browse/MC-311727)): it fires during ordinary jumping and movement, at most once per player every 10 seconds, and keeps spamming the log.

Editing the server's `log4j2.xml` also works, but that is a **global** change: get it wrong and the server may lose important log lines, and it only affects the server side. This plugin takes a different route — **it only touches MCDR**.

## Two key design decisions

### 1. Hide the echo, never discard the info

The plugin uses MCDR's `InfoActionFlag.hidden()`, **not** `discarded()`:

|                          | Console echo | Dispatched to plugin events | MCDR state detection |
| ------------------------ | ------------ | --------------------------- | -------------------- |
| `hidden()` (this plugin) | ❌ hidden     | ✅ intact                    | ✅ works              |
| `discarded()`            | ❌ hidden     | ❌ lost                      | ⚠️ may break         |

Keeping `process` means the line is **still dispatched to MCDR's info reactors and plugin events**. As a result, **even an overly broad rule cannot break MCDR's own "server startup / stop / player join-leave" detection** — the worst case is simply that you don't see the line on the console. This is the plugin's most important safety property.

### 2. The server's own log file is untouched

`server/logs/latest.log` is written by the server process itself through log4j, entirely independent of this plugin. **Not a single original record is lost.** So:

- Need the full raw log → read `server/logs/latest.log`
- Want a clean MCDR console / web panel → use this plugin

## Installation

1. Download `ServerLogFilter-vX.Y.Z.mcdr` from [Releases](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/../../releases), or build it yourself (see below)
2. Drop it into the `plugins/` folder of the MCDR instance:

```
<MCDR dir>/plugins/ServerLogFilter-vX.Y.Z.mcdr
```

Running several backends? Put one copy in each — configurations are independent.

3. Activate:

- MCDR already running: `!!MCDR reload plugin server_log_filter`
- Otherwise: just start the server

## Configuration

`config/server_log_filter/config.json` is generated on first load:

```json
{
    "patterns": [
        "standing on air - force-sending blocks below"
    ],
    "log_matched_lines": false,
    "report_on_server_stop": true
}
```

| Key                     | Type       | Description                                                                                                                                    |
| ----------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `patterns`              | `string[]` | Regex rules. Matched against the **body** of each line (MCDR has already stripped the `[time] [thread/level]:` prefix). A match hides the line |
| `log_matched_lines`     | `bool`     | Debug aid. When `true`, every hidden line is written to the MCDR log at INFO level                                                             |
| `report_on_server_stop` | `bool`     | On server stop, log a summary of how many lines were hidden this run                                                                           |

> **Matching uses `re.search` (substring match), not full match.**
> Writing `standing on air` matches the whole line — no `.*` needed.
> The flip side: a `.` in your pattern matches any character, so use `\.` for a literal dot.

The config file is JSON and **does not support comments**.

## Commands

| Command                   | Permission | Description                                                  |
| ------------------------- | ---------- | ------------------------------------------------------------ |
| `!!logfilter`             | user       | Show status: rule count and per-rule hit counts              |
| `!!logfilter list`        | user       | Same as above                                                |
| `!!logfilter test <text>` | user       | Check whether a line would be hidden, and which rule matches |
| `!!logfilter reload`      | admin      | Re-read the config file and apply it immediately             |

`!!logfilter test` is especially handy: paste a line from your log to verify the rule without waiting for it to actually fire.

## Adding more rules

Just append the log body you want to filter to the `patterns` array:

```json
{
    "patterns": [
        "standing on air - force-sending blocks below",
        "Ignoring chat session from .* due to missing Services public key",
        "^\\[Async Chat Thread"
    ],
    "log_matched_lines": false,
    "report_on_server_stop": true
}
```

Verify with `!!logfilter test <text>` first, then `!!logfilter reload`.

A malformed regex will not crash the plugin — the rule is skipped with a warning in the MCDR log and the remaining rules keep working.

## Verification

### Unit tests (filtering logic, edge cases, safety properties)

- The target spam line is hidden while `process` is preserved (the key safety property)
- **15 classes of must-not-touch lines verified individually**: `Done (...)!`, player join/leave,
  `Stopping the server` / `Stopping server`, `moved too quickly`, `moved wrongly`,
  `Rejecting UseItemOnPacket`, `dropping items too fast`, chat signature warnings,
  `lost connection`, the version banner, `Preparing level`, death messages,
  `Saving and pausing game...`
- No crash on `""` / `None` / whitespace-only `content`
- Matches regardless of player name
- Multiple rules keep independent counts; `reload` resets counters
- An invalid regex is skipped with a warning and does not affect other rules
- Nearly-identical-but-different lines are **not** matched (proving it is not a blanket filter)

### End-to-end (real MCDR + a fake server, full lifecycle)

Observed console echo (default rule):

| Log line                                                         | Result                   |
| ---------------------------------------------------------------- | ------------------------ |
| `Player <any name> standing on air - force-sending blocks below` | ✅ hidden (0 occurrences) |
| `Steve moved too quickly!` / `moved wrongly!`                    | ✅ kept                   |
| `Steve joined the game`                                          | ✅ kept                   |
| Any ordinary log line                                            | ✅ kept                   |
| `Stopping server`                                                | ✅ kept                   |

Plugin log:

```
Plugin server_log_filter@1.0.2 loaded
Enabled 1 log filter rule; matches are hidden from the MCDR console only, the server log is unaffected
Hidden 3 server log lines from the MCDR console this run (server log file unaffected)
```

**No errors at all.**

There is also a **canary-backed end-to-end case** guarding the "hidden but still dispatched" safety
property: it makes the filter *also* match the server-startup line, then asserts both that the line
left the console **and** that MCDR's `SERVER_STARTUP` event was still dispatched. That is what makes
`hidden()` and `discarded()` observably different — with the default rule alone, both look identical,
because noise lines never take part in lifecycle detection. See [tests/README.md](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/tests/README.md).

### Running the tests

The behaviour above is covered by an automated suite (`tests/`, 66 cases) that runs against a real
MCDR — **including the end-to-end group below**, which boots an actual MCDR instance, loads the
`.mcdr` produced by `pack.py`, and drives a fake server through a full lifecycle:

```bash
python -m pip install --target .testlibs -r tests/requirements-test.txt
PYTHONPATH=.testlibs python -m pytest tests -v      # Windows: $env:PYTHONPATH=".testlibs"
```

The suite asserts the plugin's key safety property: a hidden line **keeps `process` and only
loses `echo_to_console`** — that it **really is absent from the console**, and that **events are
still dispatched**. If a future MCDR release changes the semantics of `hidden()`, the tests fail
loudly instead of letting the plugin misbehave silently on your server.
The end-to-end group takes ~5–6 s (one MCDR boot shared by all cases); skip it with
`MCDR_SKIP_E2E=1`.
See [tests/README.md](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/tests/README.md) for details.

## Building from source

The repository follows MCDR's standard layout — root metadata plus a same-named code package:

```
MCDR-ServerLogFilter/
├── mcdreforged.plugin.json
├── LICENSE
├── README.md
├── README_en.md
├── CHANGELOG.md
├── pack.py
└── server_log_filter/
    └── __init__.py
```

Build with the included, allowlist-based packer:

```bash
python pack.py            # -> ServerLogFilter-v<version>.mcdr
```

> **Why an allowlist and not a skip list?** An earlier version of this section used
> `rglob("*")` with a short `skip` set, which is a *denylist*: any new file in the repo
> silently ends up in the release artifact. Two concrete consequences:
> 
> 1. **The artifact would fail to load at all.** MCDR validates the root entries of a
>    `.mcdr` (`PackedPlugin._check_dir_legality`) and raises
>    `IllegalPluginStructure: Packed plugin cannot contain other module` for a root-level
>    `conftest.py` or `setup.py`. The test suite's `conftest.py` sits exactly there, so the
>    denylist approach ships a plugin that cannot be loaded.
> 2. **Runaway size.** After installing `.testlibs/` per `tests/README.md`, the denylist
>    bundled all of MCDR and its dependencies: measured at **1362 files / 7.11 MB**
>    (allowlist: 6 files / ~17 KiB).
> 
> `test_packaged_artifact_is_loadable` in `tests/test_plugin.py` runs `pack.py` and checks
> the result with MCDR's own validation, so this class of regression cannot come back.

## Requirements

- MCDReforged **>= 2.15.0**

  > Why not 2.13? The plugin's core design relies on `InfoActionFlag.hidden()`
  > (strip the console echo only, keep event dispatch), and that class was introduced in
  > **MCDR 2.15.0**. In 2.14.x and earlier, `InfoFilter` only supports
  > "return `False` to discard the whole line", which cannot reproduce this plugin's
  > behaviour, so those versions are not supported.
  > Installing on an older MCDR never fails silently — MCDR reports
  > `dependency mcdreforged@x.y.z does not satisfy version requirement >=2.15.0`.

- Python >= 3.9 (bundled with MCDR)

## Compatibility

| Dimension | Support                                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| MCDR      | **>= 2.15.0** (2.15.0 / 2.15.7 / 2.16.0 tested)                                                                                              |
| Minecraft | **Independent of the MC version.** 1.16.5 / 1.19.4 / 1.20.1 / 1.20.6 / 1.21.8 / 1.21.11 / 26.1 / 26.2 / 26.3 all tested against real servers |

Filtering happens on the MCDR side (matching each line of the server's stdout), so it does
not change with the MC version. The only version-dependent part is **what the default rule
targets**: `standing on air - force-sending blocks below` is only produced by **MC 26.3**.
On earlier versions the plugin still works — the default rule simply never matches anything,
and you can configure `patterns` to filter whatever noise your version emits.

## License

[MIT](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/LICENSE)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ServerLogFilter-v1.0.2.mcdr](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/tag/v1.0.2) | 1.0.2 | 2026/10/02 08:42:25 | 6.99KB | 3 | [Download](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/download/v1.0.2/ServerLogFilter-v1.0.2.mcdr) |
| [ServerLogFilter-v1.0.1.mcdr](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/tag/v1.0.1) | 1.0.1 | 2026/10/01 12:54:16 | 4.73KB | 5 | [Download](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/download/v1.0.1/ServerLogFilter-v1.0.1.mcdr) |
| [ServerLogFilter-v1.0.0.mcdr](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/tag/v1.0.0) | 1.0.0 | 2026/10/01 12:39:20 | 4.76KB | 6 | [Download](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/download/v1.0.0/ServerLogFilter-v1.0.0.mcdr) |

