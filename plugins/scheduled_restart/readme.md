**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## scheduled_restart

### Basic Information

- Plugin ID: `scheduled_restart`
- Plugin Name: Scheduled Restart
- Version: 1.2.1
  - Metadata version: 1.2.1
  - Release version: 1.2.1
- Total downloads: 11
- Authors: [fangzi2006](https://github.com/fangzi2006)
- Repository: https://github.com/fangzi2006/MCDR-Scheduled-Restart
- Repository plugin page: https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src
- Labels: [`Management`](/labels/management/readme.md)
- Description: Cron-style scheduled server restarts with configurable multi-stage notifications (chat / title)

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# scheduled_restart · MCDReforged Scheduled Restart Plugin

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

![MCDReforged](https://img.shields.io/badge/MCDReforged-%3E%3D2.12.0-green.svg)

Schedule Minecraft server restarts with **Linux cron expressions**, and send **chat messages** or
**titles (title/subtitle)** to all players at multiple configured times before the restart.

- Core feature: automatic scheduled restart (uses MCDR's `restart` by default; can also just stop the server / stop and exit MCDR / run a custom command)
- Any combination by month / week / day / hour / minute: `0 4 * * *`, `30 3 * * 1`, `0 5 1 * *`, `@daily`, …
- Unlimited notifications, written as **an array of objects**, each with its own advance time and delivery method
- Delivery methods: `chat` (tellraw), `title`, `actionbar`, `command` (arbitrary command)
- Supports `§` legacy color codes and the `color` field, optional sound effects, and placeholders
- Whispers the countdown to players on join; restart history persisted to disk; config hot-reload; a single broken config entry only skips itself
- Pure Python, **no third-party dependencies**, ships its own cron parser (no `croniter` needed)
- Schedules can be managed with in-game commands: `list` / `add` / `remove` / `enable` / `disable` / `test`

---

## Installation

**Option 1: Install with an MCDR command (recommended)**

Run this in the MCDR console or in-game (requires admin permission):

```
!!MCDR plugin install scheduled_restart
```

Afterwards run `!!MCDR plugin reload scheduled_restart`, or restart MCDR.

**Option 2: Download the plugin package**

Download `scheduled_restart-v<version>.mcdr` from the [Releases](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../../../releases/latest) page and drop it into
MCDR's `plugins/` directory, then restart MCDR or run `!!MCDR plugin load <filename>`.

**Option 3: Directory plugin**

Put everything under `src/` into `plugins/scheduled_restart/`, so the final layout looks like:

```
plugins/scheduled_restart/mcdreforged.plugin.json
plugins/scheduled_restart/scheduled_restart/__init__.py
```

The config file is generated on first load: `config/scheduled_restart/config.json`
(see [examples/config.json](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../examples/config.json)).

> The default config ships with just 1 example schedule and it has `"enabled": false`, so **it will not
> restart out of the box**. Run `!!srestart reload` after editing, or create a new schedule directly with
> `!!srestart add <name> <cron>`.

---

## Quick Start

1. Edit `config/scheduled_restart/config.json`, set the example schedule's `enabled` to `true`,
   or copy it and change the `cron`:

   ```json
   {
     "name": "Daily 4AM restart",
     "enabled": true,
     "cron": "0 4 * * *",
     "restart_method": "mcdr_restart",
     "use_default_notifications": true
   }
   ```

2. Run `!!srestart reload` in-game or in the console (requires admin permission).

3. Run `!!srestart list` to confirm the "next restart time"; run `!!srestart test <index>`
   to preview what those notifications look like in-game right away (it will not actually restart).

---

## Configuration Reference

### Top-level fields

| Field                       | Type          | Default     | Description                                                                                                                                                                 |
| --------------------------- | ------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                   | bool          | `true`      | Master switch; no scheduling at all when `false`                                                                                                                            |
| `timezone`                  | string | null | `null`      | Timezone such as `"Asia/Shanghai"`; `null` means follow the local timezone of the MCDR process                                                                              |
| `check_interval_seconds`    | number        | `1.0`       | Scheduler thread polling interval (seconds); usually no need to change                                                                                                      |
| `skip_missed_notifications` | bool          | `true`      | Whether to skip notifications that are already expired when the plan is generated (avoids a burst of stale notifications right after a reload)                              |
| `notify_on_join`            | bool          | `true`      | Whether to whisper the restart countdown to players when they join                                                                                                          |
| `join_message`              | string        | see example | Join whisper content, supports placeholders                                                                                                                                 |
| `log_history`               | bool          | `true`      | Whether to write every restart to `config/scheduled_restart/history.jsonl`                                                                                                  |
| `history_size`              | int           | `100`       | How many recent entries to keep when the history file grows too large                                                                                                       |
| `command_alias`             | string        | `""`        | Custom shorthand command prefix, e.g. `"!!sr"`; leave empty to keep only `!!srestart`                                                                                       |
| `default_notifications`     | array         | 1 example   | **Default notification group**, used when a schedule has `use_default_notifications: true`                                                                                  |
| `schedules`                 | array         | 3 examples  | Restart schedule list                                                                                                                                                       |
| `_readme`                   | array         | —           | Notes written inside the config file, for reading only; edit freely (JSON has no comments, so the notes live in this field; all examples avoid characters needing escaping) |

### `schedules[]` (schedules)

| Field                       | Type   | Default        | Description                                                                                                                          |
| --------------------------- | ------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `name`                      | string | `ScheduleN`    | Schedule name; you can also refer to it by index in commands; duplicates get `#2` appended                                           |
| `enabled`                   | bool   | `true`         | Whether this schedule is enabled                                                                                                     |
| `cron`                      | string | required       | cron expression, see the next section                                                                                                |
| `restart_method`            | string | `mcdr_restart` | `mcdr_restart` / `stop` / `stop_exit` / `custom` / `none`                                                                            |
| `custom_command`            | string | `stop`         | The server command to send when `restart_method=custom`                                                                              |
| `custom_auto_start`         | bool   | `false`        | In `custom` mode, whether to auto `start()` after the server stops                                                                   |
| `restart_delay_seconds`     | number | `0`            | Extra delay in seconds before actually restarting (supports `"30s"`, `"1m"`); **notifications are based on the real restart moment** |
| `kick_players`              | bool   | `false`        | Whether to `kick @a` before restarting (the `@a` selector needs 1.20.3+)                                                             |
| `kick_message`              | string | see example    | Kick message                                                                                                                         |
| `use_default_notifications` | bool   | `true`         | `true` uses the top-level `default_notifications`; `false` uses this schedule's own `notifications`                                  |
| `notifications`             | array  | `[]`           | This schedule's own notifications; if this array is present but `use_default_notifications` is omitted, it is treated as `false`     |

`restart_method` explained:

- `mcdr_restart`: calls MCDR's `server.restart()` (soft stop → wait → start again), the MCDR process keeps running
- `stop`: only sends the stop command, MCDR keeps running (good when an external supervisor handles restarts)
- `stop_exit`: stops the server and exits MCDR too (good when systemd or similar pulls it back up)
- `custom`: executes `custom_command`, optionally with `custom_auto_start`
- `none`: only sends notifications, no restart (useful for "announce upcoming maintenance")

### `notifications[]` (notifications)

| Field                          | Type            | Default                               | Description                                                                                                                                                                                                                                                                               |
| ------------------------------ | --------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                      | bool            | `true`                                | Whether this notification is enabled                                                                                                                                                                                                                                                      |
| `advance_time`                 | number | string | `60`                                  | How far in advance to send it; accepts a plain number of seconds, or duration text such as `"5m"`, `"1h30m"`                                                                                                                                                                              |
| `type`                         | string          | `chat`                                | `chat` / `title` / `actionbar` / `command`                                                                                                                                                                                                                                                |
| `message`                      | string          | `""`                                  | Text for `chat` / `actionbar`                                                                                                                                                                                                                                                             |
| `title`                        | string          | `""`                                  | Main title for `title`                                                                                                                                                                                                                                                                    |
| `subtitle`                     | string          | `""`                                  | Subtitle for `title`                                                                                                                                                                                                                                                                      |
| `times`                        | object          | `{"fade_in":1,"stay":4,"fade_out":1}` | Title fade-in / stay / fade-out durations, **in seconds** (converted to ticks internally)                                                                                                                                                                                                 |
| `color`                        | string | null   | `null`                                | Color name (`yellow`, `red`, `gold`…) or `#RRGGBB`; you can also use `§e` directly in the text                                                                                                                                                                                            |
| `sound`                        | string | null   | `null`                                | Sound ID such as `minecraft:block.note_block.pling`, played after the notification                                                                                                                                                                                                        |
| `sound_source`                 | string          | `master`                              | Sound channel; on older servers (1.8~1.12) set it to `""` to omit that argument                                                                                                                                                                                                           |
| `sound_position`               | string          | `"@s"`                                | Where the sound plays: `"@s"` = each player hears it at their own position (1.13+, via `execute as @a at @s`); coordinate text (`"~ ~ ~"`, `"100 64 100"`) = fixed position (works on 1.8+, `~ ~ ~` from console equals world spawn); `""` = omit coordinates as well as volume and pitch |
| `sound_volume` / `sound_pitch` | number          | `1.0`                                 | Volume / pitch (ignored when `sound_position` is empty)                                                                                                                                                                                                                                   |
| `command`                      | string          | `""`                                  | The command to send when `type=command`, supports placeholders                                                                                                                                                                                                                            |

A complete "multiple notifications" example:

```json
{
  "name": "Daily 4AM restart",
  "enabled": true,
  "cron": "0 4 * * *",
  "restart_method": "mcdr_restart",
  "use_default_notifications": false,
  "notifications": [
    { "advance_time": "30m", "type": "chat",  "message": "§e[Maintenance] §fServer restarts in §b{remaining}§f (at §b{time}§f)" },
    { "advance_time": "10m", "type": "title", "title": "§eRestart countdown", "subtitle": "§fRemaining §b{remaining}",
      "times": { "fade_in": 0.5, "stay": 3, "fade_out": 0.5 },
      "sound": "minecraft:block.note_block.pling" },
    { "advance_time": 60, "type": "actionbar", "message": "§c60 seconds until restart" },
    { "advance_time": 10, "type": "title", "title": "§cRestarting now!", "subtitle": "§fFind a safe spot to log off" },
    { "advance_time": 0,  "type": "chat",  "message": "§c[Maintenance] §fThe server is restarting, please reconnect shortly" }
  ]
}
```

---

## cron Syntax

Standard Linux cron: **5 fields** `minute hour day month weekday`; **6 fields** `second minute hour day month weekday` is also supported.

| Syntax                                                                               | Meaning                                                  |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| `*` / `?`                                                                            | Any value                                                |
| `5`                                                                                  | Exact value                                              |
| `1-10`                                                                               | Range                                                    |
| `1,3,5`                                                                              | List                                                     |
| `*/15`                                                                               | Step (every 15 minutes)                                  |
| `1-10/2`                                                                             | Step within a range                                      |
| `5/10`                                                                               | Start at 5, step 10 up to the maximum (cronie extension) |
| `JAN`~`DEC`                                                                          | Month abbreviations                                      |
| `SUN`~`SAT`                                                                          | Weekday abbreviations; both `0` and `7` mean Sunday      |
| `@yearly` / `@monthly` / `@weekly` / `@daily`(`@midnight`) / `@hourly` / `@minutely` | Common macros                                            |

Common examples:

| cron           | Meaning                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------- |
| `0 4 * * *`    | Every day at 04:00                                                                                                  |
| `30 3 * * 1`   | Every Monday at 03:30                                                                                               |
| `0 5 1 * *`    | The 1st of every month at 05:00                                                                                     |
| `0 0 1 1 *`    | Every January 1st at 00:00                                                                                          |
| `0 */6 * * *`  | Every 6 hours (0, 6, 12, 18)                                                                                        |
| `0 4 * * 1,4`  | Every Monday and Thursday at 04:00                                                                                  |
| `0 4 1 * 1`    | The 1st of the month **or** every Monday at 04:00 (day and weekday restrictions are OR'd, matching cron convention) |
| `30 0 4 * * *` | 6-field form: every day at 04:00:30                                                                                 |
| `@daily`       | Every day at 00:00                                                                                                  |

`!!srestart list` translates each expression into Chinese (e.g. `每天 04:00`, `每周一 03:30`) so you can double-check it.

---

## Placeholders

Use these in `message` / `title` / `subtitle` / `command` / `join_message`; they are substituted when sent:

| Placeholder           | Meaning                             | Example               |
| --------------------- | ----------------------------------- | --------------------- |
| `{remaining}`         | Remaining time in Chinese format    | `5分`, `1小时2分3秒`       |
| `{remaining_seconds}` | Remaining seconds (integer)         | `300`                 |
| `{remaining_minutes}` | Remaining minutes (rounded up)      | `5`                   |
| `{time}`              | Restart time of day                 | `04:00:00`            |
| `{date}`              | Restart date                        | `2026-07-22`          |
| `{datetime}`          | Full timestamp                      | `2026-07-22 04:00:00` |
| `{schedule}`          | Schedule name                       | `每天凌晨4点重启`            |
| `{cron}`              | cron expression                     | `0 4 * * *`           |
| `{index}` / `{total}` | Which notification / how many total | `2` / `5`             |

---

## Commands & Permissions

Root command: `!!srestart` (`!!srestart help` shows help). **All players** can view the schedule list and the next
restart time; `status` / `history` require **helper**; modifying commands require **admin**; the console has the
highest permission by default.

If you set `command_alias` in the config (for example `"!!sr"`), then `!!sr` is fully equivalent to `!!srestart` —
help text, tab completion, and permission checks all apply to both.

> **Minecraft's `/op` is not the same as MCDR's admin.** MCDR has its own independent permission system,
> and Minecraft op players do **not** automatically get admin permission.
> To let a player use modifying commands, run this in the console:
> `!!MCDR permission set <player> admin`.

Schedules are referred to by **index** (the `[#1]`, `[#2]`… shown by `!!srestart list`), and schedule names are
accepted too; the index is the schedule's position in the `schedules` array + 1, so it never shifts even if some
schedule is skipped due to a config error.

| Command                                 | Permission  | Description                                                                                                       |
| --------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| `!!srestart list`                       | All players | All schedules: index, enabled state, cron, description, next restart time with remaining time, notification count |
| `!!srestart next`                       | All players | Next restart time and countdown                                                                                   |
| `!!srestart status`                     | helper      | Master switch, scheduler thread, timezone, current plan, config warnings/errors                                   |
| `!!srestart history [count]`            | helper      | Recent restart records (time / schedule / method / automatic or manual)                                           |
| `!!srestart test <index|name>`          | admin       | Sends that schedule's notifications in advance order, **no restart**, for previewing                              |
| `!!srestart enable [<index|name>|all]`  | admin       | Enable a schedule and **write it to the config file** (takes effect immediately)                                  |
| `!!srestart disable [<index|name>|all]` | admin       | Disable a schedule and **write it to the config file** (takes effect immediately); no argument means all          |
| `!!srestart add <name> <cron>`          | admin       | Create a schedule: enabled by default, uses the top-level `default_notifications` group                           |
| `!!srestart remove <index|name>`        | admin       | Delete a schedule                                                                                                 |
| `!!srestart reload`                     | admin       | Re-read the config file and rebuild the schedule                                                                  |
| `!!srestart cancel`                     | admin       | Cancel the pending restart (skips this run; the next one still happens as scheduled)                              |

A few examples:

```
!!srestart list                                    # see the indexes
!!srestart add DailyRestart 0 4 * * *              # create: every day 04:00, effective immediately
!!srestart add "Weekly Monday" 30 3 * * 1          # quote names containing spaces
!!srestart test 2                                  # preview schedule #2's notifications (no restart)
!!srestart disable 2                               # turn off schedule #2 and write it to the config file
!!srestart enable all                              # turn on all schedules
!!srestart remove 2                                # delete schedule #2
```

Both indexes and schedule names support tab completion. **To restart the server right now, use MCDR's own
`!!MCDR server restart`** (this plugin focuses on "restart on schedule" and deliberately does not duplicate an
immediate-restart command).

> `add` only requires "name + cron": the created schedule is enabled by default and uses the top-level default
> notification group; to give a schedule its own notifications, edit its `notifications` in the config file and
> set `use_default_notifications` to `false`.
> 
> `enable` / `disable` modify **the config file** (persistent), they do not apply to the current run only;
> they write the `enabled` field of the matching entry in the `schedules` array and leave everything else
> (your own extra fields, the informational `_readme`, etc.) untouched. So a schedule that is disabled in the
> config file can still be turned on with a command.

---

## FAQ

**Q: Why are all schedules disabled in the default config?**
To avoid the server restarting unexpectedly right after you install the plugin. Change `enabled` and reload.

**Q: Why is `{remaining}` off by a few seconds?**
Scheduling precision is `check_interval_seconds` (1 second by default); notifications fire "when the time comes",
so normal drift stays within 1 second.

**Q: After a plugin reload / server restart, are past notifications re-sent?**
Not by default (`skip_missed_notifications: true`). For example, if you start the plugin at 3:59 for a 4:00 restart,
the 5-minute and 1-minute notifications are marked expired and skipped, and only the ones still in time are sent;
set it to `false` to re-send everything immediately.

**Q: Why doesn't `timezone` work on Windows?**
Python cannot read Windows' built-in timezone database; you need `pip install tzdata` to use names like
`"Asia/Shanghai"`. Without it a warning is printed and it falls back to the local timezone of the MCDR process.

**Q: Why doesn't `kick_players` work?**
`kick @a` requires Minecraft 1.20.3+. On older versions keep it `false` and let the server kick players naturally
on shutdown, or use a `type: "command"` notification to send your own `tellraw` / `kickall` command.

**Q: Should I use `stop` or `mcdr_restart`?**
Use `mcdr_restart` if MCDR handles the restart; if systemd / screen / a panel or another external supervisor pulls
the server back up, use `stop` (or `stop_exit` so MCDR exits too, avoiding getting stuck).

**Q: I configured `sound` but hear nothing / get a coordinate error.**
Java's `playsound` syntax is `playsound <sound> [<channel>] <target> [<position>] [<volume>] [<pitch>]`,
and **position comes before volume**: to customize volume/pitch you must provide coordinates first, otherwise
`… @a 1 1` is parsed as coordinates (which need x y z) and errors out.

The plugin defaults to `"sound_position": "@s"`, generating:

```
execute as @a at @s run playsound <sound> master @s ~ ~ ~ <volume> <pitch>
```

meaning **each player hears it at their own position** (1.13+). If you prefer anchoring the sound at a fixed
location, set `sound_position` to coordinate text; if the server is **1.12 or older** (no `execute as/at`), use
`"sound_position": "~ ~ ~"` together with `"sound_source": ""`:

```json
{ "advance_time": 30, "type": "title", "title": "§eRestart countdown",
  "sound": "minecraft:block.note_block.pling",
  "sound_source": "", "sound_position": "~ ~ ~" }
```

> Notifications also support `type: "command"`, so you can write your own `playsound` / `title` command and bypass
> these conventions entirely.

**Q: What happens if the config has mistakes?**
* A single field with the wrong type → the default value is used, a warning is logged, and the plugin keeps running
  (it also writes the normalized config back to the file)
* A whole schedule with a broken `cron` → only that schedule is skipped, an error is logged, and
  **nothing is written back** (your content is preserved so you can fix it)
* Both warnings and errors are visible via `!!srestart status` or the console log

**Q: Can I configure multiple schedules?**
Yes. The scheduler only ever executes "the nearest" restart to avoid two schedules fighting each other; a cancelled
run will not trigger again.

**Q: How do I restart the server immediately?**
Use MCDR's own `!!MCDR server restart` (admin). This plugin's `trigger` command was removed on purpose — it only
borrowed a schedule's restart method while skipping all notifications, so it had little to do with the schedule
itself. If you want players notified before an immediate restart, set the cron to the nearest minute/hour, or use
`!!srestart test <index>` to preview the notification text first.

**Q: Do `enable` / `disable` change the config file, or only the current run?**
They change the config file (persistent): they write `schedules[i].enabled` and hot-reload immediately. So a
schedule that is disabled in the config file can still be turned on with `!!srestart enable <index>`; a schedule
with a broken cron can be toggled by index too, and the plugin reminds you that "the cron is invalid, fix it before
it actually takes effect". Nothing else in the config file (your own extra fields, etc.) is touched.

**Q: What happens to notifications while the server is not running?**
They are skipped with a warning (`服务器当前未运行，跳过提醒`). When the server process is gone, MCDR cannot deliver
`tellraw` / `title` into the game and only logs `Server has been terminated, cannot send command to its stdin`;
the schedule itself is kept and will run normally once the server is back. Restarts behave the same way — they are
skipped rather than pretending to succeed while the server is down.

**Q: Where do I see the plugin's own logs?**
They go to the MCDR console (prefix `[scheduled_restart]`). MCDR's `logs/MCDR.log` mainly records MCDR's own
messages, so the plugin additionally writes every restart to `config/scheduled_restart/history.jsonl`, viewable
with `!!srestart history`.

---

## Design Notes

* **Single-schedule scheduling**: the scheduler thread wakes up every `check_interval_seconds`, works out "the
  nearest restart among all enabled schedules", and maintains only that one; every second it checks whether any
  notification has come due.
* **Notification time = real restart moment − `advance_time`**; `restart_delay_seconds` shifts that baseline too,
  so wording like "5 minutes left" always stays accurate.
* **Restarts run in a separate worker thread**: `server.restart()` blocks until the server is back up, so running
  it in a worker thread avoids stalling the scheduling loop; notifications are paused during a restart.
* **Duplicate-trigger protection**: a "schedule + moment" pair that already triggered or was cancelled is recorded,
  so the same moment can never restart twice.
* **cron efficiency**: it jumps day by day to find matching dates, then picks the nearest time within that day,
  instead of brute-force scanning minute by minute.
* **Indexes stay aligned with the config file**: each schedule remembers its position in the `schedules` array
  (`source_index`), and the `[#N]` shown by `list` is that +1; even if a schedule is skipped due to a bad cron, the
  indexes never shift, so `enable/disable/remove <index>` always points at the one you saw.
* **Config-modifying commands write the file directly**: `enable / disable / add / remove` only touch the
  corresponding entry's fields in the `schedules` array, leaving your own extra fields and informational content
  intact; writes use "write a temp file then replace"; UTF-8 BOM is stripped before reading, and a thoroughly
  corrupted file is first backed up as `config.json.broken-<timestamp>` before being regenerated.

---

## License

Copyright (C) 2026 fangzi2006 <1439885013@qq.com>

This project is released under the **GNU General Public License v3.0 or later**; full terms are in [LICENSE](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../LICENSE).
You may freely use, modify, and redistribute it, but derivative works must be open-sourced under the same license.
See [CHANGELOG.md](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../CHANGELOG.md) for the change log.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [scheduled_restart-v1.2.1.mcdr](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/tag/v1.2.1) | 1.2.1 | 2026/10/03 11:26:56 | 36.41KB | 7 | [Download](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/download/v1.2.1/scheduled_restart-v1.2.1.mcdr) |
| [scheduled_restart-v1.1.1.mcdr](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/tag/v1.1.1) | 1.1.1 | 2026/09/30 12:15:10 | 35.29KB | 4 | [Download](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/download/v1.1.1/scheduled_restart-v1.1.1.mcdr) |

