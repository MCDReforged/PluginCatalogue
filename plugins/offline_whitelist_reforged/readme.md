**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## offline_whitelist_reforged

### Basic Information

- Plugin ID: `offline_whitelist_reforged`
- Plugin Name: OfflineWhitelistReforged
- Version: 1.1.0
  - Metadata version: 1.1.0
  - Release version: 1.1.0
- Total downloads: 345
- Authors: [Aimerny](https://github.com/Aimerny)
- Repository: https://github.com/Aimerny/OfflineWhitelistReforged
- Repository plugin page: https://github.com/Aimerny/OfflineWhitelistReforged/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: A whitelist plugin in offline server

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.6.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.6.0 |

```
pip install "mcdreforged>=2.6.0"
```

### Introduction

# OfflineWhiteListReforged

简单小巧的离线服白名单管理插件

## 使用方式
```
!!wr help - 显示帮助消息
!!wr list - 显示全部玩家的白名单
!!wr add <player> - 为<player>添加白名单
!!wr remove <player> - 移除<player>的白名单
!!wr on - 打开白名单
!!wr off - 关闭白名单
```

## 权限要求

使用MCDR的权限系统,权限要求由配置文件配置,默认如下
```json5
{
    "perms": {
        "on": 4, // owner
        "off": 4, // owner
        "list": 2, // helper
        "add": 3, // admin
        "remove": 3 //admin
    }
}
```
`help`: 无权限要求

`list`: helper及以上

`add`,`remove`: admin及以上

`off, on`: 仅owner(控制台权限等同于owner)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [OfflineWhitelistReforged-v1.1.0.mcdr](https://github.com/Aimerny/OfflineWhitelistReforged/releases/tag/v1.1.0) | 1.1.0 | 2024/08/02 18:28:34 | 5.16KB | 14 | [Download](https://github.com/Aimerny/OfflineWhitelistReforged/releases/download/v1.1.0/OfflineWhitelistReforged-v1.1.0.mcdr) |
| [OfflineWhitelistReforged-v1.0.0.mcdr](https://github.com/Aimerny/OfflineWhitelistReforged/releases/tag/v1.0.0) | 1.0.0 | 2023/06/15 09:30:39 | 4.31KB | 331 | [Download](https://github.com/Aimerny/OfflineWhitelistReforged/releases/download/v1.0.0/OfflineWhitelistReforged-v1.0.0.mcdr) |

