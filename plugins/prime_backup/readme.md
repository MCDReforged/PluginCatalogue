**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## prime_backup

### Basic Information

- Plugin ID: `prime_backup`
- Plugin Name: Prime Backup
- Version: 1.10.2
  - Metadata version: 1.10.2
  - Release version: 1.10.2
- Total downloads: 7528
- Authors: [Fallen_Breath](https://github.com/Fallen-Breath)
- Repository: https://github.com/TISUnion/PrimeBackup
- Repository plugin page: https://github.com/TISUnion/PrimeBackup/tree/master
- Labels: [`Management`](/labels/management/readme.md)
- Description: A powerful backup plugin for MCDR, an advanced backup solution for your Minecraft world

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [APScheduler](https://pypi.org/project/APScheduler) | \>=3.8,\<4 |
| [SQLAlchemy](https://pypi.org/project/SQLAlchemy) | \>=2 |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.12.0 |
| [pathspec](https://pypi.org/project/pathspec) |  |
| [psutil](https://pypi.org/project/psutil) |  |
| [pytz](https://pypi.org/project/pytz) |  |
| [typing_extensions](https://pypi.org/project/typing_extensions) |  |
| [xxhash](https://pypi.org/project/xxhash) | \>=3 |
| [zstandard](https://pypi.org/project/zstandard) |  |

```
pip install "APScheduler>=3.8,<4" "SQLAlchemy>=2" "mcdreforged>=2.12.0" pathspec psutil pytz typing_extensions "xxhash>=3" zstandard
```

### Introduction

# Prime Backup

**English** | [中文](https://github.com/TISUnion/PrimeBackup/tree/master/README.zh.md)

A powerful backup plugin for MCDR, an advanced backup solution for your Minecraft world

Document: https://tisunion.github.io/PrimeBackup/

## Features

- Only stores files with changes with the hash-based file pool. Supports unlimited number of backup
- Comprehensive backup operations, including backup/restore, list/delete, import/export, etc
- Smooth in-game interaction, with most operations achievable through mouse clicks
- Highly customizable backup pruning strategies, similar to the strategy use by [PBS](https://pbs.proxmox.com/docs/prune-simulator/)
- Crontab jobs, including automatic backup, automatic pruning, etc.
- Supports use as a command-line tool. Manage the backups without MCDR

![!!pb command](https://raw.githubusercontent.com/TISUnion/PrimeBackup/master/docs/img/pb_welcome.png)

## Requirements

[MCDReforged](https://github.com/Fallen-Breath/MCDReforged) requirement: `>=2.12.0`

Python package requirements: See [requirements.txt](https://github.com/TISUnion/PrimeBackup/tree/master/requirements.txt)

## Usages

See the document: https://tisunion.github.io/PrimeBackup/

## How it works

Prime Backup maintains a custom file pool to store the backup files. Every file in the pool is identified with the hash value of its content.
With that, Prime Backup can deduplicate files with same content, and only stores 1 copy of them, greatly reduces the burden on disk usage.

Besides that, Prime Backup also supports compression on the stored files, which reduces the disk usage further more

PrimeBackup is capable of storing various of common file types, including regular files, directories, and symbolic links. For these 3 types:

- Regular file: Prime Backup calculates its hash values first. If the hash does not exist in the file pool, 
  Prime backup will (compress and) store its content into a new blob in the file pool.
  The file status, including mode, uid, mtime etc., will be stored in the database
- Directory: Prime Backup will store its information in the database
- Symlink: Prime Backup will store the symlink itself, instead of the linked target

## Thanks

The idea for the hash-based file pool is inspired by https://github.com/z0z0r4/better_backup

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [PrimeBackup-v1.10.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.2) | 1.10.2 | 2025/05/04 17:57:38 | 206.96KB | 1249 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.2/PrimeBackup-v1.10.2.pyz) |
| [PrimeBackup-v1.10.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.1) | 1.10.1 | 2025/05/03 18:12:53 | 206.92KB | 45 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.1/PrimeBackup-v1.10.1.pyz) |
| [PrimeBackup-v1.10.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.0) | 1.10.0 | 2025/04/30 17:19:43 | 206.52KB | 110 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.0/PrimeBackup-v1.10.0.pyz) |
| [PrimeBackup-v1.9.5.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.5) | 1.9.5 | 2025/03/30 15:12:03 | 173.98KB | 566 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.5/PrimeBackup-v1.9.5.pyz) |
| [PrimeBackup-v1.9.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.4) | 1.9.4 | 2025/03/29 16:10:17 | 173.99KB | 55 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.4/PrimeBackup-v1.9.4.pyz) |
| [PrimeBackup-v1.9.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.3) | 1.9.3 | 2025/03/29 13:29:39 | 173.93KB | 18 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.3/PrimeBackup-v1.9.3.pyz) |
| [PrimeBackup-v1.9.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.2) | 1.9.2 | 2025/03/28 08:51:03 | 173.92KB | 32 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.2/PrimeBackup-v1.9.2.pyz) |
| [PrimeBackup-v1.9.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.1) | 1.9.1 | 2025/03/15 12:51:27 | 172.43KB | 249 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.1/PrimeBackup-v1.9.1.pyz) |
| [PrimeBackup-v1.9.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.0) | 1.9.0 | 2025/03/15 10:26:03 | 172.42KB | 14 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.0/PrimeBackup-v1.9.0.pyz) |
| [PrimeBackup-v1.8.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.3) | 1.8.3 | 2024/09/17 09:51:24 | 148.13KB | 2065 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.3/PrimeBackup-v1.8.3.pyz) |
| [PrimeBackup-v1.8.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.2) | 1.8.2 | 2024/09/11 13:09:48 | 148.12KB | 122 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.2/PrimeBackup-v1.8.2.pyz) |
| [PrimeBackup-v1.8.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.1) | 1.8.1 | 2024/07/22 09:46:44 | 147.69KB | 636 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.1/PrimeBackup-v1.8.1.pyz) |
| [PrimeBackup-v1.8.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.0) | 1.8.0 | 2024/07/22 09:48:39 | 147.61KB | 18 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.0/PrimeBackup-v1.8.0.pyz) |
| [PrimeBackup-v1.7.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.4) | 1.7.4 | 2024/04/20 10:07:23 | 146.64KB | 930 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.4/PrimeBackup-v1.7.4.pyz) |
| [PrimeBackup-v1.7.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.3) | 1.7.3 | 2024/03/10 18:48:38 | 146.27KB | 290 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.3/PrimeBackup-v1.7.3.pyz) |
| [PrimeBackup-v1.7.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.2) | 1.7.2 | 2024/02/25 01:48:39 | 146.17KB | 121 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.2/PrimeBackup-v1.7.2.pyz) |
| [PrimeBackup-v1.7.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.1) | 1.7.1 | 2024/02/24 18:44:14 | 146.19KB | 20 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.1/PrimeBackup-v1.7.1.pyz) |
| [PrimeBackup-v1.7.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.0) | 1.7.0 | 2024/02/24 17:50:46 | 145.99KB | 22 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.0/PrimeBackup-v1.7.0.pyz) |
| [PrimeBackup-v1.6.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.3) | 1.6.3 | 2024/01/02 09:28:32 | 141.03KB | 475 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.3/PrimeBackup-v1.6.3.pyz) |
| [PrimeBackup-v1.6.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.2) | 1.6.2 | 2023/12/26 15:28:18 | 141.02KB | 98 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.2/PrimeBackup-v1.6.2.pyz) |
| [PrimeBackup-v1.6.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.1) | 1.6.1 | 2023/12/23 13:07:44 | 140.69KB | 50 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.1/PrimeBackup-v1.6.1.pyz) |
| [PrimeBackup-v1.6.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.0) | 1.6.0 | 2023/12/22 18:09:21 | 140.68KB | 32 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.0/PrimeBackup-v1.6.0.pyz) |
| [PrimeBackup-v1.5.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.5.0) | 1.5.0 | 2023/12/18 18:16:48 | 138.58KB | 61 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.5.0/PrimeBackup-v1.5.0.pyz) |
| [PrimeBackup-v1.4.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.1) | 1.4.1 | 2023/12/17 16:53:56 | 135.02KB | 31 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.1/PrimeBackup-v1.4.1.pyz) |
| [PrimeBackup-v1.4.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.0) | 1.4.0 | 2023/12/16 12:24:06 | 134.92KB | 37 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.0/PrimeBackup-v1.4.0.pyz) |
| [PrimeBackup-v1.3.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.3.0) | 1.3.0 | 2023/12/13 16:12:06 | 126.51KB | 46 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.3.0/PrimeBackup-v1.3.0.pyz) |
| [PrimeBackup-v1.2.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.2.0) | 1.2.0 | 2023/12/12 18:23:26 | 124.45KB | 25 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.2.0/PrimeBackup-v1.2.0.pyz) |
| [PrimeBackup-v1.1.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.1.0) | 1.1.0 | 2023/12/11 18:06:40 | 120.68KB | 33 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.1.0/PrimeBackup-v1.1.0.pyz) |
| [PrimeBackup-v1.0.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.1) | 1.0.1 | 2023/12/10 17:26:14 | 116.92KB | 52 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.1/PrimeBackup-v1.0.1.pyz) |
| [PrimeBackup-v1.0.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.0) | 1.0.0 | 2023/12/10 15:15:49 | 116.83KB | 26 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.0/PrimeBackup-v1.0.0.pyz) |

