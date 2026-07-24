**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## pip_installer

### Basic Information

- Plugin ID: `pip_installer`
- Version: *Data fetching failed*
- Total downloads: 335
- Authors: [Mooling0602](https://github.com/Mooling0602)
- Repository: https://github.com/Mooling0602/PiPInstaller-MCDR
- Repository plugin page: https://github.com/Mooling0602/PiPInstaller-MCDR/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

### Introduction

# PiPInstaller-MCDR

为面板服解决Python依赖安装问题！

> About I18n: there's no translation plans at present.
> 
> PRs for translation are welcome.

## 用法

**注意：使用前通过插件报错和使用文档等信息，确认你需要额外安装的Python依赖的PyPI包名！**

**对于较为复杂需要较长安装时间的Python包，你应该另开终端/控制台/Shell手动安装和管理会话！**

在MCDR的控制台上使用`!!pipi <包名（可限定版本）>`或`!!pip install <包名（可限定版本）>`从PyPI安装所需的Python依赖。使用空格分隔多个包名。
> 目前不支持在游戏客户端中执行这些指令，如果你这么做，插件将提示请在控制台上执行。

### 安装过程控制

由于插件在v0.3.0进行了一次底层重构，命令的功能和用法得到极大的拓展和变更，故现在需要详细参考[插件使用文档](https://github.com/Mooling0602/PiPInstaller-MCDR/tree/main/USAGE.md)。

你也可以直接在 MCDR 控制台中执行 `!!pipi help` 查看帮助页面。

## 声明（插件使用协议）

- 此插件的维护者有权根据开发进展、开源协议、MCDR 功能变化等因素，随时更新此部分内容，**使用此插件即视为你同意这些内容及其更新，因违反插件使用协议而造成的任何后果，此插件的维护者及MCDReforged的开发者不承担任何责任。**。

> 你可以在 Git 提交中查看历史版本。

- **MCDReforged的开发者没有计划提供类似直接补全安装插件缺失的PyPI依赖的功能（内置的插件管理器已处理的足够完善），因此不要向他们发出于此相关的任何功能请求。**

- **用户通过远程地址安装的未知来源的插件包，需自行确认安全性并自负风险，此插件的维护者和MCDReforged的开发者不对此承担任何责任。第三方插件包下载后，需要按照PiPInstaller的提示使用MCDR的内建命令自行加载，遇到问题请先向该插件的开发者反馈。**

- **若在使用插件的命令时遇到问题，用户可在此仓库发起Issues进行反馈；若在MCDR外使用变相解决的办法，则用户需要自行确认MCDR的命令是否在你的操作环境中可用，并且用户应该知道这种做法是不受推荐的，请不要因为在使用此方法遇到问题时进行任何反馈。**

- **用户应该详细阅读这篇[MCDR 安装文档](https://docs.mcdreforged.com/zh-cn/latest/quick_start/install.html#)，构建完整的Python环境管理体系，这才是解决Python依赖问题的根本所在**

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [PiPInstaller-v0.3.0-rc4.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.3.0-rc4) | 0.3.0-rc4 | 2026/07/01 10:22:13 | 8.67KB | 12 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.3.0-rc4/PiPInstaller-v0.3.0-rc4.mcdr) |
| [PiPInstaller-v0.3.0-rc3.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.3.0-rc3) | 0.3.0-rc3 | 2026/07/01 04:33:38 | 8.43KB | 4 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.3.0-rc3/PiPInstaller-v0.3.0-rc3.mcdr) |
| [PiPInstaller-v0.3.0.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.3.0) | 0.3.0 | 2026/07/01 13:05:25 | 8.88KB | 15 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.3.0/PiPInstaller-v0.3.0.mcdr) |
| [PiPInstaller-v0.3.0-rc2.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.3.0-rc2) | 0.3.0-rc2 | 2026/06/26 07:18:18 | 8.34KB | 5 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.3.0-rc2/PiPInstaller-v0.3.0-rc2.mcdr) |
| [PiPInstaller-v0.3.0-rc1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.3.0-rc1) | 0.3.0-rc1 | 2026/06/23 09:32:20 | 7.71KB | 13 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.3.0-rc1/PiPInstaller-v0.3.0-rc1.mcdr) |
| [PiPInstaller-v0.2.3.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.2.3) | 0.2.3 | 2026/06/22 07:18:19 | 2.9KB | 21 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.2.3/PiPInstaller-v0.2.3.mcdr) |
| [PiPInstaller-v0.2.2.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.2.2) | 0.2.2 | 2025/10/21 07:26:29 | 3.02KB | 183 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.2.2/PiPInstaller-v0.2.2.mcdr) |
| [PiPInstaller-v0.2.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.2.1) | 0.2.1 | 2025/10/18 07:19:39 | 2.82KB | 14 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.2.1/PiPInstaller-v0.2.1.mcdr) |
| [PiPInstaller-v0.2.0.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.2.0) | 0.2.0 | 2025/10/18 05:31:56 | 2.22KB | 10 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.2.0/PiPInstaller-v0.2.0.mcdr) |
| [PiPInstaller-v0.1.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.1.1) | 0.1.1 | 2025/08/18 11:57:43 | 1.14KB | 25 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.1.1/PiPInstaller-v0.1.1.mcdr) |
| [PiPInstaller-v0.1.0.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.1.0) | 0.1.0 | 2025/08/18 11:41:13 | 1.11KB | 11 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.1.0/PiPInstaller-v0.1.0.mcdr) |
| [PiPInstaller-v0.0.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.0.1) | 0.0.1 | 2025/03/10 15:55:14 | 1.07KB | 22 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.0.1/PiPInstaller-v0.0.1.mcdr) |

