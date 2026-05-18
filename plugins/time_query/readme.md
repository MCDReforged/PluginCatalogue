**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## time_query

### Basic Information

- Plugin ID: `time_query`
- Plugin Name: TimeQuery
- Version: 0.1.2
  - Metadata version: 0.1.2
  - Release version: 0.1.2
- Total downloads: 239
- Authors: [Mooling0602](https://github.com/Mooling0602)
- Repository: https://github.com/Mooling0602/TimeQuery-MCDR
- Repository plugin page: https://github.com/Mooling0602/TimeQuery-MCDR/tree/main
- Labels: [`Information`](/labels/information/readme.md)
- Description: Query the time in real time and in the game.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.1 |
| [python](/plugins/python/readme.md) | \>=3.12 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.1 |
| [arrow](https://pypi.org/project/arrow) |  |

```
pip install "mcdreforged>=2.14.1" arrow
```

### Introduction

# TimeQuery-MCDR
A MCDR(full name "MCDReforged") plugin use to query the time in real and game.

README will written only by zh_CN, you can translate it with AI tools.

> Since Minecraft 26.1, the usage of `/time` has changed, and newer version of this plugin will support it.

# 用途
查询现实和游戏内的时间，以24小时制显示。

> 自Minecraft 26.1以后，`/time`的用法发生了改变，插件的新版本将支持这一改变。

# 配置
插件主配置在"config/time_query/config.yml"。

如果需要修改插件翻译，请关闭`i18n_lock`项。

# 用法
`!!time` - 显示插件命令用法

`!!time real` - 查询现实的时间，显示年月日、星期几、具体时间（精确到秒）

`!!time game` - 查询游戏内的时间，对应现实24小时制精确到分（需要Rcon支持，若无法使用Rcon环境且游戏版本在26.1以前，可以尝试插件仓库中的Daytime插件）

# TODO
- [ ] 支持在actionbar（物品栏上方）持续显示时间信息

# 指令冲突问题
若发生命令冲突的情况，可以修改配置中的`command.enable_namespace`项，插件会将原先的`!!time`命令注册为`!!time_query:time`以规避冲突

同时推荐安装[Command Aliases](https://mcdreforged.com/plugin/command_aliases)插件为插件命令设置别名，方便使用。

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [TimeQuery-v0.1.2.mcdr](https://github.com/Mooling0602/TimeQuery-MCDR/releases/tag/0.1.2) | 0.1.2 | 2026/04/13 07:42:43 | 6.86KB | 23 | [Download](https://github.com/Mooling0602/TimeQuery-MCDR/releases/download/0.1.2/TimeQuery-v0.1.2.mcdr) |
| [TimeQuery-v0.1.1.mcdr](https://github.com/Mooling0602/TimeQuery-MCDR/releases/tag/0.1.1) | 0.1.1 | 2026/04/09 18:46:34 | 5.43KB | 20 | [Download](https://github.com/Mooling0602/TimeQuery-MCDR/releases/download/0.1.1/TimeQuery-v0.1.1.mcdr) |
| [TimeQuery-v0.1.0.mcdr](https://github.com/Mooling0602/TimeQuery-MCDR/releases/tag/0.1.0) | 0.1.0 | 2026/04/04 11:54:05 | 5.43KB | 21 | [Download](https://github.com/Mooling0602/TimeQuery-MCDR/releases/download/0.1.0/TimeQuery-v0.1.0.mcdr) |
| [TimeQuery-v0.0.9.mcdr](https://github.com/Mooling0602/TimeQuery-MCDR/releases/tag/0.0.9) | 0.0.9 | 2026/04/04 07:33:31 | 4.42KB | 17 | [Download](https://github.com/Mooling0602/TimeQuery-MCDR/releases/download/0.0.9/TimeQuery-v0.0.9.mcdr) |
| [TimeQuery-v0.0.4.mcdr](https://github.com/Mooling0602/TimeQuery-MCDR/releases/tag/0.0.4) | 0.0.4 | 2024/09/20 13:06:00 | 14.47KB | 158 | [Download](https://github.com/Mooling0602/TimeQuery-MCDR/releases/download/0.0.4/TimeQuery-v0.0.4.mcdr) |

