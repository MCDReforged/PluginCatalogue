**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## shell_executor

### Basic Information

- Plugin ID: `shell_executor`
- Plugin Name: ShellExecutor
- Version: 0.0.1
  - Metadata version: 0.0.1
  - Release version: 0.0.1
- Total downloads: 17
- Authors: [Mooling0602](https://github.com/Mooling0602)
- Repository: https://github.com/Mooling0602/ShellExecutor-MCDR
- Repository plugin page: https://github.com/Mooling0602/ShellExecutor-MCDR/tree/main/src
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Quickly execute shell commands in MCDR console or in the game.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.1 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

- English
- [中文（简体）](https://github.com/Mooling0602/ShellExecutor-MCDR/tree/main/src/../README_zh_CN.md)

# ShellExecutor-MCDR
Quickly execute shell commands in MCDR console or in the game.
> Require MCDR permission level reach 4 to use.

## Usage
Use `!!shell <command>` to execute a command in default shell environment.
> Commands include spaces should be quoted by `"`, like this: `!!shell "ls server/mods/"`

Default alias for `!!shell` is `$`, install [Command Aliases](https://mcdreforged.com/plugin/command_aliases) to activate this feature.

## NOTE
- Support Linux shell at present, the plugin may not work properly on other operating systems.
> Test on Windows is welcome, feel free to submit an issue if you find any problem.

- Do not execute TUI binaries in ShellExecutor, it may break rendering the MCDR console and even freezes it. I've no idea to solve this problem at present, if you have any solution, please submit an issue or a pull request, thanks.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ShellExecutor-v0.0.1.mcdr](https://github.com/Mooling0602/ShellExecutor-MCDR/releases/tag/0.0.1) | 0.0.1 | 2026/05/15 12:08:44 | 4.65KB | 17 | [Download](https://github.com/Mooling0602/ShellExecutor-MCDR/releases/download/0.0.1/ShellExecutor-v0.0.1.mcdr) |

