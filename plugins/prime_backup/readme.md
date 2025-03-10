**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## prime_backup

### Basic Information

- Plugin ID: `prime_backup`
- Version: *Data fetching failed*
- Total downloads: 5081
- Authors: [Fallen_Breath](https://github.com/Fallen-Breath)
- Repository: https://github.com/TISUnion/PrimeBackup
- Repository plugin page: https://github.com/TISUnion/PrimeBackup/tree/master
- Labels: [`Management`](/labels/management/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

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
| [PrimeBackup-v1.8.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.3) | 1.8.3 | 2024/09/17 09:51:24 | 148.13KB | 1989 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.3/PrimeBackup-v1.8.3.pyz) |
| [PrimeBackup-v1.8.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.2) | 1.8.2 | 2024/09/11 13:09:48 | 148.12KB | 120 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.2/PrimeBackup-v1.8.2.pyz) |
| [PrimeBackup-v1.8.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.1) | 1.8.1 | 2024/07/22 09:46:44 | 147.69KB | 631 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.1/PrimeBackup-v1.8.1.pyz) |
| [PrimeBackup-v1.8.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.0) | 1.8.0 | 2024/07/22 09:48:39 | 147.61KB | 16 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.0/PrimeBackup-v1.8.0.pyz) |
| [PrimeBackup-v1.7.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.4) | 1.7.4 | 2024/04/20 10:07:23 | 146.64KB | 925 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.4/PrimeBackup-v1.7.4.pyz) |
| [PrimeBackup-v1.7.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.3) | 1.7.3 | 2024/03/10 18:48:38 | 146.27KB | 289 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.3/PrimeBackup-v1.7.3.pyz) |
| [PrimeBackup-v1.7.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.2) | 1.7.2 | 2024/02/25 01:48:39 | 146.17KB | 120 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.2/PrimeBackup-v1.7.2.pyz) |
| [PrimeBackup-v1.7.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.1) | 1.7.1 | 2024/02/24 18:44:14 | 146.19KB | 19 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.1/PrimeBackup-v1.7.1.pyz) |
| [PrimeBackup-v1.7.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.0) | 1.7.0 | 2024/02/24 17:50:46 | 145.99KB | 21 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.0/PrimeBackup-v1.7.0.pyz) |
| [PrimeBackup-v1.6.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.3) | 1.6.3 | 2024/01/02 09:28:32 | 141.03KB | 473 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.3/PrimeBackup-v1.6.3.pyz) |
| [PrimeBackup-v1.6.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.2) | 1.6.2 | 2023/12/26 15:28:18 | 141.02KB | 97 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.2/PrimeBackup-v1.6.2.pyz) |
| [PrimeBackup-v1.6.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.1) | 1.6.1 | 2023/12/23 13:07:44 | 140.69KB | 49 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.1/PrimeBackup-v1.6.1.pyz) |
| [PrimeBackup-v1.6.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.0) | 1.6.0 | 2023/12/22 18:09:21 | 140.68KB | 31 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.0/PrimeBackup-v1.6.0.pyz) |
| [PrimeBackup-v1.5.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.5.0) | 1.5.0 | 2023/12/18 18:16:48 | 138.58KB | 60 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.5.0/PrimeBackup-v1.5.0.pyz) |
| [PrimeBackup-v1.4.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.1) | 1.4.1 | 2023/12/17 16:53:56 | 135.02KB | 30 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.1/PrimeBackup-v1.4.1.pyz) |
| [PrimeBackup-v1.4.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.0) | 1.4.0 | 2023/12/16 12:24:06 | 134.92KB | 36 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.0/PrimeBackup-v1.4.0.pyz) |
| [PrimeBackup-v1.3.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.3.0) | 1.3.0 | 2023/12/13 16:12:06 | 126.51KB | 45 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.3.0/PrimeBackup-v1.3.0.pyz) |
| [PrimeBackup-v1.2.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.2.0) | 1.2.0 | 2023/12/12 18:23:26 | 124.45KB | 23 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.2.0/PrimeBackup-v1.2.0.pyz) |
| [PrimeBackup-v1.1.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.1.0) | 1.1.0 | 2023/12/11 18:06:40 | 120.68KB | 31 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.1.0/PrimeBackup-v1.1.0.pyz) |
| [PrimeBackup-v1.0.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.1) | 1.0.1 | 2023/12/10 17:26:14 | 116.92KB | 51 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.1/PrimeBackup-v1.0.1.pyz) |
| [PrimeBackup-v1.0.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.0) | 1.0.0 | 2023/12/10 15:15:49 | 116.83KB | 25 | [Download](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.0/PrimeBackup-v1.0.0.pyz) |

