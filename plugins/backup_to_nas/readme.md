**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## backup_to_nas

### Basic Information

- Plugin ID: `backup_to_nas`
- Plugin Name: Backup To Nas
- Version: 0.1.4
  - Metadata version: 0.1.4
  - Release version: 0.1.4
- Total downloads: 22
- Authors: [renzaifei](https://github.com/ren-zaifei)
- Repository: https://github.com/SDK-Minecraft-Server/BackupToNas
- Repository plugin page: https://github.com/SDK-Minecraft-Server/BackupToNas/tree/release
- Labels: [`Management`](/labels/management/readme.md)
- Description: Package the save backup as a ZIP archive and transfer it to the remote NAS using the SFTP protocol.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.10.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.10.0 |
| [paramiko](https://pypi.org/project/paramiko) | \>=3.4.0 |

```
pip install "mcdreforged>=2.10.0" "paramiko>=3.4.0"
```

### Introduction

# Backup To Nas

[简体中文](https://github.com/SDK-Minecraft-Server/BackupToNas/tree/release/README_CN.md)

Backup To Nas is an MCDReforged plugin for backing up Minecraft worlds to a remote NAS. It creates ZIP archives and transfers them over SFTP.

## Features

- Back up one or more configured worlds and upload the archive.
- Run backups on a schedule.
- Manually upload existing `.zip` files from the temporary directory.
- Query upload progress.
- Configure MCDR permission levels and SFTP connection settings.

## Installation

The plugin requires MCDR 2.10.0 or newer and Paramiko:

```bash
pip install -r requirements.txt
```

If MCDR was installed with pipx, inject Paramiko into that environment:

```bash
pipx inject mcdreforged paramiko
```

The first load creates `config/backup_to_nas/config.json`.

## Configuration

```json
{
    "permissions": {
        "help": 0,
        "make": 3,
        "interval": 3,
        "status": 0,
        "upload": 3
    },
    "interval": "",
    "temp": "./backup_to_nas",
    "turn_off_auto_save": true,
    "server_path": "./server",
    "world_names": ["world"],
    "ignore_session_lock": true,
    "sftp": {
        "host": "192.168.1.100",
        "port": 22,
        "username": "root",
        "password_file": "/etc/mcdr/backup_to_nas/sftp_password",
        "private_key_file": "",
        "remote_dir": "/minecraft-backups",
        "timeout": 30,
        "auto_add_host_key": false
    }
}
```

`server_path`, `temp`, and `world_names` select the local world locations. Relative paths use MCDR's working directory; absolute paths are recommended for production.

Choose exactly one SFTP authentication method:

- `password_file` points to a file containing the password. Trailing newlines are ignored.
- `private_key_file` points to an SSH private key.

The two fields cannot both be configured. Credentials are read from files instead of being stored in JSON. `auto_add_host_key` defaults to `false`, so the NAS host key must be added to `known_hosts` manually. Set it to `true` only when you explicitly accept automatically trusting unknown hosts.

An empty `interval` disables automatic backups. Use values such as `1s`, `30s`, `1h`, or `1d`; reload the plugin after editing the configuration.

## Commands

The default command prefix is `!!btn`:

| Command                     | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| `!!btn`                     | Show help                                                          |
| `!!btn make`                | Create and upload a backup immediately                             |
| `!!btn interval <interval>` | Set the automatic backup interval, for example `!!btn interval 6h` |
| `!!btn interval off`        | Disable automatic backups                                          |
| `!!btn status`              | Show current or last SFTP upload status                            |
| `!!btn upload`              | Upload `.zip` files from the top level of the temporary directory  |

Backups and manual uploads cannot run at the same time. Failed ZIP files remain in the temporary directory and can be retried with `!!btn upload`.

## Permissions

Each value is the minimum MCDR permission level required by that command:

| Level | Role     |
| ----: | -------- |
|     0 | Everyone |
|     1 | User     |
|     2 | Helper   |
|     3 | Admin    |
|     4 | Owner    |

The fields `permissions.help`, `permissions.make`, `permissions.interval`, `permissions.status`, and `permissions.upload` control each command. The root `help` permission also gates subcommands.


## License

This project is licensed under LGPL-3.0. See [LICENSE](https://github.com/SDK-Minecraft-Server/BackupToNas/tree/release/LICENSE).

The backup portion is inspired by [PermanentBackup](https://github.com/TISUnion/PermanentBackup).

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [BackupToNas-0.1.4.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.4) | 0.1.4 | 2026/09/22 10:30:24 | 11.28KB | 5 | [Download](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.4/BackupToNas-0.1.4.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.3) | 0.1.3 | 2026/09/22 02:23:05 | 8.41KB | 5 | [Download](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.3/BackupToNas.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.2) | 0.1.2 | 2026/09/22 02:13:57 | 11.26KB | 4 | [Download](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.2/BackupToNas.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.1) | 0.1.1 | 2026/09/22 01:21:32 | 8.63KB | 4 | [Download](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.1/BackupToNas.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.0) | 0.1.0 | 2026/09/22 01:10:48 | 8.59KB | 4 | [Download](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.0/BackupToNas.mcdr) |

