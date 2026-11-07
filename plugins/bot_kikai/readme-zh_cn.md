[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## bot_kikai

### 基本信息

- 插件 ID: `bot_kikai`
- 插件名: BotKikai
- 版本: 0.8.0
  - 元数据版本: 0.8.0
  - 发布版本: 0.8.0
- 总下载量: 715
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

一个基于 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 的 Minecraft 假人管理插件，专注于简化 [Carpet](https://github.com/gnembon/fabric-carpet) 假人的管理与操作。

> 君は道具ではなく、その名が似合う人になろんだ

## 📝 简介

在生存服或生电服中，管理假人往往面临这些痛点：
- 记不住每个机器对应的假人英文名？
- 不习惯输入冗长复杂的英文原版/Carpet 指令？
- 机器离主城太远，每次开关机都得舟车劳顿甚至跨维度跑图？

**BotKikai** 为假人引入了**别名映射系统**。只需为假人设置一个中文别名（如将 `SandBot` 别名设置为 `刷沙机`），即可直接用机器名字操控它：
- `!!bk 刷沙机 spawn` 与 `!!bk SandBot spawn` 效果完全相同；
- 在世界任意位置输入 `!!bk 刷沙机 use`，插件会自动将假人召唤到记录位置就位，并自动右键开关启动机器。

> 上古版本的[介绍视频](https://www.bilibili.com/video/BV1Rf4y1C776) By: [Nachuan川川](https://space.bilibili.com/107251863)

## 🚀 特性

- **假人别名系统**：支持为每个假人绑定多个中文或拼音别名，无需记忆英文名与机器对应关系
- **远程一键联动**：执行使用/攻击命令时若假人离线，会自动将其召唤就位并在上线后触发动作
- **交互式聊天栏面板**：单行紧凑列表与详情面板；常用动作支持一键点击直达，参数与高危操作保留填入微调，支持地图路标（Xaero / VoxelMap）分享与详细数据悬浮预览
- **分页与状态搜索**：支持按在线/离线状态筛选及关键词实时检索假人
- **灵活的别名管理**：支持独立追加与移除别名，不影响假人坐标、朝向及运行状态
- **前后缀与大小写自适应**：支持 Carpet 假人前后缀，自动记录并持久化服务端真实游戏名大小写
- **安全与稳定性**：配置热重载、原子文件保存、多级权限控制及动作生命周期安全取消

## ⚙️ 依赖

- Python >= 3.10
- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) >= 2.12.0（推荐 >= 2.16.2）
- [MinecraftDataAPI](https://github.com/Fallen-Breath/MinecraftDataAPI) >= 1.6.2
- Minecraft 服务端需要安装 [Carpet](https://github.com/gnembon/fabric-carpet) 模组

> 注：旧环境升级时请先更新上述依赖；插件不要求开启 RCON。

## 📖 命令说明

基础命令（可于配置文件中自定义）：

```minecraft
!!bk
```

### 管理与查询命令

| 命令                                               | 说明                           | 默认权限        |
| ------------------------------------------------ | ---------------------------- | ----------- |
| `!!bk`                                           | 显示帮助信息                       | 所有人 (guest) |
| `!!bk list [online|offline] [page]`              | 分页查看假人列表，可筛选在线或离线状态（每页 10 条） | 所有人 (guest) |
| `!!bk list [online|offline] search <关键词> [page]` | 搜索假人（匹配登记名、游戏名或别名）           | 所有人 (guest) |
| `!!bk <kikai>`                                   | 显示假人详情面板与操作入口                | 所有人 (guest) |
| `!!bk add <name> <kikai>`                        | 使用当前玩家所在位置和朝向添加/更新假人         | 管理员 (admin) |
| `!!bk add <name> <kikai> <dim> <pos> <facing>`   | 使用指定参数手动添加/更新假人              | 管理员 (admin) |
| `!!bk del <kikai>`                               | 删除假人记录（不会下线游戏中已在线假人）         | 管理员 (admin) |
| `!!bk <kikai> alias`                             | 打开别名管理面板                     | 管理员 (admin) |
| `!!bk <kikai> alias add <alias>`                 | 为指定假人添加别名                    | 管理员 (admin) |
| `!!bk <kikai> alias del <alias>`                 | 移除指定假人的别名                    | 管理员 (admin) |
| `!!bk reload`                                    | 重载配置文件与假人数据                  | 管理员 (admin) |

### 假人操作命令

| 命令                               | 说明                   | 默认权限      |
| -------------------------------- | -------------------- | --------- |
| `!!bk <kikai> spawn`             | 在登记位置召唤假人            | 玩家 (user) |
| `!!bk <kikai> kill`              | 移除（下线）假人             | 玩家 (user) |
| `!!bk <kikai> where`             | 显示记录位置，并让假人发光 2 分钟   | 玩家 (user) |
| `!!bk <kikai> use`               | 假人右键一次（若离线会自动先召唤上线）  | 玩家 (user) |
| `!!bk <kikai> huse [<interval>]` | 假人持续右键，可选间隔时间（单位：gt） | 玩家 (user) |
| `!!bk <kikai> atk`               | 假人左键一次（若离线会自动先召唤上线）  | 玩家 (user) |
| `!!bk <kikai> hatk [<interval>]` | 假人持续左键，可选间隔时间（单位：gt） | 玩家 (user) |
| `!!bk <kikai> stop`              | 停止假人的所有动作            | 玩家 (user) |

> 说明：命令中的 `<kikai>` 可使用假人的**登记名**、**游戏名**或任意**别名**（均不区分大小写）。

## ⚡ 快速上手

### 1. 添加假人

前往目标机器前，站好期望的位置与朝向，执行：

```minecraft
!!bk add SandBot 刷沙机
```

插件会自动记录当前维度、精确坐标与朝向。假人基础名（如 `SandBot`）仅限英文字母、数字和下划线。

*也可以手动指定完整参数（支持 `0 / -1 / 1` 或 `overworld / the_nether / the_end` 等维度别名）：*

```minecraft
!!bk add SandBot 刷沙机 minecraft:overworld 0 64 0 -154.43 3.90
```

### 2. 操控假人

```minecraft
!!bk 刷沙机           # 查看假人详情与快捷操作面板
!!bk 刷沙机 spawn     # 召唤假人上线
!!bk 刷沙机 use       # 让假人右键一次（离线会自动先上线）
!!bk 刷沙机 hatk 12   # 让假人每 12 gt（0.6 秒）攻击一次
!!bk 刷沙机 stop      # 停止假人动作
!!bk 刷沙机 kill      # 让假人下线
```

### 3. 查看与检索列表

```minecraft
!!bk list                         # 查看全部假人（第 1 页）
!!bk list 2                       # 查看全部假人（第 2 页）
!!bk list online                  # 仅查看在线假人
!!bk list offline 2               # 仅查看离线假人（第 2 页）
!!bk list search 沙               # 搜索名字或别名包含「沙」的假人
!!bk list online search farm 2    # 在线假人中搜索 farm，查看第 2 页
```

列表每行紧凑展示假人名称与快捷按钮（上线/下线/右键/详情），鼠标悬浮在名称上可快速查看详细坐标与全部别名。

### 4. 独立增删别名

无需重新登记位置，可直接增删别名：

```minecraft
!!bk 刷沙机 alias           # 打开别名管理面板
!!bk 刷沙机 alias add 沙场   # 为同一假人增加别名「沙场」
!!bk SandBot alias del 沙场  # 移除别名「沙场」（登记名不可移除）
```

## ⚙️ 配置文件

插件会在 `config/bot_kikai` 目录下自动生成两个配置文件：

### 1. `config.json`（插件设置）

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

| 配置项                    | 类型     | 默认值    | 说明                                  |
| ---------------------- | ------ | ------ | ----------------------------------- |
| `prefix_short`         | string | `!!bk` | 插件指令前缀                              |
| `spawn_max_wait_time`  | float  | `10.0` | 等待假人生成的最大超时时间（秒）                    |
| `spawn_check_interval` | float  | `0.5`  | 假人上线检测轮询间隔（秒）                       |
| `bot_name_prefix`      | string | `""`   | Carpet 假人名字前缀（如 `bot_`）             |
| `bot_name_suffix`      | string | `""`   | Carpet 假人名字后缀                       |
| `permission.bot`       | int    | `1`    | 操作假人（spawn/use/kill 等）的最低权限等级       |
| `permission.list`      | int    | `3`    | 管理假人（add/del/alias/reload 等）的最低权限等级 |

### 2. `bots.json`（假人数据）

```json
{
    "SandBot": {
        "nicknames": ["SandBot", "刷沙机", "shuashaji"],
        "dimension": "minecraft:overworld",
        "position": [-2.44, 70.0, -5.05],
        "facing": [180.0, 30.0]
    }
}
```

- `nicknames`: 假人的所有别名列表（第一项为基础登记名）
- `dimension`: 假人所在维度
- `position`: 假人位置坐标 `[x, y, z]`
- `facing`: 假人视线朝向 `[水平角, 垂直角]`
- `confirmed_name`: *（可选）* 插件自动确认并持久化的服务端真实大小写游戏名，通常由插件自动维护，无需手动干预。

### 配置重载与数据安全

- **热重载**：修改配置或假人数据后执行 `!!bk reload` 即可重新加载。若修改了 `prefix_short` 指令前缀，需执行 `!!MCDR plugin reload bot_kikai`。
- **原子保存**：插件采用临时文件与原子替换保存数据，保障文件在并发或异常退出时不损坏、不丢失。
- **历史迁移**：自 v0.6.0 起已采用双文件布局；若从 v0.4.0 以前的旧版本跨版本升级，请先使用 [v0.6.0](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.6.0) 完成自动迁移。

## 🔒 权限系统

插件直接接入 MCDR 原生[权限系统](https://docs.mcdreforged.com/zh-cn/latest/permission.html#permission-file)：

| 角色       | 等级  | 默认权限说明                                                      |
| -------- | --- | ----------------------------------------------------------- |
| `guest`  | 0   | 查看帮助、浏览列表与搜索、查看假人详情                                         |
| `user`   | 1   | 假人日常操控（`spawn` / `kill` / `use` / `atk` / `stop` / `where`） |
| `helper` | 2   | -                                                           |
| `admin`  | 3   | 假人登记与管理（`add` / `del` / `alias` / `reload`）                 |
| `owner`  | 4   | 全部最高权限                                                      |

## 📝 注意事项与交互机制

### 💬 聊天栏按钮交互机制

为了兼顾「操作的高效流畅」与「防止手滑误触」，插件对聊天栏中的所有按钮采用了**分级交互设计**：

#### 1. 分级交互设计

- **⚡ 一键点击直达（`run_command`）**
  适用于高频、无参的常规操作。在兼容环境下点击即可直接生效，无需额外按回车：
  - **日常操控**：假人上线（`spawn`）、下线（`kill`）、单次右键（`use`）、单次左键（`atk`）、停止动作（`stop`）、报点发光（`where`）；
  - **界面导航**：假人详情、列表查看、翻页、在线/离线筛选、清除搜索、刷新面板、打开别名管理；
  - **反馈跳转**：操作成功/失败反馈中的假人名称（点击直接打开该假人详情）。
  > *注：假人离线时点击交互动作，插件仍会先自动将其召唤就位；权限不足时点击依然会被后端拦截并提示。*

- **✏️ 填入输入框微调 / 二次确认（`suggest_command`）**
  点击后仅将预设指令填入玩家的聊天输入框，**由玩家确认或补充参数后，手动按回车执行**：
  - **参数微调**：持续右键/持续左键（`huse ` / `hatk `，光标自动停在末尾方便输入 gt 间隔）、列表搜索（方便输入关键词）、添加别名（`alias add `）；
  - **高危操作防误触**：删除假人记录（`del`）、移除指定别名（`alias del`），点击填入后留给玩家核对目标的机会，防止手滑误删；
  - **坐标分享**：将假人登记坐标填入聊天框，由玩家自行决定是否发送到公屏。

---

#### 2. 点击执行兼容性与服主配置推荐

自 Minecraft 1.19.1 引入聊天签名机制后，原版客户端出于安全考虑，禁止点击文本直接发送非 `/` 开头的聊天内容（1.19.1~1.21.4 点击无响应，1.21.5+ 虽放宽限制但会将内容视为原版命令而非聊天），导致 MCDR 等服务端的点击直达功能在纯原版客户端上受限。

为让服内玩家获得完整、丝滑的一键点击体验，推荐进行如下配置：

- **💡 强烈推荐（服主端配置，玩家零门槛）**：
  服务端直接安装 [LetMeClickAndSendForServer](https://github.com/Fallen-Breath/LetMeClickAndSendForServer) 模组。安装后**玩家使用纯原版客户端即可直接一键点击执行**，无需在本地安装任何模组！
- **备选方案（玩家端配置）**：
  若服务器未安装上述服务端模组，玩家也可以在自己的客户端安装 Fabric 模组 [LetMeClickAndSend](https://github.com/Fallen-Breath/LetMeClickAndSend)。
- **自定义前缀注意**：
  若在 `config.json` 中修改了命令前缀 `prefix_short`（默认为 `!!bk`），请确保兼容模组配置的正则规则（默认 `!!.*`）能够正确匹配到你的前缀。

> **友情提示**：即使未部署上述兼容模组，插件的所有功能亦完全可用——所有命令均可手动在聊天框中输入执行，带参微调和高危删除类按钮也不会受到任何影响。

### 🗺️ 坐标分享与小地图联动

在假人详情面板或执行 `!!bk <kikai> where` 报点时，展示的坐标支持一键生成主流小地图的路标分享格式，方便与队友共享机器位置：

- **点击坐标文字**：自动填入 **Xaero's Minimap / World Map** 原生路标分享格式（支持原版三维度及带命名空间的自定义模组维度）；
- **点击坐标后方的 `[V]` 按钮**：自动填入 **VoxelMap** 经典坐标分享格式。

**交互说明与细节**：
- **防误触设计**：点击仅将分享文本填入玩家聊天输入框，**需手动按回车发送到公屏**，不会自动广播打扰公屏；
- **队友无缝添加**：公开发送后，服内安装了对应地图模组的队友点击该聊天消息即可在小地图上添加路标；未安装地图模组的玩家也能直接阅读明文坐标；
- **坐标说明**：分享的坐标为假人登记时的就位点方块整数坐标（向下取整，下界坐标不自动折算倍率），非外力位移后的实时位置。

### 📌 其他注意事项

- **Carpet 前后缀一致性**：若服务端开启了假人前后缀，请务必在 `config.json` 中配置完全一致的前后缀，避免假人身份匹配异常。
- **Carpet 拉杆操作限制**：部分 Carpet 版本中假人右键可能无法正常拨动拉杆，推荐使用音符盒、红石按钮等更稳定的机械开关。
- **假人位置说明**：展示和记录的位置均为登记时的就位点，不会实时追踪假人后续在游戏内被外力位移（如水流冲走）后的位置。

## 🧪 开发与测试

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m mcdreforged pack
```

测试套件完整覆盖了配置校验、原子读写、别名管理、并发任务、命令解析及富文本面板渲染。CI 矩阵覆盖 Python 3.10 / 3.12 及 MCDR 2.12.0 / 2.16.2。

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
| [BotKikai-v0.8.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.8.0) | 0.8.0 | 2026/11/06 07:07:37 | 33.56KB | 3 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.8.0/BotKikai-v0.8.0.mcdr) |
| [BotKikai-v0.7.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.7.0) | 0.7.0 | 2026/10/30 10:34:06 | 33.11KB | 12 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.7.0/BotKikai-v0.7.0.mcdr) |
| [BotKikai-v0.6.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.6.0) | 0.6.0 | 2026/10/27 18:59:05 | 26.13KB | 9 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.6.0/BotKikai-v0.6.0.mcdr) |
| [BotKikai-v0.5.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.5.0) | 0.5.0 | 2025/09/03 08:49:34 | 21.75KB | 405 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.5.0/BotKikai-v0.5.0.mcdr) |
| [BotKikai-v0.4.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.4.0) | 0.4.0 | 2025/08/29 09:58:15 | 21.61KB | 44 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.4.0/BotKikai-v0.4.0.mcdr) |
| [BotKikai-v0.3.1.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.3.1) | 0.3.1 | 2025/08/21 10:00:20 | 20.7KB | 42 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.3.1/BotKikai-v0.3.1.mcdr) |
| [BotKikai-v0.3.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.3.0) | 0.3.0 | 2025/08/20 09:42:58 | 20.54KB | 35 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.3.0/BotKikai-v0.3.0.mcdr) |
| [BotKikai-v0.2.1.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.2.1) | 0.2.1 | 2025/08/18 08:27:53 | 20.37KB | 33 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.2.1/BotKikai-v0.2.1.mcdr) |
| [BotKikai-v0.2.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.2.0) | 0.2.0 | 2025/08/15 11:52:11 | 20.35KB | 37 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.2.0/BotKikai-v0.2.0.mcdr) |
| [BotKikai-v0.1.0.mcdr](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/tag/v0.1.0) | 0.1.0 | 2025/07/14 08:14:12 | 20.18KB | 95 | [下载](https://github.com/Jerry-FaGe/MCDR-BotKikai/releases/download/v0.1.0/BotKikai-v0.1.0.mcdr) |

