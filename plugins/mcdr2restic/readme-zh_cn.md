[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mcdr2restic

### 基本信息

- 插件 ID: `mcdr2restic`
- 插件名: MCDR2Restic
- 版本: 0.5.0
  - 元数据版本: 0.5.0
  - 发布版本: 0.5.0
- 总下载量: 49
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

MCDR2Restic 是一个 MCDReforged 插件，用于在服务端正常运行时定时调用 restic 备份指定目录。

**此readme正要重构，可能含有过时信息**

## 前置要求 / Prerequisites
> 本项目负责调用 restic。默认配置下，如果 MCDR 工作目录找不到 restic，则会自动下载对应系统的 restic ，非默认目录该功能不生效

> 在使用本项目之前，请先了解 restic 的基本原理及配置方法，并确保能够独立使用 restic。
> restic的使用方法已经超出此文档范围（[restic手册](https://restic.readthedocs.io/en/stable/)）。大部分备份功能均需要基础的restic知识。Restic 是一款快速、高效且安全的开源备份工具，其去重备份功能尤为适合与MC服务器使用，可大幅减小备份体积。

> 虽然本插件默认配置会自动处理restic的安装，但仍然建议学习restic使用方法和高级配置，你会用上的。


# 语言 **中文| [English](https://github.com/pfdr2333/MCDR2restic/tree/main/README_EN.md)**
本项目支持中文和英语，跟随MCDR语言

This project supports both Chinese and English, following the MCDR language conventions.

## 功能

- 定时调用 restic 备份
- 可中断当前备份任务
- 自动下载restic
- 支持 OneBot QQ 通知和 Discord Webhook 通知
- 中英文消息和配置注释
- 无人游玩跳过正常备份：触发时执行一次 `list`，并结合 join/left 事件判断
- 支持强制备份调度：不受玩家活动感知影响，默认关闭
- 配置安全检查：本地 restic 仓库不能位于备份源目录内，避免仓库被备份进自身
- 自动化，安全且简单的快照恢复

## 安装
> **快速开始：将插件放入`mcdr`的`plugins`目录然后`!!MCDR reload all`即可以默认配置自动运行**

1. 将 `MCDR2Restic.mcdr`放入 MCDR 的 `plugins/`。
2. Python 依赖声明在包内根目录的 `requirements.txt`，由 MCDR 处理：

   - `PyYAML>=6.0`
   - `websocket-client>=1.8.0`

   OneBot 通知使用的依赖包名是 `websocket-client`，Python 导入名是 `websocket`。如果误装了另一个同名包导致 `websocket.WebSocketApp` 不存在，插件会给出提示

   如果 MCDR 依赖安装失败，请修复 MCDR 使用的 Python 环境后重载；如果误装了错误的 `websocket` 包，需要从该环境中移除它。

   在国内网络环境下，如果 MCDR 安装依赖下载失败，请给 MCDR 使用的 Python/pip 配置 PyPI 镜像或代理后重试。

3. 启动/重载 MCDR 后，如果 `config/mcdr2restic/config.yml` 不存在，插件会自动生成一份适配当前系统的示例配置。注释语言会跟随 MCDR 当前语言：中文使用中文注释，其他语言使用英文注释。

   在 Windows 上首次生成配置时，示例会自动改为 `.\restic.exe`、`.\restic-repo`、`.\server\world` 这类路径，并使用 YAML 单引号避免反斜杠转义问题。

4. 按需修改配置文件，修改完成后执行 `!!restic reload`

<!--
## 配置
<details>
  <summary>配置详解</summary>
运行时状态会写入 `config/mcdr2restic/state.yml`，例如玩家进入/退出标志、最近在线检查结果和最近备份结果。

`!!restic status` 会附带显示 restic 快照列表。快照列表缓存写入 SQLite（默认 `config/mcdr2restic/snapshots.sqlite3`），并在本插件执行 `init`、维护命令或备份命令后自动标记失效；下一次查看状态时再刷新缓存。默认每页显示 10 条，可通过 `snapshot_cache.page_size` 调整。

恢复任务同样写入 SQLite。`!!restic restore <snapshot>` 会加入整份快照恢复任务；`!!restic restore <snapshot> file /server/whitelist.json` 和 `!!restic restore <snapshot> folder /server/region` 会按 restic 工作目录根路径加入单文件/文件夹恢复任务。任务不会立即执行，`!!restic restore apply` 会先创建一个带 `restore.pre_restore_backup_tag` 的保护快照，再通过 MCDR 停止 MC、恢复文件、启动 MC；停服和启动阶段由 MCDR hook 接力。如果恢复队列执行失败，插件会在启动 MC 前立即恢复到这份保护快照，队列会保留以便排查。

`schedule.require_player_activity_in_wait_period` 为 `true` 时，正常定时备份采用纯事件驱动加触发时检查：

- 本周期有人加入：备份
- 无人加入，触发时 `list` 检查在线人数为 0：跳过
- 无人加入，触发时 `list` 检查在线人数不为 0：备份
- 无人加入，但本周期有人退出，即使触发时在线人数为 0：备份

在线人数通过 MCDR RCON 执行 `schedule.online_check_command`，默认是 Minecraft 的 `list` 命令。建议在 MCDR 中启用 RCON，否则插件只能依赖 join/left 事件估算在线人数。

```yaml
schedule:
  interval_seconds: 0
  cron_expression: "0 0 0,3,6,9,12,15,18,21 * * *"
  require_player_activity_in_wait_period: true
  online_check_command: "list"
```

`force_schedule` 是强制备份调度，不遵循玩家活动感知，默认关闭。它和正常调度一样支持固定间隔或 6 位 cron：`interval_seconds > 0` 时优先使用固定间隔；`interval_seconds = 0` 且 `cron_expression` 不是 `"0"` 时使用 cron；两者都为 0 时关闭。

```yaml
force_schedule:
  interval_seconds: 0
  cron_expression: "0"
```

`maintenance_schedule` 是仓库维护调度，独立于备份流程，默认每天 `03:00` 执行一次 `restic.maintenance_commands`。`cron_expression` 留空时仍使用默认 `03:00`；写成 `"0"` 表示关闭。维护不会执行 `save-off`、`save-all`、`save-on`。如果维护和备份同一时间触发，先备份；如果二者错开但运行冲突，后到者会等待当前任务结束。

```yaml
maintenance_schedule:
  interval_seconds: 0
  cron_expression: "0 0 3 * * *"
```

`update_check` 是版本更新检查，默认开启。插件加载时会在后台检查一次，之后每天 `00:00` 检查一次；只写日志提示，不会自动下载或更新插件。需要关闭时把 `enabled` 改为 `false`。

```yaml
update_check:
  enabled: true
  check_on_startup: true
  daily_time: "00:00"
  api_url: "https://api.github.com/repos/pfdr2333/MCDR2restic/releases/latest"
  release_page_url: "https://github.com/pfdr2333/MCDR2restic/releases/latest"
  proxy_prefixes:
    - "https://gh.llkk.cc/"
    - "https://gh-proxy.com/"
    - "https://hub.gitmirror.com/"
  timeout_seconds: 10
```

默认生成的 restic 配置是一个可直接运行的最小本地示例：

```yaml
restic:
  executable: "./restic"
  working_directory: ""
  repository: "./restic-repo"
  password: "123456"
  password_file: ""
  auto_download: true
  download_version: "latest"
  download_proxy_prefixes:
    - "https://gh.llkk.cc/"
    - "https://gh-proxy.com/"
    - "https://hub.gitmirror.com/"
  download_timeout_seconds: 120
  auto_init_local_repository: true
  environment: {}
  maintenance_commands:
    - [
        "forget",
        "--keep-daily", "7",
        "--prune"
      ]
  backup_command:
    - "backup"
    - "./server/world"
    - "--tag"
    - "minecraft"
    - "--host"
    - "mcdr2Restic"
  timeout_seconds: 0
  progress_interval_seconds: 5
```

备份顺序现在是：`save-off` -> `save-all` -> `restic backup` -> `save-on`。仓库维护由 `maintenance_schedule` 单独触发，不再作为备份前步骤运行。

这样在 Linux/Windows amd64 上，即使 MCDR 工作目录下还没有默认路径的 restic，插件也会尝试自动下载。首次生成配置时默认只备份 `./server/world`；如果生成时检测到 `./server/world`、`./server/world_nether`、`./server/world_the_end` 三个目录都存在，会自动写入三世界目录。Windows 首次生成配置时会自动使用 `.\restic.exe` 和反斜杠路径，并默认排除 `session.lock`，避免 Minecraft 文件锁导致 restic 返回 3。示例密码 `123456` 只用于降低首次配置门槛，正式使用请改成自己的强密码。

自动下载会先请求 GitHub latest release API；如果 `api.github.com` 失败，会退回到内置的 `v0.19.1` 下载链接。下载时先试官方 GitHub 地址，再按 `download_proxy_prefixes` 顺序尝试代理。

`restic.password` 优先级高于 `restic.password_file`。如果 `password` 留空字符串，插件才会设置 `RESTIC_PASSWORD_FILE` 使用密码文件。`restic.repository` 会自动写入 `RESTIC_REPOSITORY`。

`restic.auto_init_local_repository` 为 `true` 时，如果本地仓库不存在或缺少 `config`，插件会在备份前自动执行 `restic init`。S3、B2、rest、sftp、rclone 等远端仓库不会自动初始化。

备份开始前会执行配置安全检查：如果本地 `restic.repository` 位于 `backup_command` 指定的备份源目录内，例如备份 `.` 且仓库是 `./restic-repo`，插件会直接终止备份并通知管理员。请把仓库放到备份源目录之外，或调整 `backup_command`。

`restic.timeout_seconds` 控制 restic 命令流程超时，`0` 表示不限制；旧配置中的默认 `3600` 会在迁移时更新为 `0`。`restic.progress_interval_seconds` 控制 `backup`/`restore` 的 `--json` 进度回显间隔，默认每 5 秒写入一次 MCDR 日志；备份通知仍保持原来的开始/成功/失败行为，不会因进度回显刷通知。

`restic.environment` 会在执行每条 restic 命令时叠加到环境变量中，适合加入 S3/B2 等后端需要的密钥变量。`repository`、`password`、`password_file` 会自动转换为 restic 对应环境变量，因此通常不需要在 `environment` 里重复写 `RESTIC_REPOSITORY`、`RESTIC_PASSWORD` 或 `RESTIC_PASSWORD_FILE`。

通知支持 OneBot QQ 和 Discord Webhook，二者默认关闭，可以同时启用。Discord 只需要填入频道 Webhook URL：

```yaml
discord:
  enabled: false
  webhook_url: ""
  username: "MCDR2Restic"
  avatar_url: ""
  message_prefix: "[MCDR2Restic]"
  mention_user_ids: []
  mention_role_ids: []
  mention_everyone: false
  send_timeout_seconds: 10
```

`messages` 里可以自定义管理员通知文本。可用变量包括：`{prefix}`、`{label}`、`{start_time}`、`{end_time}`、`{duration_seconds}`、`{status}`、`{message}`、`{detail}`、`{error}`。如果需要输出字面量花括号，请写成 `{{` 或 `}}`。
</details>
-->

## 命令

- `!!restic status` 查看状态
- `!!restic status p X` 查看 restic 快照列表第 X 页
- `!!restic restore SNAPSHOT` 添加整份快照恢复任务
- `!!restic restore SNAPSHOT file /server/path` 添加单文件恢复任务
- `!!restic restore SNAPSHOT folder /server/path` 添加文件夹恢复任务
- `!!restic restore list` 查看恢复任务列表
- `!!restic unrestore ID/all` 删除某个/所有恢复任务
- `!!restic restore apply` 执行恢复任务队列
- `!!restic start` 启用定时备份
- `!!restic stop` 禁用定时备份，并请求停止当前备份
- `!!restic backup` 立即备份
- `!!restic reload` 重载配置

默认命令权限等级为 `3`，可在配置中修改。

## 构建与发布

本地执行 `pack\build.bat`，或运行 `python tools/pack_plugin.py --output-dir dist`，会生成符合 MCDR 插件目录结构的 `.mcdr` 归档。归档包含 `mcdreforged.plugin.json`、`requirements.txt`、入口包和元数据声明的资源目录。

GitHub Actions 会在每次推送或 Pull Request 时检查并保存构建产物；推送形如 `v0.5.0` 的 Git 标签时，会自动构建并创建 GitHub Release，发布生成的 `.mcdr` 文件。

# 贡献
欢迎提交PR和ISSUE

# 演示
下面的图片显示了使用Restic备份MC的优势，每个快照都是那个时间点的完整备份，仅占用一半空间
![alt text](https://raw.githubusercontent.com/pfdr2333/MCDR2restic/main/image.png)

# 许可证

本项目采用 **[GNU General Public License v3.0 (GPL-3.0)](https://github.com/pfdr2333/MCDR2restic/tree/main/LICENSE)** 许可证发布。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MCDR2Restic_v0.5.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.5.0) | 0.5.0 | 2026/08/08 20:12:04 | 151.34KB | 17 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.5.0/MCDR2Restic_v0.5.0.mcdr) |
| [MCDR2Restic_v0.4.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.4.0) | 0.4.0 | 2026/07/09 04:25:11 | 252.82KB | 6 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.4.0/MCDR2Restic_v0.4.0.mcdr) |
| [MCDR2restic_v0.3.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.3.0) | 0.3.0 | 2026/07/08 09:33:34 | 170.36KB | 4 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.3.0/MCDR2restic_v0.3.0.mcdr) |
| [MCDR2Restic_v0.2.0.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.2.0) | 0.2.0 | 2026/07/08 04:58:57 | 154.57KB | 5 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.2.0/MCDR2Restic_v0.2.0.mcdr) |
| [MCDR2restic_v0.1.9.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.9) | 0.1.9 | 2026/07/08 04:03:03 | 150.17KB | 5 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.9/MCDR2restic_v0.1.9.mcdr) |
| [MCDR2restic_v0.1.8.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.8) | 0.1.8 | 2026/07/08 02:17:27 | 149.04KB | 6 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.8/MCDR2restic_v0.1.8.mcdr) |
| [MCDR2restic_v0.1.7.mcdr](https://github.com/pfdr2333/MCDR2restic/releases/tag/v0.1.7) | 0.1.7 | 2026/07/08 02:03:44 | 136.64KB | 6 | [下载](https://github.com/pfdr2333/MCDR2restic/releases/download/v0.1.7/MCDR2restic_v0.1.7.mcdr) |

