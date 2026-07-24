[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## games_ai

### 基本信息

- 插件 ID: `games_ai`
- 插件名: GamesAI
- 版本: 0.5.10
  - 元数据版本: 0.5.10
  - 发布版本: 0.5.10
- 总下载量: 717
- 作者: [yello](https://github.com/PengZixuan30)
- 仓库: https://github.com/PengZixuan30/Games_AI
- 仓库插件页: https://github.com/PengZixuan30/Games_AI/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 此插件可以让你在游戏中使用AI

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [openai](https://pypi.org/project/openai) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install openai requests
```

### 介绍

<div align="center">

# GamesAI for MCDReforged

[English](https://github.com/PengZixuan30/Games_AI/tree/main//README.md)  |  简体中文  |  [繁體中文](https://github.com/PengZixuan30/Games_AI/tree/main//README.zh-TW.md)

[反馈问题](https://github.com/PengZixuan30/Games_AI/issues/new)  |  [反馈想法](https://github.com/PengZixuan30/Games_AI/discussions/new/choose)  |  [加入Q群](https://qm.qq.com/q/jDQQaUPNmw)

[转至Fabric版本](https://github.com/PengZixuan30/GamesAI)

</div>

> [!NOTE]
> **GamesAI 插件/模组 QQ 交流群：849544707** — 欢迎加入交流群讨论问题、反馈建议，以及分享 prompt、skills、tools 等配置！

> [!NOTE]
> 欢迎使用版本 0.5.10！当前版本引入了 **通用 `extra_body` 配置** 替代 `thinking` 布尔开关，支持完整的 API 请求参数自定义。见[本次更新](#本次更新)

> [!IMPORTANT]
> **0.5.10 破坏性变更**：`thinking` 布尔配置已被通用 `extra_body` 字典替代。如果你使用了 `"thinking": true`，必须迁移为 `"extra_body": {"thinking": {"type": "enabled"}}`。详见[迁移指南](#1-extra_body--通用-api-参数配置破坏性变更)。

<details>
<summary>目录(点击展示)</summary>

- [GamesAI for MCDReforged](#gamesai-for-mcdreforged)
  - [安装](#安装)
  - [使用](#使用)
  - [配置](#配置)
    - [1.prefix](#1prefix)
    - [2.permission](#2permission)
    - [3.max\_history](#3max_history)
    - [4.all\_ai](#4all_ai)
    - [5.default\_ai](#5default_ai)
  - [工具、Skills 与自定义工具](#工具skills-与自定义工具)
    - [工具](#工具)
    - [Skills 技能](#skills-技能)
    - [自定义工具](#自定义工具)
  - [本次更新](#本次更新)
    - [Version 0.5.10](#version-0510)
      - [1. `extra_body` — 通用 API 参数配置（破坏性变更）](#1-extra_body--通用-api-参数配置破坏性变更)
    - [Version 0.5.9](#version-059)
      - [1. System 消息重构](#1-system-消息重构)
      - [2. 新增 `ai_read_all_data` 工具](#2-新增-ai_read_all_data-工具)
      - [3. 数据库实时注入](#3-数据库实时注入)
      - [4. Thinking 消息样式](#4-thinking-消息样式)
      - [5. Bug 修复与稳定性](#5-bug-修复与稳定性)
  - [鸣谢与声明](#鸣谢与声明)
  - [赞助与贡献者名单](#赞助与贡献者名单)
  - [许可证](#许可证)

</details>

## 安装

在MCDR控制台中使用如下命令以安装插件\(鉴于现版本的MCDR下载器并不稳定，使用此命令可能无法下载最新版，不建议使用此命令安装\)

`!!MCDR plugin install games_ai`

---

或者在[MCDR插件仓库](https://mcdreforged.com/plugin/games_ai)中获取并安装到你的插件目录内

如果选择手动安装，请先安装Python包OpenAI和requests，使用如下命令安装
```bash
pip install openai requests
```

## 使用

在任何地方输入命令`!!gamesai`以显示这个插件的所有功能

| 指令                            | 用途                           |
| ----------------------------- | ---------------------------- |
| `!!gamesai clear`             | 清除玩家的历史聊天记录，历史聊天记录与公共数据库无关   |
| `!!gamesai clearall`          | 清除所有玩家的历史聊天记录，历史聊天记录与公共数据库无关 |
| `!!gamesai reload`            | 重新加载插件配置文件                   |
| `!!gamesai check`             | 检查插件更新                       |
| `!!gamesai speedtest [model]` | 测试 API 服务器连接延迟，不指定模型时测试全部    |

---

你也可以直接输入`!!ask`向AI提问或者聊天或者帮你做一些事情

| 指令                              | 用途                                                                           |
| ------------------------------- | ---------------------------------------------------------------------------- |
| `!!ask <content>`               | 向AI提问或者聊天或者帮你做一些事情，content为你想让AI做的事情或者你想问AI的问题                               |
| `!!ask -m <model> <content>`    | 使用指定的模型向AI提问或者聊天或者帮你做一些事情，model为你想使用的模型的AI_ID或昵称，content为你想让AI做的事情或者你想问AI的问题 |
| `!!ask -n <content>`            | 向AI提问但不使用历史记录（当前对话仍会被保存）                                                     |
| `!!ask -n -m <model> <content>` | 使用指定的模型且不使用历史记录提问                                                            |

---

输入`!!data`获取有关数据库指令的信息

> [!TIP]
> 更新到0.3.0及以上版本时会自动添加数据库

| 指令                           | 用途                                      |
| ---------------------------- | --------------------------------------- |
| `!!data write <key> <value>` | 在公共数据库内添加一条数据，其中key不能包含空格，value可以是任意字符串 |
| `!!data add <key> <value>`   | 将value追加到公共数据库中的key中，不存在时自动创建新key       |
| `!!data del <key>`           | 在公共数据库内删除一条数据，无论key是否存在                 |
| `!!data read <key>`          | 读取公共数据库中key对应的value                     |
| `!!data list`                | 读取公共数据库中的所有内容                           |
| `!!data list keys`           | 读取公共数据库中的所有key                          |

## 配置

默认配置文件结构如下:

```json
{
  "prefix": "[GamesAI]",
  "permission": 3,
  "max_history": 10,
  "all_ai": {
      "<Your AI ID>":{
          "prompt": "你是一名成熟、稳重的Minecraft机器人工具，你的名字叫做“GamesAI”",
          "ai_name": "[GamesAI]",
          "base_url": "<Your API Base URL>",
          "ai_model": "<Your AI Model>",
          "api_key": "<Your API Key>",
          "extra_body": {}
      }
    },
  "default_ai": "<Your AI ID>"
  }
```

---

以下是每个参数的简介:

### 1.prefix
值的类型: str

默认值: \[GamesAI\]

填入插件的名称，以在插件的回复之前加上一个前缀，可以包含Minecraft格式化代码

### 2.permission
值的类型：int

默认值：3

执行`!!data`等指令所必须达到的权限，见[MCDR权限相关文档](https://docs.mcdreforged.com/zh-cn/latest/permission.html)


### 3.max_history
值的类型: int

默认值: 10

填入每个玩家最大可保留的历史记录，与公共数据库无关。设置为 `0` 时完全禁用历史记录功能

### 4.all_ai
值的类型: dict

默认值：见文件

填入所有的AI信息，由多个字典组成，每个字典为一个AI模型，字典的键即为插件内部的AI_ID

**prompt**: 这项配置用于为每个AI编写提示词。使用`> xxx.md`将提示词指向`config/games_ai/prompt/xxx.md`文件，不限文件类型

**ai_name**: 这项配置与prefix功能类似，但是你现在需要单独为每一个模型设置，可以包含Minecraft格式化代码

**base_url**, **ai_model**, **api_key**: 与以前的相关配置功能相同，但是你现在需要单独为每一个模型设置

**extra_body**：请参考各API提供商对 `extra_body` 项的说明以编写。对于DeepSeek用户，想要移植原有 `thinking` 的，直接填写 `{"thinking": {"type": "enabled"}}`。不填时默认 `{}`（空）。

### 5.default_ai
值的类型: str

默认值: \<Your AI ID\>

填入当用户直接使用`!!ask`时使用的模型，应该填入all_ai字典中的某一个键\(即为插件内部的AI_ID\)，如果错填，会导致无法正常使用`!!ask`指令

## 工具、Skills 与自定义工具
### 工具
GamesAI插件提供了很多自带的工具，见下表。如果你想要更多的工具，可以选择[向作者投稿](https://github.com/PengZixuan30/Games_AI/issues/new)或者选择[自定义工具](#自定义工具)

<details>
<summary>点击查看所有的自带工具</summary>

|         工具ID          |             传入参数             | 用途                                                                                                      |
| :-------------------: | :--------------------------: | ------------------------------------------------------------------------------------------------------- |
|  get_online_players   |              无               | 获取服务器内在线的玩家列表。依赖于`online_player_api`插件，不存在时自动关闭此工具                                                      |
|  get_whitelist_name   |              无               | 获取服务器完整的白名单列表。依赖于`whitelist_api`插件，不存在时自动关闭此工具                                                          |
|   add_to_whitelist    |            `name`            | 将某个玩家添加到白名单中。依赖于`whitelist_api`插件，不存在时自动关闭此工具                                                           |
| remove_from_whitelist |            `name`            | 将某个玩家从白名单删除。依赖于`whitelist_api`插件，不存在时自动关闭此工具                                                            |
| search_minecraft_wiki |           `query`            | 让AI搜索Minecraft Wiki，以确保回答更准确                                                                            |
|      calculator       |         `expression`         | 简单的数学表达式计算器                                                                                             |
|    item_caculator     | `expression`,`single_limit`  | 数学表达式计算器，并将最终结果转换为物品计数法，即 盒、组、个，自动适应物品的堆叠数，不存在时默认使用64                                                   |
|      add_pos_pos      |   `name`,`pos`,`dimension`   | 在指定位置添加一个坐标点。依赖于`where2go`或`location_marker`插件，两者都存在时，优先使用`where2go`，均不存在时，自动关闭此工具                      |
|     add_pos_here      |            `name`            | 在玩家的位置添加一个坐标点，控制台执行时自动关闭此工具。依赖于`where2go`或`location_marker`插件，两者都存在时，优先使用`where2go`，均不存在时，自动关闭此工具       |
|      remove_pos       |            `name`            | 删除一个坐标点，`where2go`版本会自动将name转换为id。依赖于`where2go`或`location_marker`插件，两者都存在时，优先使用`where2go`，均不存在时，自动关闭此工具 |
|      search_pos       |            `name`            | 搜索一个坐标点。依赖于`where2go`或`location_marker`插件，两者都存在时，优先使用`where2go`，均不存在时，自动关闭此工具                           |
|      get_all_pos      |              无               | 获取所有的坐标点列表.依赖于`where2go`或`location_marker`插件，两者都存在时，优先使用`where2go`，均不存在时，自动关闭此工具                        |
|     ai_read_data      |            `key`             | 读取一条数据库内容                                                                                               |
|   ai_read_all_keys    |              无               | 获取数据库中所有的键                                                                                              |
|   ai_read_all_data    |              无               | 一次性读取数据库中所有键值对                                                                                          |
|     ai_write_data     |        `key`,`value`         | 向数据库中写入一条数据\(覆写模式\)                                                                                     |
|      ai_add_data      |        `key`,`value`         | 向数据库中写入一条数据\(追加模式\)                                                                                     |
|      read_skills      |           `skills`           | 读取已注册的技能指导文件，引导 AI 执行特定任务                                                                               |
|     write_skills      | `skills`、`summary`、`content` | 创建或覆写一个技能文件并注册到技能索引中                                                                                    |
|     modify_skills     | `skills`、`summary`、`content` | 修改已有技能文件并更新索引中的简介                                                                                       |
|     delete_skills     |           `skills`           | 删除一个技能文件并从技能索引中移除                                                                                       |
|   read_custom_tools   |              无               | 读取当前自定义 `tools.py` 文件的内容                                                                                |
|  modify_custom_tools  |           `tools`            | 用新代码替换整个自定义 `tools.py` 文件                                                                               |
|  append_custom_tools  |           `tools`            | 向自定义 `tools.py` 文件末尾追加新工具代码                                                                             |
|     setting_timer     |          `duration`          | 暂停执行指定秒数后再继续下一步操作                                                                                       |
|     reload_plugin     |              无               | 热重载插件以应用配置、技能和自定义工具的更改，不会丢失聊天记录                                                                         |
|      ai_del_data      |            `key`             | 删除数据库中的一条数据                                                                                             |

</details>

### Skills 技能

Skills 技能系统让你可以编写指导文件来规范 AI 处理特定任务的方式——例如白名单管理、假人控制等。

技能文件存放在 `config/games_ai/skills/` 目录下，格式为 Markdown（`.md`）。要注册一项技能，编辑 `config/games_ai/skills/skills.json`。以下是一个示例配置（`whitelist.md` 和 `player.md` 仅为示例文件名，并非插件内置文件）：

```json
[
    {
        "file": "whitelist.md",
        "description": "添加/删除/查询白名单时都应读取此技能文件"
    },
    {
        "file": "player.md",
        "description": "创建/控制/删除假人时必须读取此技能文件"
    }
]
```

- **`file`** — 技能文件名（相对于 `skills` 文件夹）。
- **`description`** — 展示给 AI 的简短提示，说明何时应当读取此技能。

技能注册后会出现在 AI 的系统提示中。AI 可以使用 **`read_skills`** 工具在执行相关任务前读取技能文件的完整内容。

> [!TIP]
> GamesAI 内置了两个**技能文件**：`skills_management.md`（如何管理技能文件）和 `custom_tools_management.md`（如何修改自定义工具）。AI 在修改技能或工具之前会自动读取这些文件。

> [!TIP]
> Skills 就像 AI 的「标准作业程序 (SOP)」——确保 AI 每次都遵循正确的工作流程。

### 自定义工具
通过修改`config/games_ai/tools/tools.py`文件来实现自定义修改工具

先来看看默认值如何

```python
from mcdreforged.command.command_source import CommandSource
from games_ai.games_ai_tool import register_tool

@register_tool(description="My Custom Tool")
def my_custom_tool(source: CommandSource, ai_prefix: str):
    return "Tool execution completed"
```

> [!IMPORTANT]
> 代码中的`from games_ai.games_ai_tool import register_tool`和函数定义前的`@register_tool`必须存在

> [!TIP]
> 在 0.5.7+ 版本中，AI 可以**自主读取、修改和追加**自定义工具文件。只需让 AI 帮你添加新工具——它会先读取当前文件，编写新代码（使用 `append_custom_tools` 追加而非覆盖），然后重载插件。

可见，这是十分简单的结构。

接下来我将告诉你如何实践，比如下面的例子：搜索baidu.com

<details>

<summary>点击展开</summary>

想要知道如何实现搜索baidu.com，参考GamesAI源代码中的工具`search_minecraft_wiki`无疑是最好的选择：

```python
@register_tool(description="搜索Minecraft Wiki以获取相关信息, 请不要使用此方法搜索与Minecraft无关的东西。如果返回了Search results页面, 你可以通过先浏览此页面, 再进行一次精确查询", tr_key="searching_minecraft_wiki", parameters={
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "要搜索的内容，例如某个物品、怪物、机制等的名称。"
        }
    },
    "required": ["query"]
})
def search_minecraft_wiki(source: CommandSource, ai_prefix: str, query: str):
    source.reply(f'{ai_prefix}{source.get_server().rtr("games_ai.tools.searching_minecraft_wiki", query=query)}')
    lang = source.get_server().get_mcdr_language()
    if lang == "en_us":
        search_url = f"https://minecraft.wiki/?search={query}"
    else:
        search_url = f"https://zh.minecraft.wiki/?search={query}"
    response = requests.get(search_url)
    if response.status_code == 200:
        return f"一下是搜索内容 {query} 的结果:\n{response.content.decode('utf-8')}"
    else:
        return "无法访问Minecraft Wiki进行搜索"
```

首先来看工具的注册，其中的`description`类似于提示词，是必填项，是给AI提供的；其中的`tr_key`是内部方法，外部编写tools.py时不需要包含此项；而`parameters`就是AI需要传入的参数，可根据实际情况决定是否填写，其中的`properties`用于填写所有的传入参数，其中的`required`项则表示有哪些参数是必填的，注意`properties`与函数定义中传入参数的位置关系，应该需要一一对应。

例如：
```python
@register_tool(description="搜索百度")
```

但是，搜索百度肯定需要传入搜索内容，所以：
```python
@register_tool(description="搜索百度", parameters={
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "要搜索的内容"
        }
    },
    "required": ["query"]
})
```

好了，你已经学会如何注册工具了，接下来就可以写函数定义了：
```python
def search_baidu(source: CommandSource, ai_prefix: str, query: str):
```

上面的代码中，`source`和`ai_prefix`项必须编写，因为它们始终会被传入

接下来写函数体：
```python
def search_baidu(source: CommandSource, ai_prefix: str, query: str):
    ...
    return ...
