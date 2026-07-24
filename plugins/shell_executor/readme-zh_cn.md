[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## shell_executor

### 基本信息

- 插件 ID: `shell_executor`
- 插件名: ShellExecutor
- 版本: 0.0.1
  - 元数据版本: 0.0.1
  - 发布版本: 0.0.1
- 总下载量: 17
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/ShellExecutor-MCDR
- 仓库插件页: https://github.com/Mooling0602/ShellExecutor-MCDR/tree/main/src
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 快速的在 MCDR 控制台或游戏内执行 shell 命令。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.1 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

- 中文（简体）
- [English](https://github.com/Mooling0602/ShellExecutor-MCDR/tree/main/src/../README.md)

# ShellExecutor-MCDR
在 MCDR 控制台或游戏中快速执行 shell 命令。
> 需要 MCDR 权限等级达到 4 才能使用。

## 用法
使用 `!!shell <command>` 在默认 shell 环境中执行命令。
> 包含空格的命令应该用 `"` 引起来，例如：`!!shell "ls server/mods/"`

`!!shell` 的默认别名是 `$`，安装 [Command Aliases](https://mcdreforged.com/plugin/command_aliases) 来激活此功能（命令别名）。

## 注意
- 目前支持 Linux shell，插件可能在其他操作系统上无法正常工作。
> 欢迎在 Windows 上测试，如果发现任何问题，请随时提交 issue。

- 不要在 ShellExecutor 中执行 TUI 二进制文件，这可能会打断 MCDR 控制台的渲染，甚至导致冻结。我没有解决这个问题的办法，如果你有任何解决方案，请提交 issue 或 pull request，谢谢。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ShellExecutor-v0.0.1.mcdr](https://github.com/Mooling0602/ShellExecutor-MCDR/releases/tag/0.0.1) | 0.0.1 | 2026/05/15 12:08:44 | 4.65KB | 17 | [下载](https://github.com/Mooling0602/ShellExecutor-MCDR/releases/download/0.0.1/ShellExecutor-v0.0.1.mcdr) |

