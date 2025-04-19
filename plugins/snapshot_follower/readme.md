**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## snapshot_follower

### Basic Information

- Plugin ID: `snapshot_follower`
- Plugin Name: Snapshot Follower
- Version: 1.2.0
  - Metadata version: 1.2.0
  - Release version: 1.2.0
- Total downloads: 14
- Authors: [Fallen_Breath](https://github.com/Fallen-Breath)
- Repository: https://github.com/Fallen-Breath/SnapshotFollower
- Repository plugin page: https://github.com/Fallen-Breath/SnapshotFollower/tree/master
- Labels: [`Management`](/labels/management/readme.md)
- Description: Keep your Minecraft server up-to-date with the latest snapshot

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install mcdreforged requests
```

### Introduction

# Snapshot Follower

**English** | [中文](https://github.com/Fallen-Breath/SnapshotFollower/tree/master/README_cn.md)

Keep your Minecraft server up-to-date with the latest snapshot

The plugin periodically queries about the latest Minecraft snapshot from [mojang API](https://launchermeta.mojang.com/mc/game/version_manifest.json).
When a new snapshot is spotted, it will download the snapshot `server.jar`, stop the running server, replace the `server.jar`
and finally start the server with the latest Minecraft snapshot

> [!NOTE] 
> When the plugin is loaded or the server starts, the plugin will try to detect the current Minecraft version of the server 
> by reading the `version.json` inside the jar file, so it knows if the currently running Minecraft version matches the latest snapshot.
> 
> If the detection fails, the plugin will simply assume that the current Minecraft version is the latest snapshot

Optionally, an HTTP POST webhook can be triggered when the update finishes

## Configuration

Config file path: `config/snapshot_follower/config.json`

```json5
{
    "enabled": true,  // Switch of the plugin, default true

    "check_interval": 60.0,  // Interval between each check
    "server_jar_path": "server/server.jar",  // Path of the server jar file. It needs to be writeable for the update-ability
    "keep_downloaded_jar": true,  // If it should keep the downloaded server.jar file after updating. Downloaded jars will be at `config/snapshot_follower/jars`
    "version_blacklist": [],  // A version blacklist. Versions inside will be ignored. Useful for skipping those unwanted snapshots

    "http_proxy": "http://127.0.0.1:1081",  // Optional, a http proxy url to be used for HTTP requesting
    "https_proxy": "http://127.0.0.1:1081",  // Optional, a http proxy url to be used for HTTP requesting
    "request_timeout": 10.0,  // HTTP request timeout, in seconds

    "webhook": {
        "enabled": true,  // Switch of the webwook feature. An HTTP POST request will be sent when the update finishes
        "use_http_proxy": false,  // If the webhook HTTP request should use the http proxy defined above
        "url": "http://127.0.0.1:8080/my/callback",  // Webhook url
        "headers": {  // Webhook HTTP headers. Can be empty
            "Authorization": "Bearer foobar"
        },
        "body": "Server has been updated to {{version}}"  // Webhook body. The placeholder {{version}} will be replaced with the updated version (e.g. 24w39a)
    }
}
```

## TODO

- [ ] Broadcast, wait and delay-if-requested before update
- [ ] Backup (using other plugins) before update

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [SnapshotFollower-v1.2.0.mcdr](https://github.com/Fallen-Breath/SnapshotFollower/releases/tag/v1.2.0) | 1.2.0 | 2025/04/02 19:02:45 | 7.54KB | 2 | [Download](https://github.com/Fallen-Breath/SnapshotFollower/releases/download/v1.2.0/SnapshotFollower-v1.2.0.mcdr) |
| [SnapshotFollower-v1.1.0.mcdr](https://github.com/Fallen-Breath/SnapshotFollower/releases/tag/v1.1.0) | 1.1.0 | 2024/10/01 17:59:34 | 7.35KB | 12 | [Download](https://github.com/Fallen-Breath/SnapshotFollower/releases/download/v1.1.0/SnapshotFollower-v1.1.0.mcdr) |

