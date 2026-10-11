**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## velocity_forget_me

### Basic Information

- Plugin ID: `velocity_forget_me`
- Plugin Name: Velocity Forget Me
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 4
- Authors: tanh_Heng
- Repository: https://github.com/LazyAlienServer/VelocityForgetMe
- Repository plugin page: https://github.com/LazyAlienServer/VelocityForgetMe/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Clear a RememberMe server record after an immediate player disconnect.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.2.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# Velocity Forget Me

[中文](https://github.com/LazyAlienServer/VelocityForgetMe/tree/main/./README.md) | English

A helper plugin for Velocity based on [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) and [RememberMe](https://github.com/ActualPlayer/RememberMe). When a player connects to a backend server and disconnects shortly afterwards because of a connection failure, it removes the file record so the player is not sent back to the failing server on the next login.

## Features

- Supports a configurable connection-log regular expression.
- Uses `(player, server)` as the session identity.
  - Sessions for the same player on different servers are independent.
- Treats a same-server connection followed by a disconnect within three seconds as an immediate disconnect by default.
- Removes a record only when all of these conditions hold:
  - a matching connection session exists;
  - the connection and disconnect server names are equal;
  - the disconnect is within the configured time window;
  - the player's UUID is resolved successfully;
  - the RememberMe file content equals the server name.

## Dependencies

- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) `>=2.2.0`
- Network access to the PlayerDB API.

## Limitations

- [VelocityRememberServer](https://github.com/TISUnion/VelocityRememberServer) is not currently planned for support. [RememberMe](https://github.com/ActualPlayer/RememberMe) may be a newer alternative for this use case.
- Only file-based RememberMe records are supported; LuckPerms `last-server` metadata is not supported.
- If no matching disconnect event arrives, the session remains in memory until that session disconnects or the plugin is unloaded/reloaded.
- UUID resolution depends on the external PlayerDB service; records are retained when lookup fails.

## Preview

```
[Server] [23:38:45 INFO]: [server connection] tanh_Heng -> survival has connected
[Server] [23:38:45 INFO]: [server connection] tanh_Heng -> creative has disconnected
[Server] [23:38:45 INFO]: [connected player] tanh_Heng (/223.64.14.141:10642) has disconnected
[Server] [23:38:45 INFO]: [server connection] tanh_Heng -> survival has disconnected
[MCDR] [23:38:45] [Thread-48 (process)/INFO] [velocity_forget_me]: Removed RememberMe record for tanh_Heng after an early disconnect
```
Next time when tanh_Heng join Velocity, he won't join survival server.

## Configuration File

The default configuration is:

```json
{
    "record_directory": "plugins/rememberme",
    "disconnect_window_seconds": 3.0,
    "connection_regex": "^\\[server connection\\]\\s*(?P<player>[A-Za-z0-9_]{1,16})\\s*->\\s*(?P<server>\\S+)\\s+has\\s+(?P<action>connected|disconnected)$",
    "uuid_api_url": "https://playerdb.co/api/player/minecraft/{player}",
    "uuid_api_timeout_seconds": 5.0,
    "uuid_cache_seconds": 3600.0
}
```

### Configuration options

**record_directory** `str` | Default: `plugins/rememberme`
- Directory containing RememberMe records. Relative paths are resolved against MCDR's configured `working_directory`.

**disconnect_window_seconds** `float` | Default: `3.0`
- Must be greater than `0`. Maximum time between connection and disconnect for record removal.

**connection_regex** `str` | Default: `^\\[server connection\\]\\s*(?P<player>[A-Za-z0-9_]{1,16})\\s*->\\s*(?P<server>\\S+)\\s+has\\s+(?P<action>connected|disconnected)$`
- Matches `Info.content` and must define named groups `player` (player name), `server` (server name), and `action` (`connected` or `disconnected`). The default matches:

  ```text
  [server connection] Steve -> lobby has connected
  [server connection] Steve -> lobby has disconnected
  ```

- MCDR removes the timestamp and thread prefix before exposing `Info.content`; the expression does not need to match the complete raw log line.

**uuid_api_url** `str` | Default: `https://playerdb.co/api/player/minecraft/{player}`
- Must be an HTTP(S) URL template containing `{player}`.

**uuid_api_timeout_seconds** `float` | Default: `5.0`
- Must be greater than `0`. UUID request timeout.

**uuid_cache_seconds** `float` | Default: `3600.0`
- Must be non-negative. Cache duration for online UUIDs by player name. This only reduces API requests and does not change server-scoped session isolation.

## RememberMe Record Format

The plugin expects one file per player:

```text
<record_directory>/<uuid>.txt
```

The file should contain the saved server name, for example:

```text
lobby
```

Before removal, all three values must be equal:

```text
connection server == disconnect server == file content
```

If the file contains `survival` while the session is for `lobby`, the file is retained.

## Logging

The plugin does not log every successful connection and disconnect.

Typical messages are:

- `INFO`: record removed successfully;
- `WARNING`: invalid configuration, UUID lookup failure, server mismatch, or record mismatch;
- `ERROR`: file read/delete failure or an unexpected processing exception;
- `DEBUG`: record missing or disappearing before deletion.

A successful removal looks like:

```text
Removed RememberMe record for Player after an early disconnect
```

## Invalid Configuration

The plugin uses MCDR's native config loader:

- If the config file does not exist, MCDR creates it with the default values;
- If the file cannot be read or contains an invalid value, the plugin logs a `WARNING` and disables processing;
- The plugin does not continue with an unvalidated configuration;
- Reload the plugin after editing the configuration.

## Developer Documentation

Implementation details, session isolation, event ordering, and threading are documented in [Developer Documentation](https://github.com/LazyAlienServer/VelocityForgetMe/tree/main/./docs/development_en.md).

*This plugin is completed with AI's assistance.*

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [VelocityForgetMe-v1.0.0.mcdr](https://github.com/LazyAlienServer/VelocityForgetMe/releases/tag/v1.0.0) | 1.0.0 | 2026/08/05 16:11:13 | 18.73KB | 4 | [Download](https://github.com/LazyAlienServer/VelocityForgetMe/releases/download/v1.0.0/VelocityForgetMe-v1.0.0.mcdr) |

