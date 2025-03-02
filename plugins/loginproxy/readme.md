**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## loginproxy

### Basic Information

- Plugin ID: `loginproxy`
- Version: *Data fetching failed*
- Total downloads: N/A
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/login_proxy_mcdr
- Repository plugin page: https://github.com/kmcsr/login_proxy_mcdr/tree/master
- Labels: [`Management`](/labels/management/readme.md), [`API`](/labels/api/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

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

*Data fetching failed*

