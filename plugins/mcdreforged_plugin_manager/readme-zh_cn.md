[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mcdreforged_plugin_manager

### 基本信息

- 插件 ID: `mcdreforged_plugin_manager`
- 插件名: MCDReforged Plugin Manager
- 版本: 2.2.0
  - 元数据版本: 2.2.0
  - 发布版本: 2.2.0
- 总下载量: 2347
- 作者: [Ivan1F](https://github.com/Ivan-1F)
- 仓库: https://github.com/Ivan-1F/MCDReforgedPluginManager
- 仓库插件页: https://github.com/Ivan-1F/MCDReforgedPluginManager/tree/master
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 轻松管理你的 MCDReforged 插件

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.0.0 |
| [requests](https://pypi.org/project/requests) |  |

```
pip install "mcdreforged>=2.0.0" requests
```

### 介绍

MCDReforgedPluginManager
-----

> [!TIP]
> Deprecated, use [MCDR's built-in plugin installer](https://docs.mcdreforged.com/en/latest/command/mcdr.html#plugin-catalogue-access) instead

**English** | [中文](https://github.com/Ivan-1F/MCDReforgedPluginManager/tree/master/./README_cn.md)

> Manage your mcdreforged plugins with ease

MCDReforgedPluginManager (short for `mpm`) is a MCDReforged plugin manager based on [PluginCatalogue](https://github.com/MCDReforged/PluginCatalogue)

MCDReforgedPluginManager fetch plugin metadata from [PluginCatalogue](https://github.com/MCDReforged/PluginCatalogue) and update automatically at regular intervals

![overview](https://raw.githubusercontent.com/Ivan-1F/MCDReforgedPluginManager/master/./screenshots/en_us.gif)

## Features

- Dependency checking
- Update checking
- Plugin installation & uninstallation
- Plugin upgrading
- Plugin searching

## Requirements

[MCDReforged](https://github.com/Fallen-Breath/MCDReforged) requirement: `>=2.0.0`

Python package requirements: See [requirements.txt](https://github.com/Ivan-1F/MCDReforgedPluginManager/blob/master/requirements.txt)

## Configuration

The configuration file is `config/mcdreforged_plugin_manager/config.yml`

The commented default config file will be generated when mpm is loaded for the first time:

```yaml
# Configure file for MCDReforgedPluginManager


# The minimum permission level to use MPM commands
# 使用 MCDReforgedPluginManager 指令的最低权限
permission: 4

# The source of plugin catalogue to fetch data, should be the url to download the whole meta branch
# 插件仓库数据源，应是下载整个 meta 分支的链接
source: https://github.com/MCDReforged/PluginCatalogue/archive/refs/heads/meta.zip

# The timeout for network requests
# 网络请求的超时时间
timeout: 5

# The time interval between each cache (unit: minute)
# 定时更新插件索引的时间间隔（单位：分钟）
cache_interval: 2

# If set to true, the plugin will check plugin updates after each scheduled cache
# 若设为 true，插件将在每次定时更新插件索引后自动检查更新
check_update: true

# The path to install the plugin, should be one of the value of 'plugin_directories' of the MCDR config
# 安装插件的位置，应是 MCDR 配置中的 'plugin_directories' 中的一个
install_path: plugins

# Proxy addresses, both http and https is optional
# 代理地址，http 与 https 都是可选的
proxy:
  http:
  https:
```

Follow the comments and modify the config, use `!!MCDR plg reload mcdreforged_plugin_manager` to reload the config

## Commands

- `!!mpm`: Display MPM help message
- `!!mpm list [labels]`: List all the plugins.
  - If labels is specified, only plugins with specified labels will be displayed
  - `labels` can be a single label or multiple labels split by `,`. Accepted labels: `information`, `tool`, `management`, `api`
- `!!mpm search <query>`: Search plugins based on the keyword
- `!!mpm info <plugin_id>`: Show detailed information of a plugin
- `!!mpm install <plugin_ids>`: Install plugins, as well plugin dependencies and required python packages
- `!!mpm uninstall <plugin_ids>`: Uninstall plugins
- `!!mpm upgrade <plugin_ids>`: Upgrade plugins to the latest version
- `!!mpm confirm`: Confirm the operation
- `!!mpm checkupdate`: Manually check update for all installed plugins

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MCDReforgedPluginManager-v2.2.0.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v2.2.0) | 2.2.0 | 2024/07/01 05:36:50 | 22.81KB | 391 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v2.2.0/MCDReforgedPluginManager-v2.2.0.mcdr) |
| [MCDReforgedPluginManager-v2.1.1.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v2.1.1) | 2.1.1 | 2024/06/23 09:29:28 | 22.62KB | 84 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v2.1.1/MCDReforgedPluginManager-v2.1.1.mcdr) |
| [MCDReforgedPluginManager-v2.1.0.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v2.1.0) | 2.1.0 | 2024/06/18 12:28:23 | 22.62KB | 69 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v2.1.0/MCDReforgedPluginManager-v2.1.0.mcdr) |
| [MCDReforgedPluginManager-v2.0.0.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v2.0.0) | 2.0.0 | 2023/04/14 16:46:28 | 22.64KB | 669 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v2.0.0/MCDReforgedPluginManager-v2.0.0.mcdr) |
| [MCDReforgedPluginManager-v1.3.3.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.3.3) | 1.3.3 | 2023/04/02 14:32:45 | 21.79KB | 91 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.3.3/MCDReforgedPluginManager-v1.3.3.mcdr) |
| [MCDReforgedPluginManager-v1.3.2.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.3.2) | 1.3.2 | 2023/02/20 13:52:39 | 21.6KB | 170 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.3.2/MCDReforgedPluginManager-v1.3.2.mcdr) |
| [MCDReforgedPluginManager-v1.3.1.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.3.1) | 1.3.1 | 2022/11/30 08:48:02 | 21.54KB | 282 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.3.1/MCDReforgedPluginManager-v1.3.1.mcdr) |
| [MCDReforgedPluginManager-v1.3.0.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.3.0) | 1.3.0 | 2022/11/22 15:10:19 | 21.45KB | 125 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.3.0/MCDReforgedPluginManager-v1.3.0.mcdr) |
| [MCDReforgedPluginManager-v1.2.1.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.2.1) | 1.2.1 | 2022/07/27 06:28:27 | 21.3KB | 233 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.2.1/MCDReforgedPluginManager-v1.2.1.mcdr) |
| [MCDReforgedPluginManager-v1.2.0.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.2.0) | 1.2.0 | 2022/04/23 08:20:17 | 21.3KB | 109 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.2.0/MCDReforgedPluginManager-v1.2.0.mcdr) |
| [MCDReforgedPluginManager-v1.1.1.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.1.1) | 1.1.1 | 2022/04/19 03:49:16 | 21.05KB | 41 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.1.1/MCDReforgedPluginManager-v1.1.1.mcdr) |
| [MCDReforgedPluginManager-v1.1.0.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.1.0) | 1.1.0 | 2022/04/19 03:43:49 | 20.95KB | 39 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.1.0/MCDReforgedPluginManager-v1.1.0.mcdr) |
| [MCDReforgedPluginManager-v1.0.0.mcdr](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/tag/v1.0.0) | 1.0.0 | 2022/04/17 08:39:08 | 20.89KB | 44 | [下载](https://github.com/Ivan-1F/MCDReforgedPluginManager/releases/download/v1.0.0/MCDReforgedPluginManager-v1.0.0.mcdr) |

