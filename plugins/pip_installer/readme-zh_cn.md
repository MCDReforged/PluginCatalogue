[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## pip_installer

### 基本信息

- 插件 ID: `pip_installer`
- 插件名: PiPInstaller
- 版本: 0.2.2
  - 元数据版本: 0.2.2
  - 发布版本: 0.2.2
- 总下载量: 151
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/PiPInstaller-MCDR
- 仓库插件页: https://github.com/Mooling0602/PiPInstaller-MCDR/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 在MCDR控制台中安装Python包依赖！

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.1.0 |

```
pip install "mcdreforged>=2.1.0"
```

### 介绍

# PiPInstaller-MCDR

为面板服解决Python依赖安装问题！

> For English users: I'm sorry but please translate by yourself, AI tools would be fine.
> 
> PRs for translation are welcome.

## 用法

**注意：使用前通过插件报错和使用文档等信息，确认你需要额外安装的Python依赖的PyPI包名！**

**对于较为复杂需要较长安装时间的Python包，你应该另开终端/控制台/Shell手动安装和管理会话！**

在MCDR的控制台上使用`!!pipi <包名（可限定版本）>`或`!!pip install <包名（可限定版本）>`从PyPI安装所需的Python依赖。使用空格分隔多个包名。
> 目前不支持在游戏客户端中执行这些指令，如果你这么做，插件将提示请在控制台上执行。

### 安装过程控制

> 于0.2.1添加

安装插件Command Aliases后，可以通过`!!pipi enable_aliases`启用命令别名。
> 使用`!!MCDR plg install command_aliases --confirm`来安装此可选依赖。

命令别名将被注册到`config/command_aliases/config.json`中。

> 于v0.2.0添加

`!!pip install <package> [-q]` - 安装Python（PyPI）包，支持空格分割多个包名，支持用`-q`参数静默安装。
> 也可以使用`!!pipi <package> [-q]`

`!!pip cancel` - 取消当前进行中的安装任务
> 在启用命令别名后，也可以使用`!!pipc`

`!!pip status` - 查看当前进行中的安装任务状态
> 在启用命令别名后，也可以使用`!!pips`

## 声明

- **MCDReforged的开发者没有计划提供类似直接补全安装插件缺失的PyPI依赖的功能，因此不要向他们发出于此相关的任何功能请求。**
- **若在使用插件的命令时遇到问题，可在此仓库发起Issues进行反馈；若在MCDR外使用变相解决的办法，则你需要自行确认MCDR的命令是否在你的操作环境中可用，并且你应该知道这种做法是不受推荐的，请不要因为在使用此方法遇到问题时向MCDR的开发者反馈**
- **你应该详细阅读这篇[安装相关文档](https://docs.mcdreforged.com/zh-cn/latest/quick_start/install.html#)，构建完整的Python环境管理体系，这才是解决Python依赖问题的根本所在**

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [PiPInstaller-v0.2.2.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.2.2) | 0.2.2 | 2025/10/21 07:26:29 | 3.02KB | 91 | [下载](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.2.2/PiPInstaller-v0.2.2.mcdr) |
| [PiPInstaller-v0.2.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.2.1) | 0.2.1 | 2025/10/18 07:19:39 | 2.82KB | 9 | [下载](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.2.1/PiPInstaller-v0.2.1.mcdr) |
| [PiPInstaller-v0.2.0.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.2.0) | 0.2.0 | 2025/10/18 05:31:56 | 2.22KB | 4 | [下载](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.2.0/PiPInstaller-v0.2.0.mcdr) |
| [PiPInstaller-v0.1.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.1.1) | 0.1.1 | 2025/08/18 11:57:43 | 1.14KB | 21 | [下载](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.1.1/PiPInstaller-v0.1.1.mcdr) |
| [PiPInstaller-v0.1.0.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.1.0) | 0.1.0 | 2025/08/18 11:41:13 | 1.11KB | 8 | [下载](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.1.0/PiPInstaller-v0.1.0.mcdr) |
| [PiPInstaller-v0.0.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.0.1) | 0.0.1 | 2025/03/10 15:55:14 | 1.07KB | 18 | [下载](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.0.1/PiPInstaller-v0.0.1.mcdr) |

