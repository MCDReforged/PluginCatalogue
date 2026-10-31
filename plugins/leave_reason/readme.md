**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## leave_reason

### Basic Information

- Plugin ID: `leave_reason`
- Plugin Name: LeaveReason
- Version: 1.3.0
  - Metadata version: 1.3.0
  - Release version: 1.3.0
- Total downloads: 22
- Authors: [chuan_yi_awa](https://github.com/wellcy666)
- Repository: https://github.com/wellcy666/leave_reason
- Repository plugin page: https://github.com/wellcy666/leave_reason/tree/main/src
- Labels: [`Information`](/labels/information/readme.md)
- Description: Detect abnormal player disconnections (kick, timeout, ban, not whitelisted) and broadcast the reason to chat

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# LeaveReason

Detects abnormal player disconnections (kick, timeout, ban, not whitelisted) and broadcasts the reason to chat.

> Same plugin used by the AZ Tech Server, review group `1101978932`.

Parses server logs and fills in the "why" when a player leaves. The "who left" part itself is shown by the server or a chat forwarding plugin.

## Detectable reasons

| Reason             | Public chat example                                                     |
| ------------------ | ----------------------------------------------------------------------- |
| Kicked             | `xxx left the game, reason: kicked from server (You have been removed)` |
| Connection timeout | `xxx left the game, reason: connection timed out`                       |
| Banned             | `xxx left the game, reason: banned`                                     |
| Not whitelisted    | `xxx left the game, reason: not whitelisted`                            |
| Uncategorized      | `xxx left the game, reason: Attempting to attack an invalid entity`     |

All texts are configurable.

## How it works

- Kicked / timeout happen in-game, log is `<player> lost connection: <reason>`, player name is available directly.
- Banned is blocked by vanilla `banlist.json` at login, log is `Disconnecting <address>: You are banned ...`.
- Whitelist is blocked by vanilla `whitelist.json` at login, log is `Disconnecting <address>: You are not white-listed ...`.

> When banned / whitelist blocks at login, the log usually has no player name, so `message_no_name` is used instead. The backend log just doesn't record it — not a bug.

## Installation

Drop `leave_reason.mcdr` into MCDR's `plugins/` directory, then `!!MCDR plugin load leave_reason.mcdr` (or restart).

## Commands

| Command                | Description      | Permission |
| ---------------------- | ---------------- | ---------- |
| `!!lr`                 | Help             | 4          |
| `!!lr on` / `!!lr off` | Toggle broadcast | 4          |
| `!!lr reload`          | Reload config    | 4          |
| `!!lr status`          | Show status      | 4          |

Permission level 4 = owner / console. Prefix `!!lr` is the `PREFIX` constant in the code.

## Configuration

`config/leave_reason/config.json` is generated on first load, apply changes with `!!lr reload`. Common fields:

| Field                         | Purpose                                                                 |
| ----------------------------- | ----------------------------------------------------------------------- |
| `enabled`                     | Master switch                                                           |
| `message` / `message_no_name` | Message format, `{player}`=name, `{reason}`=reason                      |
| `reason_text`                 | Text for the four categories (`kick` / `timeout` / `ban` / `whitelist`) |
| `append_kick_detail`          | Append the raw kick reason                                              |
| `show_unknown`                | Also broadcast unmatched reasons                                        |
| `dedup_seconds`               | Dedup window per player + reason                                        |
| `keywords`                    | Classification keywords                                                 |

Minimal config:

```json
{
    "config_version": 2,
    "enabled": true,
    "message": "§7[§c!§7] §e{player} §7left the game, reason: §f{reason}",
    "message_no_name": "§7[§c!§7] §eA player §7was refused to join, reason: §f{reason}",
    "reason_text": {
        "kick": "Kicked from server",
        "timeout": "Connection timed out",
        "ban": "Banned",
        "whitelist": "Not whitelisted"
    }
}
```

Upgrading from 1.2.x: old configs without `config_version` get backed up as `config.json.bak`.

## Tuning

1. Set `debug` to `true` and `!!lr reload`, test with a non-whitelisted player and a banned player, check the `[leave_reason][debug]` output.
2. If the whitelist block isn't vanilla `not white-listed` but a plugin kicking players, add keywords from that custom text to `keywords.whitelist`.
3. Normal disconnects (`Disconnected`) are ignored in `keywords.ignore` by default; remove it to detect them.

## Feedback

QQ: `2683654412`.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [leave_reason.mcdr](https://github.com/wellcy666/leave_reason/releases/tag/v1.3.0) | 1.3.0 | 2026/10/22 13:25:03 | 8.62KB | 22 | [Download](https://github.com/wellcy666/leave_reason/releases/download/v1.3.0/leave_reason.mcdr) |

