[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## scheduled_restart

### 基本信息

- 插件 ID: `scheduled_restart`
- 插件名: Scheduled Restart
- 版本: 1.2.1
  - 元数据版本: 1.2.1
  - 发布版本: 1.2.1
- 总下载量: 11
- 作者: [fangzi2006](https://github.com/fangzi2006)
- 仓库: https://github.com/fangzi2006/MCDR-Scheduled-Restart
- 仓库插件页: https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 按 Linux cron 表达式定时重启服务器，支持多条自定义提醒（聊天框 / 大标题）

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# scheduled_restart · MCDReforged 定时重启插件

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

![MCDReforged](https://img.shields.io/badge/MCDReforged-%3E%3D2.12.0-green.svg)

## English version: [README_EN.md](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../README_EN.md) ##

按 **Linux cron 表达式** 定时重启 Minecraft 服务器，并在重启前按你设定的多个时间点，  
向全服玩家发送 **聊天框消息** 或 **大标题（title/subtitle）** 提醒。

- 主需求：定时自动重启（默认调用 MCDR 的 `restart`，也可以只停服 / 停服并退出 / 执行自定义指令）
- 按月 / 周 / 日 / 时 / 分任意组合：`0 4 * * *`、`30 3 * * 1`、`0 5 1 * *`、`@daily`……
- 提醒条数不限，**用「数组里放对象」的写法**，每条提醒自由设置提前时间与通知方式
- 通知方式：`chat` 聊天框（tellraw）、`title` 大标题、`actionbar` 物品栏上方、`command` 执行任意指令
- 支持 `§` 旧版颜色代码与 `color` 字段，可选音效，支持占位符
- 玩家进服时私聊告知倒计时；重启历史落盘；配置热重载；单条坏配置只跳过它自己
- 纯 Python 实现，**不依赖任何第三方库**，自带 cron 解析器（不装 `croniter`）
- 计划可直接用指令管理：`list` / `add` / `remove` / `enable` / `disable` / `test`

---

## 下载与安装

**方式一：用 MCDR 命令安装（推荐）**

在 MCDR 控制台或游戏里执行（需要 admin 权限）：

```
!!MCDR plugin install scheduled_restart
```

装完后执行 `!!MCDR plugin reload scheduled_restart` 或重启 MCDR 即可生效。

**方式二：下载插件包**

到 [Releases](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../../../releases/latest) 页面下载 `scheduled_restart-v<版本>.mcdr`，放进 MCDR 的  
`plugins/` 目录，重启 MCDR 或执行 `!!MCDR plugin load <文件名>`。

**方式三：目录插件**

把 `src/` 里的内容整体放到 `plugins/scheduled_restart/` 下，最终形如：

```
plugins/scheduled_restart/mcdreforged.plugin.json
plugins/scheduled_restart/scheduled_restart/__init__.py
```

首次加载后会自动生成配置：`config/scheduled_restart/config.json`（内容见 [examples/config.json](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../examples/config.json)）。

> 默认配置里就 1 个示例计划、而且它是 `"enabled": false` 的，**开箱不会自己重启**；改完用 `!!srestart reload` 生效，  
> 或者直接用 `!!srestart add <名字> <cron>` 新建一个计划。

---

## 快速开始

1. 编辑 `config/scheduled_restart/config.json`，把示例计划的 `enabled` 改成 `true`，或照抄一份改 `cron`：
   ```json
   {
     "name": "每天凌晨4点重启",
     "enabled": true,
     "cron": "0 4 * * *",
     "restart_method": "mcdr_restart",
     "use_default_notifications": true
   }
   ```
2. 在游戏里或控制台执行 `!!srestart reload`（需要 admin 权限）。
3. 执行 `!!srestart list` 确认「下次重启时间」，执行 `!!srestart test <序号>`  
   可以立刻预览这套提醒在游戏里长什么样（不会真的重启）。

---

## 配置文件详解

### 顶层字段

| 字段                          | 类型     | 默认值    | 说明                                                                  |                                                 |
| --------------------------- | ------ | ------ | ------------------------------------------------------------------- | ----------------------------------------------- |
| `enabled`                   | bool   | `true` | 插件总开关，`false` 时完全不调度                                                |                                                 |
| `timezone`                  | string | null   | `null`                                                              | 时区，如 `"Asia/Shanghai"`；`null` 表示跟随 MCDR 进程的本地时区 |
| `check_interval_seconds`    | number | `1.0`  | 调度线程轮询间隔（秒），一般不用改                                                   |                                                 |
| `skip_missed_notifications` | bool   | `true` | 计划生成时已经过期的提醒是否跳过（避免重载后补发一堆过期提醒）                                     |                                                 |
| `notify_on_join`            | bool   | `true` | 玩家进服时是否私聊告知重启倒计时                                                    |                                                 |
| `join_message`              | string | 见示例    | 进服私聊内容，支持占位符                                                        |                                                 |
| `log_history`               | bool   | `true` | 是否把每次重启写入 `config/scheduled_restart/history.jsonl`                  |                                                 |
| `history_size`              | int    | `100`  | 历史文件过大时保留的最近条数                                                      |                                                 |
| `command_alias`             | string | `""`   | 自定义简化指令前缀，如 `"!!sr"`；留空则只保留 `!!srestart`                            |                                                 |
| `default_notifications`     | array  | 1 条示例  | **默认提醒组**，计划里 `use_default_notifications: true` 时使用                 |                                                 |
| `schedules`                 | array  | 3 个示例  | 重启计划列表                                                              |                                                 |
| `_readme`                   | array  | —      | 写在配置文件里的说明，仅供阅读，可随意修改（JSON 不支持注释，所以说明放在这个字段里；配置文件里的示例都已写成不需要转义的纯文本） |                                                 |

### `schedules[]`（计划）

| 字段                          | 类型     | 默认值            | 说明                                                               |
| --------------------------- | ------ | -------------- | ---------------------------------------------------------------- |
| `name`                      | string | `计划N`          | 计划名，指令里也可以用序号代替；重名会自动加 `#2`                                      |
| `enabled`                   | bool   | `true`         | 该计划是否启用                                                          |
| `cron`                      | string | 必填             | cron 表达式，见下节                                                     |
| `restart_method`            | string | `mcdr_restart` | `mcdr_restart` / `stop` / `stop_exit` / `custom` / `none`        |
| `custom_command`            | string | `stop`         | `restart_method=custom` 时下发的服务端指令                                |
| `custom_auto_start`         | bool   | `false`        | `custom` 模式下，等服务器停止后是否自动 `start()`                               |
| `restart_delay_seconds`     | number | `0`            | 到点后再延迟多少秒真正重启（支持 `"30s"`、`"1m"` 写法）；**提醒以真正重启的时刻为基准**            |
| `kick_players`              | bool   | `false`        | 重启前是否先 `kick @a` 踢人（1.20.3+ 才支持 `@a` 选择器）                        |
| `kick_message`              | string | 见示例            | 踢人提示语                                                            |
| `use_default_notifications` | bool   | `true`         | `true` 用顶层 `default_notifications`；`false` 用本计划的 `notifications` |
| `notifications`             | array  | `[]`           | 本计划专属提醒；写了这个数组但没写 `use_default_notifications` 时，自动视为 `false`     |

`restart_method` 说明：

- `mcdr_restart`：调用 MCDR 的 `server.restart()`（软停服 → 等待 → 重新启动），MCDR 进程保持运行
- `stop`：只下发停服指令，MCDR 继续运行（适合自己有用进程守护/编排重启的场景）
- `stop_exit`：停服后让 MCDR 一起退出（适合交给 systemd 等守护进程拉起）
- `custom`：执行 `custom_command`，可选 `custom_auto_start`
- `none`：只发提醒不重启（可用于「提前预告维护」）

### `notifications[]`（提醒）

| 字段                             | 类型     | 默认值                                   | 说明                                                                                                                                                     |                                                         |
| ------------------------------ | ------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| `enabled`                      | bool   | `true`                                | 是否启用这条提醒                                                                                                                                               |                                                         |
| `advance_time`                 | number | string                                | `60`                                                                                                                                                   | 提前多久发送；支持数字秒数，也支持 `"5m"`、`"1h30m"`、`"1天2小时"` 这类时长文本     |
| `type`                         | string | `chat`                                | `chat`（聊天框）/ `title`（大标题）/ `actionbar` / `command`                                                                                                     |                                                         |
| `message`                      | string | `""`                                  | `chat` / `actionbar` 的文本                                                                                                                               |                                                         |
| `title`                        | string | `""`                                  | `title` 的主标题                                                                                                                                           |                                                         |
| `subtitle`                     | string | `""`                                  | `title` 的副标题                                                                                                                                           |                                                         |
| `times`                        | object | `{"fade_in":1,"stay":4,"fade_out":1}` | 大标题的淡入/停留/淡出时间，**单位秒**（内部换算成 tick）                                                                                                                     |                                                         |
| `color`                        | string | null                                  | `null`                                                                                                                                                 | 颜色名（`yellow`、`red`、`gold`…）或 `#RRGGBB`；也可以直接写在文本里用 `§e` |
| `sound`                        | string | null                                  | `null`                                                                                                                                                 | 音效 ID，如 `minecraft:block.note_block.pling`，会在提醒后播放      |
| `sound_source`                 | string | `master`                              | 音效频道；老版本（1.8~1.12）服务端可设为 `""` 以省略该参数                                                                                                                   |                                                         |
| `sound_position`               | string | `"@s"`                                | 音效播放位置：`"@s"` = 每个玩家在自己位置听到（1.13+，用 `execute as @a at @s` 实现）；坐标文本（`"~ ~ ~"`、`"100 64 100"`）= 固定位置播放（1.8+ 都能用，`~ ~ ~` 在控制台执行时等于世界出生点）；`""` = 省略坐标与音量音调 |                                                         |
| `sound_volume` / `sound_pitch` | number | `1.0`                                 | 音量 / 音调（`sound_position` 为空时这两项会被忽略）                                                                                                                   |                                                         |
| `command`                      | string | `""`                                  | `type=command` 时下发的指令，支持占位符                                                                                                                            |                                                         |

一个「多条提醒」的完整例子：

```json
{
  "name": "每天凌晨4点重启",
  "enabled": true,
  "cron": "0 4 * * *",
  "restart_method": "mcdr_restart",
  "use_default_notifications": false,
  "notifications": [
    { "advance_time": "30m", "type": "chat",  "message": "§e[维护] §f服务器将在 §b{remaining} §f后重启（§b{time}§f）" },
    { "advance_time": "10m", "type": "title", "title": "§e重启倒计时", "subtitle": "§f剩余 §b{remaining}",
      "times": { "fade_in": 0.5, "stay": 3, "fade_out": 0.5 },
      "sound": "minecraft:block.note_block.pling" },
    { "advance_time": 60, "type": "actionbar", "message": "§c60 秒后重启" },
    { "advance_time": 10, "type": "title", "title": "§c马上重启！", "subtitle": "§f快找地方下线" },
    { "advance_time": 0,  "type": "chat",  "message": "§c[维护] §f服务器正在重启，请稍后重新连接" }
  ]
}
```

---

## cron 写法

沿用 Linux cron：**5 个字段** `分 时 日 月 周`；也支持 **6 个字段** `秒 分 时 日 月 周`。

| 写法                                                                                   | 含义                            |
| ------------------------------------------------------------------------------------ | ----------------------------- |
| `*` / `?`                                                                            | 任意值                           |
| `5`                                                                                  | 具体值                           |
| `1-10`                                                                               | 范围                            |
| `1,3,5`                                                                              | 列表                            |
| `*/15`                                                                               | 步长（每 15 分钟）                   |
| `1-10/2`                                                                             | 范围内步长                         |
| `5/10`                                                                               | 从 5 开始、步长 10 直到最大值（cronie 扩展） |
| `JAN`~`DEC`                                                                          | 月份英文缩写                        |
| `SUN`~`SAT`                                                                          | 星期英文缩写；`0` 与 `7` 都表示周日        |
| `@yearly` / `@monthly` / `@weekly` / `@daily`(`@midnight`) / `@hourly` / `@minutely` | 常用宏                           |

常用示例：

| cron           | 含义                                               |
| -------------- | ------------------------------------------------ |
| `0 4 * * *`    | 每天 04:00                                         |
| `30 3 * * 1`   | 每周一 03:30                                        |
| `0 5 1 * *`    | 每月 1 日 05:00                                     |
| `0 0 1 1 *`    | 每年 1 月 1 日 00:00                                 |
| `0 */6 * * *`  | 每 6 小时（0、6、12、18 点）                              |
| `0 4 * * 1,4`  | 每周一、周四 04:00                                     |
| `0 4 1 * 1`    | 每月 1 日 **或** 每周一 04:00（日与周同时限定时取「或」，与 cron 惯例一致） |
| `30 0 4 * * *` | 6 字段写法：每天 04:00:30                               |
| `@daily`       | 每天 00:00                                         |

`!!srestart list` 会把每个表达式翻译成中文（例如 `每天 04:00`、`每周一 03:30`），方便核对。

---

## 占位符

写在 `message` / `title` / `subtitle` / `command` / `join_message` 里，发送时替换：

| 占位符                   | 含义            | 示例                    |
| --------------------- | ------------- | --------------------- |
| `{remaining}`         | 中文剩余时长        | `5分`、`1小时2分3秒`        |
| `{remaining_seconds}` | 剩余秒数（整数）      | `300`                 |
| `{remaining_minutes}` | 剩余分钟数（向上取整）   | `5`                   |
| `{time}`              | 重启时刻          | `04:00:00`            |
| `{date}`              | 重启日期          | `2026-07-22`          |
| `{datetime}`          | 完整时刻          | `2026-07-22 04:00:00` |
| `{schedule}`          | 计划名           | `每天凌晨4点重启`            |
| `{cron}`              | cron 表达式      | `0 4 * * *`           |
| `{index}` / `{total}` | 这是第几条提醒 / 共几条 | `2` / `5`             |

---

## 指令与权限

根指令：`!!srestart`（`!!srestart help` 查看帮助）。所有玩家都能查看计划列表与下次重启时间；  
`status` / `history` 需要 **helper**；变更类指令需要 **admin**；控制台默认为最高权限。

如果你的配置文件设置了 `command_alias`（例如 `"!!sr"`），则 `!!sr` 与 `!!srestart` 完全等价，  
帮助信息、Tab 补全、权限检查都同时生效。

> **Minecraft 的 `/op` 不等于 MCDR 的 admin**。MCDR 有自己独立的权限系统，  
> 默认情况下 Minecraft op 玩家并不会自动获得 admin 权限。  
> 如果你希望某个玩家能使用变更类指令，请在控制台执行：  
> `!!MCDR permission set <玩家名> admin`。

计划统一用 **序号** 指代（`!!srestart list` 里显示的 `[#1]`、`[#2]`…），也兼容直接写计划名；  
序号就是配置文件 `schedules` 数组的下标 +1，即使某条计划写错被跳过也不会错位。

| 指令                                  | 权限     | 说明                                         |
| ----------------------------------- | ------ | ------------------------------------------ |
| `!!srestart list`                   | 所有玩家   | 所有计划：序号、开关状态、cron、中文描述、下次重启时间与剩余时间、提醒条数    |
| `!!srestart next`                   | 所有玩家   | 下一次重启的时间与倒计时                               |
| `!!srestart status`                 | helper | 总开关、调度线程、时区、当前计划、配置警告/错误                   |
| `!!srestart history [条数]`           | helper | 最近的重启记录（时间 / 计划 / 方式 / 自动或手动）              |
| `!!srestart test <序号|计划名>`          | admin  | 按提前量依次发送该计划的提醒，**不会重启**，用于预览               |
| `!!srestart enable [<序号|计划名>|all]`  | admin  | 启用计划并**写入配置文件**（立即生效）                      |
| `!!srestart disable [<序号|计划名>|all]` | admin  | 禁用计划并**写入配置文件**（立即生效）；不带参数表示全部             |
| `!!srestart add <计划名> <cron>`       | admin  | 新建计划：默认启用、使用顶层 `default_notifications` 提醒组 |
| `!!srestart remove <序号|计划名>`        | admin  | 删除计划                                       |
| `!!srestart reload`                 | admin  | 重新读取配置文件并重建调度                              |
| `!!srestart cancel`                 | admin  | 取消当前待执行的重启（本次不重启，下次照常）                     |

几个例子：

```
!!srestart list                                    # 看序号
!!srestart add 每日重启 0 4 * * *                   # 新建：每天 04:00，立刻生效
!!srestart add "每周一 凌晨" 30 3 * * 1              # 名字带空格用引号
!!srestart test 2                                  # 预览 2 号计划的提醒（不会重启）
!!srestart disable 2                               # 关掉 2 号计划并写进配置文件
!!srestart enable all                              # 打开全部计划
!!srestart remove 2                                # 删除 2 号计划
```

序号和计划名都支持 Tab 补全。**想立刻重启服务器请用 MCDR 自带的 `!!MCDR server restart`**  
（本插件专注于"按时重启"，不再重复提供立刻重启的指令）。

> `add` 只要求「名字 + cron」：新建出来的计划默认启用、使用顶层默认提醒组；  
> 想让某条计划用自己的提醒，编辑配置文件里的 `notifications` 并把  
> `use_default_notifications` 改成 `false` 即可。
> 
> `enable` / `disable` 是**改配置文件**的（持久），不是只对本次运行生效；  
> 它直接操作 `schedules` 数组里对应条目的 `enabled` 字段，其它内容（你自己加的字段、  
> 注释性的 `_readme` 等）原样保留。所以配置文件里本来就是关闭的计划也能被打开。

---

## 常见问题

**Q：为什么默认配置里所有计划都是关的？**  
避免装上插件后服务器在你没准备好的时候突然重启。改完 `enabled` 再 `reload` 即可。

**Q：`{remaining}` 显示的时间和实际差几秒？**  
调度精度是 `check_interval_seconds`（默认 1 秒），提醒按「到点即发」处理，正常误差在 1 秒内。

**Q：插件重载 / 服务器重启后，过去的提醒会补发吗？**  
默认不会（`skip_missed_notifications: true`）。例如 3:59 才启动插件而计划 4:00 重启，  
5 分钟和 1 分钟的提醒会被标记为「已过期」跳过，只发还来得及的那几条；设为 `false` 则会立刻补发。

**Q：`timezone` 在 Windows 上无效？**  
Windows 自带的时区数据库 Python 读不到，需要 `pip install tzdata` 才能使用 `"Asia/Shanghai"` 这类名字；  
没装时会打印一条警告并自动回退到跟随 MCDR 进程的本地时区。

**Q：`kick_players` 没生效？**  
`kick @a` 需要 Minecraft 1.20.3+；老版本请保持 `false`，让服务器关服时自然踢人，或用  
`type: "command"` 的提醒自己下发 `tellraw`/`kickall` 之类的指令。

**Q：`stop` 和 `mcdr_restart` 怎么选？**  
由 MCDR 负责重启选 `mcdr_restart`；如果用 systemd/screen/宝塔等外部守护负责拉起，选 `stop`  
（或 `stop_exit`，让 MCDR 也退出，避免卡住）。


**Q：配了 `sound` 却听不到声音 / 报坐标错误？**
Java 的 `playsound` 语法是 `playsound <音效> [<频道>] <目标> [<坐标>] [<音量>] [<音调>]`，
**坐标排在音量前面**：想自定义音量/音调就必须先给坐标，否则 `… @a 1 1` 里的 `1 1`
会被当成坐标（坐标需要 x y z 三个分量）而报错。

插件默认用 `"sound_position": "@s"`，生成的是

```
execute as @a at @s run playsound <音效> master @s ~ ~ ~ <音量> <音调>
```

也就是**每个玩家在自己位置听到**（1.13+）。如果你更希望音效锚定在某个固定位置，
把 `sound_position` 写成坐标文本；如果服务端是 **1.12 及更早**（没有 `execute as/at`），
用 `"sound_position": "~ ~ ~"` + `"sound_source": ""`：

```json
{ "advance_time": 30, "type": "title", "title": "§e重启倒计时",
  "sound": "minecraft:block.note_block.pling",
  "sound_source": "", "sound_position": "~ ~ ~" }
```

> 提醒也支持 `type: "command"`，你可以完全自己写 `playsound`/`title` 指令绕过这些约定。

**Q：配置写错了会怎样？**
* 单个字段类型写错 → 使用默认值，并记一条警告，插件照常运行（会顺手把规范化后的配置写回文件）
* 整个计划的 `cron` 写错 → 只跳过该计划，记一条错误，**不写回文件**（保留你写的内容方便修正）
* 用 `!!srestart status` 或看控制台日志都能看到这些警告/错误

**Q：能同时配多条计划吗？**
可以。调度器每次只执行「最近的一次」重启，避免两个计划挨得太近互相打架；被取消的那一次不会再触发。

**Q：怎么立刻重启服务器？**
用 MCDR 自带的 `!!MCDR server restart`（admin）。本插件的 `trigger` 指令已按需求移除——
它当时只是借用计划的重启方式、提醒全部跳过，和计划本身关系很弱。想让玩家先收到提醒再重启，
就把计划的 cron 设到最近的整分/整点，或用 `!!srestart test <序号>` 先预览提醒文案。

**Q：`enable` / `disable` 是改配置文件还是只对本次运行生效？**
改配置文件（持久）：直接写 `schedules[i].enabled` 并立刻热重载生效。所以配置文件里本来就是
关闭的计划也能用 `!!srestart enable <序号>` 打开；写错了 cron 的计划用序号同样能开关，
插件会顺带提醒你「cron 有误，修正后才会真正生效」。配置文件里其它内容（你自己加的字段等）不会被动。

**Q：服务器没在运行时，提醒会怎样？**
会跳过并记一条警告（`服务器当前未运行，跳过提醒`）。因为服务器进程不在时 MCDR 无法把
`tellraw` / `title` 送进游戏，只会丢一句 `Server has been terminated, cannot send command to its stdin`；
计划本身会保留，等服务器起来后照常执行。重启动作同理——服务器没运行时会跳过而不是假装执行成功。

**Q：插件自己的日志在哪里看？**
打在 MCDR 控制台（`[scheduled_restart]` 前缀）。MCDR 的 `logs/MCDR.log` 主要记录 MCDR 自身消息，
所以插件另外把每次重启写进 `config/scheduled_restart/history.jsonl`，可用 `!!srestart history` 查看。

---

## 开发与测试

本项目在**虚拟环境**里开发和验证（MCDReforged 2.16.0 + Python 3.13）：

```bash
# 创建虚拟环境并安装 MCDR / pytest
uv venv --python 3.13 .venv
uv pip install --python .venv/Scripts/python.exe mcdreforged pytest     # Windows
# uv pip install --python .venv/bin/python mcdreforged pytest           # Linux

# 跑测试（231 个用例：cron 解析、配置容错、配置文件读改写、配置自动升级、提醒渲染、调度时序、指令树、打包结构、插件生命周期）
.venv/Scripts/python.exe -m pytest -q

# 重新生成示例配置 / 打包插件
.venv/Scripts/python.exe tools/generate_example_config.py
.venv/Scripts/python.exe tools/build_plugin.py
```

单元测试用假服务器接口（`tests/fakes.py`）驱动真实的调度逻辑与 **MCDR 自己的指令解析器**，
并用 MCDR 的元数据校验器、`zipimport` 验证 `.mcdr` 包的合法性；
调度部分的时间全部来自可注入的时钟，测试是确定性的（不依赖真实等待）。

---

## 目录结构

```
mcdr-scheduled-restart/
├── src/                            # 插件本体（打包成 .mcdr 或直接放进 plugins/）
│   ├── mcdreforged.plugin.json     # 插件元数据
│   └── scheduled_restart/
│       ├── __init__.py             # MCDR 入口（on_load / on_unload / on_player_joined）
│       ├── cron.py                 # cron 解析、下次触发时间、中文描述
│       ├── config.py               # 配置默认值、校验、容错、读取前处理（去 BOM / 坏文件备份）
│       ├── config_store.py         # 配置文件读改写（enable / disable / add / remove 指令用）
│       ├── notify.py               # 提醒渲染与发送
│       ├── scheduler.py            # 调度线程、倒计时状态机、重启执行、历史记录
│       └── command.py              # !!srestart 指令树
├── examples/config.json            # 生成出来的默认配置
├── tests/                          # 231 个单元测试
├── e2e/                            # 真实 MCDR 端到端测试（模拟服务端、测试驱动插件、实测证据）
├── tools/build_plugin.py           # 打包 .mcdr
├── tools/generate_example_config.py
├── CHANGELOG.md                    # 更新日志
└── LICENSE                         # GPL-3.0
```

---

## 打包与发布

### 先决条件

* **Python >= 3.8**（打包脚本只用标准库的 `zipfile`，不需要装 MCDR、也不需要装任何第三方库）
* 确认 `src/mcdreforged.plugin.json` 里的 `version` 是你想发布的版本号——
  它会**同时决定包内版本和输出文件名** `dist/<插件 id>-v<版本>.mcdr`

### 一条命令打包

```bash
python tools/build_plugin.py
# 已生成插件包: dist/scheduled_restart-v1.2.1.mcdr（35530 字节）
# sha256: c32e93f8f09b1f4d0ed351be4fcbb18579416d77187d60d08c44813b23855284
```

> 上面是本次构建的真实输出。注意 sha256 每次重新打包都会变（zip 里记录了文件的修改时间），
> 所以它适合用来「校验某次发布下载到的文件有没有损坏/被替换」，不适合写死在文档里当常量。
> 发布时把这条 sha256 一起贴到 Release 说明里，使用者就能核对下载的附件。

脚本按**自身所在位置**定位工程，所以在任意工作目录下都能执行。
可用参数：

```bash
python tools/build_plugin.py -o build/my_plugin.mcdr      # 指定输出路径
python tools/build_plugin.py -s other/src -o build/x.mcdr # 指定源码目录 + 输出
```

打包逻辑（也是 `tests/test_package.py` 里在验证的规则）：

| 行为   | 说明                                                             |
| ---- | -------------------------------------------------------------- |
| 打包起点 | `src/` **里面**的内容（不是把 `src` 这个目录本身打进去）                          |
| 必含文件 | `mcdreforged.plugin.json`（必须在包根）、`scheduled_restart/` 整个包      |
| 自动跳过 | `__pycache__/`、`.mypy_cache/`、`.pytest_cache/`、`*.pyc`、`*.pyo` |
| 压缩方式 | `ZIP_DEFLATED`，已存在的同名输出会先删除再重建                                 |
| 输出位置 | 默认 `dist/`（该目录已被 `.gitignore` 忽略，不进仓库）                         |

> **为什么必须从 `src/` 里面开始打包？**
> MCDR 对打包插件有一条硬性校验：包根目录只允许出现 `mcdreforged.plugin.json`
> 和**与插件 id 同名的那个包**（这里是 `scheduled_restart/`）。
> 如果打成 `src/scheduled_restart/...` 这种多了一层 `src/` 的结构，MCDR 会直接报
> `IllegalPluginStructure` 拒绝加载。

### 手工打包

`.mcdr` 就是一个普通 zip，手工打包也可以，只要结构对。**注意手工打包不会自动跳过
`__pycache__`，打包前先删掉它**，否则会把这些缓存文件一起塞进包里：

```bash
# Linux / macOS
cd src                                   # 关键：进到 src 里面
find . -name '__pycache__' -type d -exec rm -rf {} +
zip -r ../dist/scheduled_restart.mcdr . -x '*/__pycache__/*' '*.pyc'
```

```powershell
# Windows（Compress-Archive 不支持排除规则，所以先删掉缓存目录）
cd src
Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
Compress-Archive -Path * -DestinationPath ..\dist\scheduled_restart.mcdr -Force
```

打包后确认结构正确：

```bash
python -m zipfile -l dist/scheduled_restart-v1.2.1.mcdr
# 应当只看到：mcdreforged.plugin.json、scheduled_restart/__init__.py、scheduled_restart/*.py
```

也可以把扩展名改成 `.zip` 直接用解压软件查看。


把这个值与 Release 说明里公布的 sha256 比对，就能确认下载到的附件没有被改过或损坏。

### 打包后自检

1. **跑测试**：`test_package.py` 会自动用 `tools/build_plugin.py` 打一次包，校验布局合法性，
   并把 `.mcdr` 加进 `sys.path` **真正 import 一次**，确认打包后的导入路径没问题：

   ```bash
   python -m pytest tests/test_package.py -q
   ```

2. **装进 MCDR 看日志**：把 `.mcdr` 放进 `plugins/`，启动后应当看到

   ```
   [MCDR] [TaskExecutor/INFO]: Plugin scheduled_restart@1.2.1 loaded
   ```

   并在控制台看到 `[scheduled_restart] v1.2.1 已加载：…`；用 `!!MCDR plugin list` 也能看到它。

3. **不想打包**也可以直接用「目录插件」模式调试：把 `src/` 里的内容复制到
   `plugins/scheduled_restart/`，改完代码执行 `!!MCDR plugin reload scheduled_restart` 即可，
   比每次重新打包快得多。

### 发布到 GitHub Release

```bash
git tag -a v1.2.1 -m "v1.2.1"
git push origin main --follow-tags

# 附带插件包发布（装了 GitHub CLI 的话）
gh release create v1.2.1 dist/scheduled_restart-v1.2.1.mcdr \
  --title "v1.2.1" --notes-file CHANGELOG.md      # 或 --generate-notes 让 GitHub 自动生成
```

没有 `gh` 就在网页上操作：**Releases → Draft a new release** → 选 tag `v1.2.1`
→ 说明可直接复制 [CHANGELOG.md](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../CHANGELOG.md) 里对应版本的段落 → 上传 `dist\scheduled_restart-v1.2.1.mcdr` → Publish。

> 仓库里**不放**构建产物（`dist/` 已被忽略），插件包一律通过 Release 附件分发：
> 这样每次改代码不会给仓库历史塞进二进制文件，而使用者仍能在 Release 页面直接下载。

---

## 设计说明

* **单计划调度**：调度线程每 `check_interval_seconds` 醒一次，算出「所有启用计划里最近的一次重启」，
  然后只维护这一个计划；每秒检查有没有到某条提醒的发送时刻。
* **提醒时刻 = 真正重启时刻 − `advance_time`**；`restart_delay_seconds` 会同时推迟提醒基准，
  保证「还有 5 分钟」这类文案始终准确。
* **重启在独立工作线程里执行**：`server.restart()` 会阻塞到服务器重启完成，
  放在工作线程里不会卡住调度循环；重启期间暂停发送提醒。
* **防重复触发**：已经触发或已被取消的「某个计划 + 某个时刻」会被记下来，同一时刻绝不会重启两次。
* **cron 计算效率**：按天跳着找匹配日期，再在当天挑最近的时分秒，不用逐分钟暴力扫描。
* **序号对齐配置文件**：每个计划记住自己在 `schedules` 数组里的下标（`source_index`），
  `list` 显示的 `[#N]` 就是它 +1；即使某条计划 cron 写错被跳过，序号也不会错位，
  `enable/disable/remove <序号>` 永远指向你看到的那一条。
* **改配置的指令直接改文件**：`enable / disable / add / remove` 只改 `schedules` 数组里对应条目的字段，
  你自己加的字段与注释性内容原样保留；写入采用「先写临时文件再替换」；
  读取前会去掉 UTF-8 BOM，文件彻底损坏时先备份成 `config.json.broken-<时间>` 再重新生成。

---

## 许可证

Copyright (C) 2026 fangzi2006 <1439885013@qq.com>

本项目以 **GNU General Public License v3.0 or later** 发布，完整条款见 [LICENSE](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../LICENSE)。
你可以自由使用、修改、再发布，但衍生作品需要以同样的许可证开源。
更新记录见 [CHANGELOG.md](https://github.com/fangzi2006/MCDR-Scheduled-Restart/tree/main/src/../CHANGELOG.md)。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [scheduled_restart-v1.2.1.mcdr](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/tag/v1.2.1) | 1.2.1 | 2026/10/03 11:26:56 | 36.41KB | 7 | [下载](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/download/v1.2.1/scheduled_restart-v1.2.1.mcdr) |
| [scheduled_restart-v1.1.1.mcdr](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/tag/v1.1.1) | 1.1.1 | 2026/09/30 12:15:10 | 35.29KB | 4 | [下载](https://github.com/fangzi2006/MCDR-Scheduled-Restart/releases/download/v1.1.1/scheduled_restart-v1.1.1.mcdr) |