```

函数体中可以是任何你需要的操作，最后记得一定要`return`，否则AI将无法正确处理结果

`tools.py`的完整示例：
```python
import requests
from games_ai.games_ai_tool import register_tool

@register_tool(
    description="使用百度搜索互联网上的信息。当你需要查找实时信息、新闻、百科知识等时使用此工具。",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "要在百度搜索的关键词或问题"
            }
        },
        "required": ["query"]
    }
)
def search_baidu(source, ai_prefix: str, query: str):
    source.reply(f'{ai_prefix}正在搜索百度：{query}...')

    try:
        url = "https://www.baidu.com/s"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, params={"wd": query}, headers=headers, timeout=10)

        if response.status_code != 200:
            return f"百度搜索失败，HTTP 状态码：{response.status_code}"

        # 简单提取页面文本（去除 HTML 标签）
        import re
        text = response.text
        # 移除 script 和 style 标签内容
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        # 移除 HTML 标签
        text = re.sub(r'<[^>]+>', '', text)
        # 合并多余空白
        text = re.sub(r'\s+', ' ', text).strip()

        # 截断过长内容（保留前 3000 字符，适合 AI 上下文）
        max_len = 3000
        if len(text) > max_len:
            text = text[:max_len] + "\n...(内容已截断)"

        return f"百度搜索「{query}」的结果：\n{text}"

    except requests.Timeout:
        return "百度搜索请求超时，请稍后重试"
    except Exception as e:
        return f"百度搜索出错：{str(e)}"
