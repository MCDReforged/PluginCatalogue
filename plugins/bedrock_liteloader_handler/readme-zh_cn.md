[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## bedrock_liteloader_handler

### 基本信息

- 插件 ID: `bedrock_liteloader_handler`
- 插件名: BedrockLiteloaderHandler
- 版本: 1.2.1
  - 元数据版本: 1.2.1
  - 发布版本: 1.2.1
- 总下载量: 66
- 作者: [Elec glacier](https://github.com/Elec-Glacier), [jiangyan](https://github.com/jiangyan03)
- 仓库: https://github.com/Elec-Glacier/liteloader_handler
- 仓库插件页: https://github.com/Elec-Glacier/liteloader_handler/tree/main
- 标签: [`服务端处理器`](/labels/handler/readme-zh_cn.md)
- 描述: 一个让基岩版也能使用MCDR的处理器

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.13.2 |

```
pip install "mcdreforged>=2.13.2"
```

### 介绍

[English](https://github.com/Elec-Glacier/liteloader_handler/blob/main/README.md) | **中文**

# Bedrock Liteloader Handler
一个让基岩版也能使用MCDR及其插件的服务端处理器

## 使用之前
原版的BDS是不能输出玩家聊天的。所以你可以使用行为包或者是更改服务端来实现玩家聊天输出

## 使用说明
1. 从仓库[releases](https://github.com/Elec-Glacier/liteloader_handler/releases)中现在最新版本
2. 将下载的文件放入到MCDR的"plugins"文件夹里
3. 启动MCDR
4. 更改config文件夹中的配置文件，选择处理器（默认是原版处理器）
5. 重载配置文件

## 注意
LeviLamina的1.0.0版本后，MCDR无法获取更改过的服务端输出。你可以使用一个支持pty的应用作为桥梁。[更多细节](https://github.com/Elec-Glacier/liteloader_handler/issues/13)
1.2.0版本后，对PrimeBackup做了专门的适配。你可以在config里关掉。

## MCDR插件安装注意
由于基岩版和Java版判若两个游戏，所以在使用其他插件之前，确保知道其是如何工作的并保证能正常运行。

## 注意事项
由于[BDS-3791](https://bugs.mojang.com/browse/BDS-3791)，你可能需要插件修改服务端进行修复，如[UnicodeFixer](https://www.minebbs.com/resources/unicodefixer.6991/)。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BedrockLiteloaderHandler-v1.2.1.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.2.1) | 1.2.1 | 2025/03/14 17:56:17 | 6.04KB | 15 | [下载](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.2.1/BedrockLiteloaderHandler-v1.2.1.mcdr) |
| [BedrockLiteloaderHandler-v1.2.0.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.2.0) | 1.2.0 | 2025/01/31 13:07:18 | 6.0KB | 8 | [下载](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.2.0/BedrockLiteloaderHandler-v1.2.0.mcdr) |
| [BedrockLiteloaderHandler-v1.1.2.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.1.2) | 1.1.2 | 2025/01/05 05:21:18 | 5.69KB | 16 | [下载](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.1.2/BedrockLiteloaderHandler-v1.1.2.mcdr) |
| [BedrockLiteloaderHandler-v1.1.1.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.1.1) | 1.1.1 | 2024/12/14 11:34:03 | 4.32KB | 10 | [下载](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.1.1/BedrockLiteloaderHandler-v1.1.1.mcdr) |
| [BedrockLiteloaderHandler-v1.0.0.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.0.0) | 1.0.0 | 2024/12/07 20:36:24 | 6.91KB | 17 | [下载](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.0.0/BedrockLiteloaderHandler-v1.0.0.mcdr) |

