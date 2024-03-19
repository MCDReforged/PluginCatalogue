[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## matrix_sync

### 基本信息

- 插件 ID: `matrix_sync`
- 插件名: MatrixSync
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 11
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/MatrixSync-MCDR
- 仓库插件页: https://github.com/Mooling0602/MatrixSync-MCDR/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`信息`](/labels/information/readme-zh_cn.md)
- 描述: 同步Matrix群组和线上游戏的消息.

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [matrix-nio](https://pypi.org/project/matrix-nio) |  |
| [aiofiles](https://pypi.org/project/aiofiles) |  |
| [asyncio](https://pypi.org/project/asyncio) |  |

```
pip install matrix-nio aiofiles asyncio
```

### 介绍

# MatrixSync-MCDR
一个MCDR（全称[MCDReforged](https://mcdreforged.com/)）插件，用于同步Matrix群组和线上游戏之间的消息。

关于[Matrix](https://matrix.org/)：一个开放的去中心化的网络通讯协议，用于聊天软件。

开发过程中使用了pypi中的项目[matrix-nio](https://pypi.org/project/matrix-nio/)。

当前已完成预览开发版本，支持线上游戏的消息上报到群组中，详情可以先看看issue。

## 用法
从Release下载最新版本，甩到plugins文件夹或你设置的存放插件的文件夹内，然后注意控制台输出的提示即可。

## 注意
- 首次加载插件会初始化配置并自动卸载插件，你需要修改完默认配置后，重启服务器或重载插件才能正常使用。
- 不打算支持加密信息（EE2E），有需要自行修改。
- i18n将在正式版本（v1.1.0）以后得到支持。
- 房间消息转发到游戏内的功能还在开发，由于看不懂文档，可能还需要很长时间。
- For English(and other languages) users, you need to use translate tools at present.

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MatrixSync-v1.0.0.mcdr](https://github.com/Mooling0602/MatrixSync-MCDR/releases/tag/1.0.0) | 1.0.0 | 2024/03/10 14:01:47 | 2.69KB | 5 | [下载](https://github.com/Mooling0602/MatrixSync-MCDR/releases/download/1.0.0/MatrixSync-v1.0.0.mcdr) |
| [MatrixSync-v0.1.0.mcdr](https://github.com/Mooling0602/MatrixSync-MCDR/releases/tag/0.1.0) | 0.1.0 | 2024/03/06 05:34:25 | 2.48KB | 6 | [下载](https://github.com/Mooling0602/MatrixSync-MCDR/releases/download/0.1.0/MatrixSync-v0.1.0.mcdr) |

