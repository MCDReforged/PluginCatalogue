[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## connect_core

### 基本信息

- 插件 ID: `connect_core`
- 插件名: ConnectCore
- 版本: 0.1.6
  - 元数据版本: 0.1.6
  - 发布版本: 0.1.6
- 总下载量: 32
- 作者: [zhongbai233](https://github.com/zhongbai2333)
- 仓库: https://github.com/zhongbai2333/ConnectCore
- 仓库插件页: https://github.com/zhongbai2333/ConnectCore/tree/master
- 标签: [`API`](/labels/api/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 将你的Minecraft Server连接到一起并控制。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [cryptography](https://pypi.org/project/cryptography) | \>=44.0.0 |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.4 |
| [prompt_toolkit](https://pypi.org/project/prompt_toolkit) | \>=3.0.50 |
| [psutil](https://pypi.org/project/psutil) | \>=6.1.1 |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0.2 |
| [websockets](https://pypi.org/project/websockets) | \>=14.2 |

```
pip install "cryptography>=44.0.0" "mcdreforged>=2.14.4" "prompt_toolkit>=3.0.50" "psutil>=6.1.1" "PyYAML>=6.0.2" "websockets>=14.2"
```

### 介绍

# ConnetCore

这是一个MCDReforged的前置插件，也可以独立使用，用于将你的服务器建立成插件控制群组，主要用于子服务器间插件的通信，比如为跨服聊天提供API和通信支持。拥有较高的安全性和简易的配置，适合各种服务器环境。

[English](https://github.com/zhongbai2333/ConnectCore/tree/master/README.md) | 简中

## 使用方法

### 独立使用

1. 将`ConnectCore.pyz`文件放在一个空文件夹内。
2. 在命令行中运行以下命令：
   `python ConnectCore.pyz server` 或者 `python ConnectCore.pyz client` 以启服务端或客户端。
3. 根据提示进行配置。

### 作为MCDR插件使用

1. 将`ConnectCore.pyz`文件放在MCDR的插件目录内（通常是`plugins`文件夹）。
2. 启动MCDR服务器，然后使用`!!connectcore init`命令来启用初始化程序。
3. 根据提示进行配置。

## 开发

- 详细的中文开发文档可以在[DOCS](https://github.com/zhongbai2333/ConnectCore/tree/master/doc)中找到。
- 样例插件请前往[ExamplePlugin](https://github.com/zhongbai2333/ExamplePlugin)

## 注意事项

- 确保你的服务器和客户端能够正确连接到网络。
- 一组服务器只有一个服务端，可以有多个客户端
- 如果你遇到任何问题，请查看插件的[WIKI](https://github.com/zhongbai2333/ConnectCore/wiki)或联系开发者。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ConnectCore-v0.1.6.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.6) | 0.1.6 | 2025/02/07 08:21:06 | 53.61KB | 13 | [下载](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.6/ConnectCore-v0.1.6.pyz) |
| [ConnectCore-v0.1.5.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.5) | 0.1.5 | 2025/02/06 15:15:40 | 53.58KB | 2 | [下载](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.5/ConnectCore-v0.1.5.pyz) |
| [ConnectCore-v0.1.4.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.4) | 0.1.4 | 2025/02/04 14:44:35 | 53.3KB | 5 | [下载](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.4/ConnectCore-v0.1.4.pyz) |
| [ConnectCore-v0.1.3.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.3) | 0.1.3 | 2025/02/04 07:24:02 | 52.66KB | 2 | [下载](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.3/ConnectCore-v0.1.3.pyz) |
| [ConnectCore-v0.1.2.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.2) | 0.1.2 | 2025/02/04 01:30:25 | 51.13KB | 2 | [下载](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.2/ConnectCore-v0.1.2.pyz) |
| [ConnectCore-v0.1.1.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.1) | 0.1.1 | 2025/02/03 15:25:34 | 50.58KB | 2 | [下载](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.1/ConnectCore-v0.1.1.pyz) |
| [ConnectCore-v0.1.0.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.0) | 0.1.0 | 2025/01/26 02:57:59 | 47.95KB | 6 | [下载](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.0/ConnectCore-v0.1.0.pyz) |

