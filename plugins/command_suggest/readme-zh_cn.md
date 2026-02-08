[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## command_suggest

### 基本信息

- 插件 ID: `command_suggest`
- 插件名: CommandSuggest
- 版本: 1.0.4
  - 元数据版本: 1.0.4
  - 发布版本: 1.0.4
- 总下载量: 357
- 作者: [PairZhu](https://github.com/PairZhu)
- 仓库: https://github.com/PairZhu/CommandSuggest-MCDR
- 仓库插件页: https://github.com/PairZhu/CommandSuggest-MCDR/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 支持参数提示的MCDR命令补全插件。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [uvicorn](https://pypi.org/project/uvicorn) |  |
| [fastapi](https://pypi.org/project/fastapi) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |

```
pip install uvicorn fastapi mcdreforged
```

### 介绍

# 🚀 CommandSuggest-MCDR

**[English](https://github.com/PairZhu/CommandSuggest-MCDR/tree/master/./README.en.md) | 简体中文**

[![Modrinth Downloads](https://img.shields.io/modrinth/dt/mcdrcmdsuggest?logo=modrinth&label=Modrinth)
](https://modrinth.com/mod/mcdrcmdsuggest)

## ✨ 更优雅的MCDR命令补全实现

需要配合[McdrCmdSuggest](https://modrinth.com/mod/mcdrcmdsuggest)服务端Mod使用。

CommandSuggest-MCDR是一个MCDR插件，为[MCDReforged](https://github.com/Fallen-Breath/MCDReforged)提供更优雅的命令补全功能。通过在Minecraft服务端中注册MCDR命令并发送到客户端，使玩家可以获得原生的命令补全体验。

![1757522576816](https://raw.githubusercontent.com/PairZhu/CommandSuggest-MCDR/master/image/1757522576816.png)

## 🛠️ 特性

- ⚡ 原生命令补全体验：将MCDR命令注册为Minecraft原生命令，允许静默发送MCDR命令
- 💡 支持参数建议补全（MCDR插件中的suggests方法）
- 🖥️ 纯服务端Mod，客户端无需安装，支持原版客户端
- 🛡️ 不依赖mixins，更易于维护多版本，**1.14 ~ 1.21.8**正式版全版本支持
- ⚙️ 默认配置全自动，无需手动配置也可开箱即用

## 📦 安装

1. 从[Modrinth](https://modrinth.com/mod/mcdrcmdsuggest)或[GitHub Releases](https://github.com/PairZhu/McdrCmdSuggest/releases)下载最新版本的McdrCmdSuggest
2. 将下载的jar文件放入Minecraft服务端的mods文件夹中
3. 在服务器端安装此插件`!!MCDR plugin install command_suggest`
4. 重启服务器

## ⚙️ 配置
| 配置项          | 描述                            | 默认值         |
| ------------ | ----------------------------- | ----------- |
| `mode`       | 通信模式，目前仅支持`http`              | `http`      |
| `host`       | http服务器监听的主机地址                | `localhost` |
| `port`       | http服务器监听的端口号，设置为0则自动选择一个可用端口 | `0`         |
| `force_load` | 是否强制加载插件，即使未检测到Mod也尝试连接Mod服务器 | `false`     |


## 📝 使用方法

将原有的MCDR命令以`/`开头的Minecraft标准命令形式输入，然后在游戏中使用Tab键进行命令补全即可。例如`/!!help`, `/!!MCDR xxx`（无需配置其它插件或修改插件代码）。

## 🔍 与其他模组的比较

与其他MCDR命令补全模组相比，McdrCmdSuggest提供了以下优势：

- **更优雅的实现**：直接利用Minecraft原生的命令系统，提供更流畅的用户体验
- **更全面的功能**：支持参数建议补全，适应更多复杂的命令结构
- **更好的兼容性**：MCDR命令不以"!"或"!!"开头也可补全，兼容更多的插件
- **更少的依赖项**：不依赖mixins，减少潜在的维护成本，无需客户端Mod

## 🧩 技术细节

McdrCmdSuggest通过以下方式实现命令补全：

1. 注册一个特殊的命令`__mcdrcmdsuggest_register`，用于接收服务器发送的命令注册信息
2. 根据接收到的信息，动态注册Minecraft命令
3. 如果命令包含参数建议（suggests），则将为其添加suggests方法，向配套的MCDR插件查询建议结果（默认使用http，仅服务端和MCDR进行本地通讯，无需暴露端口），客户端的建议由Minecraft自带的通讯协议传输

## 🤝 贡献

欢迎提交问题报告和功能请求！

## 🙏 致谢

- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) - 强大的Minecraft服务器管理框架
- [ZhuRuoLing/MCDRCommandCompletionReforged-Mod](https://github.com/ZhuRuoLing/MCDRCommandCompletionReforged-Mod) - 提供了参考实现
- [AnzhiZhang/MCDRCommandFabric](https://github.com/AnzhiZhang/MCDRCommandFabric) - 提供了参考实现

## 📄 声明

本模组大量参考了 [ZhuRuoLing/MCDRCommandCompletionReforged-Mod](https://github.com/ZhuRuoLing/MCDRCommandCompletionReforged-Mod) 和 [AnzhiZhang/MCDRCommandFabric](https://github.com/AnzhiZhang/MCDRCommandFabric) 的代码和实现。没有他们的工作，这个模组不可能实现。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [CommandSuggest-v1.0.4.mcdr](https://github.com/PairZhu/CommandSuggest-MCDR/releases/tag/v1.0.4) | 1.0.4 | 2026/01/16 06:00:38 | 16.8KB | 70 | [下载](https://github.com/PairZhu/CommandSuggest-MCDR/releases/download/v1.0.4/CommandSuggest-v1.0.4.mcdr) |
| [CommandSuggest-v1.0.3.mcdr](https://github.com/PairZhu/CommandSuggest-MCDR/releases/tag/v1.0.3) | 1.0.3 | 2025/11/23 18:38:29 | 16.76KB | 143 | [下载](https://github.com/PairZhu/CommandSuggest-MCDR/releases/download/v1.0.3/CommandSuggest-v1.0.3.mcdr) |
| [CommandSuggest-v1.0.2.mcdr](https://github.com/PairZhu/CommandSuggest-MCDR/releases/tag/v1.0.2) | 1.0.2 | 2025/10/07 03:51:56 | 16.51KB | 86 | [下载](https://github.com/PairZhu/CommandSuggest-MCDR/releases/download/v1.0.2/CommandSuggest-v1.0.2.mcdr) |
| [CommandSuggest-v1.0.1.mcdr](https://github.com/PairZhu/CommandSuggest-MCDR/releases/tag/v1.0.1) | 1.0.1 | 2025/10/06 16:57:41 | 16.42KB | 4 | [下载](https://github.com/PairZhu/CommandSuggest-MCDR/releases/download/v1.0.1/CommandSuggest-v1.0.1.mcdr) |
| [CommandSuggest-v1.0.0.mcdr](https://github.com/PairZhu/CommandSuggest-MCDR/releases/tag/v1.0.0) | 1.0.0 | 2025/09/11 11:42:26 | 15.59KB | 54 | [下载](https://github.com/PairZhu/CommandSuggest-MCDR/releases/download/v1.0.0/CommandSuggest-v1.0.0.mcdr) |

