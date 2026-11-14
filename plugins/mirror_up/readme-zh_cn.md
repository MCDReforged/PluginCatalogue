[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mirror_up

### 基本信息

- 插件 ID: `mirror_up`
- 插件名: MirrorUP
- 版本: 0.6.4
  - 元数据版本: 0.6.4
  - 发布版本: 0.6.4
- 总下载量: 26
- 作者: [MiYui34](https://github.com/MiYui34)
- 仓库: https://github.com/MiYui34/MirrorUP
- 仓库插件页: https://github.com/MiYui34/MirrorUP/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 镜像服增量同步：只传变更的文件与变更的 region chunk。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [xxhash](https://pypi.org/project/xxhash) |  |

```
pip install xxhash
```

### 介绍

# MirrorUP

MCDR 镜像服**增量**同步插件：只传真正变了的文件，`.mca` 再细到 chunk。

## 特性

- **文件级增量**：跨轮索引记下每个文件的 `size / mtime / 哈希`，没变的文件不读、不传。
- **chunk 级增量**：region 文件只看脏 chunk（时间戳过滤 + 哈希确认），未变的 chunk 直接复用。
- **镜像纠偏**：镜像上被玩家改过的文件，下一轮会被发现并恢复。
- **原子写入**：先写临时文件再替换，镜像上不会出现半个文件；写入失败下一轮自动重试。
- **原地写 region**：`.mca` 默认 append-and-commit + 8KB 头 journal，一个 chunk 变了就只写它；碎片攒多了自动整理。
- **外置 chunk 也增量**：`.mcc` 外置容器的 region 只搬迁占位记录，内容变化按普通文件增量同步；不再被任何 region 引用的 `.mcc` 会被清理（`sync.clean_mcc_orphans`）。
- **跨机同步**：主服用 `exporter` 模式只读提供数据（HTTP + Bearer token，可上 TLS），镜像侧不用挂载主服目录。
- **自动停服**：支持 `rcon`、MCSManager（`mcsm`）与自定义命令（`external`）停/启镜像；停不下来就拒绝写入。
- **多镜像目标**：一份源、多个镜像目录，共享一个索引（按目标分区），每个目标可以有自己的停服方式。
- **校验与历史**：`!!mu verify` 核对源/镜像/索引三方是否一致（`--deep` 比哈希），`!!mu history` 查看每轮结果。
- **定时同步**：间隔 60 秒 ~ 7 天，可随时开关。

## 安装

需要 MCDR ≥ 2.12.0、Python ≥ 3.9。

1. 从 [Releases](https://github.com/MiYui34/MirrorUP/releases) 下载 `MirrorUP-v0.6.4.mcdr` 放进 MCDR 的 `plugins/`；或者把仓库里的 `MirrorUP/` 目录放进去（目录名建议 `MirrorUP`）。
2. 安装依赖：`pip install xxhash`。MCDR 只校验依赖、不会自动安装，缺依赖会在日志里报 `RequirementCheckFailure`。
3. 重启 MCDR，首次加载会生成 `config/mirror_up/config.json`。

## 快速开始

1. 编辑配置里的 `source.root`（主服目录）和 `target.root`（镜像服目录），相对路径以 **MCDR 根目录** 为基准。
2. **停掉镜像服**，在主服执行 `!!mu diff` 查看本轮计划。
3. 确认无误后执行 `!!mu sync`。
4. 看到"目标已更新完毕"后手动启动镜像服。
5. 需要自动同步：`!!mu schedule set 30m`，再 `!!mu schedule on`。

## 配置

首次启动生成 `config/mirror_up/config.json`，改完执行 `!!mu reload` 生效。

| 键                                 | 默认                                 | 说明                                                                                             |
| --------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------- |
| `source.root`                     | `./server`                         | 主服目录（含 `world/`、`mods/`）                                                                       |
| `source.transport`                | `local`                            | `local` 直接读盘；`agent` 从主服的 exporter 拉取                                                          |
| `source.agent.url`                | `http://127.0.0.1:25580`           | exporter 地址（`transport=agent` 时用）                                                              |
| `source.agent.token`              | 空                                  | 与 exporter 的 `agent_server.token` 一致                                                           |
| `source.agent.tls_pin_sha256`     | 空                                  | 可选，固定自签证书指纹                                                                                    |
| `source.agent.verify_copy`        | `true`                             | 每个文件下载完再发一次 `/v1/stat` 复核；跨机高延迟时可设 `false` 省掉一半往返                                              |
| `role`                            | `driver`                           | `driver` 执行同步；`exporter` 只对外提供数据                                                               |
| `target.root`                     | `./Mirror/server`                  | 镜像服目录（单目标时的简写；等价于 `targets[0]`）                                                                |
| `targets`                         | 一个 `default`                       | 多镜像目标：`[{"name","root","enabled","mirror_control"?}]`，每个目标可覆盖停服配置                              |
| `sets`                            | `world`、`mods`                     | 同步哪些目录；`config/`、`server.properties` 默认不同步                                                     |
| `exclude`                         | `session.lock`、`*.tmp`、`logs/**` 等 | glob 排除，命中目录整棵跳过                                                                               |
| `sync.concurrency`                | `8`                                | 并行拷贝数；跨机高延迟链路可以调到 16                                                                           |
| `sync.verify_target`              | `true`                             | 每轮检查镜像是否被改动                                                                                    |
| `sync.region_delta`               | `true`                             | `.mca` 走 chunk 级增量，`false` 退回整文件                                                               |
| `sync.region_write_mode`          | `inplace`                          | `inplace` 原地追加，`rebuild` 重建后替换                                                                 |
| `sync.journal`                    | `true`                             | `inplace` 的 region 头快照；`false` 会降级为 `rebuild`                                                  |
| `sync.clean_mcc_orphans`          | `true`                             | 删除不再被任何 region 引用的 `.mcc` 外置 chunk                                                             |
| `log.history_keep`                | `20`                               | `!!mu history` 保留多少轮                                                                           |
| `source_flush.enabled`            | `true`                             | 扫描前 `save-off` + `save-all flush`，扫描后 `save-on`；`transport=agent` 或目标用 `adapter: "self"` 时自动关闭 |
| `mirror_control.adapter`          | `manual`                           | `manual` 只检查；`rcon` / `external` / `mcsm` 自动停启；`self` 控制本 MCDR 自己的服（就地同步）                      |
| `mirror_control.rcon`             | `127.0.0.1:25575`                  | RCON 停服参数                                                                                      |
| `mirror_control.external`         | 空                                  | `stop_cmd` / `start_cmd` / `probe_cmd` 自定义命令                                                   |
| `mirror_control.mcsm`             | 空                                  | MCSManager 面板：`base_url`、`apikey`（v9）或 `username`/`password`（v10）、`uuid`、`remote_uuid`         |
| `mirror_control.start_after_sync` | `true`                             | 同步后自动启动镜像并等端口就绪                                                                                |
| `agent_server`                    | `127.0.0.1:25580`                  | exporter 的监听地址、token 与 TLS 证书                                                                  |
| `schedule.interval_seconds`       | `3600`                             | 自动同步间隔，60 ~ 604800 秒                                                                           |

## 就地同步：命令在哪个服敲，就同步哪个服

想把插件**装到每一台服**上、玩家站在哪台服敲 `!!mu sync` 就同步哪台服，用 `self` 适配器：

- **主服**：`role: "exporter"`，只读地对外提供世界（`agent_server` + token）。
- **镜像服**：`role: "driver"`，`source.transport: "agent"` 指向主服，`targets` 只留一个指向自己：

```json
"targets": [
  { "name": "self", "root": "./server",
    "mirror_control": { "adapter": "self", "notify_players_sec": 10 } }
]
```

`adapter: "self"` 的意思就是“目标是我这个 MCDR 管的服务器”。有变更时插件会：

1. 在服里广播停服提示（`notify_players_sec` 秒，0 表示不提示）；
2. 调 `server.stop()` 停掉本服——**MCDR 不会退出**；
3. 等 `session.lock` 释放，再写入差异；
4. `server.start()` 把本服拉起来，并等它重新可连。

停的是服务端而不是 MCDR，所以同步线程不会被一起停掉。没变更时这四步一步都不做，只是 stat 一遍。

## 跨机同步（可选）

主服与镜像不在同一台机器、或者不想让镜像侧挂载主服目录时，用 `exporter` + `agent`：

1. **主服**（MCDR 里装同一个插件）：
   - `role` 改成 `"exporter"`；
   - `agent_server.host` 改成 `0.0.0.0`（或内网 IP），`port` 默认 `25580`；
   - `agent_server.token` 填一个至少 16 字符的随机串；
   - 执行 `!!mu reload`（或重启 MCDR），日志出现「exporter 已监听」。
2. **镜像侧**（driver）：
   - `source.transport` 改成 `"agent"`；
   - `source.agent.url` 填 `http://<主服IP>:25580`；
   - `source.agent.token` 填同一个 token。
3. 公网部署请开 TLS（`agent_server.tls.enabled` + 证书），并在驱动端填 `tls_pin_sha256` 固定指纹。

exporter 只读：它不写任何东西，也不执行同步命令。`!!mu status` 在 exporter 上显示监听地址与对外提供的 set。

跨机时 `source_flush` 会被自动关闭（driver 不在源服那台机器上，`save-off` 只会发给本机镜像服）；目标用 `adapter: "self"` 时同理（本机正是要写入的那台）。请保证 exporter 侧的世界已经落盘：要么主服定期保存，要么同步前在主服执行一次 `save-all flush`。

## 命令

| 命令                      | 权限  | 说明                                  |
| ----------------------- | --- | ----------------------------------- |
| `!!mu sync`             | 2   | 同步一次                                |
| `!!mu sync --dry-run`   | 2   | 只出计划，不动镜像                           |
| `!!mu sync --full`      | 2   | 忽略索引，全量重算哈希                         |
| `!!mu sync --force`     | 2   | 跳过安全检查（空源保护、版本门禁）                   |
| `!!mu diff`             | 2   | 同 `--dry-run`                       |
| `!!mu status`           | 0   | 索引规模、各目标上次同步、待重试项                   |
| `!!mu verify [--deep]`  | 2   | 校验源/镜像/索引一致性；`--deep` 逐个比哈希（会读全部内容） |
| `!!mu history [N]`      | 0   | 最近 N 轮同步结果（默认 10，最多 50）             |
| `!!mu cancel`           | 2   | 取消进行中的同步                            |
| `!!mu schedule on|off`  | 3   | 开关自动同步                              |
| `!!mu schedule set 30m` | 3   | 设置间隔（`s`/`m`/`h`/`d`）               |
| `!!mu index rebuild`    | 3   | 丢弃索引，下一轮全量                          |
| `!!mu reload`           | 3   | 重读配置                                |

## 注意事项

- **镜像必须完全停止才能同步**。默认 `manual` 适配器用 `session.lock` 判断；`rcon` / `external` 可以自动停服；`self`（就地同步）会自己停本服再拉起——但停不下来时会中止同步，绝不在镜像还活着时写盘。
- **不做备份**。镜像上被覆盖的区块和模组没有历史版本。
- **写入量不等于读取量**。`.mca` 默认 `inplace`，改动一个 chunk 时目标端只写这个 chunk 加 16KB（新头 + journal）；`rebuild` 模式才会重写整个 region。
- **不覆盖配置文件**。`config/`、`server.properties` 不在默认同步范围内，手动加进去会覆盖镜像的配置。
- **空源保护**。源目录扫出 0 个文件但索引里有记录（路径写错、磁盘没挂载）时会中止，不会清空镜像；确认要清空请加 `--force`。
- **版本门禁**。源与镜像 `level.dat` 的 MC 版本不一致时拒绝写入。
- **跨机要保证 token 一致**。driver 与 exporter 的 token 不同会直接连不上；exporter 是只读的，不提供任何写入接口。

## 常见问题

- **"扫描到 0 个文件，但索引中有 N 条记录"**：源路径写错或磁盘未挂载。修好后重跑；确实要清空镜像再加 `--force`。
- **"版本不一致"**：镜像世界来自旧版本。先用同一版本启动一次镜像，或确认要覆盖后 `--force`。
- **"待重试 N 项"**：文件在拷贝途中一直被改写或被占用（常见于正在写盘的 region），下一轮会自动重试。
- **换了世界或改了源根**：`world_id` 对不上会拒绝旧索引，执行 `!!mu index rebuild`。
- **"源端不可用"**：跨机时连不上 exporter、token 不对，或主服没开 `role=exporter`。检查地址、端口、token 和主服日志里的「exporter 已监听」。
- **"自动停服失败"**：`rcon` 连不上或 `external` 脚本返回非零。镜像没停下来就不会写盘，修好适配器再同步。
- **`self` 报"本服没有退出"**：本服不响应 MCDR 发出的 `stop`（被包装脚本接管、卡在保存，或根本不是能被 MCDR 停止的服务端）。手动关掉本服后再执行 `!!mu sync`；插件在确认退出前不会写入任何文件。

## 版本

当前 `0.6.4`：文件级 + chunk 级增量、原地写 region（含头 journal 与碎片整理）、镜像纠偏、定时同步、跨机 agent 传输（含 TLS）、`.mcc` 外置 chunk 增量与孤儿清理、多镜像目标（共享索引）、校验与同步历史、MCSM/rcon/external 自动停服、**就地同步（`adapter: "self"`：命令在哪台服敲就停/写/启哪台服）**、Python API。

`0.6.2` 修复：`!!MCDR plugin install mirror_up` 时，依赖列表里的 `xxhash>=3.0` 会被 MCDR 直接拼成 PyPI 链接，`>` 在 URL 里非法，服务端解析聊天组件时报 `Invalid chat component: Illegal character in path`。插件库的依赖列表读的是仓库里的 `requirements.txt`（不是 `mcdreforged.plugin.json` 的 `requirements` 字段），所以 0.6.1 只改后者没有生效；0.6.2 把 `requirements.txt` 也改成不带版本约束的 `xxhash`。

`0.6.3` 修复：以 `role: "exporter"` 加载插件时，agent 绑定端口会走 `HTTPServer.server_bind()`，其中 `socket.getfqdn()` 的反向 DNS 查询在 macOS 上可能阻塞十几秒，触发 MCDR 的 `TaskExecutor 线程已经 10 秒没有响应` 警告。现在改为直接绑定，不再做反向解析。

`0.6.4` 修复：跨机同步时每个文件都新建一条 TCP 连接（下载完还要再发一次 `/v1/stat` 复核），几万个小文件时光是握手就要几个小时。现在每个线程复用一条 keep-alive 连接，连接被对端关掉时自动换新重试；`sync.concurrency` 默认从 4 提到 8；新增 `source.agent.verify_copy`（默认 `true`），设为 `false` 可省掉每个文件那次复核往返。

## 许可证

[GPL-3.0](https://github.com/MiYui34/MirrorUP/tree/main/LICENSE) © MiYui34。分发修改版需要同样以 GPL-3.0 开源，并保留版权声明。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MirrorUP-v0.6.4.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.4) | 0.6.4 | 2026/11/14 03:56:56 | 90.07KB | 1 | [下载](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.4/MirrorUP-v0.6.4.mcdr) |
| [MirrorUP-v0.6.3.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.3) | 0.6.3 | 2026/11/10 13:10:15 | 89.25KB | 6 | [下载](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.3/MirrorUP-v0.6.3.mcdr) |
| [MirrorUP-v0.6.2.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.2) | 0.6.2 | 2026/11/10 12:53:45 | 89.04KB | 5 | [下载](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.2/MirrorUP-v0.6.2.mcdr) |
| [MirrorUP-v0.6.1.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.1) | 0.6.1 | 2026/11/10 11:44:39 | 89.04KB | 6 | [下载](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.1/MirrorUP-v0.6.1.mcdr) |
| [MirrorUP-v0.6.0.mcdr](https://github.com/MiYui34/MirrorUP/releases/tag/v0.6.0) | 0.6.0 | 2026/11/09 07:21:01 | 89.05KB | 8 | [下载](https://github.com/MiYui34/MirrorUP/releases/download/v0.6.0/MirrorUP-v0.6.0.mcdr) |

