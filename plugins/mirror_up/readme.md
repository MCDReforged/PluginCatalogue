**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mirror_up

### Basic Information

- Plugin ID: `mirror_up`
- Plugin Name: MirrorUP
- Version: 0.6.4
  - Metadata version: 0.6.4
  - Release version: 0.6.4
- Total downloads: 26
- Authors: [MiYui34](https://github.com/MiYui34)
- Repository: https://github.com/MiYui34/MirrorUP
- Repository plugin page: https://github.com/MiYui34/MirrorUP/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Incremental mirror sync: only changed files and changed region chunks are transferred.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [xxhash](https://pypi.org/project/xxhash) |  |

```
pip install xxhash
```

### Introduction

# MirrorUP

Incremental mirror sync for MCDR: only files that actually changed are transferred, and `.mca` regions are synced chunk by chunk.

## Features

- **File-level increment**: a cross-run index remembers every file's `size / mtime / hash`, so unchanged files are never read or copied again.
- **Chunk-level increment**: only dirty chunks inside a region are touched (timestamp filter + hash confirmation); unchanged chunks are reused in place.
- **Mirror drift recovery**: files modified on the mirror side are detected on the next round and restored.
- **Atomic writes**: data goes to a temporary file first, then `os.replace`; a half-written file never appears on the mirror, and failures are retried next round.
- **In-place region writes**: `.mca` uses append-and-commit with an 8 KB header journal, so changing one chunk writes about one chunk; fragmentation is compacted automatically.
- **External chunks too**: regions whose chunks live in `.mcc` files only move their placeholder records; `.mcc` contents are synced as ordinary files, and orphaned `.mcc` files are cleaned up.
- **Cross-machine sync**: the main server can run as a read-only `exporter` (HTTP + Bearer token, optional TLS pinning), so the mirror does not need the main server's disk mounted.
- **Automatic server stop**: `rcon`, MCSManager (`mcsm`), custom commands (`external`) and `self` (the server this MCDR manages). If the target cannot be stopped, nothing is written.
- **Multiple mirror targets**: one source, several mirror directories, each with its own stop method.
- **Verify & history**: `!!mu verify` checks source / mirror / index consistency (`--deep` compares hashes), `!!mu history` lists past rounds.
- **Scheduled sync**: interval from 60 seconds to 7 days, toggleable at runtime.

## Requirements

MCDR ≥ 2.12.0, Python ≥ 3.9, `xxhash`.

## Install

1. Put the plugin into MCDR's `plugins/` directory (the packed `MirrorUP-v0.6.4.mcdr` or the `MirrorUP/` folder).
2. `pip install xxhash`. MCDR only verifies requirements, it does not install them; a missing package shows `RequirementCheckFailure` in the log.
3. Restart MCDR. `config/mirror_up/config.json` is generated on first load.

## Quick start

1. Edit `source.root` (main server directory) and `target.root` (mirror directory). Relative paths are resolved against the **MCDR root**, not the server working directory.
2. `!!mu diff` prints the plan without touching anything.
3. `!!mu sync` stops the mirror (if needed), writes the difference and starts it again.
4. For periodic sync: `!!mu schedule set 30m` then `!!mu schedule on`.

## Configuration (highlights)

| Key                         | Default         | Meaning                                                                                               |
| --------------------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| `source.root`               | `./server`      | Main server directory (the one containing `world/`, `mods/`)                                          |
| `source.transport`          | `local`         | `local` reads the disk directly; `agent` pulls from an exporter                                       |
| `role`                      | `driver`        | `driver` runs sync; `exporter` only serves data                                                       |
| `targets`                   | one `default`   | `[{"name","root","enabled","mirror_control"?}]`, per-target overrides                                 |
| `sets`                      | `world`, `mods` | Directories to sync; `config/` and `server.properties` are excluded by default                        |
| `sync.concurrency`          | `4`             | Parallel copy workers                                                                                 |
| `sync.verify_target`        | `true`          | Detect files changed on the mirror each round                                                         |
| `sync.region_delta`         | `true`          | Chunk-level `.mca` sync; `false` falls back to whole files                                            |
| `sync.region_write_mode`    | `inplace`       | `inplace` appends and commits; `rebuild` writes a new file and replaces                               |
| `sync.journal`              | `true`          | 8 KB region header snapshot for `inplace`; `false` forces `rebuild`                                   |
| `source_flush.enabled`      | `true`          | `save-off` + `save-all flush` around the scan; auto-disabled for `agent` transport and `self` targets |
| `mirror_control.adapter`    | `manual`        | `manual` only checks; `rcon` / `external` / `mcsm` / `self` stop and start the server                 |
| `schedule.interval_seconds` | `3600`          | Auto-sync interval, 60 – 604800 seconds                                                               |

## In-place sync: run the command on the server you want to sync

Use the `self` adapter when the plugin is installed on every server and players run `!!mu sync` wherever they are:

- **Main server**: `role: "exporter"`, serves its world read-only via `agent_server` + token.
- **Mirror**: `role: "driver"`, `source.transport: "agent"` pointing at the main server, and a single target pointing at itself:

```json
"targets": [
  { "name": "self", "root": "./server",
    "mirror_control": { "adapter": "self", "notify_players_sec": 10 } }
]
```

`adapter: "self"` means "the target is the server this MCDR manages". When something changed, the plugin:

1. announces the restart (`notify_players_sec` seconds, `0` disables it);
2. calls `server.stop()` — **MCDR itself keeps running**;
3. waits for `session.lock` to be released, then writes the difference;
4. calls `server.start()` and waits until the server is reachable again.

Because only the server process stops, the sync thread keeps running. When nothing changed, none of these steps happen — it is just a `stat` sweep.

## Cross-machine sync (optional)

1. **Main server** (same plugin installed): `role: "exporter"`, `agent_server.host: "0.0.0.0"`, a random `token` of at least 16 characters, then `!!mu reload`. The log shows the exporter listening.
2. **Mirror** (driver): `source.transport: "agent"`, `source.agent.url: "http://<main-ip>:25580"`, same token.
3. For public networks, enable TLS (`agent_server.tls`) and pin the certificate with `source.agent.tls_pin_sha256`.

The exporter is read-only: it never writes and never runs sync commands. `source_flush` is disabled automatically in this mode; make sure the main server's world is flushed (`save-all flush`) before syncing.

## Commands

| Command                 | Permission | Meaning                                                 |
| ----------------------- | ---------- | ------------------------------------------------------- |
| `!!mu sync`             | 2          | Sync once                                               |
| `!!mu sync --dry-run`   | 2          | Plan only, nothing is written                           |
| `!!mu sync --full`      | 2          | Ignore the index, re-hash everything                    |
| `!!mu sync --force`     | 2          | Skip safety checks (empty source, version gate)         |
| `!!mu diff`             | 2          | Same as `--dry-run`                                     |
| `!!mu status`           | 0          | Index size, last sync per target, pending retries       |
| `!!mu verify [--deep]`  | 2          | Check source / mirror / index; `--deep` compares hashes |
| `!!mu history [N]`      | 0          | Recent rounds (default 10, max 50)                      |
| `!!mu cancel`           | 2          | Cancel the running sync                                 |
| `!!mu schedule on|off`  | 3          | Toggle auto-sync                                        |
| `!!mu schedule set 30m` | 3          | Set the interval (`s`/`m`/`h`/`d`)                      |
| `!!mu index rebuild`    | 3          | Drop the index; next round is a full sync               |
| `!!mu reload`           | 3          | Reload the configuration                                |

## Notes

- **The mirror must be fully stopped for writes**. `manual` uses `session.lock`; `rcon` / `external` / `self` stop it automatically. If it cannot be stopped, the sync aborts and nothing is written.
- **No backups**. Overwritten chunks and mod files have no previous versions.
- **Write volume ≠ read volume**. With `inplace`, changing one chunk writes that chunk plus 16 KB (new header + journal); `rebuild` rewrites the whole region.
- **Configuration files are not synced**. `config/` and `server.properties` are outside the default sets; adding them overwrites the mirror's own configuration.
- **Empty-source guard**: if the source scans to 0 files while the index has records, the sync aborts instead of wiping the mirror. Use `--force` only when you really mean it.
- **Version gate**: source and mirror `level.dat` MC versions must match.

## Version

`0.6.4` — file-level + chunk-level increment, in-place region writes (header journal + compaction), mirror drift recovery, scheduled sync, cross-machine agent transport (with TLS), `.mcc` external chunk increment and orphan cleanup, multiple mirror targets, verify & history, MCSM/rcon/external/self auto stop, in-place sync (`adapter: "self"`), Python API.

`0.6.2` fix: `!!MCDR plugin install mirror_up` used to fail with `Invalid chat component: Illegal character in path` because MCDR builds the PyPI link from the raw requirement string (`xxhash>=3.0`) and `>` is not a legal URL character. The catalogue reads the dependency list from `requirements.txt` in the repository (not from the `requirements` field in `mcdreforged.plugin.json`), so 0.6.1 only changing the latter had no effect; 0.6.2 also changes `requirements.txt` to plain `xxhash`.

`0.6.3` fix: loading the plugin as `role: "exporter"` could block for seconds while binding the agent port, because `HTTPServer.server_bind()` calls `socket.getfqdn()` for a reverse DNS lookup; on macOS this made MCDR's watchdog report `TaskExecutor has not responded for 10 seconds`. The server now binds directly without the lookup.

`0.6.4` fix: cross-machine sync opened a new TCP connection for every file (plus a second `/v1/stat` request to verify each download), so tens of thousands of small files spent hours in handshakes alone. Each worker thread now reuses one keep-alive connection and transparently reconnects when the peer closes it; `sync.concurrency` defaults to 8; new `source.agent.verify_copy` (default `true`) can be set to `false` to skip the per-file verification round trip.

## License

[GPL-3.0](https://github.com/MiYui34/MirrorUP/tree/main/LICENSE) © MiYui34.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MirrorUP-v0.6.4.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.4) | 0.6.4 | 2026/11/14 03:56:56 | 90.07KB | 1 | [Download](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.4/MirrorUP-v0.6.4.mcdr) |
| [MirrorUP-v0.6.3.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.3) | 0.6.3 | 2026/11/10 13:10:15 | 89.25KB | 6 | [Download](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.3/MirrorUP-v0.6.3.mcdr) |
| [MirrorUP-v0.6.2.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.2) | 0.6.2 | 2026/11/10 12:53:45 | 89.04KB | 5 | [Download](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.2/MirrorUP-v0.6.2.mcdr) |
| [MirrorUP-v0.6.1.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.1) | 0.6.1 | 2026/11/10 11:44:39 | 89.04KB | 6 | [Download](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.1/MirrorUP-v0.6.1.mcdr) |
| [MirrorUP-v0.6.0.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.0) | 0.6.0 | 2026/11/09 07:21:01 | 89.05KB | 8 | [Download](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.0/MirrorUP-v0.6.0.mcdr) |

