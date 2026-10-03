[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## server_log_filter

### 基本信息

- 插件 ID: `server_log_filter`
- 插件名: Server Log Filter
- 版本: 1.0.2
  - 元数据版本: 1.0.2
  - 发布版本: 1.0.2
- 总下载量: 14
- 作者: [Pau1am](https://github.com/Pau1am)
- 仓库: https://github.com/Pau1am/MCDR-ServerLogFilter
- 仓库插件页: https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 用可配置的正则规则，把服务端的刷屏日志从 MCDR 控制台隐去，同时不影响服务端自身的日志文件。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# MCDR-ServerLogFilter

**语言 / Language:** **简体中文** | [English](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/README_en.md)

一个 MCDReforged 插件：**把服务端的刷屏日志从 MCDR 控制台隐去，同时完整保留服务端自己的日志文件。**

[![MCDR](https://img.shields.io/badge/MCDReforged-%3E%3D2.15-blue)](https://mcdreforged.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/LICENSE)
[![Python](https://img.shields.io/badge/python-%3E%3D3.9-blue)](https://www.python.org/)

---

## 为什么需要它

MCDR 会把服务端打印的每一行原样回显到控制台。绝大多数情况下这正是我们想要的，但有些服务端版本会反复打印不含任何有效信息的日志行，例如 Minecraft 26.3 的：

```
[Server thread/INFO]: Player Steve standing on air - force-sending blocks below
```

这是 26.3 新增的「幽灵方块自动修复」机制打的 INFO 日志，属于官方**误报**（Mojira [MC-311474](https://bugs.mojang.com/browse/MC-311474) / [MC-311727](https://bugs.mojang.com/browse/MC-311727)）——玩家正常跳跃和移动时也会触发，每人每 10 秒最多一条，会持续刷屏。

直接改服务端的 `log4j2.xml` 也能过滤，但那是**全局性**改动：改错了可能让服务端丢失重要日志，而且只对服务端生效。本插件换了个思路——**只在 MCDR 这一侧动手**。

## 两个关键设计

### 1. 只隐去回显，不丢弃信息

插件使用 MCDR 的 `InfoActionFlag.hidden()`，**不是** `discarded()`：

|                 | 控制台回显 | 派发给插件事件 | MCDR 状态检测 |
| --------------- | ----- | ------- | --------- |
| `hidden()`（本插件） | ❌ 不显示 | ✅ 照常    | ✅ 正常      |
| `discarded()`   | ❌ 不显示 | ❌ 收不到   | ⚠️ 可能失效   |

保留 `process` 意味着这些行**依然会正常派发给 MCDR 的信息响应器和插件事件**。因此**即使你的规则写得过于宽泛，也不会破坏 MCDR 自身的「服务端启动完成 / 停止 / 玩家进出」检测**——最多只是控制台上看不到而已。这是本插件最重要的安全属性。

### 2. 服务端日志完全不受影响

服务端自己的 `server/logs/latest.log` 由服务端进程用 log4j 独立写入，与本插件无关，**原始记录一条不少**。所以：

- 想查完整的原始日志 → 翻 `server/logs/latest.log`
- 想让 MCDR 控制台 / 网页面板干净 → 用本插件

## 安装

1. 从 [Releases](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/../../releases) 下载 `ServerLogFilter-vX.Y.Z.mcdr`，或自行打包（见下）
2. 放进对应 MCDR 实例的 `plugins/` 目录：

```
<MCDR目录>/plugins/ServerLogFilter-vX.Y.Z.mcdr
```

有多个子服就每个子服各放一份，配置互相独立。

3. 生效：

- MCDR 运行中：`!!MCDR reload plugin server_log_filter`
- 未运行：直接开服

## 配置

首次加载会自动生成 `config/server_log_filter/config.json`：

```json
{
    "patterns": [
        "standing on air - force-sending blocks below"
    ],
    "log_matched_lines": false,
    "report_on_server_stop": true
}
```

| 字段                      | 类型         | 说明                                                        |
| ----------------------- | ---------- | --------------------------------------------------------- |
| `patterns`              | `string[]` | 正则规则列表。对每行日志的**正文**（MCDR 已剥掉 `[时间] [线程/级别]:` 前缀）做匹配，命中即隐去 |
| `log_matched_lines`     | `bool`     | 调试用。设为 `true` 会把被隐去的行以 INFO 级别写进 MCDR 日志，方便确认规则生效         |
| `report_on_server_stop` | `bool`     | 服务端停止时，在 MCDR 日志里汇总本次共隐去多少行                               |

> **匹配方式是 `re.search`（包含匹配），不是全匹配。**
> 写 `standing on air` 就能命中整行，不需要加 `.*`。
> 反过来要注意：**正则里的 `.` 匹配任意字符**，想匹配字面点号请写 `\.`。

配置文件是 JSON，**不支持注释**。

## 命令

| 命令                      | 权限    | 说明                   |
| ----------------------- | ----- | -------------------- |
| `!!logfilter`           | user  | 查看状态：规则数与各规则命中次数     |
| `!!logfilter list`      | user  | 同上                   |
| `!!logfilter test <文本>` | user  | 测试某行是否会被隐去，并指出命中哪条规则 |
| `!!logfilter reload`    | admin | 重读配置文件并立即生效，无需重启     |

`!!logfilter test` 特别实用：把日志原文粘进去就能确认规则对不对，不用真等它触发。

## 用例：加更多规则

把要过滤的日志正文加进 `patterns` 数组即可：

```json
{
    "patterns": [
        "standing on air - force-sending blocks below",
        "Ignoring chat session from .* due to missing Services public key",
        "^\\[Async Chat Thread"
    ],
    "log_matched_lines": false,
    "report_on_server_stop": true
}
```

改完先 `!!logfilter test <文本>` 验证，再 `!!logfilter reload`。

规则写错不会导致插件崩溃——编译失败的规则会被跳过并在 MCDR 日志里给出警告，其余规则照常工作。

## 已验证内容

### 单元测试（过滤逻辑、边界与安全属性）

- 目标刷屏行被隐去，且保留 `process`（关键安全属性）
- **15 类绝不能误伤的行逐一验证不受影响**：启动完成 `Done (...)!`、玩家进出、`Stopping the server` /
  `Stopping server`、`moved too quickly`、`moved wrongly`、`Rejecting UseItemOnPacket`、
  `dropping items too fast`、聊天签名问题、`lost connection`、版本启动行、`Preparing level`、
  死亡消息、`Saving and pausing game...`
- `content` 为 `""` / `None` / 纯空白时不崩溃
- 换玩家名同样命中
- 多规则各自独立计数；`reload` 后计数归零
- 非法正则被跳过且产生警告，不影响其他规则
- 近乎相同但不同的行**不**命中（证明不是无脑全过滤）

### 端到端（真实 MCDR + 假服务端，跑完整生命周期）

控制台回显实测（默认规则）：

| 日志行                                                          | 结果           |
| ------------------------------------------------------------ | ------------ |
| `Player <任意玩家> standing on air - force-sending blocks below` | ✅ 隐去（出现 0 次） |
| `Steve moved too quickly!` / `moved wrongly!`                | ✅ 保留         |
| `Steve joined the game`                                      | ✅ 保留         |
| 任意普通日志行                                                      | ✅ 保留         |
| `Stopping server`                                            | ✅ 保留         |

插件日志：

```
插件 server_log_filter@1.0.2 已加载
已启用 1 条日志过滤规则；命中后仅从 MCDR 控制台隐去，服务端日志不受影响
本次运行共从 MCDR 控制台隐去 3 行服务端日志（服务端日志文件不受影响）
```

全程**无任何报错**。

另外还有一条**带 canary 的端到端用例**，专门守「隐去但保留事件分发」这个安全属性：
它额外让过滤规则命中**服务端启动行**，然后同时断言「该行确实离开了控制台」和
「MCDR 的 `SERVER_STARTUP` 事件仍然被派发」。这样 `hidden()` 与 `discarded()`
这两种实现才会产生可观测的差异——否则默认规则只匹配刷屏行，而刷屏行不参与生命周期判定，
两种实现看起来一模一样。详见 [tests/README.md](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/tests/README.md)。

### 运行测试

上面的行为都有对应的自动化测试（`tests/`，共 66 个用例），可以在真实 MCDR 上复跑——**包括本节
「端到端」这一组**，它会启动一个真正的 MCDR 实例、加载 `pack.py` 产出的 `.mcdr`、并用假服务端
跑完整个生命周期：

```bash
python -m pip install --target .testlibs -r tests/requirements-test.txt
PYTHONPATH=.testlibs python -m pytest tests -v      # Windows: $env:PYTHONPATH=".testlibs"
```

测试断言了本插件最关键的安全属性——被隐去的行**保留 `process`、仅摘掉 `echo_to_console`**，
并且**真的没有出现在控制台上**，同时**事件仍然照常派发**。
如果未来 MCDR 改变 `hidden()` 的语义，测试会直接失败，而不是让插件在服务器上静默出问题。
端到端组约需 5～6 秒（共用一次 MCDR 启动），可用 `MCDR_SKIP_E2E=1` 跳过。
细则见 [tests/README.md](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/tests/README.md)。

## 自行打包

本插件是 MCDR 标准的「根元数据 + 同名代码子包」：

```
MCDR-ServerLogFilter/
├── mcdreforged.plugin.json
├── LICENSE
├── README.md
├── README_en.md
├── CHANGELOG.md
└── server_log_filter/
    └── __init__.py
```

打包时**只准放行上面这些文件**，用「白名单」而不是「黑名单」。仓库里已经附带了这个打包脚本：

```bash
python pack.py            # 生成 ServerLogFilter-v<版本号>.mcdr
```

> **为什么必须用白名单？** 早期版本的这一节用的是 `rglob("*")` 加一个很短的 `skip` 列表，
> 那是**黑名单**思路，会被仓库里任何新文件悄悄带进发布包。两个具体后果：
> 
> 1. **发布包直接加载失败。** MCDR 会校验 `.mcdr` 根级条目（`PackedPlugin._check_dir_legality`），
>    根目录出现 `conftest.py`、`setup.py` 这类模块就抛
>    `IllegalPluginStructure: Packed plugin cannot contain other module`。测试用的
>    `conftest.py` 恰好就在根目录，所以黑名单方案会让插件**完全无法加载**。
> 2. **体积失控。** 按 `tests/README.md` 装了 `.testlibs/` 之后，黑名单会把整个 MCDR
>    及其依赖一起打进包里：实测 **1362 个文件、7.11 MB**（白名单为 6 个文件、约 17 KiB）。
> 
> `tests/test_plugin.py` 里的 `test_packaged_artifact_is_loadable` 会跑一遍 `pack.py`，
> 并用 MCDR 自己的校验逻辑检查产物，所以这类回归不会再溜过去。
> 
> `pack.py` 本身不进包，原因和 `conftest.py` 相同——根级模块会让 MCDR 拒绝加载。

## 环境要求

- MCDReforged **>= 2.15.0**

  > 为什么不是 2.13？本插件的核心设计依赖 `InfoActionFlag.hidden()`（只摘控制台回显、保留事件分发），
  > 而这个类是 **MCDR 2.15.0** 才引入的。2.14.x 及更早的 `InfoFilter` 只有「返回 `False` 即丢弃整条」
  > 的语义，无法等价实现本插件的行为，所以不支持。
  > 装到旧版本上不会静默出错——MCDR 会直接提示 `依赖项 mcdreforged@x.y.z 不满足版本约束 >=2.15.0`。

- Python >= 3.9（随 MCDR 自带）

## 兼容性

| 维度        | 支持情况                                                                                                 |
| --------- | ---------------------------------------------------------------------------------------------------- |
| MCDR      | **>= 2.15.0**（2.15.0 / 2.15.7 / 2.16.0 已实测）                                                          |
| Minecraft | **与 MC 版本无关**。1.16.5 / 1.19.4 / 1.20.1 / 1.20.6 / 1.21.8 / 1.21.11 / 26.1 / 26.2 / 26.3 均已用真实服务端实测通过 |

过滤发生在 MCDR 侧（对服务端 stdout 逐行匹配），因此不随 MC 版本变化。
需要注意的只是**默认规则的目标日志**：`standing on air - force-sending blocks below`
仅由 **MC 26.3** 产生，装到更早版本上插件照常工作、只是默认规则不会命中任何内容——
此时可以按自己的需要配置 `patterns` 过滤别的刷屏日志。

## 许可证

[MIT](https://github.com/Pau1am/MCDR-ServerLogFilter/tree/main/LICENSE)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ServerLogFilter-v1.0.2.mcdr](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/tag/v1.0.2) | 1.0.2 | 2026/10/02 08:42:25 | 6.99KB | 3 | [下载](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/download/v1.0.2/ServerLogFilter-v1.0.2.mcdr) |
| [ServerLogFilter-v1.0.1.mcdr](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/tag/v1.0.1) | 1.0.1 | 2026/10/01 12:54:16 | 4.73KB | 5 | [下载](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/download/v1.0.1/ServerLogFilter-v1.0.1.mcdr) |
| [ServerLogFilter-v1.0.0.mcdr](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/tag/v1.0.0) | 1.0.0 | 2026/10/01 12:39:20 | 4.76KB | 6 | [下载](https://github.com/Pau1am/MCDR-ServerLogFilter/releases/download/v1.0.0/ServerLogFilter-v1.0.0.mcdr) |

