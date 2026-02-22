**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## loginproxy

### Basic Information

- Plugin ID: `loginproxy`
- Plugin Name: LoginProxy
- Version: 0.9.0
  - Metadata version: 0.9.0
  - Release version: 0.9.0
- Total downloads: 3157
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/login_proxy_mcdr
- Repository plugin page: https://github.com/kmcsr/login_proxy_mcdr/tree/master
- Labels: [`Management`](/labels/management/readme.md), [`API`](/labels/api/readme.md)
- Description: A Minecraft login proxy plugin

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.3.0 |
| [python](/plugins/python/readme.md) | ^3.12 |
| [kpi](/plugins/kpi/readme.md) | ~1.5.1 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [pycryptodome](https://pypi.org/project/pycryptodome) | \>=3.21.0 |

```
pip install "pycryptodome>=3.21.0"
```

### Introduction


- English
- [中文](https://github.com/kmcsr/login_proxy_mcdr/tree/master/README_zh.MD)

# Login Proxy

*If it's useful, please give a star :)*

Similar project: <https://github.com/kmcsr/go-liter>

## Feature

- Use **reverse proxy** to proxy minecraft server **login package**, *clients will never bypassing the whitelist*
- The best offline whitelist plugin

## Current supported Minecraft version

`1.8 ~ 1.21.4`

## Dependencies

| ID                                                             | Release Link                                           | Is Optional |
| -------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| [`kpi`](https://github.com/kmcsr/kpi_mcdr)                     | <https://github.com/kmcsr/kpi_mcdr/releases>           | required    |
| [`packet_parser`](https://github.com/kmcsr/packet_parser_mcdr) | <https://github.com/kmcsr/packet_parser_mcdr/releases> | optional    |

## How to configure it

1. (TODO)

## Config files

#### loginproxy/config.json _(the mainly config file)_

```javascript
{
    "minimum_permission_level": { // Command permissions
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
        "removeip": 3,
    },
    "proxy_addr": { // The address of proxy server, please never make it as same as the minecraft server address
        "ip": "", // IPv4 ip for the proxy server, set it `null` to disable ipv4
        "port": 25565, // The port for the IPv4 IP above
        "ipv6": "::", // IPv6 ip for the proxy server, set it `null` to disable IPv6
        "ipv6_port": 25565, // The port for the IPv6 IP above
    },
    "enable_whitelist": false, // enable/disable whitelist
    "enable_ip_whitelist": false, // enable/disable ip whitelist
    "whitelist_level": 3, // Ignore whitelist when player have permission above or equal this
    "kick_cmd": "kick {name} {reason}", // Kick command to kick online player out; leave it empty for force disconnect the player
    "messages": {
        "banned.name": "Your account has been banned", // Show when player's name has been banned
        "banned.ip": "Your ip has been banned", // Show when client's IP has been banned
        "whitelist.name": "Your account not in the whitelist", // Show when player's name not in the whitelist
        "whitelist.ip": "Your ip not in the whitelist" // Show when client's IP not in the whitelist
    },
    "allow_transfer": true, // whether or not allow player transfer from another server
    "enable_packet_proxy": false, // whether or not parse network packets. Must install packet_parser first. Required for most plugins that depends on loginproxy
    "online_mode": false, // same as online-mode in vanilla server.properties
    "identify_by_online_uuid": true, // use uuid instead of player name to identify a player (used in blacklist/whitelist)
    "uuid_cache_ttl": 3600 // uuid request cache time in seconds
}
```

#### loginproxy/list.json _(blacklist & whitelist file)_

```javascript
{
    "banned": [], // Banned players
    "bannedip": [], // Banned IPs
    "allow": [], // Whitelist of players
    "allowip": [] // Whitelist of IPs
}
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [LoginProxy-v0.9.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.9.0) | 0.9.0 | 2025/04/20 03:09:08 | 37.64KB | 600 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.9.0/LoginProxy-v0.9.0.mcdr) |
| [LoginProxy-v0.8.7.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.7) | 0.8.7 | 2025/02/08 04:56:27 | 36.39KB | 207 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.7/LoginProxy-v0.8.7.mcdr) |
| [LoginProxy-v0.8.6.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.6) | 0.8.6 | 2025/02/08 03:43:45 | 36.5KB | 32 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.6/LoginProxy-v0.8.6.mcdr) |
| [LoginProxy-v0.8.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.5) | 0.8.5 | 2025/02/08 01:41:16 | 36.5KB | 30 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.5/LoginProxy-v0.8.5.mcdr) |
| [LoginProxy-v0.8.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.3) | 0.8.3 | 2025/02/07 22:18:35 | 36.11KB | 29 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.3/LoginProxy-v0.8.3.mcdr) |
| [LoginProxy-v0.8.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.2) | 0.8.2 | 2025/02/07 15:36:40 | 34.68KB | 29 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.2/LoginProxy-v0.8.2.mcdr) |
| [LoginProxy-v0.8.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.1) | 0.8.1 | 2025/02/07 14:47:26 | 34.56KB | 29 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.1/LoginProxy-v0.8.1.mcdr) |
| [LoginProxy-v0.8.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.8.0) | 0.8.0 | 2025/02/07 14:23:10 | 34.56KB | 30 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.8.0/LoginProxy-v0.8.0.mcdr) |
| [LoginProxy-v0.7.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.4) | 0.7.4 | 2025/02/06 22:31:22 | 32.91KB | 79 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.4/LoginProxy-v0.7.4.mcdr) |
| [LoginProxy-v0.7.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.3) | 0.7.3 | 2025/02/06 19:50:30 | 32.89KB | 30 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.3/LoginProxy-v0.7.3.mcdr) |
| [LoginProxy-v0.7.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.2) | 0.7.2 | 2025/02/06 19:43:46 | 32.89KB | 28 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.2/LoginProxy-v0.7.2.mcdr) |
| [LoginProxy-v0.7.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.1) | 0.7.1 | 2025/02/06 15:16:13 | 32.85KB | 27 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.1/LoginProxy-v0.7.1.mcdr) |
| [LoginProxy-v0.7.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.7.0) | 0.7.0 | 2025/02/06 14:44:38 | 32.92KB | 34 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.7.0/LoginProxy-v0.7.0.mcdr) |
| [LoginProxy-v0.6.12.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.12) | 0.6.12 | 2025/02/01 20:25:20 | 29.83KB | 38 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.12/LoginProxy-v0.6.12.mcdr) |
| [LoginProxy-v0.6.11.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.11) | 0.6.11 | 2024/08/10 07:51:11 | 29.86KB | 175 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.11/LoginProxy-v0.6.11.mcdr) |
| [LoginProxy-v0.6.10.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.10) | 0.6.10 | 2024/02/04 00:27:18 | 29.81KB | 239 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.10/LoginProxy-v0.6.10.mcdr) |
| [LoginProxy-v0.6.9.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.9) | 0.6.9 | 2024/02/04 00:20:17 | 29.82KB | 44 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.9/LoginProxy-v0.6.9.mcdr) |
| [LoginProxy-v0.6.8.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.8) | 0.6.8 | 2024/02/04 00:01:20 | 29.77KB | 41 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.8/LoginProxy-v0.6.8.mcdr) |
| [LoginProxy-v0.6.7.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.7) | 0.6.7 | 2024/02/03 23:50:11 | 29.75KB | 42 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.7/LoginProxy-v0.6.7.mcdr) |
| [LoginProxy-v0.6.6.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.6) | 0.6.6 | 2024/02/03 22:44:36 | 29.65KB | 47 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.6/LoginProxy-v0.6.6.mcdr) |
| [LoginProxy-v0.6.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.5) | 0.6.5 | 2024/02/01 15:17:25 | 29.67KB | 46 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.5/LoginProxy-v0.6.5.mcdr) |
| [LoginProxy-v0.6.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.4) | 0.6.4 | 2023/12/03 04:57:14 | 29.65KB | 85 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.4/LoginProxy-v0.6.4.mcdr) |
| [LoginProxy-v0.6.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.3) | 0.6.3 | 2023/12/03 00:23:42 | 29.62KB | 46 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.3/LoginProxy-v0.6.3.mcdr) |
| [LoginProxy-v0.6.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.2) | 0.6.2 | 2023/10/02 18:30:38 | 29.57KB | 77 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.2/LoginProxy-v0.6.2.mcdr) |
| [LoginProxy-v0.6.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.1) | 0.6.1 | 2023/06/09 04:09:34 | 29.53KB | 205 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.1/LoginProxy-v0.6.1.mcdr) |
| [LoginProxy-v0.6.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.0) | 0.6.0 | 2023/06/08 18:47:46 | 29.51KB | 46 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.0/LoginProxy-v0.6.0.mcdr) |
| [LoginProxy-v0.5.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.3) | 0.5.3 | 2023/03/04 00:14:20 | 25.14KB | 119 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.3/LoginProxy-v0.5.3.mcdr) |
| [LoginProxy-v0.5.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.2) | 0.5.2 | 2023/03/01 19:18:15 | 24.15KB | 47 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.2/LoginProxy-v0.5.2.mcdr) |
| [LoginProxy-v0.5.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.1) | 0.5.1 | 2022/12/28 01:52:08 | 23.06KB | 129 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.1/LoginProxy-v0.5.1.mcdr) |
| [LoginProxy-v0.5.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.0) | 0.5.0 | 2022/12/27 01:49:47 | 23.03KB | 64 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.0/LoginProxy-v0.5.0.mcdr) |
| [LoginProxy-v0.4.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.4) | 0.4.4 | 2022/12/24 07:25:28 | 22.74KB | 63 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.4/LoginProxy-v0.4.4.mcdr) |
| [LoginProxy-v0.4.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.3) | 0.4.3 | 2022/12/24 07:14:18 | 22.74KB | 44 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.3/LoginProxy-v0.4.3.mcdr) |
| [LoginProxy-v0.4.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.2) | 0.4.2 | 2022/12/24 05:31:31 | 22.74KB | 43 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.2/LoginProxy-v0.4.2.mcdr) |
| [LoginProxy-v0.4.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.1) | 0.4.1 | 2022/12/24 05:17:19 | 22.74KB | 43 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.1/LoginProxy-v0.4.1.mcdr) |
| [LoginProxy-v0.4.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.0) | 0.4.0 | 2022/11/25 08:00:14 | 22.72KB | 75 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.0/LoginProxy-v0.4.0.mcdr) |
| [LoginProxy-v0.3.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.5) | 0.3.5 | 2022/11/20 21:06:17 | 22.83KB | 42 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.5/LoginProxy-v0.3.5.mcdr) |
| [LoginProxy-v0.3.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.4) | 0.3.4 | 2022/11/20 20:34:13 | 22.85KB | 42 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.4/LoginProxy-v0.3.4.mcdr) |
| [LoginProxy-v0.3.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.3) | 0.3.3 | 2022/11/20 20:00:17 | 22.85KB | 41 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.3/LoginProxy-v0.3.3.mcdr) |
| [LoginProxy-v0.3.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.2) | 0.3.2 | 2022/11/20 19:02:39 | 22.73KB | 41 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.2/LoginProxy-v0.3.2.mcdr) |
| [LoginProxy-v0.3.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.1) | 0.3.1 | 2022/10/23 06:38:37 | 22.72KB | 49 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.1/LoginProxy-v0.3.1.mcdr) |

