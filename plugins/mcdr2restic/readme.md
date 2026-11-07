**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mcdr2restic

### Basic Information

- Plugin ID: `mcdr2restic`
- Plugin Name: MCDR2Restic
- Version: 0.10.0
  - Metadata version: 0.10.0
  - Release version: 0.10.0
- Total downloads: 75
- Authors: [pfdr2333](https://github.com/pfdr2333)
- Repository: https://github.com/pfdr2333/MCDR2restic
- Repository plugin page: https://github.com/pfdr2333/MCDR2restic/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Schedule deduplicated incremental restic backups with multi-channel notifications.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0 |
| [websocket-client](https://pypi.org/project/websocket-client) | \>=1.8.0 |

```
pip install "PyYAML>=6.0" "websocket-client>=1.8.0"
```

### Introduction

# MCDR2Restic

[![CI](https://github.com/pfdr2333/MCDR2restic/actions/workflows/ci.yml/badge.svg)](https://github.com/pfdr2333/MCDR2restic/actions/workflows/ci.yml)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://github.com/pfdr2333/MCDR2restic/tree/main/LICENSE)

An MCDReforged plugin that runs [restic](https://restic.readthedocs.io/en/stable/) deduplicated incremental backups for Minecraft servers, with scheduling, snapshot restore, and multi-channel notifications.

**[中文](https://github.com/pfdr2333/MCDR2restic/tree/main/README.md) | English**

## Features

- Scheduled backups via 6-field cron or fixed intervals; a running backup can be interrupted
- Skips scheduled backups when nobody is playing, using join/left events plus a `list` online check
- Forced backup scheduling that ignores player activity (disabled by default)
- Automatic restic download (Linux/Windows amd64) with outdated copies upgraded automatically, using built-in official, self-hosted mirror and proxy sources
- Snapshot restore: full snapshot, single file, or folder — including restore into a chosen directory
- Automatic pre-restore safety snapshot with rollback on failure
- Repository maintenance: `forget`/`prune` and friends, scheduled independently
- Notifications via OneBot QQ, Discord, and a custom webhook, all can be enabled at once
- Bilingual (Chinese/English) messages and config comments, following the MCDR language
- Configuration safety check: the restic repository must not sit inside a backup source

## Demo

Every snapshot is a complete backup of its point in time while only consuming incremental storage:

![Demo](https://raw.githubusercontent.com/pfdr2333/MCDR2restic/main/image.png)

## Requirements

- MCDReforged >= 2.12.0
- Python dependencies are installed by MCDR from `requirements.txt` (`PyYAML`, `websocket-client`)

> Familiarize yourself with basic restic concepts before using this plugin ([restic manual](https://restic.readthedocs.io/en/stable/)). The default configuration works out of the box, but advanced use cases such as remote repositories and retention policies still require restic knowledge.

## Installation

The plugin is published in the MCDR plugin repository — one command installs it:

```text
!!MCDR plugin install mcdr2restic
```

Updating later is also a one-liner:

```text
!!MCDR plugin install -U mcdr2restic
```

Manual installation: grab `MCDR2Restic.mcdr` from the latest [Release](https://github.com/pfdr2333/MCDR2restic/releases), drop it into MCDR's `plugins/` directory, and run `!!MCDR reload all`. On first load a sample configuration tailored to your system is generated at `config/mcdr2restic/config.yml` — the defaults just work:

- restic is downloaded, kept up to date and the local repository initialized automatically
- `./server/world` is backed up by default (all three world directories are added when detected)
- On Windows the sample uses `.\config\mcdr2restic\restic.exe`-style backslash paths and excludes `session.lock`

Adjust the configuration as needed, then run `!!m2r reload`.

> Only the world directories are backed up by default. For full restore capability, consider backing up the entire `./server` directory or even the whole MCDR root, protecting server files beyond the save data.
> 
> The example password `123456` only lowers the entry barrier — change it for production use.
> 
> The OneBot dependency is named `websocket-client` (imported as `websocket`). If a conflicting package with the same name is installed, the plugin reports the problem. If dependency installation fails behind mainland-China networks, configure a PyPI mirror or proxy for the Python environment MCDR uses.

## Commands

The default root is `!!restic` with `!!m2r` as an alias (fully equivalent); shorter `!!m2r` examples are used below, and typing the bare root shows the status.

| Command                                           | Description                                                              |
| ------------------------------------------------- | ------------------------------------------------------------------------ |
| `!!m2r status [p <page>]`                         | Show status and the snapshot list                                        |
| `!!m2r backup`                                    | Trigger an immediate backup                                              |
| `!!m2r start` / `stop`                            | Enable / disable scheduled backups                                       |
| `!!m2r cancel`                                    | Cancel the currently running task without touching the scheduling switch |
| `!!m2r init`                                      | Initialize the repository manually                                       |
| `!!m2r unlock`                                    | Unlock the repository                                                    |
| `!!m2r maintenance`                               | Run repository maintenance manually                                      |
| `!!m2r restore <snapshot>`                        | Queue a full-snapshot restore                                            |
| `!!m2r restore <snapshot> file <path>`            | Queue a single-file restore                                              |
| `!!m2r restore <snapshot> folder <path>`          | Queue a folder restore                                                   |
| `!!m2r restore <snapshot> to <dir>`               | Queue a full-snapshot restore into a chosen directory (no server stop)   |
| `!!m2r restore <snapshot> to <dir> file <path>`   | Queue a single-file restore into a chosen directory                      |
| `!!m2r restore <snapshot> to <dir> folder <path>` | Queue a folder restore into a chosen directory                           |
| `!!m2r restore list`                              | Show queued restore tasks                                                |
| `!!m2r restore apply`                             | Apply the restore task queue                                             |
| `!!m2r restore apply --skip-safety`               | Apply the restore task queue without a safety snapshot                   |
| `!!m2r unrestore <ID>|all`                        | Delete one / all restore tasks                                           |
| `!!m2r notify-test`                               | Send a test message to all enabled notification channels                 |
| `!!m2r reload`                                    | Reload configuration                                                     |

The default command permission level is `3` and can be changed in the configuration.

Queued tasks are not executed immediately. When running `restore apply`:

- **Restore into the server working directory** (default): a safety snapshot is created first, then Minecraft is stopped via MCDR, files are restored, and the server starts again; failures roll back to the safety snapshot automatically. Adding `--skip-safety` skips the safety snapshot — rollback is then impossible, so use it carefully.
- **Restore into a chosen directory** (when every task carries `to`): the server keeps running while the restore executes; target directories inside the restic repository or backup sources are rejected.

## Documentation

Full configuration references, scheduling details, and FAQs live in the [online docs](https://m2r.pfdr.cc/) (Chinese; sources under [docs/](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/index.md)):

- [Getting started](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/getting-started.md)
- [Commands](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/commands.md)
- [Configuration](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/configuration.md)
- [Restore & status](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/restore.md)
- [FAQ](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/faq.md)

## Development & Build

```bash
# Run tests (coverage must stay at or above 65%)
python -m coverage run --branch --source=mcdr2restic,tools -m unittest discover -s tests -p "test_*.py"
python -m coverage report --fail-under=65

# Build the .mcdr archive
python tools/pack_plugin.py --output-dir dist

# Preview the docs site locally (Material for MkDocs)
pip install -r requirements-docs.txt
mkdocs serve
```

After editing `lang/zh_cn.json` or `en_us.json`, run `python tools/sync_language_resources.py` to regenerate `zh_tw` and keep both language file copies in sync; CI verifies that both `lang/` copies match and fails when they do not.

GitHub Actions runs the tests and stores build artifacts on every push; pushing a tag like `v0.6.0` builds the archive and publishes a release automatically.

## Contributing

Issues and pull requests are welcome.

## License

This project is released under the [GPL-3.0](https://github.com/pfdr2333/MCDR2restic/tree/main/LICENSE) license.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MCDR2Restic_v0.10.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.10.0) | 0.10.0 | 2026/11/07 04:03:05 | 216.08KB | 1 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.10.0/MCDR2Restic_v0.10.0.mcdr) |
| [MCDR2Restic_v0.9.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.9.0) | 0.9.0 | 2026/11/06 23:47:04 | 209.81KB | 3 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.9.0/MCDR2Restic_v0.9.0.mcdr) |
| [MCDR2Restic_v0.6.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.6.0) | 0.6.0 | 2026/11/04 21:37:13 | 171.47KB | 3 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.6.0/MCDR2Restic_v0.6.0.mcdr) |
| [MCDR2Restic_v0.5.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.5.0) | 0.5.0 | 2026/08/08 20:12:04 | 151.34KB | 29 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.5.0/MCDR2Restic_v0.5.0.mcdr) |
| [MCDR2Restic_v0.4.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.4.0) | 0.4.0 | 2026/07/09 04:25:11 | 252.82KB | 8 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.4.0/MCDR2Restic_v0.4.0.mcdr) |
| [MCDR2restic_v0.3.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.3.0) | 0.3.0 | 2026/07/08 09:33:34 | 170.36KB | 5 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.3.0/MCDR2restic_v0.3.0.mcdr) |
| [MCDR2Restic_v0.2.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.2.0) | 0.2.0 | 2026/07/08 04:58:57 | 154.57KB | 6 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.2.0/MCDR2Restic_v0.2.0.mcdr) |
| [MCDR2restic_v0.1.9.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.9) | 0.1.9 | 2026/07/08 04:03:03 | 150.17KB | 6 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.9/MCDR2restic_v0.1.9.mcdr) |
| [MCDR2restic_v0.1.8.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.8) | 0.1.8 | 2026/07/08 02:17:27 | 149.04KB | 7 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.8/MCDR2restic_v0.1.8.mcdr) |
| [MCDR2restic_v0.1.7.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.7) | 0.1.7 | 2026/07/08 02:03:44 | 136.64KB | 7 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.7/MCDR2restic_v0.1.7.mcdr) |