```

</details>

## 本次更新

### Version 0.5.10

#### 1. `extra_body` — 通用 API 参数配置（破坏性变更）

之前的 `thinking` 布尔配置项已被替换为通用的 `extra_body` 字典。请参考各API提供商的说明以编写此项。

> [!WARNING]
> **破坏性变更**：如果你之前使用了 `"thinking": true`，请按如下方式迁移：
> 
> ```json
> // 之前 (0.5.9)
> { "thinking": true }
> 
> // 之后 (0.5.10) — 适用于DeepSeek用户
> { "extra_body": { "thinking": { "type": "enabled" } } }
> ```
> 
> 对于其他API提供商，请查阅其文档以了解正确的 `extra_body` 格式。

### Version 0.5.9

#### 1. System 消息重构

发送给 AI 的 system 提示词现已重构为 **四条独立消息**：

1. **当前时间与语言** — 当前服务器时间和 MCDR 语言设置
2. **AI 提示词** — `all_ai` 中配置的模型专属 system prompt
3. **已注册 Skills** — 当前已注册的技能列表（含内置技能）
4. **数据库内容** — 当前公共数据库的数据

这一分离提升了对 system 消息格式有严格要求的模型（如 DeepSeek）的兼容性，同时也让提示词结构更加清晰、便于维护。

#### 2. 新增 `ai_read_all_data` 工具

新增内置工具 `ai_read_all_data`，允许 AI 一次性读取公共数据库中的所有键值对。此前 AI 需要先调用 `ai_read_all_keys` 获取所有 key，再逐个调用 `ai_read_data` 读取——现在可以一步完成。

#### 3. 数据库实时注入

每次 `!!ask` 请求时，当前公共数据库的内容会自动注入到 system 消息中。这意味着 AI 无需先调用工具就能掌握最新的数据库状态，提升数据相关查询的响应质量。

#### 4. Thinking 消息样式

「正在思考...」状态消息现在使用 Minecraft 灰色格式（`§7...§r`），使其与 AI 的实际回复在视觉上有明显区分。

#### 5. Bug 修复与稳定性

- 修复了 `ai_read_all_data` 返回非字符串值（`list[tuple]`）导致 DeepSeek 等严格 API 返回 HTTP 400 错误的问题。工具调用结果现在始终返回正确格式的字符串。

## 鸣谢与声明
特别感谢望海公社服务器为此插件的测试提供了基础

特别感谢 [william-song-shy (William Song)](https://github.com/william-song-shy) 为 `!!ask` 无历史模式提供的建议。

特别感谢 [ZhangZuoqian (张作乾)](https://github.com/ZhangZuoqian) 为测速指令提供的建议。

AI\(LLM\)模型生成的一切内容与此插件无关

自定义工具造成的一切后果与本插件无关

## 赞助与贡献者名单

赞助地址：[爱发电](https://ifdian.net/a/yello)

为GamesAI赞助的将会出现在下列的赞助者名单中（当前没有赞助者）：

| #   | 赞助者 | 金额  | 日期  |
| --- | --- | --- | --- |
| -   | -   | -   | -   |

## 许可证
MIT License, Copyright (c) 2026 yello

<div align = "center">

---

[回到顶部](#gamesai-for-mcdreforged)

</div>

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [GamesAI-v0.5.10.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.10) | 0.5.10 | 2026/07/22 07:03:08 | 52.39KB | 10 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.10/GamesAI-v0.5.10.mcdr) |
| [GamesAI-v0.5.9.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.9) | 0.5.9 | 2026/07/22 06:14:53 | 53.52KB | 2 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.9/GamesAI-v0.5.9.mcdr) |
| [GamesAI-v0.5.8.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.8) | 0.5.8 | 2026/07/21 03:22:17 | 51.09KB | 11 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.8/GamesAI-v0.5.8.mcdr) |
| [GamesAI-v0.5.7.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.7) | 0.5.7 | 2026/07/19 03:45:10 | 50.45KB | 15 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.7/GamesAI-v0.5.7.mcdr) |
| [GamesAI-v0.5.6.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.6) | 0.5.6 | 2026/07/14 11:32:49 | 54.39KB | 16 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.6/GamesAI-v0.5.6.mcdr) |
| [GamesAI-v0.5.5.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.5) | 0.5.5 | 2026/07/08 11:08:15 | 51.89KB | 18 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.5/GamesAI-v0.5.5.mcdr) |
| [GamesAI-v0.5.4.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.4) | 0.5.4 | 2026/06/05 16:23:44 | 43.34KB | 48 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.4/GamesAI-v0.5.4.mcdr) |
| [GamesAI-v0.5.3.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.3) | 0.5.3 | 2026/05/24 08:27:26 | 41.59KB | 35 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.3/GamesAI-v0.5.3.mcdr) |
| [GamesAI-v0.5.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.2) | 0.5.2 | 2026/05/24 03:31:00 | 39.75KB | 30 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.2/GamesAI-v0.5.2.mcdr) |
| [GamesAI-v0.5.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.1) | 0.5.1 | 2026/05/16 14:33:47 | 37.42KB | 46 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.1/GamesAI-v0.5.1.mcdr) |
| [GamesAI-v0.5.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.5.0) | 0.5.0 | 2026/05/10 06:56:40 | 35.83KB | 42 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.5.0/GamesAI-v0.5.0.mcdr) |
| [GamesAI-v0.4.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.2) | 0.4.2 | 2026/05/02 14:47:09 | 23.1KB | 52 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.2/GamesAI-v0.4.2.mcdr) |
| [GamesAI-v0.4.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.1) | 0.4.1 | 2026/05/01 12:03:32 | 20.61KB | 51 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.1/GamesAI-v0.4.1.mcdr) |
| [GamesAI-v0.4.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.4.0) | 0.4.0 | 2026/04/26 05:25:45 | 20.0KB | 53 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.4.0/GamesAI-v0.4.0.mcdr) |
| [GamesAI-v0.3.2.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.2) | 0.3.2 | 2026/04/18 01:20:54 | 17.06KB | 69 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.2/GamesAI-v0.3.2.mcdr) |
| [GamesAI-v0.3.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.1) | 0.3.1 | 2026/04/12 06:15:12 | 14.82KB | 52 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.1/GamesAI-v0.3.1.mcdr) |
| [GamesAI-v0.3.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.3.0) | 0.3.0 | 2026/04/11 14:21:17 | 11.37KB | 49 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.3.0/GamesAI-v0.3.0.mcdr) |
| [GamesAI-v0.2.1.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.1) | 0.2.1 | 2026/04/04 04:27:04 | 8.45KB | 57 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.1/GamesAI-v0.2.1.mcdr) |
| [Game.sAI-v0.2.0.mcdr](https://github.com/PengZixuan30/Games_AI/releases/tag/0.2.0) | 0.2.0 | 2026/03/29 03:10:14 | 3.49KB | 61 | [下载](https://github.com/PengZixuan30/Games_AI/releases/download/0.2.0/Game.sAI-v0.2.0.mcdr) |

