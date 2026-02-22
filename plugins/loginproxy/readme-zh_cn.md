[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## loginproxy

### 基本信息

- 插件 ID: `loginproxy`
- 插件名: LoginProxy
- 版本: 0.9.0
  - 元数据版本: 0.9.0
  - 发布版本: 0.9.0
- 总下载量: 3157
- 作者: [zyxkad](https://github.com/zyxkad)
- 仓库: https://github.com/kmcsr/login_proxy_mcdr
- 仓库插件页: https://github.com/kmcsr/login_proxy_mcdr/tree/master
- 标签: [`管理`](/labels/management/readme-zh_cn.md), [`API`](/labels/api/readme-zh_cn.md)
- 描述: Minecraft 服务器登录代理兼白名单插件

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.3.0 |
| [python](/plugins/python/readme-zh_cn.md) | ^3.12 |
| [kpi](/plugins/kpi/readme-zh_cn.md) | ~1.5.1 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [pycryptodome](https://pypi.org/project/pycryptodome) | \>=3.21.0 |

```
pip install "pycryptodome>=3.21.0"
```

### 介绍


- [English](https://github.com/kmcsr/login_proxy_mcdr/tree/master/README.MD)
- 中文

# Login Proxy

*如果本插件有用, 请给个star吧 :)*

类似项目: <https://github.com/kmcsr/go-liter>

## 特性

- 使用**反向代理**代理 Minecraft 服务器**登录包**, *不必担心客户端绕开白名单*
- 最好的离线登录白名单插件
- 为 MCDR 最高级的白名单 ~~(没有之一)~~
- 可扩展, 可以监听并自定义玩家登录事件
- 支持 IP Network
- 支持解析并自定义 Minecraft 数据流

## 目前支持的 Minecraft 版本

`1.8 ~ 1.21.4`

## 依赖

| ID                                                             | 下载链接                                                   | 是否可选 |
| -------------------------------------------------------------- | ------------------------------------------------------ | ---- |
| [`kpi`](https://github.com/kmcsr/kpi_mcdr)                     | <https://github.com/kmcsr/kpi_mcdr/releases>           | 必须   |
| [`packet_parser`](https://github.com/kmcsr/packet_parser_mcdr) | <https://github.com/kmcsr/packet_parser_mcdr/releases> | 可选   |

## FAQ

- 问: loginproxy会增加玩家延迟吗?
- 答: 完全没有延迟是**不可能的**. 但loginproxy只会转发数据流, 中间不执行任何格外操作, 所以正常状态下延迟影响**可忽略不计** _(<1ms)_.

- 问: loginproxy的白名单与*原版白名单*兼容吗?
- 答: loginproxy白名单是基于*minecraft服务端连接协议*实现的, **与原版白名单不冲突**.
  您**无法**通过原版白名单指令控制本插件, 本插件也**不会影响到原版白名单的工作**.
  如果您**同时启用**了*本插件白名单*与*原版白名单(或者其他插件/mod的白名单)*, 您必须保证玩家**同时存在每个白名单列表中**才能进行游戏.

- 问: 服务端无法启动怎么办?
- 答: 请确保minecraft服务端IP或端口与loginproxy端口不重复.

## 如何安装&配置

1. 从 [releases](https://github.com/kmcsr/login_proxy_mcdr/releases/) 下载最新的 .mcdr 文件至插件文件夹
2. 调整您的minecraft服务器端口 _(在server.properties)_, 使其不与本插件的`proxy_addr`重复 _(如果您使用spigot等第三方服务端, 请确保端口等基本信息与`server.properties`同步)_
3. 调整您的防火墙配置, 防止外部连接连接您的minecraft服务端 _(或者让您的服务端监听`127.0.0.1`)_
4. 将服务端的 `online-mode` 设为 `false`. 如果需要, 可以启用本插件配置文件中的 `online_mode` 选项.
5. 启动 MCDR

## 指令

| 指令格式                                  | 介绍              |
| ------------------------------------- | --------------- |
| `!!lp help`                           | 显示帮助信息, `!!lp`同 |
| `!!lp list`                           | 列出所有的玩家及其IP     |
| `!!lp query <name>`                   | 查询玩家连接IP        |
| `!!lp banned`                         | 列出黑名单           |
| `!!lp ban <name>`                     | 禁止玩家连接          |
| `!!lp banip <ip>`                     | 禁止IP连接          |
| `!!lp pardon <name>`                  | 允许玩家连接          |
| `!!lp pardonip <ip>`                  | 允许IP连接          |
| `!!lp whitelist`                      | 列出白名单和IP白名单     |
| `!!lp whitelist [enable|disable]`     | 启用/禁用白名单        |
| `!!lp whitelist [enableip|disableip]` | 启用/禁用IP白名单      |
| `!!lp allow <name>`                   | 将玩家添加至白名单       |
| `!!lp allowip <ip>`                   | 将IP添加至IP白名单     |
| `!!lp remove <name>`                  | 将玩家从白名单中移除      |
| `!!lp removeip <ip>`                  | 将IP从IP白名单中移除    |

## 配置文件

#### loginproxy/config.json _(主配置文件)_

```javascript
{
    "minimum_permission_level": { // 指令权限
        "help": 0,
        "list": 1,
        "query": 2,
        "banned": 2,
        "ban": 2,
        "banip": 3,
        "pardon": 3,
        "pardonip": 3,
        "whitelist": 2,
        "enable": 3,
        "disable": 3,
        "allow": 3,
        "allowip": 3,
        "remove": 3,
        "removeip": 3
    },
    "proxy_addr": { // 代理服务器地址&端口. 请注意不要与 Minecraft 服务端重复! 否则服务端将无法启动
        "ip": "", // 代理服务器 IPv4 专用 IP, 设置为 null 禁用 IPv4
        "port": 25565 // IPv4 IP 对应的端口
        "ipv6": "::", // 代理服务器 IPv6 专用 IP, 设置为 null 禁用 IPv6
        "ipv6_port": 25565, // IPv6 IP 对应的端口
    },
    "enable_whitelist": false, // 是否启用白名单
    "enable_ip_whitelist": false, // 是否启用IP白名单
    "whitelist_level": 3, // 当玩家拥有高于或等于此权限时, 忽略白名单
    "kick_cmd": "kick {name} {reason}", // 将在线玩家踢出游戏的指令; 留空为强制断开连接 (不推荐)
    "messages": { // 一些提示消息
        "banned.name": "Your account has been banned", // 当玩家名被禁止时提示
        "banned.ip": "Your ip has been banned", // 当玩家 IP 被禁止时提示
        "whitelist.name": "Your account is not in the whitelist", // 当玩家名不在白名单时提示
        "whitelist.ip": "Your ip is not in the whitelist" // 当 玩家名/IP 不在白名单时提示
    },
    "allow_transfer": true, // 是否允许客户端转移到此服务器.
    "enable_packet_proxy": false, // 是否解析数据包. 必须先安装 packet_parser. 需要为大部分依赖于 LoginProxy 的插件启用.
    "online_mode": false, // 是否为在线模式
    "identify_by_online_uuid": true, // 使用 uuid 而非用户名判断玩家身份 (在黑白名单中使用)
    "uuid_cache_ttl": 3600 // uuid 查询缓存时间 (秒)
}
```

#### loginproxy/list.json _(玩家白名单&黑名单列表)_

```javascript
{
    "banned": [], // 被禁止的玩家名
    "bannedip": [], // 被禁止的IP
    "allow": [], // 玩家名白名单
    "allowip": [] // IP白名单
}
```

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [LoginProxy-v0.9.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.9.0) | 0.9.0 | 2025/04/20 03:09:08 | 37.64KB | 600 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.9.0/LoginProxy-v0.9.0.mcdr) |
| [LoginProxy-v0.8.7.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.7) | 0.8.7 | 2025/02/08 04:56:27 | 36.39KB | 207 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.7/LoginProxy-v0.8.7.mcdr) |
| [LoginProxy-v0.8.6.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.6) | 0.8.6 | 2025/02/08 03:43:45 | 36.5KB | 32 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.6/LoginProxy-v0.8.6.mcdr) |
| [LoginProxy-v0.8.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.5) | 0.8.5 | 2025/02/08 01:41:16 | 36.5KB | 30 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.5/LoginProxy-v0.8.5.mcdr) |
| [LoginProxy-v0.8.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.3) | 0.8.3 | 2025/02/07 22:18:35 | 36.11KB | 29 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.3/LoginProxy-v0.8.3.mcdr) |
| [LoginProxy-v0.8.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.2) | 0.8.2 | 2025/02/07 15:36:40 | 34.68KB | 29 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.2/LoginProxy-v0.8.2.mcdr) |
| [LoginProxy-v0.8.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.1) | 0.8.1 | 2025/02/07 14:47:26 | 34.56KB | 29 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.1/LoginProxy-v0.8.1.mcdr) |
| [LoginProxy-v0.8.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.0) | 0.8.0 | 2025/02/07 14:23:10 | 34.56KB | 30 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.0/LoginProxy-v0.8.0.mcdr) |
| [LoginProxy-v0.7.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.4) | 0.7.4 | 2025/02/06 22:31:22 | 32.91KB | 79 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.4/LoginProxy-v0.7.4.mcdr) |
| [LoginProxy-v0.7.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.3) | 0.7.3 | 2025/02/06 19:50:30 | 32.89KB | 30 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.3/LoginProxy-v0.7.3.mcdr) |
| [LoginProxy-v0.7.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.2) | 0.7.2 | 2025/02/06 19:43:46 | 32.89KB | 28 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.2/LoginProxy-v0.7.2.mcdr) |
| [LoginProxy-v0.7.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.1) | 0.7.1 | 2025/02/06 15:16:13 | 32.85KB | 27 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.1/LoginProxy-v0.7.1.mcdr) |
| [LoginProxy-v0.7.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.0) | 0.7.0 | 2025/02/06 14:44:38 | 32.92KB | 34 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.0/LoginProxy-v0.7.0.mcdr) |
| [LoginProxy-v0.6.12.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.12) | 0.6.12 | 2025/02/01 20:25:20 | 29.83KB | 38 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.12/LoginProxy-v0.6.12.mcdr) |
| [LoginProxy-v0.6.11.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.11) | 0.6.11 | 2024/08/10 07:51:11 | 29.86KB | 175 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.11/LoginProxy-v0.6.11.mcdr) |
| [LoginProxy-v0.6.10.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.10) | 0.6.10 | 2024/02/04 00:27:18 | 29.81KB | 239 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.10/LoginProxy-v0.6.10.mcdr) |
| [LoginProxy-v0.6.9.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.9) | 0.6.9 | 2024/02/04 00:20:17 | 29.82KB | 44 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.9/LoginProxy-v0.6.9.mcdr) |
| [LoginProxy-v0.6.8.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.8) | 0.6.8 | 2024/02/04 00:01:20 | 29.77KB | 41 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.8/LoginProxy-v0.6.8.mcdr) |
| [LoginProxy-v0.6.7.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.7) | 0.6.7 | 2024/02/03 23:50:11 | 29.75KB | 42 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.7/LoginProxy-v0.6.7.mcdr) |
| [LoginProxy-v0.6.6.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.6) | 0.6.6 | 2024/02/03 22:44:36 | 29.65KB | 47 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.6/LoginProxy-v0.6.6.mcdr) |
| [LoginProxy-v0.6.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.5) | 0.6.5 | 2024/02/01 15:17:25 | 29.67KB | 46 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.5/LoginProxy-v0.6.5.mcdr) |
| [LoginProxy-v0.6.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.4) | 0.6.4 | 2023/12/03 04:57:14 | 29.65KB | 85 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.4/LoginProxy-v0.6.4.mcdr) |
| [LoginProxy-v0.6.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.3) | 0.6.3 | 2023/12/03 00:23:42 | 29.62KB | 46 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.3/LoginProxy-v0.6.3.mcdr) |
| [LoginProxy-v0.6.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.2) | 0.6.2 | 2023/10/02 18:30:38 | 29.57KB | 77 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.2/LoginProxy-v0.6.2.mcdr) |
| [LoginProxy-v0.6.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.1) | 0.6.1 | 2023/06/09 04:09:34 | 29.53KB | 205 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.1/LoginProxy-v0.6.1.mcdr) |
| [LoginProxy-v0.6.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.0) | 0.6.0 | 2023/06/08 18:47:46 | 29.51KB | 46 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.0/LoginProxy-v0.6.0.mcdr) |
| [LoginProxy-v0.5.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.3) | 0.5.3 | 2023/03/04 00:14:20 | 25.14KB | 119 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.3/LoginProxy-v0.5.3.mcdr) |
| [LoginProxy-v0.5.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.2) | 0.5.2 | 2023/03/01 19:18:15 | 24.15KB | 47 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.2/LoginProxy-v0.5.2.mcdr) |
| [LoginProxy-v0.5.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.1) | 0.5.1 | 2022/12/28 01:52:08 | 23.06KB | 129 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.1/LoginProxy-v0.5.1.mcdr) |
| [LoginProxy-v0.5.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.0) | 0.5.0 | 2022/12/27 01:49:47 | 23.03KB | 64 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.0/LoginProxy-v0.5.0.mcdr) |
| [LoginProxy-v0.4.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.4) | 0.4.4 | 2022/12/24 07:25:28 | 22.74KB | 63 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.4/LoginProxy-v0.4.4.mcdr) |
| [LoginProxy-v0.4.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.3) | 0.4.3 | 2022/12/24 07:14:18 | 22.74KB | 44 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.3/LoginProxy-v0.4.3.mcdr) |
| [LoginProxy-v0.4.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.2) | 0.4.2 | 2022/12/24 05:31:31 | 22.74KB | 43 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.2/LoginProxy-v0.4.2.mcdr) |
| [LoginProxy-v0.4.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.1) | 0.4.1 | 2022/12/24 05:17:19 | 22.74KB | 43 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.1/LoginProxy-v0.4.1.mcdr) |
| [LoginProxy-v0.4.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.0) | 0.4.0 | 2022/11/25 08:00:14 | 22.72KB | 75 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.0/LoginProxy-v0.4.0.mcdr) |
| [LoginProxy-v0.3.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.5) | 0.3.5 | 2022/11/20 21:06:17 | 22.83KB | 42 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.5/LoginProxy-v0.3.5.mcdr) |
| [LoginProxy-v0.3.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.4) | 0.3.4 | 2022/11/20 20:34:13 | 22.85KB | 42 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.4/LoginProxy-v0.3.4.mcdr) |
| [LoginProxy-v0.3.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.3) | 0.3.3 | 2022/11/20 20:00:17 | 22.85KB | 41 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.3/LoginProxy-v0.3.3.mcdr) |
| [LoginProxy-v0.3.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.2) | 0.3.2 | 2022/11/20 19:02:39 | 22.73KB | 41 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.2/LoginProxy-v0.3.2.mcdr) |
| [LoginProxy-v0.3.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.1) | 0.3.1 | 2022/10/23 06:38:37 | 22.72KB | 49 | [下载](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.1/LoginProxy-v0.3.1.mcdr) |

