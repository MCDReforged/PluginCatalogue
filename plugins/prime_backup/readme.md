**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## prime_backup

### Basic Information

- Plugin ID: `prime_backup`
- Plugin Name: Prime Backup
- Version: 1.12.0
  - Metadata version: 1.13.0-beta.4
  - Release version: 1.12.0
- Total downloads: 12944
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
| [blake3](https://pypi.org/project/blake3) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.12.0 |
| [pathspec](https://pypi.org/project/pathspec) |  |
| [psutil](https://pypi.org/project/psutil) |  |
| [pydantic](https://pypi.org/project/pydantic) | \>=2 |
| [pytz](https://pypi.org/project/pytz) |  |
| [typing_extensions](https://pypi.org/project/typing_extensions) |  |
| [xxhash](https://pypi.org/project/xxhash) | \>=3 |
| [zstandard](https://pypi.org/project/zstandard) |  |

```
pip install "APScheduler>=3.8,<4" "SQLAlchemy>=2" blake3 "mcdreforged>=2.12.0" pathspec psutil "pydantic>=2" pytz typing_extensions "xxhash>=3" zstandard
```

### Introduction

# Prime Backup

**English** | [中文](https://github.com/TISUnion/PrimeBackup/tree/master/README.zh.md)

A powerful backup plugin for MCDR, an advanced backup solution for your Minecraft world

Document: https://tisunion.github.io/PrimeBackup/

## Features

- Hash-based, compressed file pool deduplication. Only new or changed data is stored, with no hard limit on backup count
- Optional blob chunking algorithm. Supports CDC (content-defined chunking) for large, locally edited files to improve deduplication across backups
- Safe restore workflow: confirmation + countdown, automatic pre-restore backup, recycle-bin rollback, and data verification
- Comprehensive backup operations, including backup/restore, list/delete, import/export, comments/tags, etc.
- Smooth in-game interaction, with most operations achievable through mouse clicks
- Rich database toolkit: overview statistics, integrity validation, orphan cleanup, file deletion, and hash/compression method migration
- Highly customizable backup pruning strategies, similar to the strategy used by [PBS](https://pbs.proxmox.com/docs/prune-simulator/)
- Scheduled jobs for automatic backup creation and backup pruning, support fixed intervals and crontab expressions
- Provides a command-line tool if you want to manage backups without MCDR. Also supports mounting as a filesystem via FUSE

![!!pb command](https://raw.githubusercontent.com/TISUnion/PrimeBackup/master/docs/img/pb_welcome.png)

## Requirements

[MCDReforged](https://github.com/Fallen-Breath/MCDReforged) requirement: `>=2.12.0`

Python package requirements: See [requirements.txt](https://github.com/TISUnion/PrimeBackup/tree/master/requirements.txt)

## Usages

See the document: https://tisunion.github.io/PrimeBackup/

## How it works

Prime Backup maintains a custom file pool to store backup data. Every stored object is identified by a hash of its content.
With that, Prime Backup can deduplicate files with the same content, and only stores 1 copy of them, greatly reducing disk usage

Prime Backup also supports compression on stored data to further reduce disk usage

For large and locally edited files, Prime Backup can optionally use CDC (Content-Defined Chunking) for better deduplication.
The file is split into content-defined chunks. Each chunk is hashed and reused across backups when unchanged, only new chunks are stored

Prime Backup stores common file types, including regular files, directories, and symbolic links. For these 3 types:

- Regular file: Prime Backup calculates hashes (and size)
  If CDC is enabled, it stores the file as a chunked blob that references chunks; chunks are deduplicated and compressed individually
  Otherwise, it stores a direct blob; the whole file is deduplicated and compressed as a single unit
  File metadata such as mode, uid, and mtime are stored in the database
- Directory: Prime Backup stores its information in the database
- Symlink: Prime Backup stores the symlink itself instead of the linked target

## Thanks

The idea for the hash-based file pool is inspired by https://github.com/z0z0r4/better_backup

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [PrimeBackup-v1.12.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.12.0) | 1.12.0 | 2025/12/14 17:24:45 | 218.39KB | 1845 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.12.0/PrimeBackup-v1.12.0.pyz) |
| [PrimeBackup-v1.11.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.11.0) | 1.11.0 | 2025/08/30 17:39:56 | 210.03KB | 1424 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.11.0/PrimeBackup-v1.11.0.pyz) |
| [PrimeBackup-v1.10.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.3) | 1.10.3 | 2025/08/02 14:59:01 | 208.04KB | 625 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.3/PrimeBackup-v1.10.3.pyz) |
| [PrimeBackup-v1.10.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.2) | 1.10.2 | 2025/05/04 17:57:38 | 206.96KB | 1699 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.2/PrimeBackup-v1.10.2.pyz) |
| [PrimeBackup-v1.10.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.1) | 1.10.1 | 2025/05/03 18:12:53 | 206.92KB | 95 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.1/PrimeBackup-v1.10.1.pyz) |
| [PrimeBackup-v1.10.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.0) | 1.10.0 | 2025/04/30 17:19:43 | 206.52KB | 160 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.0/PrimeBackup-v1.10.0.pyz) |
| [PrimeBackup-v1.9.5.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.5) | 1.9.5 | 2025/03/30 15:12:03 | 173.98KB | 634 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.5/PrimeBackup-v1.9.5.pyz) |
| [PrimeBackup-v1.9.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.4) | 1.9.4 | 2025/03/29 16:10:17 | 173.99KB | 96 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.4/PrimeBackup-v1.9.4.pyz) |
| [PrimeBackup-v1.9.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.3) | 1.9.3 | 2025/03/29 13:29:39 | 173.93KB | 60 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.3/PrimeBackup-v1.9.3.pyz) |
| [PrimeBackup-v1.9.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.2) | 1.9.2 | 2025/03/28 08:51:03 | 173.92KB | 70 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.2/PrimeBackup-v1.9.2.pyz) |
| [PrimeBackup-v1.9.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.1) | 1.9.1 | 2025/03/15 12:51:27 | 172.43KB | 286 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.1/PrimeBackup-v1.9.1.pyz) |
| [PrimeBackup-v1.9.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.0) | 1.9.0 | 2025/03/15 10:26:03 | 172.42KB | 53 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.0/PrimeBackup-v1.9.0.pyz) |
| [PrimeBackup-v1.8.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.3) | 1.8.3 | 2024/09/17 09:51:24 | 148.13KB | 2109 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.3/PrimeBackup-v1.8.3.pyz) |
| [PrimeBackup-v1.8.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.2) | 1.8.2 | 2024/09/11 13:09:48 | 148.12KB | 158 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.2/PrimeBackup-v1.8.2.pyz) |
| [PrimeBackup-v1.8.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.1) | 1.8.1 | 2024/07/22 09:46:44 | 147.69KB | 676 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.1/PrimeBackup-v1.8.1.pyz) |
| [PrimeBackup-v1.8.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.0) | 1.8.0 | 2024/07/22 09:48:39 | 147.61KB | 51 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.0/PrimeBackup-v1.8.0.pyz) |
| [PrimeBackup-v1.7.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.4) | 1.7.4 | 2024/04/20 10:07:23 | 146.64KB | 966 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.4/PrimeBackup-v1.7.4.pyz) |
| [PrimeBackup-v1.7.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.3) | 1.7.3 | 2024/03/10 18:48:38 | 146.27KB | 323 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.3/PrimeBackup-v1.7.3.pyz) |
| [PrimeBackup-v1.7.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.2) | 1.7.2 | 2024/02/25 01:48:39 | 146.17KB | 153 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.2/PrimeBackup-v1.7.2.pyz) |
| [PrimeBackup-v1.7.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.1) | 1.7.1 | 2024/02/24 18:44:14 | 146.19KB | 54 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.1/PrimeBackup-v1.7.1.pyz) |
| [PrimeBackup-v1.7.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.0) | 1.7.0 | 2024/02/24 17:50:46 | 145.99KB | 56 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.0/PrimeBackup-v1.7.0.pyz) |
| [PrimeBackup-v1.6.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.3) | 1.6.3 | 2024/01/02 09:28:32 | 141.03KB | 507 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.3/PrimeBackup-v1.6.3.pyz) |
| [PrimeBackup-v1.6.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.2) | 1.6.2 | 2023/12/26 15:28:18 | 141.02KB | 131 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.2/PrimeBackup-v1.6.2.pyz) |
| [PrimeBackup-v1.6.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.1) | 1.6.1 | 2023/12/23 13:07:44 | 140.69KB | 82 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.1/PrimeBackup-v1.6.1.pyz) |
| [PrimeBackup-v1.6.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.0) | 1.6.0 | 2023/12/22 18:09:21 | 140.68KB | 63 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.0/PrimeBackup-v1.6.0.pyz) |
| [PrimeBackup-v1.5.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.5.0) | 1.5.0 | 2023/12/18 18:16:48 | 138.58KB | 93 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.5.0/PrimeBackup-v1.5.0.pyz) |
| [PrimeBackup-v1.4.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.1) | 1.4.1 | 2023/12/17 16:53:56 | 135.02KB | 62 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.1/PrimeBackup-v1.4.1.pyz) |
| [PrimeBackup-v1.4.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.0) | 1.4.0 | 2023/12/16 12:24:06 | 134.92KB | 69 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.0/PrimeBackup-v1.4.0.pyz) |
| [PrimeBackup-v1.3.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.3.0) | 1.3.0 | 2023/12/13 16:12:06 | 126.51KB | 80 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.3.0/PrimeBackup-v1.3.0.pyz) |
| [PrimeBackup-v1.2.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.2.0) | 1.2.0 | 2023/12/12 18:23:26 | 124.45KB | 58 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.2.0/PrimeBackup-v1.2.0.pyz) |
| [PrimeBackup-v1.1.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.1.0) | 1.1.0 | 2023/12/11 18:06:40 | 120.68KB | 65 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.1.0/PrimeBackup-v1.1.0.pyz) |
| [PrimeBackup-v1.0.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.1) | 1.0.1 | 2023/12/10 17:26:14 | 116.92KB | 83 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.1/PrimeBackup-v1.0.1.pyz) |
| [PrimeBackup-v1.0.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.0) | 1.0.0 | 2023/12/10 15:15:49 | 116.83KB | 58 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.0/PrimeBackup-v1.0.0.pyz) |

