**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## pip_installer

### Basic Information

- Plugin ID: `pip_installer`
- Plugin Name: PiPInstaller
- Version: 0.1.1
  - Metadata version: 0.1.1
  - Release version: 0.1.1
- Total downloads: 45
- Authors: [Mooling0602](https://github.com/Mooling0602)
- Repository: https://github.com/Mooling0602/PiPInstaller-MCDR
- Repository plugin page: https://github.com/Mooling0602/PiPInstaller-MCDR/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Install Python dependencies in MCDR console.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# PiPInstaller-MCDR
为面板服解决Python依赖安装问题！

## 用法
**注意：使用前通过插件报错和使用文档等信息，确认你需要额外安装的Python依赖的PyPI包名！**

**对于较为复杂需要较长安装时间的Python包，你应该另开终端/控制台/Shell手动安装和管理会话！**

在MCDR的控制台上使用`!!pipi <包名（可限定版本）>`或`!!pip install <包名（可限定版本）>`从PyPI安装所需的Python依赖。使用空格分隔多个包名。
> 目前不支持在游戏客户端中执行这些指令，如果你这么做，插件将提示请在控制台上执行。

如果你没有运行MCDR，则无需此插件，下面有一个变相解决的办法（不是很方便，但理论上可行）：
> 简幻欢等面板用户请注意，该方法大概率不支持你的运行环境，直接忽略，请直接在MCDR控制台上执行命令！

1. 新建一个空的zip压缩包，假设为plugin.zip
2. 创建一个requirements.txt并写上你要安装的依赖
3. 把这个txt文件塞进压缩包里面
4. 修改压缩包的文件名后缀为mcdr，如plugin.mcdr
5. 打开这个压缩包所在的目录，运行`mcdreforged pim pipi plugin.mcdr`

不出意外的话，你所需的依赖应该能被正确的安装到MCDR所在的Python环境中。

## 声明
- **MCDReforged的开发者没有计划提供类似直接补全安装插件缺失的PyPI依赖的功能，因此不要向他们发出于此相关的任何功能请求。**
- **若在使用插件的命令时遇到问题，可在此仓库发起Issues进行反馈；若在MCDR外使用变相解决的办法，则你需要自行确认MCDR的命令是否在你的操作环境中可用，并且你应该知道这种做法是不受推荐的，请不要因为在使用此方法遇到问题时向MCDR的开发者反馈**
- **你应该详细阅读这篇[安装相关文档](https://docs.mcdreforged.com/zh-cn/latest/quick_start/install.html#)，构建完整的Python环境管理体系，这才是解决Python依赖问题的根本所在**

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [PiPInstaller-v0.1.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.1.1) | 0.1.1 | 2025/08/18 11:57:43 | 1.14KB | 20 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.1.1/PiPInstaller-v0.1.1.mcdr) |
| [PiPInstaller-v0.1.0.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.1.0) | 0.1.0 | 2025/08/18 11:41:13 | 1.11KB | 8 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.1.0/PiPInstaller-v0.1.0.mcdr) |
| [PiPInstaller-v0.0.1.mcdr](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/tag/0.0.1) | 0.0.1 | 2025/03/10 15:55:14 | 1.07KB | 17 | [Download](https://github.com/Mooling0602/PiPInstaller-MCDR/releases/download/0.0.1/PiPInstaller-v0.0.1.mcdr) |

