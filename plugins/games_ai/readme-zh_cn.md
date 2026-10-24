[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## games_ai

### 基本信息

- 插件 ID: `games_ai`
- 版本: *数据拉取失败*
- 总下载量: 1491
- 作者: [yello](https://github.com/PengZixuan30)
- 仓库: https://github.com/PengZixuan30/Games_AI
- 仓库插件页: https://github.com/PengZixuan30/Games_AI/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: *数据拉取失败*

### 插件依赖

*数据拉取失败*

### 包依赖

*数据拉取失败*

### 介绍

<div align="center">

# GamesAI for MCDReforged

[English](https://github.com/PengZixuan30/Games_AI/tree/main//README.md)  |  简体中文  |  [繁體中文](https://github.com/PengZixuan30/Games_AI/tree/main//README.zh-TW.md)

[反馈问题](https://github.com/PengZixuan30/Games_AI/issues/new)  |  [反馈想法](https://github.com/PengZixuan30/Games_AI/discussions/new/choose)  |  [加入Q群](https://qm.qq.com/q/jDQQaUPNmw)

[转至Fabric版本](https://github.com/PengZixuan30/GamesAI)

</div>

> [!NOTE]
> **GamesAI 插件/模组 QQ 交流群：849544707** — 欢迎加入交流群讨论问题、反馈建议，以及分享 prompt、skills、tools 等配置！

> [!NOTE]
> 欢迎使用版本 0.8.0！本次加入**跨服连接**：多个 MCDR 实例通过 WebSocket 组成一个集群，其中一台成为 hub，承载 AI、对话历史与公共数据库，其余实例以客户端接入、转发玩家的命令（集群级命令由它们自己执行）；工具仍留在各实例本地 —— 每个请求都携带发起实例本地的工具 schema；假人（Mineflayer bot）也从「自己监听端口」改为接入集群的客户端。详见[跨服连接文档](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/cross-server.md)。每条对话也会**落盘**(存在与 `!!data` 同一个数据库文件的 `chat_history` 表里),重载、更新、重启乃至卸载插件都不会再丢失;新增的 `send_message_to_player_ai` 工具还能让当前用户的助手把一条消息转交给另一个用户的对话。最新的改动让 `!!ask stop` 保留本轮已写入的历史，并新增按名字清理历史的 `!!gamesai clear <name>`。

<details>
<summary>目录(点击展示)</summary>

- [GamesAI for MCDReforged](#gamesai-for-mcdreforged)
  - [安装](#安装)
  - [快速上手](#快速上手)
    - [1. 首次启动：让插件自己把依赖装好](#1-首次启动让插件自己把依赖装好)
    - [2. 配置一个 AI](#2-配置一个-ai)
    - [3. 验证连通并问出第一句话](#3-验证连通并问出第一句话)
    - [4. 对话存在哪里（以及怎么清理）](#4-对话存在哪里以及怎么清理)
    - [5. 给 AI 加能力：工具与技能（可选）](#5-给-ai-加能力工具与技能可选)
    - [6. 让 AI 开一个假人（可选）](#6-让-ai-开一个假人可选)
    - [7. 把多台实例连成集群（可选）](#7-把多台实例连成集群可选)
    - [8. 日常维护](#8-日常维护)
    - [命令速查](#命令速查)
  - [技术文档](#技术文档)
  - [AI 在本项目中的角色](#ai-在本项目中的角色)
  - [鸣谢与声明](#鸣谢与声明)
  - [赞助与贡献者名单](#赞助与贡献者名单)
  - [许可证](#许可证)

</details>

## 安装

在MCDR控制台中使用如下命令以安装插件

`!!MCDR plugin install games_ai`

环境要求：Python 3.12 或更高、MCDReforged 2.15.0 或更高（清单声明 `mcdreforged >= 2.15.0`；插件运行在 MCDR 自己的解释器上）。仅在启用 Mineflayer 假人时才需要 Node.js 18+ 与 npm。

---

或者在[MCDR插件仓库](https://mcdreforged.com/plugin/games_ai)中获取并安装到你的插件目录内

如果选择手动安装：插件的 Python 包由它自己处理 —— 首次启动时检查 `openai`、`requests`、`websockets`，缺哪个就用 pip 补装（先用本机 pip 配置，失败了再用阿里云 PyPI 镜像重试），装好之后自动重载插件。只有两次都失败时才需要你介入，日志里会给出可以直接复制的命令（`python -m pip` 形式）：

```bash
python -m pip install openai requests websockets
```

`!!MCDR plugin install games_ai` 也无法预先安装任何东西：包清单位于插件内部（`games_ai/requirements.txt`），而 MCDR 只读取插件根目录下的 `requirements.txt`，然后才加载插件。因此哪种安装方式一开始都缺这些包，插件会在首次启动时自行补装（见 [PIM](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/pim.md)）；只有两次 pip 尝试都失败时，才用上面的手动命令，装完后执行 `!!MCDR plugin reload games_ai` 让插件重新加载。

从旧版本升级无需手动改配置：旧的 `mineflayer_bot.websocket.url` 会在首次加载时迁移为顶层的 `websocket.uri`。集群中，运行旧构建的节点无法听从 hub 的更新顺序，所以要在每个实例上手动安装一次新构建（`!!MCDR plugin install -U -y games_ai`）。只有 hub 需要有可被访问的端口，而 `wss://` 的 uri 只能作为客户端。

插件会自己维护自己：更新器会替换插件自己的文件（集群感知、下载校验、失败回滚），Python 包管理器会补装缺失的包。两者见 [PIM：插件自己的安装管理器](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/pim.md)。

## 快速上手

### 1. 首次启动：让插件自己把依赖装好

把插件放进 `plugins/`，启动服务器（已经装过时执行 `!!MCDR plugin reload games_ai` 即可）。首次启动时它会检查三个 Python 包（`openai`、`requests`、`websockets`），缺哪个就用 pip 补装 —— 先用本机 pip 配置，失败后改用阿里云 PyPI 镜像重试 —— 然后重载自己：

```text
Installing the missing Python package(s) with pip: ...
[deps] ...
Dependencies installed; reloading the plugin...
Dependencies are ready; the plugin is fully loaded again (openai, requests, websockets)
```

这期间插件处于"已加载但不工作"状态：不注册命令、不启动假人，也不建立跨服链路。两次尝试都失败时，日志会打出 `Could not install: ...` 以及需要手动执行的命令（`python -m pip install openai requests websockets`）；执行它，再 `!!MCDR plugin reload games_ai`。详见 [PIM：Python 包管理器](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/pim.md#python-包管理器)与[缺少 Python 依赖包](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/troubleshooting.md#缺少-python-依赖包)。

### 2. 配置一个 AI

打开 `config/games_ai/config.json`（首次启动时自动生成），填好一个 `all_ai` 条目和 `default_ai`：

```json
{
  "all_ai": {
    "<你的 AI ID>": {
      "prompt": "你是一个成熟可靠的 Minecraft 助手。",
      "ai_name": "[GamesAI]",
      "base_url": "<你的 API Base URL>",
      "ai_model": "<你的 AI 模型>",
      "api_key": "<你的 API Key>",
      "extra_body": {}
    }
  },
  "default_ai": "<你的 AI ID>"
}
```

- `all_ai` 里每个条目是一个模型，条目的键就是插件的内部 AI_ID。
- `base_url`、`ai_model`、`api_key` 分别是服务商的 OpenAI 兼容接口地址、模型名和密钥。
- `ai_name` 是 AI 回复时使用的前缀（支持 Minecraft 格式代码）。
- `extra_body` 会原样传给服务商 —— 例如思考模型可以写 `{"thinking": {"type": "enabled"}}`。
- `default_ai` 必须正好等于 `all_ai` 里的某个键：它就是直接 `!!ask` 时使用的模型。
- 可选的 `context_window` 用来覆盖该模型的[上下文自动管理](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#上下文自动管理)窗口。

提示词很长时不必写进配置文件：把 `prompt` 写成 `"> my_prompt.md"`，正文会从 `config/games_ai/prompt/my_prompt.md` 读取。

改完执行 `!!gamesai reload`。`!!gamesai config get <key>` 与 `!!gamesai config set <key> <value>` 可以处理顶层简单键，但 `config set` 会拒绝复杂的 `all_ai` 与 `mineflayer_bot` 块，也不会解析带点的键，这两块请在文件里改。全部键的含义见[配置](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/configuration.md#3all_ai)。

### 3. 验证连通并问出第一句话

`!!gamesai speedtest` 会向每个模型的 `<base_url>/models` 发一次请求并打印延迟（`!!gamesai speedtest <model>` 只测一个）。然后直接和它说话：

```text
!!ask 你好，你在吗？
```

`!!ask` 对所有玩家开放。围绕它的还有：`!!ask -n <content>` 不带历史回答，`!!ask -f <content>`（别名 `--forced`）把问题并入正在运行的那一轮，`!!ask switch <model>` 把对话交给另一个模型（旧模型先做摘要转接），`!!ask stop` 停掉你名下所有在途工作并**保留本轮已经写入的内容**，`!!ask context [玩家]` / `!!ask context --all` 查看上下文占用。详见 [AI 请求链路](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#上下文查看)与[停止正在进行的对话](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#停止正在进行的对话)。

### 4. 对话存在哪里（以及怎么清理）

每条对话都会在每轮结束后写入 `config/games_ai/database/public_database.db` 的 `chat_history` 表（与 `!!data` 同一个文件、不同的表），并在每次插件加载时恢复。因此重载、更新、重启乃至卸载插件都不会再丢失。

`!!gamesai clear` 删除你自己的对话；`!!gamesai clear <name>` 删除指定玩家的对话（需要配置的 `permission` 等级，会先停掉对方正在跑的回合）；`!!gamesai clearall` 删除所有人的（同样需要权限）。详见[对话持久化](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#对话持久化)。

### 5. 给 AI 加能力：工具与技能（可选）

插件自带 27 个内置工具（世界查询、公共数据、技能、假人）。一次请求能拿到哪些工具，取决于玩家的 MCDR 权限等级与配置里的 `permission` —— 低等级玩家根本看不到管理类工具。

- **自定义工具**：首次启动会生成 `config/games_ai/tools/tools.py`，里面带一个 `@register_tool` 骨架；把你的函数写进去，然后 `!!gamesai reload`。详见[工具](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/tools.md#2-在-toolspy-中自定义工具)。
- **技能**：`config/games_ai/skills/skills.json` 是技能索引，AI 通过 `read_skills` 读取其中列出的文件，也可以自己写和维护。详见[技能](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/skills.md#3-添加自己的技能)。

### 6. 让 AI 开一个假人（可选）

服务器上需要安装 Node.js 18+ 与 npm。然后设置凭据并启动：

```text
!!aibot set username <Minecraft 账号名>
!!aibot set password <密码>
!!aibot set auth microsoft
!!aibot join
```

`!!aibot leave` 再次停掉它。`config.json` 里对应的设置是 `mineflayer_bot` 下的 `enabled`、`cycle_interval`（自治控制器多久决策一次，默认 15 秒）与 `bot.username` / `bot.password` / `bot.auth`（`microsoft`、`mojang` 或 `offline`）。假人作为客户端接入集群，自己不开端口；服务器地址从 `server.properties` 读取。`username`/`password`/`auth` 只在 Node 进程（重）启动时读取，所以改完要用 `!!aibot set` 并重启（`!!aibot leave`，再 `!!aibot join`）；`!!gamesai config set` 会拒绝整个 `mineflayer_bot` 块。详见 [Mineflayer 假人](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/mineflayer-bot.md#指令)。

### 7. 把多台实例连成集群（可选）

其中一台成为 **hub**（拥有 AI、对话历史与公共数据库），其余实例作为**客户端**接入并转发玩家的命令；工具仍各实例自带。在每台实例 `config.json` 的 `websocket` 块里指向 hub：

```json
{
  "websocket": {
    "uri": "ws://<hub 地址>:8080",
    "force_server": false,
    "name": ""
  }
}
```

在该地址上探测到 GamesAI hub 的实例会成为客户端；什么都没探测到（且自己绑得住该地址）的实例会当 hub，`force_server` 则强制当 hub。入网按节点进行：在 hub 上用 `!!gamesai node pending` 看等待名单，`!!gamesai node token <name>` 签发 token，目标实例自己用 `!!gamesai node claim <token>` 入网。`websocket.name` 留空时由实例目录派生。集群更新由 hub 排序 —— 先节点、后 hub。其余键（`allow_app_id`、`token_ttl_hours`、`auto_enroll`、`identity_file`）见[配置 §6](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/configuration.md#6websocket)；完整说明见[跨服连接](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/cross-server.md#注册每个实例一份-token)与[集群更新](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/cross-server.md#集群更新)。

### 8. 日常维护

- `!!gamesai reload` 重新读取配置、技能与工具，必要时重启假人；跨服链路继续运行。`websocket.*` 的改动要用 `!!MCDR plugin reload games_ai`（或 `!!gamesai node claim` / `node forget`，它们会重建链路），因为链路是在加载时建立的。详见[热重载](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/hot-reload.md#触发热重载)。
- `!!gamesai check` 检查是否有新版本，并刷新上下文窗口表；集群里由 hub 协调。插件会更新自己的文件（下载校验、失败回滚）并自我修复 Python 包 —— 见 [PIM](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/pim.md)。
- `!!gamesai debug` 切换完整请求日志；`!!gamesai debug thread` 列出插件持有的线程。
- `!!data` 管理 AI 可读的公共键值数据库。
- 出问题了？看[故障排查](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/troubleshooting.md)，里面按日志行给出处理办法。

---

### 命令速查

输入 `!!gamesai` 可查看游戏内功能列表（`!!gamesai node …` 用于集群注册，`!!aibot …` 用于假人）；下表列出的是最常用的指令。

| 指令                                                                      | 用途                                                                                                                                                                  |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!gamesai clear`                                                       | 清除你自己的历史聊天记录。它存放在公共数据库文件的独立数据表中,该指令会删除你那一行。`!!gamesai clear <name>` 改为清除另一位玩家的历史记录，需要达到配置中的 `permission` 等级；该玩家还在进行的对话轮会先被停止。                                       |
| `!!gamesai clearall`                                                    | 清除所有玩家的历史聊天记录(包括已存储的行)。                                                                                                                                             |
| `!!gamesai reload`                                                      | 重新加载配置、技能与工具并重启 Bot；跨服链路会继续运行。详见[热重载](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/hot-reload.md#热重载)。                                             |
| `!!gamesai check`                                                       | 检查插件更新，并强制刷新上下文窗口表。集群里由 hub 执行并发起一轮更新：节点先装、hub 最后装（见[跨服连接](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/cross-server.md#集群更新)）                     |
| `!!gamesai speedtest [model]`                                           | 测试 API 服务器连接延迟，不指定模型时测试全部                                                                                                                                           |
| `!!gamesai config get <key>`                                            | 读取一个配置项的值。                                                                                                                                                          |
| `!!gamesai config set <key> <value>`                                    | 修改一个配置项的值（自动适配旧值类型，修改后自动触发[热重载](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/hot-reload.md#热重载)）。                                                  |
| `!!gamesai node <pending|token|list|revoke|rotate|claim|status|forget>` | 集群注册与节点管理；见[跨服连接](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/cross-server.md#注册每个实例一份-token)。                                                    |
| `!!aibot join | leave`                                                  | 启动或停止假人（Mineflayer bot）；`!!aibot set <key> <value>` 可修改假人凭据并重载。见 [Mineflayer Bot](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/mineflayer-bot.md)。 |

---

你也可以直接输入`!!ask`向AI提问或者聊天或者帮你做一些事情

| 指令                     | 用途                                                                                                                                                                                                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!!ask <content>`      | 向AI提问或者聊天或者帮你做一些事情，content为你想让AI做的事情或者你想问AI的问题                                                                                                                                                                                                             |
| `!!ask -n <content>`   | 向AI提问但不使用历史记录（当前对话仍会被保存）                                                                                                                                                                                                                                   |
| `!!ask -f <content>`   | 强制提问：不等待当前轮结束，将消息并入正在运行的对话轮（别名 `--forced`）。详见[AI 请求链路与对话机制](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#ai-请求链路与对话机制)。                                                                                            |
| `!!ask switch <model>` | 切换当前对话使用的 AI 模型，model为AI_ID或昵称。切换时清空历史，并在你下次提问前由旧模型压缩为摘要转接给新模型，详见[切换模型时的摘要转接](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#切换模型时的摘要转接)。                                                                            |
| `!!ask stop`           | 立即停止你名下所有正在进行的对话：运行中的对话轮（含工具调用）、正在进行的 `!!ask -n` 提问、以及你委派给 Bot 的任务。**本轮已经写入的内容会保留在历史里** —— 只有结果始终没有回来的那个工具调用会被丢弃；`!!ask -f` 排队消息会保留，由你下一轮合并。详见[停止正在进行的对话](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#停止正在进行的对话)。 |
| `!!ask context [玩家]`   | 查看上下文占用：模型与窗口来源、已用比例、距离压缩还有多少余量、逐轮规模与缓存命中。不填玩家即查看自己。详见[上下文查看](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#上下文查看)。                                                                                                 |
| `!!ask context --all`  | 按模型汇总全服所有玩家的上下文用量（零用量的模型不列出），悬停可看该模型自这些对话创建以来的累计用量（重载与重启都不会丢失）。详见[上下文查看](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#上下文查看)。                                                                                      |
| `!!ask compact`        | 立即压缩较早的历史（忽略窗口触发线），由你下次提问前的预检完成，指令本身不阻塞。详见[上下文查看](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md#上下文查看)。                                                                                                             |

---

输入`!!data`获取有关数据库指令的信息

> [!TIP]
> 数据库会在首次启动时自动创建，无需额外的升级步骤。

| 指令                           | 用途                                      |
| ---------------------------- | --------------------------------------- |
| `!!data write <key> <value>` | 在公共数据库内添加一条数据，其中key不能包含空格，value可以是任意字符串 |
| `!!data add <key> <value>`   | 将value追加到公共数据库中的key中，不存在时自动创建新key       |
| `!!data del <key>`           | 在公共数据库内删除一条数据，无论key是否存在                 |
| `!!data read <key>`          | 读取公共数据库中key对应的value                     |
| `!!data list`                | 读取公共数据库中的所有内容                           |
| `!!data list keys`           | 读取公共数据库中的所有key                          |

---

## 技术文档

技术细节集中在 [`docs/zh_cn/`](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/)：请求如何组装并保持在窗口内、每个配置项的含义、工具与技能系统如何工作、机器人如何被驱动、出问题时怎么排查。

| 文档                                                                                                | 内容                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AI 请求链路](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/ai-request-pipeline.md)   | 请求链路、无历史 `!!ask -n`、`!!ask switch` 摘要转接、`!!ask stop`、上下文自动管理、每玩家状态                                                                                                                                                  |
| [配置](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/configuration.md)              | `config.json` 的全部键：`prefix`、`permission`、`all_ai`（含 `context_window`）、`default_ai`、`mineflayer_bot`、`websocket`（`uri`、`force_server`、`allow_app_id`、`name`、`token_ttl_hours`、`auto_enroll`、`identity_file`）以及自我更新行为 |
| [工具](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/tools.md)                      | 27 个内置工具、在 `tools.py` 里自定义、在自己的插件里注册、权限与可见性                                                                                                                                                                         |
| [技能](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/skills.md)                     | 技能能解决什么、内置技能、`skills.json`、让 AI 自己维护、在自己的插件里注册                                                                                                                                                                      |
| [范例](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/example.md)                    | 一台真实服务器的完整配置：配置、六个技能、44 个自定义工具、一轮实操与踩坑                                                                                                                                                                              |
| [Mineflayer Bot](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/mineflayer-bot.md) | 环境要求、指令、工作原理、支持的操作、Bot 控制工具                                                                                                                                                                                         |
| [热重载](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/hot-reload.md)                | 如何触发重载、重载期间发生了什么、如何让自己的插件跟随重载                                                                                                                                                                                       |
| [跨服连接](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/cross-server.md)             | 集群角色、每节点注册、命令路由、集群更新、工具作用域                                                                                                                                                                                          |
| [PIM](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/pim.md)                       | 插件自己的安装管理器：自我更新与 Python 依赖补装                                                                                                                                                                                        |
| [故障排查](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/troubleshooting.md)          | `!!ask` 报错、Bot 报错、日志与调试                                                                                                                                                                                             |
| [测试](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/testing.md)                    | 怎么装 pytest、怎么跑全部/单个模块/按名字筛选用例、`tests/` 各部分的职责，以及跑测试需要什么                                                                                                                                                             |
| [架构](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/architecture.md)               | 按职责划分的包树、各部分之间允许怎样依赖、依赖门，以及新模块该放在哪里                                                                                                                                                                                 |
| [更新日志](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_cn/changelog.md)                | 各版本的更新说明                                                                                                                                                                                                            |

> 相同文档的其它语言版本：[English](https://github.com/PengZixuan30/Games_AI/tree/main/docs/en_us/) · [繁體中文](https://github.com/PengZixuan30/Games_AI/tree/main/docs/zh_tw/)。

---

## AI 在本项目中的角色

GamesAI 本身是 AI 驱动的插件,而 AI 也在本项目自身的维护中扮演重要角色:

1. 本 README 最初由作者(yello)排版,后全部交由 AI 修改;
2. 所有翻译文件(`lang/*.yml`)均由 AI 修改;
3. 每次发布前的逻辑检查由 AI 完成;
4. 快照/开发版本中出现的问题将由 AI 排查;
5. GitHub 反馈的 issue、PR 等将先由 AI 排查问题,再交由维护者处理。

## 鸣谢与声明
特别感谢 [WangHai Server](https://github.com/Wanghai-Server) 为此插件的测试提供了基础

特别感谢 [william-song-shy (William Song)](https://github.com/william-song-shy) 为 `!!ask` 无历史模式提供的建议。

特别感谢 [ZhangZuoqian (张作乾)](https://github.com/ZhangZuoqian) 为测速指令提供的建议。

AI\(LLM\)模型生成的一切内容与此插件无关

自定义工具造成的一切后果与本插件无关

## 赞助与贡献者名单

赞助地址：[爱发电](https://ifdian.net/a/yello)

为GamesAI赞助的将会出现在下列的赞助者名单中（当前没有赞助者）：

| #   | 赞助者 | 金额  | 日期  |
| --- | --- | --- | --- |
| -   | -   | -   | -   |

## 许可证
MIT License, Copyright (c) 2026 yello

<div align = "center">

---

[回到顶部](#gamesai-for-mcdreforged)

</div>

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [GamesAI-v0.7.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.3) | 0.7.3 | 2026/10/02 03:12:51 | 271.5KB | 31 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.3/GamesAI-v0.7.3.mcdr) |
| [GamesAI-v0.7.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.2) | 0.7.2 | 2026/09/27 06:54:23 | 262.42KB | 16 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.2/GamesAI-v0.7.2.mcdr) |
| [GamesAI-v0.7.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.1) | 0.7.1 | 2026/09/11 17:30:38 | 158.52KB | 25 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.1/GamesAI-v0.7.1.mcdr) |
| [GamesAI-v0.7.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.7.0) | 0.7.0 | 2026/08/29 17:46:11 | 112.88KB | 29 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.7.0/GamesAI-v0.7.0.mcdr) |
| [GamesAI-v0.6.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.4) | 0.6.4 | 2026/08/22 05:15:46 | 112.68KB | 37 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.4/GamesAI-v0.6.4.mcdr) |
| [GamesAI-v0.6.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.3) | 0.6.3 | 2026/08/18 09:05:58 | 107.24KB | 34 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.3/GamesAI-v0.6.3.mcdr) |
| [GamesAI-v0.6.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.2) | 0.6.2 | 2026/08/10 12:54:37 | 101.42KB | 43 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.2/GamesAI-v0.6.2.mcdr) |
| [GamesAI-v0.6.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.1) | 0.6.1 | 2026/08/07 06:52:54 | 92.88KB | 35 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.1/GamesAI-v0.6.1.mcdr) |
| [GamesAI-v0.6.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.6.0) | 0.6.0 | 2026/08/06 05:28:15 | 90.59KB | 27 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.6.0/GamesAI-v0.6.0.mcdr) |
| [GamesAI-v0.5.11.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.11) | 0.5.11 | 2026/07/28 04:27:12 | 54.15KB | 35 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.11/GamesAI-v0.5.11.mcdr) |
| [GamesAI-v0.5.10.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.10) | 0.5.10 | 2026/07/22 07:03:08 | 52.39KB | 31 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.10/GamesAI-v0.5.10.mcdr) |
| [GamesAI-v0.5.9.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.9) | 0.5.9 | 2026/07/22 06:14:53 | 53.52KB | 6 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.9/GamesAI-v0.5.9.mcdr) |
| [GamesAI-v0.5.8.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.8) | 0.5.8 | 2026/07/21 03:22:17 | 51.09KB | 32 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.8/GamesAI-v0.5.8.mcdr) |
| [GamesAI-v0.5.7.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.7) | 0.5.7 | 2026/07/19 03:45:10 | 50.45KB | 36 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.7/GamesAI-v0.5.7.mcdr) |
| [GamesAI-v0.5.6.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.6) | 0.5.6 | 2026/07/14 11:32:49 | 54.39KB | 34 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.6/GamesAI-v0.5.6.mcdr) |
| [GamesAI-v0.5.5.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.5) | 0.5.5 | 2026/07/08 11:08:15 | 51.89KB | 44 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.5/GamesAI-v0.5.5.mcdr) |
| [GamesAI-v0.5.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.4) | 0.5.4 | 2026/06/05 16:23:44 | 43.34KB | 73 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.4/GamesAI-v0.5.4.mcdr) |
| [GamesAI-v0.5.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.3) | 0.5.3 | 2026/05/24 08:27:26 | 41.59KB | 61 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.3/GamesAI-v0.5.3.mcdr) |
| [GamesAI-v0.5.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.2) | 0.5.2 | 2026/05/24 03:31:00 | 39.75KB | 58 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.2/GamesAI-v0.5.2.mcdr) |
| [GamesAI-v0.5.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.1) | 0.5.1 | 2026/05/16 14:33:47 | 37.42KB | 66 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.1/GamesAI-v0.5.1.mcdr) |
| [GamesAI-v0.5.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.0) | 0.5.0 | 2026/05/10 06:56:40 | 35.83KB | 66 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.0/GamesAI-v0.5.0.mcdr) |
| [GamesAI-v0.4.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.2) | 0.4.2 | 2026/05/02 14:47:09 | 23.1KB | 79 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.2/GamesAI-v0.4.2.mcdr) |
| [GamesAI-v0.4.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.1) | 0.4.1 | 2026/05/01 12:03:32 | 20.61KB | 80 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.1/GamesAI-v0.4.1.mcdr) |
| [GamesAI-v0.4.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.0) | 0.4.0 | 2026/04/26 05:25:45 | 20.0KB | 82 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.0/GamesAI-v0.4.0.mcdr) |
| [GamesAI-v0.3.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.2) | 0.3.2 | 2026/04/18 01:20:54 | 17.06KB | 95 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.2/GamesAI-v0.3.2.mcdr) |
| [GamesAI-v0.3.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.1) | 0.3.1 | 2026/04/12 06:15:12 | 14.82KB | 79 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.1/GamesAI-v0.3.1.mcdr) |
| [GamesAI-v0.3.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.0) | 0.3.0 | 2026/04/11 14:21:17 | 11.37KB | 77 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.0/GamesAI-v0.3.0.mcdr) |
| [GamesAI-v0.2.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.1) | 0.2.1 | 2026/04/04 04:27:04 | 8.45KB | 86 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.1/GamesAI-v0.2.1.mcdr) |
| [Game.sAI-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.0) | 0.2.0 | 2026/03/29 03:10:14 | 3.49KB | 94 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.0/Game.sAI-v0.2.0.mcdr) |

