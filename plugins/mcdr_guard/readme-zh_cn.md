[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mcdr_guard

### 基本信息

- 插件 ID: `mcdr_guard`
- 插件名: MCDR Guard
- 版本: 1.2.1
  - 元数据版本: 1.2.1
  - 发布版本: 1.2.1
- 总下载量: 14
- 作者: [yuzai114514](https://github.com/yuzai114514)
- 仓库: https://github.com/yuzai114514/mcdr-guard
- 仓库插件页: https://github.com/yuzai114514/mcdr-guard/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 服务端自动恢复，支持游戏内一键部署 MCDR 后台守护。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.7 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# MCDR Guard

服务端停了，自动拉起来。

MCDR Guard 每 5 秒检查一次服务端状态。服务端关闭后，约 30 秒内尝试启动，效果与 `!!MCDR server start` 相同。PrimeBackup 有任务时会等待，避免在回档过程中启动服务端。

需要 MCDReforged 2.15.7 或更高版本。

## 安装

从 [Releases](https://github.com/yuzai114514/mcdr-guard/releases) 下载 `.mcdr` 文件，放入 `plugins`，然后执行：

```text
!!MCDR plugin reloadall
```

升级时先移除旧的插件文件，不要同时保留两个版本。

进服后输入一次：

```text
!!guard setup
```

插件会自动部署后台守护，不用另外下载启动器或输入终端命令。输入 `!!guard` 查看版本和启用状态。以上命令需要 MCDR 管理员权限；Minecraft OP 不一定拥有该权限。

官方插件目录收录后，也可以使用以下命令安装或更新：

```text
!!MCDR plugin install mcdr_guard
!!MCDR plugin install -U mcdr_guard
```

## 使用

安装后自动启用。以下命令需要管理员权限，控制台可以直接执行。

| 命令              | 用途               |
| --------------- | ---------------- |
| `!!guard`       | 显示版本和状态          |
| `!!guard setup` | 一键部署并启用后台守护      |
| `!!guard off`   | 暂停自动恢复           |
| `!!guard on`    | 恢复自动恢复           |
| `!!guard stop`  | 暂停恢复并关闭服务端与 MCDR |

计划停服用 `!!guard stop`。只想关闭服务端做维护，先执行 `!!guard off`，再执行 `!!MCDR server stop`，否则服务端会被重新启动。暂停状态会保留到下次启动。

PrimeBackup 的任务等待适配基于 1.12.0。无法读取任务状态时，插件会等待并提示。其他需要停服操作的插件，请先手动暂停 Guard。

## 恢复 MCDR 进程

`!!guard setup` 会接管当前 MCDR，等它完全退出后再启动新进程。重复执行不会启动多个守护进程。部署记录会保留，下次启动时会自动部署守护。同目录已有 MCDR 时，新实例会拒绝启动服务端；后台运行时直接进游戏管理即可。

检测到世界锁被其他服务端占用时，会暂停自动恢复。先正常关闭多余的服务端，确认只保留一个实例，再执行 `!!guard on`。不要删除 `session.lock`。

从 1.2.0 升级：先在游戏内执行 `!!guard stop`，等旧 MCDR 和后台守护退出，替换插件后手动启动一次 MCDR，再执行 `!!guard setup`。这样会同时更新后台启动器。

自动恢复后的 MCDR 在后台运行，控制台输出写入 `.mcdr_guard/console.log`，游戏内命令照常可用。每次恢复会读取原来的 `config.yml`，生成关闭控制台输入的运行副本，保留原配置。它不注册系统服务，不能在电脑关机后启动服务器。使用自定义 `--config` 或 `--permission` 参数的环境暂不支持一键部署。

如果希望保留终端交互，也可以从 Releases 下载 `mcdr_guard_launcher.py`，放到含有 `config.yml` 的目录，在退出原来的 MCDR 后运行：

```bash
python3 mcdr_guard_launcher.py
```

Windows 使用 `python`。启动器会执行当前环境中的 `mcdreforged`，退出码为 0 时也会重启。首次等待 5 秒，连续退出时逐步延长到 60 秒。运行满 5 分钟后，等待时间恢复为 5 秒。

计划停服后，先按原来的方式启动 MCDR，再输入 `!!guard on`；使用终端启动器时也可以运行：

```bash
python3 mcdr_guard_launcher.py --resume
```

不要同时运行多个启动器或其他进程守护工具。自动恢复不处理进程卡死，也不修复导致停服的磁盘、配置或存档问题。

## 开发

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python build.py
```

产物位于 `dist`。推送与插件版本一致的 tag（例如 `v1.2.1`）会运行测试并发布 Release。官方目录提交文件位于 `catalogue/mcdr_guard`。

MIT License.

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MCDRGuard-v1.2.1.mcdr](https://github.com/yuzai114514/mcdr-guard/releases/tag/v1.2.1) | 1.2.1 | 2026/09/26 12:53:05 | 10.89KB | 5 | [下载](https://github.com/yuzai114514/mcdr-guard/releases/download/v1.2.1/MCDRGuard-v1.2.1.mcdr) |
| [MCDRGuard-v1.2.0.mcdr](https://github.com/yuzai114514/mcdr-guard/releases/tag/v1.2.0) | 1.2.0 | 2026/09/26 08:32:09 | 9.82KB | 4 | [下载](https://github.com/yuzai114514/mcdr-guard/releases/download/v1.2.0/MCDRGuard-v1.2.0.mcdr) |
| [MCDRGuard-v1.1.0.mcdr](https://github.com/yuzai114514/mcdr-guard/releases/tag/v1.1.0) | 1.1.0 | 2026/09/26 08:08:43 | 4.75KB | 5 | [下载](https://github.com/yuzai114514/mcdr-guard/releases/download/v1.1.0/MCDRGuard-v1.1.0.mcdr) |

