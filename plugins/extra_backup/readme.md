**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## extra_backup

### Basic Information

- Plugin ID: `extra_backup`
- Plugin Name: Extra Backup
- Version: 1.0.1
  - Metadata version: 1.1.0
  - Release version: 1.0.1
- Total downloads: 53
- Authors: [AVJANO](https://github.com/AVJANO)
- Repository: https://github.com/AVJANO/ExtraBackup
- Repository plugin page: https://github.com/AVJANO/ExtraBackup/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: A distributed archive backup plugin based on PrimeBackup that can automatically export archives and back them up to different locations

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.7 |
| [prime_backup](/plugins/prime_backup/readme.md) | \>=1.10.3 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [schedule](https://pypi.org/project/schedule) | \>=1.2.2 |

```
pip install "schedule>=1.2.2"
```

### Introduction

# ExtraBackup

> **ExtraBackup------为你的存档找一个（好几个）温馨的家**\
> 基于 MCDR
> 实现的分布式备份插件，可将备份自动上传至本地硬盘、NAS、甚至百度网盘（未来），用于防止服务器硬盘突然暴毙
> :P

> 注意：需要搭配PrimeBackup插件使用，没有Fallen的前置工作，这个插件不可能实现

当前版本仅实现了**本地硬盘备份**的功能；FTP 等模式仍在开发中。

------------------------------------------------------------------------

## 📦 功能简介

- 自动上传并导出 PrimeBackup 的备份文件
- 分布式存储（支持多个备份路径）
- 自动跳过重复文件
- 支持下载、删除、清理、语言切换
- 支持按时间间隔的定时任务（上传 & 清理）

------------------------------------------------------------------------

## 🧭 指令教程

### `!!exb upload <id> [tag]`

上传备份文件夹（通常是 `pb_files/export`）中的指定文件
- `id` 支持 `latest`、`~3` 等 PrimeBackup 特殊 ID
- `tag` 为备份文件的自定义标签（可不写）

------------------------------------------------------------------------

### `!!exb uploadall`

上传备份文件夹中的 **所有备份文件**，自动跳过重复文件。

------------------------------------------------------------------------

### `!!exb download <file_name> [from]`

从指定备份路径下载文件到本地
- `file_name`: 备份文件名
- `from`: 备份路径名称（可留空，留空则从任意可用路径随机下载）

------------------------------------------------------------------------

### `!!exb list [location]`

列出指定备份路径下的所有文件
- `location` 留空 → 列出本地备份文件

------------------------------------------------------------------------

### `!!exb prune [id]`

清理过时文件
- 指定 `id` → 清理该备份（无视是否过时）
- 留空 → 清理所有过时文件
- 过时时间由配置文件设定

------------------------------------------------------------------------

### `!!exb delete <file_name> <location>`

删除指定备份路径下的指定备份。

------------------------------------------------------------------------

### `!!exb lang <language>`

切换语言。\
支持：

- `zh_cn`（中文）
- `en_us`（英文）

------------------------------------------------------------------------

## ⚙️ 配置教程

### 主配置 `config.json`

``` jsonc
{
    "enable": "false",            // 是否启用该插件
    "language": "zh_cn",          // 默认语言
    "max_thread": "-1",           // 上传/下载最大线程数，-1 为无限制

    "schedule_backup": {
        "enable": "false",        // 是否启用定时上传备份
        "interval": "30m"         // 上传时间间隔
    },

    "schedule_prune": {
        "enable": "false",        // 是否启用定时清理
        "interval": "1d",         // 定时清理时间间隔
        "max_lifetime": "3d",     // 文件最大生命时间

        "prune_downloads": "true", // 是否清理 exb_downloads 文件夹
        "prune_exports": "true"   // 是否清理 pb 导出文件夹
    }
}
```

------------------------------------------------------------------------

## 📁 备份路径配置 `backup_path.json`

``` jsonc
{
    "Name1": {                          // 备份路径名称（支持中文）
        "enable": "false",              // 是否启用这个备份路径
        "mode": "ftp",                  // 备份模式："local" = 本地路径；"ftp" = FTP 远程模式
        "address": "ftp://example.com/folder", // local: 写本地路径；ftp: 写服务器地址
        "username": "username",         // FTP 用户名；local 模式留空（保留双引号）
        "password": "123456"            // FTP 密码；local 模式留空（保留双引号）
    },

    "Name2": {
        "enable": "true",
        "mode": "local",
        "address": "/folder/example",   // 本地地址
        "username": "",                 // local 留空（但双引号必须保留）
        "password": ""                  // local 留空
    }
}
                                        // 可自行扩展更多备份路径
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ExtraBackup-v1.0.1.pyz](https://github.com/AVJANO/ExtraBackup/releases/tag/v1.0.1) | 1.0.1 | 2025/11/21 01:09:59 | 97.55KB | 39 | [Download](https://github.com/AVJANO/ExtraBackup/releases/download/v1.0.1/ExtraBackup-v1.0.1.pyz) |
| [ExtraBackup-v0.1.7-alpha.pyz](https://github.com/AVJANO/ExtraBackup/releases/tag/v0.1.7) | 0.1.7 | 2025/09/02 13:38:38 | 109.68KB | 14 | [Download](https://github.com/AVJANO/ExtraBackup/releases/download/v0.1.7/ExtraBackup-v0.1.7-alpha.pyz) |

