[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## prime_backup

### 基本信息

- 插件 ID: `prime_backup`
- 插件名: Prime Backup
- 版本: 1.14.0
  - 元数据版本: 1.14.0
  - 发布版本: 1.14.0
- 总下载量: 16934
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

一个强大的 MCDR 备份插件，一套先进的 Minecraft 存档备份解决方案

中文文档：https://tisunion.github.io/PrimeBackup/zh/

## 功能特性

- 基于哈希去重与压缩的文件池：仅储存新增或变更的数据，备份数量没有硬性上限
- 可选的文件分块能力：支持固定大小分块（Fixed-Size Chunking）、内容定义分块（Content-Defined Chunking）等算法，将大文件切分为数据块并逐块去重，进一步节省空间
- 紧凑的打包存储机制：将压缩后的数据块集中写入打包文件，避免大量小文件给文件系统带来压力，同时支持完整性校验与空间整理
- 安全的回档流程：提供二次确认与倒计时、回档前自动创建临时备份、回收站式失败回滚以及数据完整性校验
- 完善的备份操作：覆盖创建、回档、列表查看、差异对比、导入导出等全流程功能
- 流畅的游戏内交互，大部分操作都能点点点
- 丰富的数据库工具集：支持数据库概览、内部对象审查、完整性校验、孤立数据清理、删除备份内指定文件以及哈希/压缩算法迁移
- 高度可自定义的备份清理策略，是 [PBS](https://pbs.proxmox.com/docs/prune-simulator/) 所用策略的同款
- 定时任务：支持自动创建备份与自动清理备份，计划规则支持固定间隔和 crontab 表达式
- 独立命令行工具：无需启动 MCDR 即可离线管理备份，并支持通过 FUSE 将备份挂载为文件系统

![!!pb command](https://raw.githubusercontent.com/TISUnion/PrimeBackup/master/docs/img/pb_welcome.zh.png)

## 依赖

- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)：`>=2.12.0`
- Python 依赖包：见 [requirements.txt](https://github.com/TISUnion/PrimeBackup/tree/master/requirements.txt)
- 可选功能依赖：见 [requirements.optional.txt](https://github.com/TISUnion/PrimeBackup/tree/master/requirements.optional.txt)

## 使用方法

参见文档：https://tisunion.github.io/PrimeBackup/zh/

## 工作原理

Prime Backup 使用自定义的文件池来储存备份数据，池中的每个数据对象都以其内容的哈希值作为唯一标识。内容完全相同的文件只会在磁盘上保存一份副本，配合可选的数据压缩，可显著降低存储空间占用

对于体积较大且常被局部修改的文件，Prime Backup 支持启用文件分块来提升去重效果。文件会被切分成多个数据块（Chunk）并分别计算哈希，未发生变化的数据块可在不同备份间直接复用，仅将新增数据块压缩后追加写入打包文件（Pack）

Prime Backup 支持常见文件系统类型，包括普通文件、目录和符号链接：

- **普通文件**：先计算文件内容哈希与大小
  - 启用分块时，文件作为分块数据对象储存，按数据块粒度独立去重、压缩并存入打包文件
  - 未启用分块时，文件作为直存数据对象，以整个文件为单位进行去重与压缩
  - 文件的权限（mode）、所有者（uid / gid）、修改时间（mtime）等元数据统一记录在数据库中
- **目录**：将其路径与元数据记录在数据库中
- **符号链接**：仅记录符号链接本身及其指向路径，不展开目标文件

## 致谢

基于哈希的文件池思路受 https://github.com/z0z0r4/better_backup 启发

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [PrimeBackup-v1.14.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.14.0) | 1.14.0 | 2026/09/15 18:10:26 | 321.88KB | 953 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.14.0/PrimeBackup-v1.14.0.pyz) |
| [PrimeBackup-v1.13.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.13.1) | 1.13.1 | 2026/07/20 10:05:55 | 317.42KB | 1442 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.13.1/PrimeBackup-v1.13.1.pyz) |
| [PrimeBackup-v1.13.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.13.0) | 1.13.0 | 2026/06/21 14:56:21 | 317.43KB | 600 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.13.0/PrimeBackup-v1.13.0.pyz) |
| [PrimeBackup-v1.12.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.12.0) | 1.12.0 | 2025/12/14 17:24:45 | 218.39KB | 2330 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.12.0/PrimeBackup-v1.12.0.pyz) |
| [PrimeBackup-v1.11.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.11.0) | 1.11.0 | 2025/08/30 17:39:56 | 210.03KB | 1500 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.11.0/PrimeBackup-v1.11.0.pyz) |
| [PrimeBackup-v1.10.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.3) | 1.10.3 | 2025/08/02 14:59:01 | 208.04KB | 638 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.3/PrimeBackup-v1.10.3.pyz) |
| [PrimeBackup-v1.10.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.2) | 1.10.2 | 2025/05/04 17:57:38 | 206.96KB | 1709 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.2/PrimeBackup-v1.10.2.pyz) |
| [PrimeBackup-v1.10.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.1) | 1.10.1 | 2025/05/03 18:12:53 | 206.92KB | 105 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.1/PrimeBackup-v1.10.1.pyz) |
| [PrimeBackup-v1.10.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.10.0) | 1.10.0 | 2025/04/30 17:19:43 | 206.52KB | 175 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.10.0/PrimeBackup-v1.10.0.pyz) |
| [PrimeBackup-v1.9.5.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.5) | 1.9.5 | 2025/03/30 15:12:03 | 173.98KB | 701 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.5/PrimeBackup-v1.9.5.pyz) |
| [PrimeBackup-v1.9.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.4) | 1.9.4 | 2025/03/29 16:10:17 | 173.99KB | 108 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.4/PrimeBackup-v1.9.4.pyz) |
| [PrimeBackup-v1.9.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.3) | 1.9.3 | 2025/03/29 13:29:39 | 173.93KB | 71 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.3/PrimeBackup-v1.9.3.pyz) |
| [PrimeBackup-v1.9.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.2) | 1.9.2 | 2025/03/28 08:51:03 | 173.92KB | 81 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.2/PrimeBackup-v1.9.2.pyz) |
| [PrimeBackup-v1.9.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.1) | 1.9.1 | 2025/03/15 12:51:27 | 172.43KB | 298 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.1/PrimeBackup-v1.9.1.pyz) |
| [PrimeBackup-v1.9.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.9.0) | 1.9.0 | 2025/03/15 10:26:03 | 172.42KB | 66 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.9.0/PrimeBackup-v1.9.0.pyz) |
| [PrimeBackup-v1.8.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.3) | 1.8.3 | 2024/09/17 09:51:24 | 148.13KB | 2127 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.3/PrimeBackup-v1.8.3.pyz) |
| [PrimeBackup-v1.8.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.2) | 1.8.2 | 2024/09/11 13:09:48 | 148.12KB | 171 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.2/PrimeBackup-v1.8.2.pyz) |
| [PrimeBackup-v1.8.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.1) | 1.8.1 | 2024/07/22 09:46:44 | 147.69KB | 688 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.1/PrimeBackup-v1.8.1.pyz) |
| [PrimeBackup-v1.8.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.8.0) | 1.8.0 | 2024/07/22 09:48:39 | 147.61KB | 62 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.8.0/PrimeBackup-v1.8.0.pyz) |
| [PrimeBackup-v1.7.4.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.4) | 1.7.4 | 2024/04/20 10:07:23 | 146.64KB | 979 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.4/PrimeBackup-v1.7.4.pyz) |
| [PrimeBackup-v1.7.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.3) | 1.7.3 | 2024/03/10 18:48:38 | 146.27KB | 338 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.3/PrimeBackup-v1.7.3.pyz) |
| [PrimeBackup-v1.7.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.2) | 1.7.2 | 2024/02/25 01:48:39 | 146.17KB | 165 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.2/PrimeBackup-v1.7.2.pyz) |
| [PrimeBackup-v1.7.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.1) | 1.7.1 | 2024/02/24 18:44:14 | 146.19KB | 68 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.1/PrimeBackup-v1.7.1.pyz) |
| [PrimeBackup-v1.7.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.7.0) | 1.7.0 | 2024/02/24 17:50:46 | 145.99KB | 69 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.7.0/PrimeBackup-v1.7.0.pyz) |
| [PrimeBackup-v1.6.3.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.3) | 1.6.3 | 2024/01/02 09:28:32 | 141.03KB | 521 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.3/PrimeBackup-v1.6.3.pyz) |
| [PrimeBackup-v1.6.2.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.2) | 1.6.2 | 2023/12/26 15:28:18 | 141.02KB | 143 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.2/PrimeBackup-v1.6.2.pyz) |
| [PrimeBackup-v1.6.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.1) | 1.6.1 | 2023/12/23 13:07:44 | 140.69KB | 93 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.1/PrimeBackup-v1.6.1.pyz) |
| [PrimeBackup-v1.6.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.6.0) | 1.6.0 | 2023/12/22 18:09:21 | 140.68KB | 74 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.6.0/PrimeBackup-v1.6.0.pyz) |
| [PrimeBackup-v1.5.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.5.0) | 1.5.0 | 2023/12/18 18:16:48 | 138.58KB | 106 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.5.0/PrimeBackup-v1.5.0.pyz) |
| [PrimeBackup-v1.4.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.1) | 1.4.1 | 2023/12/17 16:53:56 | 135.02KB | 73 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.1/PrimeBackup-v1.4.1.pyz) |
| [PrimeBackup-v1.4.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.4.0) | 1.4.0 | 2023/12/16 12:24:06 | 134.92KB | 79 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.4.0/PrimeBackup-v1.4.0.pyz) |
| [PrimeBackup-v1.3.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.3.0) | 1.3.0 | 2023/12/13 16:12:06 | 126.51KB | 94 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.3.0/PrimeBackup-v1.3.0.pyz) |
| [PrimeBackup-v1.2.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.2.0) | 1.2.0 | 2023/12/12 18:23:26 | 124.45KB | 71 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.2.0/PrimeBackup-v1.2.0.pyz) |
| [PrimeBackup-v1.1.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.1.0) | 1.1.0 | 2023/12/11 18:06:40 | 120.68KB | 76 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.1.0/PrimeBackup-v1.1.0.pyz) |
| [PrimeBackup-v1.0.1.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.1) | 1.0.1 | 2023/12/10 17:26:14 | 116.92KB | 94 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.1/PrimeBackup-v1.0.1.pyz) |
| [PrimeBackup-v1.0.0.pyz](https://github.com/TISUnion/PrimeBackup/releases/tag/v1.0.0) | 1.0.0 | 2023/12/10 15:15:49 | 116.83KB | 66 | [下载](https://github.com/TISUnion/PrimeBackup/releases/download/v1.0.0/PrimeBackup-v1.0.0.pyz) |

