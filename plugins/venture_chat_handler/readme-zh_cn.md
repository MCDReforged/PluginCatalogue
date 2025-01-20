[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## venture_chat_handler

### 基本信息

- 插件 ID: `venture_chat_handler`
- 插件名: VentureChatHandler
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 23
- 作者: [MC_Nirvana](https://github.com/MC-Nirvana)
- 仓库: https://github.com/MC-Nirvana/VentureChatHandler
- 仓库插件页: https://github.com/MC-Nirvana/VentureChatHandler/tree/main
- 标签: [`服务端处理器`](/labels/handler/readme-zh_cn.md)
- 描述: 使MCDReforged能够正常解析由VentureChat修改过后的消息

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [strip_ansi](https://pypi.org/project/strip_ansi) |  |

```
pip install strip_ansi
```

### 介绍

# VentureChatHandler
一款MCDR（全称[MCDReforged](https://mcdreforged.com/)）插件，用于使MCDReforged能够正常解析由VentureChat修改过后的消息。

## 简介
众所周知，MCDReforged是通过解析控制台日志中的玩家消息来进行操作的。而诸如VentureChat之类的聊天前缀插件会修改玩家的聊天信息的输出导致MCDReforged无法正常解析。因此，本插件应运而生。其本质上是一个解析器，用来将经过聊天前缀修改后的消息重新解析为MCDReforged可以识别的格式。

## 开发背景
2024年10月26日晚19:04，我照常对我的服务器的插件、模组进行测试，发现服务器安装的VentureChat插件（一个支持频道功能的聊天前缀插件）会导致MCDReforged的所有功能无法正常使用（初步判断是因为VentureChat修改了聊天信息，导致MCDReforged无法正常解析因此无法正常工作），于是我花了一晚上，写出来了这个解析器。用于解决这个问题。并于10月27日晚23:46将其封装为插件。

## 插件用法
1. 从[releases](https://github.com/MC-Nirvana/VentureChatHandler/releases)中下载最新版本。
2. 在MCDReforged的启动环境中安装好需要的Python依赖。
3. 将插件放进plugins文件夹里面。
4. 调整配置文件以适配服务器的聊天信息格式。
5. 重启服务器。
6. 请尽情使用吧。

## 配置文件
### config.json

| 配置项 | 配置内容 |
| - | - |
| **chat_prefix_regex** | 需要解析的玩家消息正则表达式 |

## 常见问题与解答（FAQ）
- Q: 为什么名称叫VentureChatHandler？是专门为VentureChat制作的吗？不支持其他聊天前缀插件吗？
  - > A: 因为这个插件是我为我自己服务器写的，我自己的服务器采用了VentureChat插件，因此才命名为VentureChatHandler。至于其他聊天前缀插件是否支持......我没测过，如果有兴趣可以自行测试下。理论上应该是支持市面上所有的聊天前缀插件。
- Q: 为什么上面说插件是10月27号做好的，但MCDReforged官方仓库显示是11月5号提交的。中间相差好几天啊，怎么回事？
  - > A: 因为最开始我写插件的时候只是想自己用，再加上当时MCDReforged官方仓库并没有为Handlers插件创建分类。因此没有提交（当时甚至没有创建Git仓库，是后来才创建Git存储库并决定公开的。）
- Q: 为什么我已经使用了VentureChat来修改聊天前缀，并且本插件采用默认配置的情况下依旧无法正常解析消息？
  - > A: 因为这个插件最开始是为我自己服务器所使用的VentureChat插件来设计的，而它的前缀中玩家消息的部分有一个`:`符号，这会导致在服务器启动、关闭的时候额外解析多余的消息（这些消息大多都是控制台的日志）。因此我将其修改为了`>>>`以避免这个问题。如果出现无法正常解析的情况，请根据自己所使用的聊天前缀插件中的内容来修改配置文件中的`chat_prefix_regex`中的正则表达式。

## 鸣谢
1. [Mooling0602](https://github.com/Mooling0602)
   - 在百忙之中指导我如何制作这么一个项目，并给予精神上的支持与鼓励。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [VentureChatHandler-1.0.0.mcdr](https://github.com/MC-Nirvana/VentureChatHandler/releases/tag/1.0.0) | 1.0.0 | 2024/11/03 20:30:35 | 2.09KB | 23 | [下载](https://github.com/MC-Nirvana/VentureChatHandler/releases/download/1.0.0/VentureChatHandler-1.0.0.mcdr) |

