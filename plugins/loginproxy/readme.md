**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## loginproxy

### Basic Information

- Plugin ID: `loginproxy`
- Plugin Name: LoginProxy
- Version: 0.6.11
  - Metadata version: 0.6.11
  - Release version: 0.6.11
- Total downloads: 1175
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/login_proxy_mcdr
- Repository plugin page: https://github.com/kmcsr/login_proxy_mcdr/tree/master
- Labels: [`Management`](/labels/management/readme.md), [`API`](/labels/api/readme.md)
- Description: A Minecraft login proxy Plugin

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.3.0 |
| [kpi](/plugins/kpi/readme.md) | ~1.4.6 |

### Requirements

| Python package | Requirement |
| --- | --- |

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

`1.8.x ~ 1.20.2`

## Dependencies

| ID                                       | Release Link                                 |
| ---------------------------------------- | -------------------------------------------- |
| [kpi](https://github.com/kmcsr/kpi_mcdr) | <https://github.com/kmcsr/kpi_mcdr/releases> |

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
    }
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
| [LoginProxy-v0.6.11.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.11) | 0.6.11 | 2024/08/10 07:51:11 | 29.86KB | 60 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.11/LoginProxy-v0.6.11.mcdr) |
| [LoginProxy-v0.6.10.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.10) | 0.6.10 | 2024/02/04 00:27:18 | 29.81KB | 210 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.10/LoginProxy-v0.6.10.mcdr) |
| [LoginProxy-v0.6.9.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.9) | 0.6.9 | 2024/02/04 00:20:17 | 29.82KB | 18 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.9/LoginProxy-v0.6.9.mcdr) |
| [LoginProxy-v0.6.8.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.8) | 0.6.8 | 2024/02/04 00:01:20 | 29.77KB | 15 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.8/LoginProxy-v0.6.8.mcdr) |
| [LoginProxy-v0.6.7.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.7) | 0.6.7 | 2024/02/03 23:50:11 | 29.75KB | 15 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.7/LoginProxy-v0.6.7.mcdr) |
| [LoginProxy-v0.6.6.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.6) | 0.6.6 | 2024/02/03 22:44:36 | 29.65KB | 22 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.6/LoginProxy-v0.6.6.mcdr) |
| [LoginProxy-v0.6.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.5) | 0.6.5 | 2024/02/01 15:17:25 | 29.67KB | 18 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.5/LoginProxy-v0.6.5.mcdr) |
| [LoginProxy-v0.6.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.4) | 0.6.4 | 2023/12/03 04:57:14 | 29.65KB | 60 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.4/LoginProxy-v0.6.4.mcdr) |
| [LoginProxy-v0.6.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.3) | 0.6.3 | 2023/12/03 00:23:42 | 29.62KB | 18 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.3/LoginProxy-v0.6.3.mcdr) |
| [LoginProxy-v0.6.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.2) | 0.6.2 | 2023/10/02 18:30:38 | 29.57KB | 50 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.2/LoginProxy-v0.6.2.mcdr) |
| [LoginProxy-v0.6.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.1) | 0.6.1 | 2023/06/09 04:09:34 | 29.53KB | 180 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.1/LoginProxy-v0.6.1.mcdr) |
| [LoginProxy-v0.6.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.6.0) | 0.6.0 | 2023/06/08 18:47:46 | 29.51KB | 21 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.6.0/LoginProxy-v0.6.0.mcdr) |
| [LoginProxy-v0.5.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.3) | 0.5.3 | 2023/03/04 00:14:20 | 25.14KB | 90 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.3/LoginProxy-v0.5.3.mcdr) |
| [LoginProxy-v0.5.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.2) | 0.5.2 | 2023/03/01 19:18:15 | 24.15KB | 22 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.2/LoginProxy-v0.5.2.mcdr) |
| [LoginProxy-v0.5.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.1) | 0.5.1 | 2022/12/28 01:52:08 | 23.06KB | 102 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.1/LoginProxy-v0.5.1.mcdr) |
| [LoginProxy-v0.5.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.5.0) | 0.5.0 | 2022/12/27 01:49:47 | 23.03KB | 36 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.5.0/LoginProxy-v0.5.0.mcdr) |
| [LoginProxy-v0.4.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.4) | 0.4.4 | 2022/12/24 07:25:28 | 22.74KB | 37 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.4/LoginProxy-v0.4.4.mcdr) |
| [LoginProxy-v0.4.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.3) | 0.4.3 | 2022/12/24 07:14:18 | 22.74KB | 19 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.3/LoginProxy-v0.4.3.mcdr) |
| [LoginProxy-v0.4.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.2) | 0.4.2 | 2022/12/24 05:31:31 | 22.74KB | 18 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.2/LoginProxy-v0.4.2.mcdr) |
| [LoginProxy-v0.4.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.1) | 0.4.1 | 2022/12/24 05:17:19 | 22.74KB | 17 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.1/LoginProxy-v0.4.1.mcdr) |
| [LoginProxy-v0.4.0.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.4.0) | 0.4.0 | 2022/11/25 08:00:14 | 22.72KB | 52 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.4.0/LoginProxy-v0.4.0.mcdr) |
| [LoginProxy-v0.3.5.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.5) | 0.3.5 | 2022/11/20 21:06:17 | 22.83KB | 18 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.5/LoginProxy-v0.3.5.mcdr) |
| [LoginProxy-v0.3.4.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.4) | 0.3.4 | 2022/11/20 20:34:13 | 22.85KB | 18 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.4/LoginProxy-v0.3.4.mcdr) |
| [LoginProxy-v0.3.3.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.3) | 0.3.3 | 2022/11/20 20:00:17 | 22.85KB | 17 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.3/LoginProxy-v0.3.3.mcdr) |
| [LoginProxy-v0.3.2.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.2) | 0.3.2 | 2022/11/20 19:02:39 | 22.73KB | 17 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.2/LoginProxy-v0.3.2.mcdr) |
| [LoginProxy-v0.3.1.mcdr](https://github.com/kmcsr/login_proxy_mcdr/releases/tag/v0.3.1) | 0.3.1 | 2022/10/23 06:38:37 | 22.72KB | 25 | [Download](https://github.com/kmcsr/login_proxy_mcdr/releases/download/v0.3.1/LoginProxy-v0.3.1.mcdr) |

