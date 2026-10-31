[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## bot_kikai

### 基本信息

- 插件 ID: `bot_kikai`
- 插件名: BotKikai
- 版本: 0.7.0
  - 元数据版本: 0.7.0
  - 发布版本: 0.7.0
- 总下载量: 680
- 作者: [Jerry_FaGe](https://github.com/Jerry-FaGe), [RayanceKing](https://github.com/RayanceKing)
- 仓库: https://github.com/Jerry-FaGe/MCDR-BotKikai
- 仓库插件页: https://github.com/Jerry-FaGe/MCDR-BotKikai/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 使用中文名称即可将假人精准召唤到任意位置，支持多种动作。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [python](/plugins/python/readme-zh_cn.md) | \>=3.10 |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | \>=1.6.2 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# MCDR-BotKikai（Bot機械）

一个基于 [MCDR](https://github.com/Fallen-Breath/MCDReforged) 的 Minecraft 假人管理插件，专注于简化 [Carpet](https://github.com/gnembon/fabric-carpet) 假人的管理和操作。

> 君は道具ではなく、その名が似合う人になろんだ

## 📝 简介

本插件旨在解决以下问题：

- 记不住每个机器的假人名字？
- 不习惯输入英文指令？
- 想在家里快速开关远处、其他维度的机器？

只需为每个假人设置中文别名，就能通过简单的中文名字来操控它们。比如，对于一个叫 `SandBot` 的假人，你可以给它起个别名叫"刷沙机"，这样 `!!bk SandBot spawn` 和 `!!bk 刷沙机 spawn` 的效果是完全一样的！也就是说你不需要记住哪个假人控制哪个机器，只需要确认你想开关哪个机器。

你可以在世界的任意位置输入指令 `!!bk 刷沙机 use` 即可让假人 `SandBot` 自动在刷沙机处上线，并右键开关来开启刷沙机（顺便挂机）。

> 上古版本的[介绍视频](https://www.bilibili.com/video/BV1Rf4y1C776) By: [Nachuan川川](https://space.bilibili.com/107251863)

## 🚀 特性

- 支持假人别名系统（中文、拼音等都可以）
- 独立添加、移除别名，不改变登记位置或打断假人动作
- 方便的假人位置和朝向记录
- 交互式的操作界面
- 紧凑假人列表，支持分页、按在线状态筛选和名称搜索
- 支持假人前后缀
- 自动确认并保存服务端返回的假人名字大小写，离线和重启后保留
- 支持权限管理
- 配置文件热重载
- 配置校验、原子保存和加载失败保护
- 在线状态同步及后台任务取消

## ⚙️ 依赖

- Python >= 3.10
- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) >= 2.12.0
- [MinecraftDataAPI](https://github.com/Fallen-Breath/MinecraftDataAPI) >= 1.6.2
- Minecraft 服务端需要安装 [Carpet](https://github.com/gnembon/fabric-carpet) 模组

推荐使用 MCDR 2.16.2 和 MinecraftDataAPI 1.6.2；旧环境升级时请先更新上述依赖。插件不要求开启 RCON。

## 📖 命令说明

基础命令（可于配置文件中自定义）：

```minecraft
!!bk
```

所有可用命令：

| 命令                                              | 说明                    | 权限等级  |
| ----------------------------------------------- | --------------------- | ----- |
| !!bk                                            | 显示帮助信息                | 所有人   |
| !!bk list [online|offline] [page]               | 分页查看假人列表，可筛选在线或离线     | 所有人   |
| !!bk list [online|offline] search <关键词\> [page] | 搜索登记名、假人名或别名，可叠加状态筛选  | 所有人   |
| !!bk reload                                     | 重载插件配置                | admin |
| !!bk add <name\> <kikai\>                       | 使用当前玩家位置添加假人          | admin |
| !!bk add <name\> <kikai\> [dim] [pos] [facing]  | 使用自定义参数添加假人           | admin |
| !!bk del <kikai\>                               | 删除指定假人的记录，不会让已在线假人下线  | admin |
| !!bk <kikai\> alias                             | 打开别名管理面板，选择要移除的别名     | admin |
| !!bk <kikai\> alias add <alias\>                | 添加别名，不改变登记位置和朝向       | admin |
| !!bk <kikai\> alias del <alias\>                | 移除别名，不删除记录或下线假人       | admin |
| !!bk <kikai\>                                   | 显示假人详细信息，按权限提供操作和管理入口 | 所有人   |

假人操作命令：

| 命令                               | 说明                    | 权限等级 |
| -------------------------------- | --------------------- | ---- |
| !!bk <kikai\> spawn              | 在对应位置生成假人             | user |
| !!bk <kikai\> kill               | 移除假人                  | user |
| !!bk <kikai\> where              | 显示记录的假人位置，并请求让假人发光2分钟 | user |
| !!bk <kikai\> use                | 假人右键一次                | user |
| !!bk <kikai\> huse [<interval\>] | 假人持续右键，可选间隔时间（gt）     | user |
| !!bk <kikai\> atk                | 假人左键一次                | user |
| !!bk <kikai\> hatk [<interval\>] | 假人持续左键，可选间隔时间（gt）     | user |
| !!bk <kikai\> stop               | 停止假人的所有动作             | user |

## ⚡ 快速上手

1. 为刷沙机添加一个假人并设置位置：

    ```minecraft
    !!bk add SandBot 刷沙机
    ```

   玩家站在期望的位置和朝向执行此命令，假人的位置和朝向会被自动记录。

   假人基础名称只能包含英文字母、数字和下划线；加上前后缀后的游戏名长度须为 3–16。名称和别名不区分大小写，不能与其他假人的名称、游戏名或别名重复。别名不能包含空白，也不能使用管理命令 `add`、`del`、`list`、`reload`。

   你也可以手动指定位置（不建议，挺麻烦的）：

    ```minecraft
    !!bk add SandBot 刷沙机 minecraft:overworld 0 64 0 -154.43 3.90
    ```

2. 使用假人：

    ```minecraft
    !!bk 刷沙机           # 显示假人信息和操作界面
    !!bk 刷沙机 spawn     # 召唤假人到记录的位置
    !!bk 刷沙机 use       # 让假人右键一次
    !!bk 刷沙机 hatk 12   # 让假人每 12gt 左键一次
    !!bk 刷沙机 stop      # 让假人停止动作
    !!bk 刷沙机 kill      # 让假人下线
    ```

### 列表面板

```minecraft
!!bk list                         # 全部假人，第 1 页
!!bk list 2                       # 全部假人，第 2 页
!!bk list online                  # 仅在线假人
!!bk list offline 2               # 仅离线假人，第 2 页
!!bk list search 沙               # 搜索名称或别名包含「沙」的假人
!!bk list online search farm 2    # 在线假人中搜索 farm，查看第 2 页
```

- 每页 10 条，一行一个假人；使用现有顺序中的第一个自定义别名，没有时使用登记名。列表按登记名不区分大小写的字典序排列，不会因上下线或更改别名而重新排序，也不修改存储顺序。
- 在线行提供「下线 / 右键 / 详情」，离线行提供「上线 / 右键 / 详情」。离线时「右键」沿用自动召唤逻辑，确认上线后才执行右键，召唤超时则不执行；悬浮提示会说明这一行为。其余动作和管理入口放在详情面板。没有 `permission.bot` 权限时只保留详情和列表导航，旧按钮执行时仍重新校验权限。
- 悬浮名称查看完整显示名、登记名、假人名、全部自定义别名及登记位置、朝向；列表显示名超过 7 个字符时显示前 7 个字符加「…」，不超过 7 个字符时完整显示，详情与搜索关键词的显示规则不变。按钮始终使用完整登记名，不受省略或别名变更影响。列表沿用详情的颜色语义，并同时显示「在线 / 离线」文字。
- 名称栏按当前页最长的实际显示名自适应宽度，用原版默认字体的显示占宽补普通空格，使后方按钮尽量对齐；7 个字符只是截断上限，不固定预留七字空间。先筛选、分页并截断显示名，再计算列宽，其他页或被筛除的长名称不会撑宽当前页；翻页、筛选或搜索后列宽可以随内容调整。普通空格有宽度步长，可能保留少量像素偏差；其他 Unicode 字符使用近似占宽，资源包字体或强制统一字体下不保证对齐。
- 搜索使用不区分大小写的子串匹配，覆盖登记名、含前后缀的假人名及所有别名；关键词为不含空白的单个词，数字或 `online` 等命令词也可以作为关键词。搜索只展示候选，不会对模糊匹配结果执行动作。
- 上一页、下一页和刷新保留当前状态、关键词及页码；切换状态保留关键词并回到第一页，清除搜索保留状态并回到第一页。「搜索」按钮填入当前状态下的新搜索命令，供填写关键词。
- 页码必须是正整数。请求页码超过末页时显示末页并提示；无结果时保留筛选、搜索及刷新入口。当前筛选和不可用的翻页按钮不可点击，空列表显示第 1/1 页、共 0 个，并提供帮助入口。
- 列表及刷新只读取插件内存状态，不主动查询 Minecraft、不写文件、不召唤假人。所有按钮仍为命令建议，点击后需要按回车执行；真实客户端的字体、聊天宽度和缩放可能导致自然换行。

### 详情与管理面板

- `!!bk <kikai>` 的标题使用现有顺序中的第一个自定义别名，没有自定义别名时使用登记名；不会重排或修改别名。本次暂不提供设置主别名的命令。
- 显示「假人名」「别名」「登记位置」「登记朝向」，不再重复展示基础名、游戏名。悬浮在假人名上可查看登记名；只有未确认的名字显示黄色「待确认」。
- 原版维度显示「主世界 / 下界 / 末地」，自定义维度保留完整 ID。坐标和朝向最多显示两位小数，悬浮可查看原始精度；存储和执行不舍入。点击登记位置仍填入由原始坐标向下取整得到的坐标点。
- 金色突出标题，白色展示数据，灰色标注说明，绿色表示在线或添加，红色表示离线、下线或删除，青色表示普通操作，黄色提示注意事项。面板及悬浮说明使用显式富文本颜色，避免相邻内容串色。
- 操作按钮遵循 `permission.bot`；添加、移除别名和删除记录只在满足 `permission.list` 时显示。没有操作权限仍可查看信息、刷新和返回列表；后端权限校验不变，不能靠旧面板绕过。
- 「移除别名」打开 `!!bk <kikai> alias`，每个自定义别名都有独立的移除按钮；登记名、假人名不可移除。没有自定义别名时，详情中的移除按钮置灰且不可点击。管理面板本身只读，不写文件，也不查询或召唤假人。
- 所有按钮仍为命令建议，点击后需要按回车执行。「报点/发光」和交互按钮的悬浮提示明确说明离线时会先自动召唤；「删除记录」明确说明不会让在线假人下线。位置始终是登记值，不是实时追踪结果。

### 命令反馈

```text
[BK] 刷沙机 · 已确认上线
[BK] 刷沙机 · 右键请求已发送
[BK] 刷沙机 · 每 10 gt 右键请求已发送
[BK] 刷沙机 · 下线请求已发送
[BK] 刷沙机 · 已添加别名「沙场」
```

- 操作、记录管理、别名修改及配置重载的反馈统一使用 `[BK]` 富文本提示；普通结果只发一条，不自动展开详情或刷新列表。客户端仍可能根据聊天宽度自然换行。
- 名称来源与列表一致：使用现有顺序中的第一个自定义别名，没有时使用登记名，不直接回显本次输入的别名。反馈显示完整名称，七字截断只用于列表；添加或移除别名后使用修改后的显示名。
- 悬浮名称查看登记名、假人名及别名；点击名称填入使用完整登记名的详情命令，按回车查看。删除记录成功后仍保留身份悬浮，但不再提供无效的详情链接。
- 绿色表示已确认上线或已完成的数据修改，白色表示请求已发送，灰色表示无需修改，红色表示错误。右键、左键、下线、停止和发光不宣称已经在游戏内生效；动作接口未返回具体原因时只提示「操作未完成」，不推测是超时还是取消。
- 已知错误原因保留在正文中，控制台也能直接阅读；额外排查建议及原始多行信息放入悬浮提示，不向聊天框插入多余行。「报点/发光」继续显示登记维度和向下取整的方块坐标，点击坐标填入坐标点建议，悬浮保留原始坐标并说明不是实时位置。

### 独立管理别名

只想增删别名时，不需要重新登记假人：

```minecraft
!!bk 刷沙机 alias           # 打开别名管理面板
!!bk 刷沙机 alias add 沙场   # 为同一假人增加一个别名
!!bk SandBot alias del 沙场  # 只移除该别名
!!bk SandBot                # 查看当前别名和假人信息
```

- `<kikai>` 可以使用登记名、游戏名或已有别名，匹配仍然不区分大小写。新增别名不能与其他假人的名称、游戏名、别名或顶层管理命令冲突。
- 添加已能用于查找该假人的名字、删除不存在的别名时，会提示未作修改，不重复写入。登记名和游戏名不能通过删除别名移除；即使移除全部自定义别名，假人记录仍然保留。
- 两个命令使用 `permission.list` 管理权限，默认需要 admin；玩家和控制台都可使用，不要求假人或 Minecraft 服务端在线，不会查询玩家位置、发送 Carpet 动作或取消正在等待上线的操作。
- 只更新别名字段，保留登记位置、朝向及已确认真实名。旧记录的 `nick` 会在此次编辑中统一写成 `nicknames`，其他旧字段不变；如果磁盘上的目标记录已被删除、更名，或它的别名已被手动修改，会提示先执行 `!!bk reload`，而不是覆盖那些改动。
- 原有 `!!bk add` 行为不变：对相同登记名重复执行时，仍会追加别名并更新位置、维度和朝向。仅增删别名请使用新的 `alias` 子命令。

### 假人名字与大小写

- 登记名（例如 `SandBot`）和别名仍然不区分大小写。未确认时，插件沿用「前缀 + 小写登记名 + 后缀」作为预期游戏名，不把它当作已知真实名。
- 从玩家加入、退出事件或在线玩家列表中取得与预期名匹配的名字后，插件会保存服务端返回的原始拼写。例如预期名为 `b_sandbot`，实际返回 `b_SandBot`，后续 Carpet 操作就使用 `b_SandBot`，无需将它额外写入别名列表。
- 详细面板及列表悬浮说明中的「假人名」展示这个名字。只有尚未确认时才显示「待确认」；确认一次后，离线、插件重载及服务器重启不会让它重新变为待确认，也不加「上次确认」提示。以后服务端返回不同大小写时，会更新保存的拼写。
- 修改别名、位置或朝向不会丢失已确认名字。修改登记名或前后缀后，如果目标名发生了不只是大小写的变化，原确认不再适用，需要重新从服务端确认。

## ⚙️ 配置文件

插件会在 `MCDR/config/bot_kikai` 目录下创建两个配置文件：

1. `config.json` - 插件基础配置：

    ```json
    {
        "prefix_short": "!!bk",
        "spawn_max_wait_time": 10.0,
        "spawn_check_interval": 0.5,
        "bot_name_prefix": "",
        "bot_name_suffix": "",
        "permission": {
            "bot": 1,
            "list": 3
        }
    }
    ```

   配置项说明：

   - prefix_short: 命令前缀
   - spawn_max_wait_time: 等待假人生成的最大时间（秒）
   - spawn_check_interval: 等待期间检查服务器状态的最大间隔（秒），加入事件会立即唤醒等待
   - bot_name_prefix: 在 Carpet 中设置的假人前缀
   - bot_name_suffix: 在 Carpet 中设置的假人后缀
   - permission.bot: 操作假人的最低权限等级
   - permission.list: 管理假人记录及增删别名的最低权限等级

   两个时间值必须是大于 0 的有限数值，权限值必须是 0–4 的整数。前后缀仅支持英文字母、数字和下划线，总长度不能超过 15。省略的配置项使用默认值，`permission` 也会逐项补默认值。未知配置项、无效坐标、名称冲突等会导致加载被拒绝，而不是静默重置。

2. `bots.json` - 假人数据：

    ```json
    {
        "SandBot": {
            "nicknames": ["SandBot", "刷沙机", "shuashaji"],
            "dimension": "minecraft:overworld",
            "position": [-2.44, 7.0, -5.05],
            "facing": [180.59, 29.55],
            "confirmed_name": "SandBot"
        }
    }
    ```

   配置项说明：

   - nicknames: 假人的所有别名列表
   - dimension: 假人所在维度
   - position: 假人的位置坐标 [x, y, z]
   - facing: 假人的朝向角度 [水平角, 垂直角]
   - confirmed_name: 可选，由插件自动记录的服务端名字，包含前后缀并保留大小写。未确认及旧版记录可不含此字段，无需手动补写。格式须为 3–16 个英文字母、数字或下划线；如果与当前预期名不匹配，加载时会忽略该确认。

### 旧版升级说明

- 不再自动迁移 v0.4.0 以前将假人记录存放在 `config.json` 中的旧布局。此类配置会被拒绝加载，不会自动搬移数据、重置配置或创建迁移备份，已有文件保持不变。
- 如果仍使用旧布局，请先备份整个插件配置目录，使用已发布的 [v0.6.0](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.6.0) 完成迁移，确认 `config.json` 保存插件设置、`bots.json` 保存假人记录后再升级。已有不同内容的 `bots.json` 时，请先核对并处理数据冲突，不要直接覆盖。
- 已经采用双文件布局的用户无需额外操作。`bots.json` 中的旧字段 `nick`、`dim`、`pos` 及旧类型转换仍然兼容，缺少 `confirmed_name` 的记录也可正常加载。

### 重载与数据保护

- 修改配置或假人数据后执行 `!!bk reload`。两个文件全部验证通过后才应用；从 `bots.json` 删除的记录会同步移除，游戏名未改变的在线状态会保留，并异步查询实际在线玩家列表。
- **修改 `prefix_short` 后需要执行 `!!MCDR plugin reload bot_kikai`。** 普通配置重载会明确拒绝此次变更并保留原配置，避免出现按钮前缀和已注册命令不一致。
- 文件无效时不会覆盖原文件；如果 `bots.json` 无法加载，添加、修改、删除及保存会暂停，修复文件并成功重载后恢复。已有有效内存状态仍可用于操作假人。
- 文件使用临时文件加原子替换保存，并串行提交修改。
- 名字确认会立即用于内存中的假人，不中断正在等待上线的动作；后台合并保存只补写当前文件中仍存在、目标匹配的记录的 `confirmed_name`，保留读取到的其他字段和外部删除。不变的名字不会反复写盘，队列满时延后保存，卸载时会尝试保存尚未落盘的名字。
- 名字保存失败会记录日志，已确认的内存名字仍可使用；写入失败可在后续服务端确认或重载时重试，文件读取或校验失败则需要修复并成功重载后恢复。若始终未能写入，完全重启后仍需重新确认，不会宣称已经持久化成功。
- 重载、卸载、删除记录或服务器停止时，会取消对应的未完成动作，避免旧任务稍后继续执行。后台并发限制为 4 个任务，运行及排队任务合计最多 32 个，队列满时会提示重试。
- 召唤需要收到上线事件或在线列表确认才算成功；超时不会继续发送后续动作。右键、攻击、下线等只能确认请求已发送，实际结果请结合游戏和 Carpet 日志判断。

## 🔒 权限系统

插件使用 MCDR 的[权限](https://docs.mcdreforged.com/zh-cn/latest/permission.html#permission-file)系统，默认配置：

- 假人操作权限（spawn、use、kill 等）：需要 user 及以上权限
- 假人管理权限（add、del、alias add/del 等）：需要 admin 及以上权限

权限等级对应关系：

- guest = 0
- user = 1
- helper = 2
- admin = 3
- owner = 4

## 📝 注意事项

- **关于前后缀配置**：
  - 如果服务器开启了假人前后缀，请务必在本插件配置文件中配置相同的前后缀，以防止预期之外的情况发生；
  - 如果服务器没有开启假人前后缀，您依然可以配置本插件的前后缀，这样由本插件创建的假人都会带有配置的前后缀。
- **关于命令点击执行**：
  - 自 Minecraft 1.19.1-rc1 起，由于游戏安全性更新，点击聊天框中的命令按钮将无法直接执行非 `/` 开头的命令
  - 这影响了 MCDR 插件的交互体验，包括本插件在内的绝大部分插件都改用了 `suggest_command`（命令建议）模式
  - 点击命令按钮后，命令会被填充到聊天框中，需要玩家手动按回车执行
  - 这也带来了一个好处：对于类似 `!!bk <kikai> huse [间隔gt]` 这样需要自定义参数的命令，玩家可以在发送前修改参数
  - 具体详见 [MCDReforged #203](https://github.com/MCDReforged/MCDReforged/issues/203)
- 对于某些版本的 Carpet 模组，假人可能无法操作拉杆，建议替换成音符盒式开关或其他支持假人右键的方式。
- 如果旧数据存在重复别名、非标准游戏名或无效字段，请先调整数据再升级；校验失败时原文件会保留。位置显示的是登记位置，不会实时跟踪假人被移动后的坐标。

## 🧪 开发与测试

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m mcdreforged pack
```

回归测试覆盖配置保护、旧布局拒绝与文件保留、并发保存、在线状态同步、召唤超时、生命周期取消、命令解析及只读面板渲染；面板覆盖显式颜色、悬浮提示、按权限显示、别名选择、精度保留和命令建议，列表还覆盖分页边界、组合搜索、稳定排序、空状态、长名称、中英文名称占宽、当前页自适应列宽和导航命令往返，反馈覆盖显示名一致性、确认与请求语义、无变化与错误提示、已知原因保留和安全详情入口，别名管理覆盖权限、冲突、重复操作、独立保存及不中断动作，名字确认覆盖大小写持久化、旧版兼容、目标变更失效、过期查询、队列满、外部编辑保护和保存失败恢复。CI 矩阵覆盖最低支持的 MCDR 2.12.0 和 MCDR 2.16.2，并在发布打包前运行测试；它们不替代实际 Minecraft/Carpet 环境中的验证。

## ⚠️ 声明

本插件实现的功能只要是装了 Carpet Mod 能召唤假人的服务端都可以实现，即便是这样也仍有可能引发**不香草**争议。烦请想装本插件的腐竹实装前务必了解下成员们的意愿。

## 🤝 致谢

- 感谢 [Fallen_Breath](https://github.com/Fallen-Breath) 开发的 [MCDR](https://github.com/Fallen-Breath/MCDReforged) 框架
- 感谢 [Carpet](https://github.com/gnembon/fabric-carpet) 模组提供的假人功能
- 感谢 [AnzhiZhang](https://github.com/AnzhiZhang) 的 [Bot](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/bot) 插件提供的灵感

## 📄 开源协议

[GPL-3.0 License](https://github.com/Jerry-FaGe/MCDR-BotKikai/tree/master/LICENSE)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BotKikai-v0.7.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.7.0) | 0.7.0 | 2026/10/30 10:34:06 | 33.11KB | 4 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.7.0/BotKikai-v0.7.0.mcdr) |
| [BotKikai-v0.6.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.6.0) | 0.6.0 | 2026/10/27 18:59:05 | 26.13KB | 6 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.6.0/BotKikai-v0.6.0.mcdr) |
| [BotKikai-v0.5.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.5.0) | 0.5.0 | 2025/09/03 08:49:34 | 21.75KB | 402 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.5.0/BotKikai-v0.5.0.mcdr) |
| [BotKikai-v0.4.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.4.0) | 0.4.0 | 2025/08/29 09:58:15 | 21.61KB | 41 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.4.0/BotKikai-v0.4.0.mcdr) |
| [BotKikai-v0.3.1.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.3.1) | 0.3.1 | 2025/08/21 10:00:20 | 20.7KB | 39 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.3.1/BotKikai-v0.3.1.mcdr) |
| [BotKikai-v0.3.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.3.0) | 0.3.0 | 2025/08/20 09:42:58 | 20.54KB | 32 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.3.0/BotKikai-v0.3.0.mcdr) |
| [BotKikai-v0.2.1.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.2.1) | 0.2.1 | 2025/08/18 08:27:53 | 20.37KB | 30 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.2.1/BotKikai-v0.2.1.mcdr) |
| [BotKikai-v0.2.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.2.0) | 0.2.0 | 2025/08/15 11:52:11 | 20.35KB | 34 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.2.0/BotKikai-v0.2.0.mcdr) |
| [BotKikai-v0.1.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.1.0) | 0.1.0 | 2025/07/14 08:14:12 | 20.18KB | 92 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.1.0/BotKikai-v0.1.0.mcdr) |

