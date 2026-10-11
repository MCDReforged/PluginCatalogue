[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## server_log_filter

### 基本信息

- 插件 ID: `server_log_filter`
- 插件名: Server Log Filter
- 版本: 1.4.1
  - 元数据版本: 1.4.1
  - 发布版本: 1.4.1
- 总下载量: 67
- 作者: [Pau1am](https://github.com/Pau1am)
- 仓库: https://github.com/LifeSci-Craft/MCDR-ServerLogFilter
- 仓库插件页: https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main
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

**语言 / Language:** **简体中文** | [English](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/README_en.md)

> 一个 MCDReforged 插件：把服务端反复刷屏的日志行**只从 MCDR 控制台隐去**；服务端自己的日志文件一条不少。

[![MCDR](https://img.shields.io/badge/MCDReforged-%3E%3D2.15-blue)](https://mcdreforged.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/LICENSE)
[![Python](https://img.shields.io/badge/python-%3E%3D3.9-blue)](https://www.python.org/)

|         |                                                         |
| ------- | ------------------------------------------------------- |
| 插件 ID   | `server_log_filter`                                     |
| 命令      | `!!logfilter` / `!!lf`                                  |
| 需要      | MCDR **2.15.0+**（实测 2.15.0 / 2.15.7 / 2.16.0；与 MC 版本无关） |
| License | MIT                                                     |

> 想改代码，或了解打包、测试与版本兼容性？见 [docs/DEVELOPMENT.md](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/docs/DEVELOPMENT.md)。

## 目录

- [功能](#功能)
- [安装](#安装)
- [命令](#命令)
- [配置](#配置)
- [注意](#注意)
- [License](#license)

## 功能

- 按正则规则过滤服务端输出，命中的行**只从 MCDR 控制台隐去**；服务端自己写的 `server/logs/latest.log` 一条不少
- 隐去的是控制台回显、不是丢弃：日志事件照常分发，不影响其它插件与 MCDR 的「开服完成 / 关服 / 玩家进出」判断
- 默认规则针对 Minecraft 26.3 的「standing on air」刷屏日志（官方误报，Mojira [MC-311474](https://bugs.mojang.com/browse/MC-311474) / [MC-311727](https://bugs.mojang.com/browse/MC-311727)）
- 规则随时可增删改；`!!logfilter test <文本>` 先验证再启用，不必等它真的触发
- 规则连续多个开服周期零命中时提醒一次；载入时拦截有灾难性回溯风险的规则（跳过并警告，其余规则不受影响）
- 配置写坏会先备份成 `config.json.old` 再重建；插件升级后新增选项自动补齐，你已有的取值不受影响
- 中英双语；命令全部需要管理员权限

## 安装

1. 从 [Releases](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/../../releases) 下载 `ServerLogFilter-vX.Y.Z.mcdr`，或自行打包（见 [docs/DEVELOPMENT.md](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/docs/DEVELOPMENT.md)）；
2. 放进 MCDR 的 `plugins/` 目录；
3. MCDR 运行中执行 `!!MCDR reload plugin server_log_filter`，未运行则直接开服；
4. 首次启动自动生成 `config/server_log_filter/config.json`，默认配置开箱可用。

多个子服各放一份，配置互相独立。

## 命令

`!!logfilter` 与 `!!lf` 完全等价。**所有命令都需要 MCDR 管理员权限**（与游戏内 OP 无关：MCDR 只认自己的 `permission.yml`，未登记的玩家默认是 `user`）。给自己权限：在 MCDR 控制台执行 `!!MCDR permission set <你的 ID> admin`。

| 命令                                  | 作用                                                    |
| ----------------------------------- | ----------------------------------------------------- |
| `!!logfilter`（= `!!logfilter help`） | 帮助页（游戏内聊天里每行可点击）                                      |
| `!!logfilter list`                  | 状态：当前语言与来源、每条规则的命中次数与连续零命中次数、被跳过的规则数                  |
| `!!logfilter test <文本>`             | 测试一行日志是否会被隐去、命中的是哪条规则；整行粘贴也行（会先剥掉 `[时间] [线程/级别]:` 前缀） |
| `!!logfilter reload`                | 重读配置立即生效，不必重启；已从配置中删除的规则的统计同时清除                       |
| `!!logfilter reset`                 | 清空「连续零命中」计数，重新开始观察                                    |

## 配置

配置文件是 `config/server_log_filter/config.json`，首次加载自动生成：

```json
{
    "language": "auto",
    "patterns": [
        "standing on air - force-sending blocks below"
    ],
    "log_matched_lines": false,
    "report_on_server_stop": true,
    "warn_about_stale_rules": true,
    "stale_rule_threshold": 3,
    "validate_patterns": true,
    "pattern_probe_timeout_ms": 25,
    "announce_config_upgrade": true,
    "announce_broken_config": true
}
```

<details><summary>展开选项与说明</summary>

| 字段                         | 类型         | 默认       | 说明                                                                                                |
| -------------------------- | ---------- | -------- | ------------------------------------------------------------------------------------------------- |
| `language`                 | `string`   | `"auto"` | 消息语言。`auto` 跟随 MCDR；也可写 `zh_cn` / `en_us`（大小写与 `-` / `_` 随意；`zh_tw` 回落到 `zh_cn`，缺失的档位回落到 `en_us`） |
| `patterns`                 | `string[]` | 见上       | 正则规则。对每行日志的**正文**（MCDR 已剥掉 `[时间] [线程/级别]:` 前缀）做匹配，命中即隐去                                           |
| `log_matched_lines`        | `bool`     | `false`  | 调试用：把被隐去的行以 INFO 级别写进 MCDR 日志，方便确认规则生效                                                            |
| `report_on_server_stop`    | `bool`     | `true`   | 关服时在 MCDR 日志里汇总本次共隐去多少行                                                                           |
| `warn_about_stale_rules`   | `bool`     | `true`   | 某条规则连续多个开服周期零命中时提醒一次（只在成功开服的周期上计数）                                                                |
| `stale_rule_threshold`     | `int`      | `3`      | 连续多少个开服周期零命中才提醒；`0` = 关闭这项提醒                                                                      |
| `validate_patterns`        | `bool`     | `true`   | 载入时用短探测串检查灾难性回溯，把这类规则拦下并跳过                                                                        |
| `pattern_probe_timeout_ms` | `int`      | `25`     | 上面那项检查的耗时上限（毫秒），一般不用改                                                                             |
| `announce_config_upgrade`  | `bool`     | `true`   | 升级后配置被自动补齐时，在控制台说明新增了哪些选项                                                                         |
| `announce_broken_config`   | `bool`     | `true`   | 配置写坏被备份并重置时，在控制台说明原因与备份路径                                                                         |

</details>

**匹配方式是 `re.search`（包含匹配），不是全匹配。** 写 `standing on air` 就能命中整行，不必加 `.*`；反过来 `.` 匹配任意字符，要匹配字面点号请写 `\.`。

**加规则**：把日志正文追加进 `patterns`（其余字段保持原值），先 `!!logfilter test <文本>` 验证，再 `!!logfilter reload`：

```json
{
    "patterns": [
        "standing on air - force-sending blocks below",
        "Ignoring chat session from .* due to missing Services public key"
    ]
}
```

几条说明：

- 规则编译失败只会跳过该条并在日志里警告，其余规则照常工作；想临时关掉过滤，把 `patterns` 清空再 `!!logfilter reload`。
- 零命中统计存在 `state.json`（与 `config.json` 分开，插件不会改你写的配置）；从配置里删掉规则，它的统计在 `reload` 时一并清除。
- 写坏配置时，原文件先被改名成 `config.json.old` 再重建默认配置（备份只有这一个位置）；文件不是 UTF-8 编码（比如被存成 ANSI）也算写坏。
- `warn_about_stale_rules` / `announce_config_upgrade` / `announce_broken_config` 三个播报开关**只管说不说**：备份、补齐、统计这些动作照旧执行。
- 想加一门语言：复制 `en_us.json` 改成 `<语言代码>.json`、只翻译取值，见 `server_log_filter/lang/README.md`（不需要改代码）。

## 注意

- 过滤在 MCDR 这一侧完成（对服务端输出逐行匹配），**与 MC 版本无关**；默认规则只对 MC 26.3 的日志有意义，装在其它版本上插件照常工作，只是默认规则不会命中。
- 规则别写得太宽（如 `.`、`.*`、`^`），否则控制台会看起来像「服务端没在运行」；加载时有警告，`!!logfilter list` 里也会标出。
- 查完整原始日志，永远看 `server/logs/latest.log`。

## License

[MIT](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/tree/main/LICENSE)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ServerLogFilter-v1.4.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.4.1) | 1.4.1 | 2026/10/07 04:27:30 | 20.8KB | 7 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.4.1/ServerLogFilter-v1.4.1.mcdr) |
| [ServerLogFilter-v1.4.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.4.0) | 1.4.0 | 2026/10/04 13:08:49 | 19.3KB | 8 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.4.0/ServerLogFilter-v1.4.0.mcdr) |
| [ServerLogFilter-v1.3.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.3.0) | 1.3.0 | 2026/10/04 09:49:57 | 26.88KB | 4 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.3.0/ServerLogFilter-v1.3.0.mcdr) |
| [ServerLogFilter-v1.2.2.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.2.2) | 1.2.2 | 2026/10/04 08:54:14 | 25.14KB | 5 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.2.2/ServerLogFilter-v1.2.2.mcdr) |
| [ServerLogFilter-v1.2.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.2.1) | 1.2.1 | 2026/10/04 07:33:51 | 17.87KB | 3 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.2.1/ServerLogFilter-v1.2.1.mcdr) |
| [ServerLogFilter-v1.2.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.2.0) | 1.2.0 | 2026/10/04 06:42:18 | 19.21KB | 5 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.2.0/ServerLogFilter-v1.2.0.mcdr) |
| [ServerLogFilter-v1.1.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.1.1) | 1.1.1 | 2026/10/04 05:29:16 | 14.78KB | 6 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.1.1/ServerLogFilter-v1.1.1.mcdr) |
| [ServerLogFilter-v1.1.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.1.0) | 1.1.0 | 2026/10/04 05:12:28 | 27.8KB | 4 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.1.0/ServerLogFilter-v1.1.0.mcdr) |
| [ServerLogFilter-v1.0.2.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.0.2) | 1.0.2 | 2026/10/02 08:42:25 | 6.99KB | 8 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.0.2/ServerLogFilter-v1.0.2.mcdr) |
| [ServerLogFilter-v1.0.1.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.0.1) | 1.0.1 | 2026/10/01 12:54:16 | 4.73KB | 8 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.0.1/ServerLogFilter-v1.0.1.mcdr) |
| [ServerLogFilter-v1.0.0.mcdr](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/tag/v1.0.0) | 1.0.0 | 2026/10/01 12:39:20 | 4.76KB | 9 | [下载](https://github.com/LifeSci-Craft/MCDR-ServerLogFilter/releases/download/v1.0.0/ServerLogFilter-v1.0.0.mcdr) |

