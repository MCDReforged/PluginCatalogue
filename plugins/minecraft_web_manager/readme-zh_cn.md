[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## minecraft_web_manager

### 基本信息

- 插件 ID: `minecraft_web_manager`
- 插件名: Minecraft Web Manager
- 版本: 1.2.6
  - 元数据版本: 1.2.6
  - 发布版本: 1.2.6
- 总下载量: 112
- 作者: [ForestTrees](https://github.com/ForestTrees)
- 仓库: https://github.com/ForestTrees/MinecraftWebManager
- 仓库插件页: https://github.com/ForestTrees/MinecraftWebManager/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 为 MCDReforged 管理的 Minecraft 服务器提供安全的网页仪表盘与实时控制台，支持玩家、插件、世界与 Mod 管理。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [fastapi](https://pypi.org/project/fastapi) | \>=0.115,\<1.0 |
| [uvicorn[standard]](https://pypi.org/project/uvicorn[standard]) | \>=0.30,\<1.0 |
| [python-multipart](https://pypi.org/project/python-multipart) | \>=0.0.9,\<1.0 |
| [psutil](https://pypi.org/project/psutil) | \>=6.0,\<8.0 |
| [ruamel-yaml](https://pypi.org/project/ruamel-yaml) | \>=0.17,\<0.19 |

```
pip install "fastapi>=0.115,<1.0" "uvicorn[standard]>=0.30,<1.0" "python-multipart>=0.0.9,<1.0" "psutil>=6.0,<8.0" "ruamel-yaml>=0.17,<0.19"
```

### 介绍

# Minecraft Web Manager

[English](https://github.com/ForestTrees/MinecraftWebManager/tree/main/README_en.md) | **中文**

一个 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 插件，为 Minecraft 服务器提供带登录鉴权的网页管理面板：实时控制台、玩家管理、插件与 Mod 在线管理、`server.properties` 与 MCDR `config.yml` 在线编辑、Mod 配置文件编辑、资源占用图表。

面板由插件自身托管，无需另外部署 Web 服务器，也不依赖任何 CDN 或前端构建工具。

- **版本**：1.2.6
- **依赖**：MCDReforged `>=2.15.0`、Python 3.10+
- **Python 库**：`fastapi`、`uvicorn[standard]`、`python-multipart`、`psutil`、`ruamel-yaml`

---

## 功能

### 实时控制台

- 实时推送最近1000行服务器日志输出历史
- 支持发送 Minecraft 命令与 MCDR 命令（`!!` 开头）
- 命令通道可切换 **console**（写入服务端标准输入）或 **RCON**（能拿到服务器的回复文本）
- 输入框支持 `↑` / `↓` 翻查历史命令，并支持指令提示
- 一键 启动 / 停止 / 重启 服务器

![实时控制台](https://raw.githubusercontent.com/ForestTrees/MinecraftWebManager/main/docs/img/实时控制台.png)

### 玩家管理

- **玩家列表**：汇总所有进过本服的玩家，显示在线状态、IP、在线时长、最后在线时间、所在维度与坐标；点击玩家昵称可复制该玩家的 UUID
- **假人列表**：识别出的 Carpet 假人（bot），可折叠、可行内手动标记/取消标记；点击假人昵称同样可以复制 UUID
- **对单个玩家直接执行：**设为 / 取消 OP、踢出、封禁、封禁 IP、加入 / 移出白名单
- **白名单**：开关白名单、重载名单、增删成员
- **管理员**：查看与增删 OP
- **封禁**：封禁 / 解封玩家与 IP，可填写理由

![玩家管理-玩家列表](https://raw.githubusercontent.com/ForestTrees/MinecraftWebManager/main/docs/img/玩家管理.png)

### 插件与 Mod 管理

**插件**

- **插件列表**：展示服务器内全部MCDR插件；支持一键检查更新、禁用、删除、启用、重载插件
- **配置插件**：可在线编辑插件的配置文件；二进制文件与超过 1 MiB 的文件只读
- 插件操作进行中会禁用相关按钮，防止重复触发；检查更新被拒绝（如已有其它安装任务在运行）时不会误报「全部是最新」

![插件管理](https://raw.githubusercontent.com/ForestTrees/MinecraftWebManager/main/docs/img/插件管理.png)

**Mod**

- **模组文件**：展示服务器内全部mod；支持上传、禁用、删除、配置各个mod。上传、禁用、删除都需**重启服务端**才会真正生效
- **配置文件**：可在线编辑各mod的配置文件；二进制文件与超过 1 MiB 的大文件只读不可编辑

![Mod管理](https://raw.githubusercontent.com/ForestTrees/MinecraftWebManager/main/docs/img/mod管理.png)

### 服务器配置

服务器配置页顶部通过「服务器配置 / MCDR 配置」两个子页签切换。两个子页共用统一的标题、工具栏和右侧操作区，筛选项会根据可用宽度自适应。

- **服务器配置**：在线查看与修改 `server.properties`，修改后需重启服务器后生效
- **MCDR 配置**：在线查看与编辑 MCDR 的 `config.yml` 配置文件，保存后自动执行 `!!MCDR reload config` 立即生效

![服务器配置](https://raw.githubusercontent.com/ForestTrees/MinecraftWebManager/main/docs/img/服务器配置.png)

### 服务器状态

- TPS、MSPT、Swap、磁盘、系统负载概览
- CPU 占用、内存占用、网络实时速度三张折线图，时间范围可选 10m / 30m / 1h / 6h / 12h / 1d / 3d / 7d
- 区分「整机」与「Minecraft 进程」两条曲线，1 秒精度采样保留最近 1 小时，1 分钟均值保留最近 7 天

![服务器状态](https://raw.githubusercontent.com/ForestTrees/MinecraftWebManager/main/docs/img/服务器状态.png)

### 其它

- 浅色 / 暗黑 / 跟随系统三种配色，自动记忆
- 界面语言自动跟随浏览器（简体 / 繁体中文 → 中文，其余 → 英文），也可在页面右上角 / 侧边栏手动切换并记忆
- 响应式布局，手机浏览器可用

---



## 如何安装

### 1. 一键安装指令

```
!!MCDR plugin install minecraft_web_manager
```

### 2. 插件管理

请参考mcdreforged官方文档：https://docs.mcdreforged.com/zh-cn/latest/command/mcdr.html#plugin-management


### 3. 取得初始密码

首次加载时插件会生成一次性密码并打印到 MCDR 日志（`WARNING` 级别）：

```
[Minecraft Web Manager] Minecraft Web Manager bootstrap password: xxxxxxxxxxxxxxxxxxxxxxxx
```

**请立刻保存这串密码**，它只会明文出现这一次。随后用浏览器访问：

```
http://127.0.0.1:8088
```

默认用户名 `admin`，密码即上面那串。

### 4. 忘记密码怎么办

把配置文件里的 `password.salt` 和 `password.hash` 都改成空字符串 `""`：

```json
"password": { "salt": "", "hash": "" }
```

保存后执行 `!!MCDR reload plugin minecraft_web_manager`，新的一次性密码会重新打印在 MCDR 日志里。

---



## 如何更新

### 方式一：MCDR更新指令

```
!!MCDR plugin install -U minecraft_web_manager
```

### 方式二：面板自身的更新提示

点击并确认后，将自动下载最新版本的插件与相关依赖，并自动重载插件

![更新提示](https://raw.githubusercontent.com/ForestTrees/MinecraftWebManager/main/docs/img/更新提示.png)



## 配置

配置文件位于 MCDR 工作目录下的 `config/minecraft_web_manager/config.json`，**修改后需要重载插件才会生效**。

| 键                                 | 默认值                | 说明                                                                       |
| --------------------------------- | ------------------ | ------------------------------------------------------------------------ |
| `host`                            | `127.0.0.1`        | 面板监听地址。默认仅本机可访问，改成 `0.0.0.0` 才能从其它机器打开                                   |
| `port`                            | `8088`             | 面板监听端口                                                                   |
| `username`                        | `admin`            | 登录用户名                                                                    |
| `password.salt` / `password.hash` | 自动生成               | 密码的 PBKDF2 盐值与哈希，密码本身不会存盘                                                |
| `token_secret`                    | 自动生成               | 登录令牌的签名密钥，清空它会让所有已登录会话立即失效                                               |
| `token_ttl_seconds`               | `2592000`（30 天）    | 登录会话有效期（秒）；活跃使用时到期前会自动续期                                                 |
| `panel_title`                     | `MC Web Manager`   | 面板品牌标题，显示在侧边栏与浏览器标签页（登录页标题同步）                                            |
| `bot_names`                       | `[]`               | 手动标记为假人的玩家名列表（小写）；自动识别之外的手动兜底                                            |
| `not_bot_names`                   | `[]`               | 反向名单（小写）：即使匹配名称规则或离线 UUID 也强制视为真人；行内「取消标记」会自动写入                          |
| `bot_name_patterns`               | `["(?i)^bot[_-]"]` | 假人名称正则列表；默认只对**不在 usercache 中**的玩家生效，避免误伤同名真玩家                           |
| `bot_name_patterns_apply_to_all`  | `false`            | 设为 `true` 时名称规则对所有玩家生效（适用于假人也写入 usercache 的服务端）；同名真玩家请加入 `not_bot_names` |

---



## 关于 RCON

插件的大部分功能不需要 RCON，但以下内容依赖它：

- TPS / MSPT 读数（通过 `tick query`）
- 玩家列表里的坐标与维度
- 控制台切换到 RCON 通道后才能看到命令的回复文本
- 插件重载后恢复在线玩家列表

启用方式是 **两处都要配**，且端口与密码必须一致：

- Minecraft 端：`server/server.properties` 里的 `enable-rcon`、`rcon.port`、`rcon.password`
- MCDR 端：MCDR 的 `config.yml` 里的 `rcon` 段

其中 Minecraft 端的三项可以直接在面板「服务器配置」页的「服务器配置」子页签里改（改完需重启服务器）；MCDR 端可以在「服务器配置」页的「MCDR 配置」子页签里改，保存后会自动执行 `!!MCDR reload config` 生效。

---



## 安全建议

面板拥有服务器的完整控制权（执行任意命令、封禁玩家、改配置、管理/删除插件与 mod、改写配置文件），请谨慎暴露：

- **默认只监听 `127.0.0.1`**，从外网访问建议保留这一设置，通过 SSH 隧道或内网穿透连接
- 若确实要开放到公网，请把它放在 Nginx / Caddy 等反向代理之后并启用 HTTPS。插件自身**不提供 TLS**，明文 HTTP 会让密码和令牌在链路上裸奔
- 登录接口内置简单的失败限流（同一来源 60 秒内最多尝试 10 次），并且面板的 API 文档默认关闭；会话 cookie 使用 `HttpOnly` 与 `SameSite=Strict`，页面脚本无法读取令牌
- 反向代理需要额外转发 WebSocket，否则实时控制台无法连接：

  ```nginx
  location /ws/ {
      proxy_pass http://127.0.0.1:8088;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "upgrade";
  }
  ```

- `rcon.password` 等敏感配置项在面板里只显示为空，不会下发到浏览器；留空提交表示保持原值不变
- MCDR 配置编辑器按字段展示，RCON 密码不会回显；留空提交表示保持原值不变

---



## 已知限制

- **资源占用历史存在内存中**，MCDR 重启或插件重载后会清零，重新从头累积
- **世界种子、名称、难度读自存档文件**，只在服务器存盘时更新，可能比实际状态滞后几分钟
- **玩家的 IP 与 UUID 靠解析服务器输出获得**，如果服务端日志格式特殊可能抓不到；插件重载后恢复的在线玩家没有加入时间与 IP
- **Mod 列表只识别 Fabric**（读取 `fabric.mod.json`），Forge / NeoForge mod 只会列出文件名；上传、禁用、删除按 `.jar` 文件管理，不区分加载器
- **MCDR 配置以可视化字段编辑**，写入时由 ruamel.yaml 重新生成文件；配置项集合随 MCDR 版本自动识别，新版本新增的未知字段会用通用输入框展示
- **插件检查更新 / 更新依赖 MCDR 插件仓库网络访问**，且只有打包插件（`.mcdr` / `.pyz`）可更新；检查与更新的详细输出显示在实时控制台。面板自身每次打开时检查更新，有新版本时可从侧边栏底部确认更新，执行 `!!MCDR plugin install -U minecraft_web_manager` 后自动重载；面板自身也可以在面板内重载，重载后短暂中断并自动恢复
- **假人识别**：经典 Carpet 假人按离线 UUID 精确识别；TIS/AMS/RMS 等扩展的假人可能是 Mojang 查询 UUID 或随机 UUID（v4），只能靠名称规则 + usercache 信号识别。名称规则默认只对无 usercache 记录的玩家生效，误判时可用 `not_bot_names` 或行内「取消标记」强制修正
- **Ping 值在原版服务端下无法获取**，列表中不展示
- 面板界面目前支持简体中文与英文

---



## 反馈

欢迎通过 [Issues](https://github.com/ForestTrees/MinecraftWebManager/issues) 提交问题与建议。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MinecraftWebManager-v1.2.6.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.2.6) | 1.2.6 | 2026/09/04 08:33:55 | 104.93KB | 4 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.2.6/MinecraftWebManager-v1.2.6.mcdr) |
| [MinecraftWebManager-v1.2.5.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.2.5) | 1.2.5 | 2026/09/03 03:04:38 | 104.31KB | 4 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.2.5/MinecraftWebManager-v1.2.5.mcdr) |
| [MinecraftWebManager-v1.2.4.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.2.4) | 1.2.4 | 2026/09/01 08:28:18 | 104.03KB | 4 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.2.4/MinecraftWebManager-v1.2.4.mcdr) |
| [MinecraftWebManager-v1.2.3.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.2.3) | 1.2.3 | 2026/08/26 03:16:56 | 101.97KB | 16 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.2.3/MinecraftWebManager-v1.2.3.mcdr) |
| [MinecraftWebManager-v1.2.2.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.2.2) | 1.2.2 | 2026/08/24 09:53:47 | 94.66KB | 3 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.2.2/MinecraftWebManager-v1.2.2.mcdr) |
| [MinecraftWebManager-v1.2.1.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.2.1) | 1.2.1 | 2026/08/20 01:41:38 | 93.71KB | 12 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.2.1/MinecraftWebManager-v1.2.1.mcdr) |
| [MinecraftWebManager-v1.2.0.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.2.0) | 1.2.0 | 2026/08/18 06:49:19 | 93.22KB | 9 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.2.0/MinecraftWebManager-v1.2.0.mcdr) |
| [MinecraftWebManager-v1.1.0.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.1.0) | 1.1.0 | 2026/08/15 16:25:25 | 86.39KB | 12 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.1.0/MinecraftWebManager-v1.1.0.mcdr) |
| [MinecraftWebManager-v1.0.1.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.0.1) | 1.0.1 | 2026/08/10 12:14:26 | 68.35KB | 19 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.0.1/MinecraftWebManager-v1.0.1.mcdr) |
| [MinecraftWebManager-v1.0.0.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v1.0.0) | 1.0.0 | 2026/08/10 01:58:26 | 63.47KB | 10 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v1.0.0/MinecraftWebManager-v1.0.0.mcdr) |
| [MinecraftWebManager-v0.1.1.mcdr](https://github.com/ForestTrees/MinecraftWebManager/releases/tag/v0.1.1) | 0.1.1 | 2026/08/03 06:36:30 | 55.57KB | 19 | [下载](https://github.com/ForestTrees/MinecraftWebManager/releases/download/v0.1.1/MinecraftWebManager-v0.1.1.mcdr) |

