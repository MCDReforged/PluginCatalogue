**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mcdr2restic

### Basic Information

- Plugin ID: `mcdr2restic`
- Plugin Name: MCDR2Restic
- Version: 0.5.0
  - Metadata version: 0.5.0
  - Release version: 0.5.0
- Total downloads: 49
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

MCDR2Restic is an MCDReforged plugin designed to regularly invoke restic to back up specified directories while the server is running normally.

**This readme is being refactored and may contain outdated information.**

## Prerequisites

> This project is responsible for invoking restic. Under the default configuration, if restic is not found in the config folder, it will automatically download the appropriate restic binary for your system. This feature will not take effect if a non-default directory is configured.

> Before using this project, please familiarize yourself with the core concepts and configuration methods of restic, and ensure you can use restic independently.
> The usage of restic is beyond the scope of this document (see the [restic](https://restic.readthedocs.io/en/stable/)). Most backup features require a basic understanding of restic. Restic is a fast, efficient, and secure open-source backup tool. Its deduplication capability is particularly well-suited for Minecraft servers, significantly reducing backup sizes.

> Although the plugin's default configuration handles the installation of restic automatically, it is highly recommended to learn how to use restic and its advanced configurations—you will definitely need them.

# Language **[中文](https://github.com/pfdr2333/MCDR2restic/tree/main/README.md)| English**

This project supports both Chinese and English, following the MCDR language conventions.

## Features

* Scheduled restic backups
* Ability to interrupt the ongoing backup task
* Automatically download Restic
* Supports OneBot QQ notifications and Discord Webhook notifications
* Dual-language (Chinese/English) messages and configuration comments
* Skip scheduled backups when idle: Executes a `list` command upon trigger, combined with join/left player events for precise determination
* Forced backup scheduling support: Bypasses player activity detection (disabled by default)
* Configuration safety check: The local restic repository must not be inside any backup source directory
* Automated, Secure & Simple Snapshot Restore

## Installation

> **Quick Start: Place the plugin into MCDR's `plugins` directory and run `!!MCDR reload all` to get it running automatically with the default configuration.**

1. Place `MCDR2Restic.mcdr` into the MCDR `plugins/` directory.
2. Python dependencies are declared in the package root `requirements.txt` and handled by MCDR:
* `PyYAML>=6.0`
* `websocket-client>=1.8.0`

The dependency required for OneBot notifications is named `websocket-client`, while its Python import name is `websocket`. If a conflicting package with the same name is mistakenly installed (causing `websocket.WebSocketApp` to be missing), the plugin only reports the problem and will not call pip to uninstall or reinstall packages.
If MCDR fails to install its dependencies, fix the Python environment used by MCDR and reload it. If the wrong websocket package was installed accidentally, uninstall it from that environment.

In domestic network environments (e.g., Mainland China), if MCDR dependency installation fails to download packages, configure a PyPI mirror or proxy for the Python/pip environment used by MCDR, then retry.


3. After starting or reloading MCDR, if `config/mcdr2restic/config.yml` does not exist, the plugin will automatically generate a sample configuration tailored to the current operating system. The comment language adapts to MCDR's current locale: Chinese comments for the Chinese locale, and English comments for all other locales.
   When generating the configuration for the first time on Windows, the example will automatically adapt to Windows-style paths like `.\config\mcdr2restic\restic.exe`, `.\restic-repo`, and `.\server\world`, utilizing YAML single quotes to avoid backslash escape issues.
4. Modify the configuration file as needed, then execute `!!restic reload` once finished.

<!--
## Configuration
<details>
  <summary>Detailed Configuration Guide</summary>
The runtime status is written to `config/mcdr2restic/state.yml`, tracking metrics such as player join/leave flags, recent online check results, and recent backup outcomes.

`!!restic status` also shows the restic snapshot list. The list is cached in SQLite (default: `config/mcdr2restic/snapshots.sqlite3`) and is invalidated automatically after this plugin runs `init`, maintenance commands, or backup commands. The cache is refreshed the next time status is viewed. By default, 10 snapshots are shown per page; adjust `snapshot_cache.page_size` if needed.

Restore tasks are stored in SQLite as well. `!!restic restore <snapshot>` queues a full-snapshot restore; `!!restic restore <snapshot> file /server/whitelist.json` and `!!restic restore <snapshot> folder /server/region` queue single-file/folder restores relative to the restic working directory root. Tasks are not executed immediately. `!!restic restore apply` first creates a safety backup tagged with `restore.pre_restore_backup_tag`, then uses MCDR hooks to stop Minecraft, restore files, and start Minecraft again. If the restore queue fails, the plugin immediately restores this safety snapshot before starting Minecraft again, and keeps the queue for inspection.

When `schedule.require_player_activity_in_wait_period` is set to `true`, standard scheduled backups employ a pure event-driven approach combined with a trigger-time check:

* A player joined during this period: Backup
* No player joined, and the `list` command checks 0 online players at trigger time: Skip
* No player joined, but the `list` command checks non-zero online players at trigger time: Backup
* No player joined, but a player left during this period, even if the online player count is 0 at trigger time: Backup

The online player count is checked via MCDR RCON by executing `schedule.online_check_command`, which defaults to Minecraft's `list` command. It is highly recommended to enable RCON in MCDR; otherwise, the plugin can only estimate online players based on join/leave events.

```yaml
schedule:
  interval_seconds: 0
  cron_expression: "0 0 0,3,6,9,12,15,18,21 * * *"
  require_player_activity_in_wait_period: true
  online_check_command: "list"

```

`force_schedule` represents the forced backup schedule, which bypasses player activity detection and is disabled by default. Like the normal schedule, it supports either a fixed interval or a 6-field cron expression: if `interval_seconds > 0`, the fixed interval takes priority; if `interval_seconds = 0` and `cron_expression` is not `"0"`, the cron expression is used; if both are 0, it is disabled.

```yaml
force_schedule:
  interval_seconds: 0
  cron_expression: "0"

```

`maintenance_schedule` controls repository maintenance independently from backups. By default it runs `restic.maintenance_commands` once per day at `03:00`. An empty `cron_expression` keeps the default `03:00`; set it to `"0"` to disable maintenance scheduling. Maintenance does not run `save-off`, `save-all`, or `save-on`. If maintenance and backup fire at the same time, backup runs first; if they overlap after different trigger times, the later task waits for the current one to finish.

```yaml
maintenance_schedule:
  interval_seconds: 0
  cron_expression: "0 0 3 * * *"

```

`update_check` controls version update checks and is enabled by default. The plugin checks once in the background when it loads, then once every day at `00:00`; it only writes log messages and never downloads or updates the plugin automatically. Set `enabled` to `false` to disable it.

```yaml
update_check:
  enabled: true
  check_on_startup: true
  daily_time: "00:00"
  api_url: "https://api.github.com/repos/pfdr2333/MCDR2restic/releases/latest"
  release_page_url: "https://github.com/pfdr2333/MCDR2restic/releases/latest"
  proxy_prefixes:
    - "https://gh.llkk.cc/"
    - "https://gh-proxy.com/"
    - "https://hub.gitmirror.com/"
  timeout_seconds: 10
```

The default generated restic configuration is a minimal, ready-to-run local example:

```yaml
restic:
  executable: "./config/mcdr2restic/restic"
  working_directory: ""
  repository: "./restic-repo"
  password: "123456"
  password_file: ""
  auto_download: true
  download_version: "latest"
  download_proxy_prefixes:
    - "https://gh.llkk.cc/"
    - "https://gh-proxy.com/"
    - "https://hub.gitmirror.com/"
  download_timeout_seconds: 120
  auto_init_local_repository: true
  environment: {}
  maintenance_commands:
    - [
        "forget",
        "--keep-daily", "7",
        "--prune"
      ]
  backup_command:
    - "backup"
    - "./server/world"
    - "--tag"
    - "minecraft"
    - "--host"
    - "mcdr2Restic"
  timeout_seconds: 0
  progress_interval_seconds: 5

```

The backup sequence is now `save-off` -> `save-all` -> `restic backup` -> `save-on`. Repository maintenance is triggered separately by `maintenance_schedule` and no longer runs as a pre-backup step.

This setup allows the plugin to automatically download restic on Linux/Windows amd64 even if it is not present at the default path in the config folder. A newly generated config backs up only `./server/world` by default; if `./server/world`, `./server/world_nether`, and `./server/world_the_end` all exist when the file is generated, the three world directories are written automatically. On Windows, the initial config automatically uses `.\config\mcdr2restic\restic.exe` and backslash paths, and excludes `session.lock` by default to avoid restic exit code 3 caused by Minecraft file locks. The example password `123456` is provided solely to lower the initial configuration barrier; please replace it with your own strong password for production use.

The automatic download first requests the GitHub latest release API. If `api.github.com` fails, it falls back to a built-in `v0.19.1` download link. During downloading, it will first attempt the official GitHub address, then try the proxies listed in `download_proxy_prefixes` sequentially.

`restic.password` takes precedence over `restic.password_file`. The plugin will only configure `RESTIC_PASSWORD_FILE` to use a password file if `password` is left as an empty string. The value of `restic.repository` is automatically exported to `RESTIC_REPOSITORY`.

When `restic.auto_init_local_repository` is `true`, the plugin will automatically execute `restic init` before backing up if the local repository does not exist or lacks a `config` file. Remote repositories such as S3, B2, rest, sftp, and rclone will not be initialized automatically.

You can also run `!!restic init` manually to initialize the repository using the current configuration. The plugin points to this command when remote repositories are not initialized automatically, `auto_init_local_repository` is disabled, or restic reports that the repository is not initialized.

When restic reports that the repository is locked, the plugin automatically unlocks only stale locks left by dead local processes. Other locks are preserved and the plugin points to `!!restic unlock`. Repository locks prevent multiple restic processes from writing to the same repository at the same time, so run this command only after confirming no other backup, restore, maintenance, or external restic client is using that repository.

Before a backup starts, the plugin performs a configuration safety check. If the local `restic.repository` is inside a source directory listed by `backup_command`, for example backing up `.` while using `./restic-repo`, the backup is aborted and administrators are notified. Move the repository outside the backup source or adjust `backup_command`.

`restic.timeout_seconds` controls restic command workflow timeouts. `0` means unlimited; old configs using the previous default `3600` are migrated to `0`. `restic.progress_interval_seconds` controls the `backup`/`restore --json` progress echo interval, defaulting to one MCDR log line every 5 seconds. Backup notifications keep their original start/success/failure behavior and are not spammed by progress echoes.

`restic.environment` overlays environment variables onto each executed restic command, making it ideal for adding secret variables required by backends like S3 or B2. Since `repository`, `password`, and `password_file` are automatically converted into their corresponding restic environment variables, you typically do not need to rewrite `RESTIC_REPOSITORY`, `RESTIC_PASSWORD`, or `RESTIC_PASSWORD_FILE` inside `environment`.

Notifications support both OneBot QQ and Discord Webhook. Both are disabled by default and can be enabled simultaneously. For Discord, you only need to fill in the channel Webhook URL:

```yaml
discord:
  enabled: false
  webhook_url: ""
  username: "MCDR2Restic"
  avatar_url: ""
  message_prefix: "[MCDR2Restic]"
  mention_user_ids: []
  mention_role_ids: []
  mention_everyone: false
  send_timeout_seconds: 10

```

Admin notification texts can be customized within `messages`. Available variables include: `{prefix}`, `{label}`, `{start_time}`, `{end_time}`, `{duration_seconds}`, `{status}`, `{message}`, `{detail}`, and `{error}`. If you need to output literal curly braces, write them as `{{` or `}}`.
</details>
-->

## Commands

* `!!restic status` View status
* `!!restic status p X` View page X of the restic snapshot list
* `!!restic restore SNAPSHOT` Queue a full-snapshot restore
* `!!restic restore SNAPSHOT file /server/path` Queue a single-file restore
* `!!restic restore SNAPSHOT folder /server/path` Queue a folder restore
* `!!restic restore list` View queued restore tasks
* `!!restic unrestore ID/all` Delete one/all restore tasks
* `!!restic restore apply` Apply the restore task queue
* `!!restic start` Enable scheduled backups
* `!!restic stop` Disable scheduled backups and request to stop the current backup
* `!!restic backup` Trigger an immediate backup
* `!!restic reload` Reload configuration

The default command permission level is `3`, which can be modified in the configuration.

## Build and Release

Run `pack\build.bat`, or `python tools/pack_plugin.py --output-dir dist`, to create an `.mcdr` archive with the standard MCDR plugin layout. The archive contains `mcdreforged.plugin.json`, `requirements.txt`, the entrypoint package, and all resources declared by the metadata.

GitHub Actions validates and stores a build artifact on every push or pull request. Pushing a Git tag such as `v0.5.0` automatically builds the archive and creates a GitHub Release containing the generated `.mcdr` file.

# Contributing

Pull Requests and Issues are highly welcome!

# Demo

The image below demonstrates the advantages of using Restic for Minecraft backups: each snapshot represents a full backup of that specific point in time, yet the total storage consumed is only about half of the actual data size.
![alt text](https://raw.githubusercontent.com/pfdr2333/MCDR2restic/main/image.png)

# License

This project is released under the **[GNU General Public License v3.0 (GPL-3.0)](https://github.com/pfdr2333/MCDR2restic/tree/main/LICENSE)**.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MCDR2Restic_v0.5.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.5.0) | 0.5.0 | 2026/08/08 20:12:04 | 151.34KB | 17 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.5.0/MCDR2Restic_v0.5.0.mcdr) |
| [MCDR2Restic_v0.4.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.4.0) | 0.4.0 | 2026/07/09 04:25:11 | 252.82KB | 6 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.4.0/MCDR2Restic_v0.4.0.mcdr) |
| [MCDR2restic_v0.3.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.3.0) | 0.3.0 | 2026/07/08 09:33:34 | 170.36KB | 4 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.3.0/MCDR2restic_v0.3.0.mcdr) |
| [MCDR2Restic_v0.2.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.2.0) | 0.2.0 | 2026/07/08 04:58:57 | 154.57KB | 5 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.2.0/MCDR2Restic_v0.2.0.mcdr) |
| [MCDR2restic_v0.1.9.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.9) | 0.1.9 | 2026/07/08 04:03:03 | 150.17KB | 5 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.9/MCDR2restic_v0.1.9.mcdr) |
| [MCDR2restic_v0.1.8.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.8) | 0.1.8 | 2026/07/08 02:17:27 | 149.04KB | 6 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.8/MCDR2restic_v0.1.8.mcdr) |
| [MCDR2restic_v0.1.7.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.7) | 0.1.7 | 2026/07/08 02:03:44 | 136.64KB | 6 | [Download](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.7/MCDR2restic_v0.1.7.mcdr) |

