[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mcdr2restic

### 基本信息

- 插件 ID: `mcdr2restic`
- 插件名: MCDR2Restic
- 版本: 0.10.0
  - 元数据版本: 0.10.0
  - 发布版本: 0.10.0
- 总下载量: 75
- 作者: [pfdr2333](https://github.com/pfdr2333)
- 仓库: https://github.com/pfdr2333/MCDR2restic
- 仓库插件页: https://github.com/pfdr2333/MCDR2restic/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 调用 restic 进行去重增量备份与多通道异步通知。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0 |
| [websocket-client](https://pypi.org/project/websocket-client) | \>=1.8.0 |

```
pip install "PyYAML>=6.0" "websocket-client>=1.8.0"
```

### 介绍

# MCDR2Restic

[![CI](https://github.com/pfdr2333/MCDR2restic/actions/workflows/ci.yml/badge.svg)](https://github.com/pfdr2333/MCDR2restic/actions/workflows/ci.yml)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://github.com/pfdr2333/MCDR2restic/tree/main/LICENSE)

MCDReforged 插件：调用 [restic](https://restic.readthedocs.io/en/stable/) 对 Minecraft 服务器进行去重增量备份，支持定时调度、快照恢复与多通道通知。

**中文 | [English](https://github.com/pfdr2333/MCDR2restic/tree/main/README_EN.md)**

## 功能

- 定时备份：支持 6 位 cron 与固定间隔，可中途打断
- 无人游玩自动跳过：结合 join/left 事件与 `list` 在线检查
- 强制备份调度：不受玩家活动感知影响，默认关闭
- 自动下载 restic（Linux/Windows amd64），过旧时自动升级，内置下载源含官方地址、自建镜像与加速前缀
- 快照恢复：整份快照、单文件、文件夹，支持恢复到指定目录
- 恢复前自动创建保护快照，失败自动回滚
- 仓库维护：`forget`/`prune` 等命令按计划独立执行
- 通知：OneBot QQ、Discord 与自定义 Webhook，可同时启用
- 中英双语消息与配置注释，跟随 MCDR 语言
- 配置安全检查：restic 仓库不得位于备份源目录内

## 演示

每个快照都是该时间点的完整备份，仅占用增量空间：

![演示](https://raw.githubusercontent.com/pfdr2333/MCDR2restic/main/image.png)

## 环境要求

- MCDReforged >= 2.12.0
- Python 依赖由 MCDR 按 `requirements.txt` 自动安装（`PyYAML`、`websocket-client`）

> 使用前建议先了解 restic 的基本概念与配置方法（[restic 手册](https://restic.readthedocs.io/en/stable/)）。插件的默认配置开箱即用，但远端仓库、保留策略等高级用法仍需要 restic 知识。

## 安装

插件已入库 MCDR 插件仓库，在 MCDR 终端执行一条命令即可安装：

```text
!!MCDR plugin install mcdr2restic
```

后续更新同样只需一条命令：

```text
!!MCDR plugin install -U mcdr2restic
```

也可以手动安装：下载最新 [Release](https://github.com/pfdr2333/MCDR2restic/releases) 中的 `MCDR2Restic.mcdr`，放入 MCDR 的 `plugins/` 目录后执行 `!!MCDR reload all`。首次加载会在 `config/mcdr2restic/config.yml` 自动生成适配当前系统的示例配置，默认即可运行：

- 自动下载 restic、过旧自动升级、自动初始化本地仓库
- 默认备份 `./server/world`（检测到三世界目录时自动全部写入）
- Windows 下自动使用 `.\config\mcdr2restic\restic.exe` 等反斜杠路径并排除 `session.lock`

按需修改配置后执行 `!!m2r reload`。

> 默认只备份世界目录。如需获得完整的恢复能力，建议把备份范围改为整个 `./server` 目录甚至 MCDR 根目录，保护存档之外的服务器文件状态。
> 
> 示例密码 `123456` 仅用于降低上手门槛，正式使用请修改。
> 
> OneBot 通知依赖包名为 `websocket-client`（导入名 `websocket`）。如果误装了同名的错误包导致 `websocket.WebSocketApp` 不存在，插件会给出提示。国内网络下依赖安装失败时，建议为 MCDR 使用的 Python 环境配置 PyPI 镜像或代理。

## 命令

所有命令的默认根是 `!!restic`，别名 `!!m2r`（两者完全等价），下文统一用更短的 `!!m2r` 示例；直接输入根命令即查看状态。

| 命令                                       | 说明                    |
| ---------------------------------------- | --------------------- |
| `!!m2r status [p <页码>]`                  | 查看状态与快照列表             |
| `!!m2r backup`                           | 立即备份                  |
| `!!m2r start` / `stop`                   | 启用 / 停用定时备份           |
| `!!m2r cancel`                           | 取消当前正在运行的任务，不改变定时备份开关 |
| `!!m2r init`                             | 手动初始化仓库               |
| `!!m2r unlock`                           | 解锁仓库                  |
| `!!m2r maintenance`                      | 手动执行仓库维护              |
| `!!m2r restore <快照>`                     | 添加整份快照恢复任务            |
| `!!m2r restore <快照> file <路径>`           | 添加单文件恢复任务             |
| `!!m2r restore <快照> folder <路径>`         | 添加文件夹恢复任务             |
| `!!m2r restore <快照> to <目录>`             | 添加整份快照恢复任务到指定目录（不停服）  |
| `!!m2r restore <快照> to <目录> file <路径>`   | 添加单文件恢复任务到指定目录        |
| `!!m2r restore <快照> to <目录> folder <路径>` | 添加文件夹恢复任务到指定目录        |
| `!!m2r restore list`                     | 查看恢复任务队列              |
| `!!m2r restore apply`                    | 执行恢复任务队列              |
| `!!m2r restore apply --skip-safety`      | 执行恢复任务队列，跳过保护快照       |
| `!!m2r unrestore <ID>|all`               | 删除某个 / 所有恢复任务         |
| `!!m2r notify-test`                      | 向所有已启用的通知渠道发送测试消息     |
| `!!m2r reload`                           | 重载配置                  |

默认命令权限等级为 `3`，可在配置中修改。

恢复任务不会立即执行。`restore apply` 时：

- **恢复到服务器工作目录**（默认）：先创建保护快照，再停止 Minecraft、恢复文件、重启服务端；恢复失败自动回滚到保护快照。加 `--skip-safety` 参数可跳过保护快照，恢复失败时将无法回滚，请谨慎使用。
- **恢复到指定目录**（所有任务都带 `to` 时）：不停止服务器，直接执行恢复；目标目录不得位于 restic 仓库或备份源目录内。

## 文档

完整配置说明、调度策略与常见问题见[在线文档](https://m2r.pfdr.cc/)（源文件在 [docs/](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/index.md)）：

- [快速开始](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/getting-started.md)
- [命令说明](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/commands.md)
- [配置说明](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/configuration.md)
- [状态与恢复](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/restore.md)
- [常见问题](https://github.com/pfdr2333/MCDR2restic/tree/main/docs/faq.md)

## 开发与构建

```bash
# 运行测试（覆盖率不低于 65%）
python -m coverage run --branch --source=mcdr2restic,tools -m unittest discover -s tests -p "test_*.py"
python -m coverage report --fail-under=65

# 打包 .mcdr 归档
python tools/pack_plugin.py --output-dir dist

# 本地预览文档站（Material for MkDocs）
pip install -r requirements-docs.txt
mkdocs serve
```

修改 `lang/zh_cn.json` 或 `en_us.json` 后需运行 `python tools/sync_language_resources.py` 重新生成 `zh_tw` 并同步两份语言文件；CI 会校验两份 `lang/` 是否一致，未同步时将失败。

GitHub Actions 会在每次推送时运行测试并保存构建产物；推送形如 `v0.6.0` 的 Git 标签会自动构建并创建 Release。

## 贡献

欢迎提交 Issue 与 Pull Request。

## 许可证

本项目基于 [GPL-3.0](https://github.com/pfdr2333/MCDR2restic/tree/main/LICENSE) 许可证发布。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MCDR2Restic_v0.10.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.10.0) | 0.10.0 | 2026/11/07 04:03:05 | 216.08KB | 1 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.10.0/MCDR2Restic_v0.10.0.mcdr) |
| [MCDR2Restic_v0.9.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.9.0) | 0.9.0 | 2026/11/06 23:47:04 | 209.81KB | 3 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.9.0/MCDR2Restic_v0.9.0.mcdr) |
| [MCDR2Restic_v0.6.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.6.0) | 0.6.0 | 2026/11/04 21:37:13 | 171.47KB | 3 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.6.0/MCDR2Restic_v0.6.0.mcdr) |
| [MCDR2Restic_v0.5.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.5.0) | 0.5.0 | 2026/08/08 20:12:04 | 151.34KB | 29 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.5.0/MCDR2Restic_v0.5.0.mcdr) |
| [MCDR2Restic_v0.4.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.4.0) | 0.4.0 | 2026/07/09 04:25:11 | 252.82KB | 8 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.4.0/MCDR2Restic_v0.4.0.mcdr) |
| [MCDR2restic_v0.3.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.3.0) | 0.3.0 | 2026/07/08 09:33:34 | 170.36KB | 5 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.3.0/MCDR2restic_v0.3.0.mcdr) |
| [MCDR2Restic_v0.2.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.2.0) | 0.2.0 | 2026/07/08 04:58:57 | 154.57KB | 6 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.2.0/MCDR2Restic_v0.2.0.mcdr) |
| [MCDR2restic_v0.1.9.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.9) | 0.1.9 | 2026/07/08 04:03:03 | 150.17KB | 6 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.9/MCDR2restic_v0.1.9.mcdr) |
| [MCDR2restic_v0.1.8.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.8) | 0.1.8 | 2026/07/08 02:17:27 | 149.04KB | 7 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.8/MCDR2restic_v0.1.8.mcdr) |
| [MCDR2restic_v0.1.7.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.7) | 0.1.7 | 2026/07/08 02:03:44 | 136.64KB | 7 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.7/MCDR2restic_v0.1.7.mcdr) |

