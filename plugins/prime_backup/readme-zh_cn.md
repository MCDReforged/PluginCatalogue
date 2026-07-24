[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## prime_backup

### 基本信息

- 插件 ID: `prime_backup`
- 插件名: Prime Backup
- 版本: 1.13.1
  - 元数据版本: 1.13.1
  - 发布版本: 1.13.1
- 总下载量: 14179
- 作者: [Fallen_Breath](https://github.com/Fallen-Breath)
- 仓库: https://github.com/TISUnion/PrimeBackup
- 仓库插件页: https://github.com/TISUnion/PrimeBackup/tree/master
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一个强大的MCDR备份插件，一套先进的Minecraft存档备份解决方案

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### 包依赖

| Python 包 | 依赖需求 |
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

### 介绍

# Prime Backup

[English](https://github.com/TISUnion/PrimeBackup/tree/master/README.md) | 中文

一个强大的 MCDR 备份插件，一套先进的 Minecraft 世界备份解决方案

中文文档：https://tisunion.github.io/PrimeBackup/zh/

## 功能特性

- 基于哈希的文件池与压缩去重：仅存储新增或变更的数据，备份数量没有上限
- 可选的文件分块算法：支持使用固定大小分块（Fixed-Size Chunking）、内容定义分块（Content-Defined Chunking）等算法，将文件切分成多个数据块并逐个哈希去重储存，进一步提升去重效果
- 紧凑的数据块存储方案：使用打包文件批量存储数据块文件，有效避免创建大量小文件时对文件系统的压力
- 安全的回档流程：包含确认与倒计时、回档前自动创建备份、回收站式的回滚机制以及数据完整性校验
- 流畅的游戏内交互，大部分操作都能点点点
- 完善的备份操作：包括备份回档、列表查看、差异展示、导入导出等
- 丰富的数据库工具，含对象查询、数据库概览、数据完整性校验、孤儿数据清理、备份文件删除、哈希/压缩算法迁移等功能
- 高度可自定义的备份清理策略，是 [PBS](https://pbs.proxmox.com/docs/prune-simulator/) 所用策略的同款
- 定时任务：支持自动创建备份和自动清理备份，计划方式支持固定间隔和 crontab 表达式
- 支持作为命令行工具使用，无需启动 MCDR 即可管理备份，还可以通过 FUSE 挂载为文件系统进行访问

![!!pb command](https://raw.githubusercontent.com/TISUnion/PrimeBackup/master/docs/img/pb_welcome.zh.png)

## 依赖

[MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 依赖：`>=2.12.0`

Python 包要求：见 [requirements.txt](https://github.com/TISUnion/PrimeBackup/tree/master/requirements.txt)

## 使用方法

参见文档：https://tisunion.github.io/PrimeBackup/zh/

## 工作原理

Prime Backup 使用一个自定义的文件池来存储备份数据，池中的每个对象都以其内容的哈希值作为唯一标识
通过这种方式，Prime Backup 可以对内容完全相同的文件进行去重，并只存储它们的一份副本，从而显著降低磁盘空间占用

此外，Prime Backup 还支持对存储的数据进行压缩，以进一步减少磁盘使用量

对于体积较大且仅被局部修改的文件，Prime Backup 可选择启用数据分块功能来提升去重效率。
此时，文件会被切分成多个数据块（chunk），每个数据块都会计算哈希值。
如果数据块的内容没有改变，它就可以在不同的备份中被复用，只有新的数据块载荷会作为打包条目写入

Prime Backup 支持常见的文件类型，包括普通文件、目录和符号链接；对于这三类文件：

- 普通文件：Prime Backup 会先计算其哈希值（及文件大小）
  启用分块时，文件以“chunked blob”形式存储，并引用多个数据块；数据块会独立去重，新的数据块载荷会被压缩并存储为打包条目
  否则，文件会以“direct blob”形式存储，整个文件作为一个单元进行去重和压缩
  文件的权限（mode）、用户ID（uid）、修改时间（mtime）等元数据会存储在数据库中
- 目录：Prime Backup 将其信息存储在数据库中
- 符号链接：Prime Backup 存储的是符号链接本身，而不是它所指向的目标文件

## 致谢

基于哈希的文件池思路来自 https://github.com/z0z0r4/better_backup

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [PrimeBackup-v1.13.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.13.1) | 1.13.1 | 2026/07/20 10:05:55 | 317.42KB | 94 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.13.1/PrimeBackup-v1.13.1.pyz) |
| [PrimeBackup-v1.13.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.13.0) | 1.13.0 | 2026/06/21 14:56:21 | 317.43KB | 564 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.13.0/PrimeBackup-v1.13.0.pyz) |
| [PrimeBackup-v1.12.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.12.0) | 1.12.0 | 2025/12/14 17:24:45 | 218.39KB | 2295 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.12.0/PrimeBackup-v1.12.0.pyz) |
| [PrimeBackup-v1.11.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.11.0) | 1.11.0 | 2025/08/30 17:39:56 | 210.03KB | 1467 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.11.0/PrimeBackup-v1.11.0.pyz) |
| [PrimeBackup-v1.10.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.3) | 1.10.3 | 2025/08/02 14:59:01 | 208.04KB | 627 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.3/PrimeBackup-v1.10.3.pyz) |
| [PrimeBackup-v1.10.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.2) | 1.10.2 | 2025/05/04 17:57:38 | 206.96KB | 1701 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.2/PrimeBackup-v1.10.2.pyz) |
| [PrimeBackup-v1.10.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.1) | 1.10.1 | 2025/05/03 18:12:53 | 206.92KB | 95 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.1/PrimeBackup-v1.10.1.pyz) |
| [PrimeBackup-v1.10.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.0) | 1.10.0 | 2025/04/30 17:19:43 | 206.52KB | 161 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.0/PrimeBackup-v1.10.0.pyz) |
| [PrimeBackup-v1.9.5.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.5) | 1.9.5 | 2025/03/30 15:12:03 | 173.98KB | 672 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.5/PrimeBackup-v1.9.5.pyz) |
| [PrimeBackup-v1.9.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.4) | 1.9.4 | 2025/03/29 16:10:17 | 173.99KB | 98 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.4/PrimeBackup-v1.9.4.pyz) |
| [PrimeBackup-v1.9.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.3) | 1.9.3 | 2025/03/29 13:29:39 | 173.93KB | 61 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.3/PrimeBackup-v1.9.3.pyz) |
| [PrimeBackup-v1.9.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.2) | 1.9.2 | 2025/03/28 08:51:03 | 173.92KB | 71 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.2/PrimeBackup-v1.9.2.pyz) |
| [PrimeBackup-v1.9.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.1) | 1.9.1 | 2025/03/15 12:51:27 | 172.43KB | 287 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.1/PrimeBackup-v1.9.1.pyz) |
| [PrimeBackup-v1.9.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.0) | 1.9.0 | 2025/03/15 10:26:03 | 172.42KB | 55 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.0/PrimeBackup-v1.9.0.pyz) |
| [PrimeBackup-v1.8.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.3) | 1.8.3 | 2024/09/17 09:51:24 | 148.13KB | 2116 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.3/PrimeBackup-v1.8.3.pyz) |
| [PrimeBackup-v1.8.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.2) | 1.8.2 | 2024/09/11 13:09:48 | 148.12KB | 159 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.2/PrimeBackup-v1.8.2.pyz) |
| [PrimeBackup-v1.8.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.1) | 1.8.1 | 2024/07/22 09:46:44 | 147.69KB | 679 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.1/PrimeBackup-v1.8.1.pyz) |
| [PrimeBackup-v1.8.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.0) | 1.8.0 | 2024/07/22 09:48:39 | 147.61KB | 52 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.0/PrimeBackup-v1.8.0.pyz) |
| [PrimeBackup-v1.7.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.4) | 1.7.4 | 2024/04/20 10:07:23 | 146.64KB | 968 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.4/PrimeBackup-v1.7.4.pyz) |
| [PrimeBackup-v1.7.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.3) | 1.7.3 | 2024/03/10 18:48:38 | 146.27KB | 324 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.3/PrimeBackup-v1.7.3.pyz) |
| [PrimeBackup-v1.7.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.2) | 1.7.2 | 2024/02/25 01:48:39 | 146.17KB | 154 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.2/PrimeBackup-v1.7.2.pyz) |
| [PrimeBackup-v1.7.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.1) | 1.7.1 | 2024/02/24 18:44:14 | 146.19KB | 56 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.1/PrimeBackup-v1.7.1.pyz) |
| [PrimeBackup-v1.7.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.0) | 1.7.0 | 2024/02/24 17:50:46 | 145.99KB | 57 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.0/PrimeBackup-v1.7.0.pyz) |
| [PrimeBackup-v1.6.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.3) | 1.6.3 | 2024/01/02 09:28:32 | 141.03KB | 509 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.3/PrimeBackup-v1.6.3.pyz) |
| [PrimeBackup-v1.6.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.2) | 1.6.2 | 2023/12/26 15:28:18 | 141.02KB | 131 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.2/PrimeBackup-v1.6.2.pyz) |
| [PrimeBackup-v1.6.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.1) | 1.6.1 | 2023/12/23 13:07:44 | 140.69KB | 83 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.1/PrimeBackup-v1.6.1.pyz) |
| [PrimeBackup-v1.6.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.0) | 1.6.0 | 2023/12/22 18:09:21 | 140.68KB | 64 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.0/PrimeBackup-v1.6.0.pyz) |
| [PrimeBackup-v1.5.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.5.0) | 1.5.0 | 2023/12/18 18:16:48 | 138.58KB | 95 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.5.0/PrimeBackup-v1.5.0.pyz) |
| [PrimeBackup-v1.4.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.1) | 1.4.1 | 2023/12/17 16:53:56 | 135.02KB | 62 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.1/PrimeBackup-v1.4.1.pyz) |
| [PrimeBackup-v1.4.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.0) | 1.4.0 | 2023/12/16 12:24:06 | 134.92KB | 70 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.0/PrimeBackup-v1.4.0.pyz) |
| [PrimeBackup-v1.3.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.3.0) | 1.3.0 | 2023/12/13 16:12:06 | 126.51KB | 82 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.3.0/PrimeBackup-v1.3.0.pyz) |
| [PrimeBackup-v1.2.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.2.0) | 1.2.0 | 2023/12/12 18:23:26 | 124.45KB | 61 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.2.0/PrimeBackup-v1.2.0.pyz) |
| [PrimeBackup-v1.1.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.1.0) | 1.1.0 | 2023/12/11 18:06:40 | 120.68KB | 66 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.1.0/PrimeBackup-v1.1.0.pyz) |
| [PrimeBackup-v1.0.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.1) | 1.0.1 | 2023/12/10 17:26:14 | 116.92KB | 85 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.1/PrimeBackup-v1.0.1.pyz) |
| [PrimeBackup-v1.0.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.0) | 1.0.0 | 2023/12/10 15:15:49 | 116.83KB | 58 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.0/PrimeBackup-v1.0.0.pyz) |

