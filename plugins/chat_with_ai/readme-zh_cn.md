[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## chat_with_ai

### 基本信息

- 插件 ID: `chat_with_ai`
- 插件名: Chat with AI
- 版本: 1.4.2
  - 元数据版本: 1.4.2
  - 发布版本: 1.4.2
- 总下载量: 374
- 作者: [gubai](https://github.com/gubaiovo)
- 仓库: https://github.com/gubaiovo/MCDR_chat_with_ai
- 仓库插件页: https://github.com/gubaiovo/MCDR_chat_with_ai/tree/main/chat_with_ai
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 让你的服务器接入AI

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [uuid_api](/plugins/uuid_api/readme-zh_cn.md) | \>=0.1.2 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [openai](https://pypi.org/project/openai) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install mcdreforged openai requests
```

### 介绍

# chat_with_ai
DeepSeek 恢复正常后，便尝试编写一个MCDR插件，使MC服务器能够接入DeepSeek。

使用了openai库，理论上支持openai的模型均可使用此插件对接

文章地址：https://blog.gubaiovo.com/posts/ec277bd3.html

## 使用方法

扔进plugins文件夹，然后`!!MCDR plugin reload chat_with_ai`



## Command

`!!dsp help`: 查看帮助

`!!dsp history`: 查看历史消息

`!!dsp clear`: 清空历史消息

`!!dsp system`: 查看ai预设

`!!dsp system <system>`: 设置ai预设

`!!dsp prefix`: 查看ai名称

`!!dsp prefix <prefix>`: 设置ai名称

`!!dsp init system`: 初始化角色预设

`!!dsp init prefix`: 初始化角色预设

`!!dsp init all`: 全部初始化且清空历史记录

`!!dsp msg <message>`: 与AI对话



## 鸣谢

感谢22年的自己

> 世界生成算法吞下了我的十七岁。
> 
> 那封没寄出的信还在末地折跃门边缘，
> 
> 漂浮如未完成的红石电路。
> 
> 当第一个AI村民说出预设外的对白，
> 
> 我忽然听见2022年的自己，
> 
> 在矿洞深处敲打铁轨的节奏。
> 
> 那些被放弃的坐标参数，
> 
> 正在基岩层下重新编译春天。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [chat_with_ai.mcdr](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/tag/1.4.2) | 1.4.2 | 2025/03/12 17:45:36 | 9.25KB | 231 | [下载](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/download/1.4.2/chat_with_ai.mcdr) |
| [chat_with_ai.mcdr](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/tag/1.4.1) | 1.4.1 | 2025/03/12 17:29:36 | 9.26KB | 29 | [下载](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/download/1.4.1/chat_with_ai.mcdr) |
| [chat_with_ai.mcdr](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/tag/1.4.0) | 1.4.0 | 2025/03/03 09:25:05 | 8.61KB | 47 | [下载](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/download/1.4.0/chat_with_ai.mcdr) |
| [chat_with_ai.mcdr](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/tag/1.3.0) | 1.3.0 | 2025/03/02 07:05:08 | 4.88KB | 34 | [下载](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/download/1.3.0/chat_with_ai.mcdr) |
| [chat_with_ai.mcdr](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/tag/1.2.0) | 1.2.0 | 2025/03/02 02:56:11 | 3.4KB | 33 | [下载](https://github.com/gubaiovo/MCDR_chat_with_ai/releases/download/1.2.0/chat_with_ai.mcdr) |

