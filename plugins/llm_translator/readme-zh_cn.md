[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## llm_translator

### 基本信息

- 插件 ID: `llm_translator`
- 插件名: LLM_Translator
- 版本: 1.4.0
  - 元数据版本: 1.4.0
  - 发布版本: 1.4.0
- 总下载量: 52
- 作者: [HeTao_yz](https://github.com/HeTao-yz)
- 仓库: https://github.com/HeTao-yz/llm-translator
- 仓库插件页: https://github.com/HeTao-yz/llm-translator/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`信息`](/labels/information/readme-zh_cn.md)
- 描述: 在游戏内使用大语言模型进行翻译。支持翻译玩家对话，游戏内木牌文字，讲台上的书籍内容。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | \>=1.4.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged ](https://pypi.org/project/mcdreforged ) | \>= 2.0.0 |
| [openai](https://pypi.org/project/openai) |  |
| [nbtlib](https://pypi.org/project/nbtlib) |  |

```
pip install "mcdreforged >= 2.0.0" openai nbtlib
```

### 介绍

# LLM-Translator

[English](https://github.com/HeTao-yz/llm-translator/blob/main/README_EN.md)

> 本插件的开发灵感来源于 MCDR插件 [SimpleTranslator - 插件仓库 - MCDReforged](https://mcdreforged.com/zh-CN/plugin/simple_translator)

使用大语言模型进行提供游戏内玩家对话翻译，木牌文字翻译，书籍翻译。

插件默认使用 deepseek-chat 大语言模型进行翻译工作。

## 介绍

当服务器内有不同语种玩家时，使用此插件可以良好改善沟通情况。玩家聊天信息支持多服同步转发。使用大语言模型翻译，精准度相较传统机器翻译准确率更高，适应性更强。

支持翻译游戏内：

- 玩家对话信息

- 木牌文字

- 讲台上的书籍信息

## 配置

1. 插件第一次加载成功后，将在 `/config/llm-translator/` 文件夹下生成配置文件

2. 配置文件默认使用 `deepseek-chat` 模型进行中英翻译，若符合此需求，仅需在api_key处填写你的api密钥即可使用。否则请参考下方配置文件进行修改。

```json
{
    "first_language": "zh_cn",
    "secondary_language": "en_us",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat",
    "api_key": "enter-your-api-key",
    "is_proxy_to_other_servers": false,
    "proxy_servers": [
        {
            "address": "127.0.0.1",
            "port": 25575,
            "password": ""
        },
        {
            "address": "127.0.0.1",
            "port": 25576,
            "password": ""
        }
    ]
}
```

| 字段名                           | 数据类型       | 默认值                          | 说明                     |
| ----------------------------- | ---------- | ---------------------------- | ---------------------- |
| **first_language**            | string     | `"zh_cn"`                    | 主要语言，通常设置为用户的母语或主要使用语言 |
| **secondary_language**        | string     | `"en_us"`                    | 次要语言，需要翻译成的目标语言        |
| **base_url**                  | string     | `"https://api.deepseek.com"` | 基础请求地址                 |
| **model**                     | string     | `"deepseek-chat"`            | 语言模型名称                 |
| **api_key**                   | string     | *无默认值*                       | API 访问密钥               |
| **is_proxy_to_other_servers** | boolean    | `false`                      | 是否转发聊天翻译信息至其他服务器       |
| **proxy_servers**             | list[dict] | `[]`                         | 转发服务器配置列表。需要启用rcon     |

**proxy_servers** 的rcon服务器配置：

| 字段名          | 数据类型   | 默认值           | 说明             |
| ------------ | ------ | ------------- | -------------- |
| **address**  | string | `"127.0.0.1"` | 转发服务器地址        |
| **port**     | int    | *无默认值*        | 转发服务器端口号       |
| **password** | string | `""`          | 转发服务器认证密码（如需要） |

### 配置说明

1. **基础需求**：只需填写 `api_key` 即可使用默认的 DeepSeek 模型进行玩家对话中英翻译
2. **其他语言支持**：通过修改 `first_language` 和 `secondary_language` 可支持其他语言对的翻译
3. **多模型支持**：更换 `base_url` 和 `model` 可切换到其他 LLM 服务商
4. **聊天翻译信息转发功能**：玩家信息转发至其他服务器（通常适用于Velocity等代理端多子服且已经配置了聊天信息转发的服务器），请设置 `is_proxy_to_other_servers` 为 `true` 并配置 `proxy_servers` 列表

## 使用说明

### 玩家对话翻译

游戏内聊天信息添加前缀 **`t` 和空格** 发送即可翻译。

<img width="643" height="125" alt="image" src="https://github.com/user-attachments/assets/da3c74f2-e252-46b2-a826-114a121a9565" />

### 木牌信息及书籍信息翻译

*书籍信息：书需要放在讲台上才能翻译*

使用指令 `!!tr <x> <y> <z>` 即可翻译（ <x> <y> <z> 参数为木牌或讲台上书籍坐标，参数可使用 ~ 来代指当前玩家坐标）

<img width="1754" height="978" alt="image" src="https://github.com/user-attachments/assets/927ded2c-4a81-4ec5-9912-1f06d806bc6e" />

<img width="484" height="443" alt="image" src="https://github.com/user-attachments/assets/71e7b327-8e3c-4be4-98d2-d0e5a208bebd" />
<img width="1683" height="1375" alt="image" src="https://github.com/user-attachments/assets/419d5613-b0f6-4cd4-880e-2e3f3e065b30" />

## 其他

初次开发插件有不熟练之处或不完善之处。若使用时有bug或其他建议，欢迎至Github插件源仓库处提交Issue。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [LLM_Translator_v1.4.0.mcdr](https://github.com/HeTao-yz/llm-translator/releases/tag/v1.4.0) | 1.4.0 | 2025/12/09 15:29:28 | 9.5KB | 22 | [下载](https://github.com/HeTao-yz/llm-translator/releases/download/v1.4.0/LLM_Translator_v1.4.0.mcdr) |
| [LLM_Translator_v1.3.1.mcdr](https://github.com/HeTao-yz/llm-translator/releases/tag/v1.3.1) | 1.3.1 | 2025/11/27 05:42:59 | 7.09KB | 15 | [下载](https://github.com/HeTao-yz/llm-translator/releases/download/v1.3.1/LLM_Translator_v1.3.1.mcdr) |
| [llm-translator-v1.0.0.mcdr](https://github.com/HeTao-yz/llm-translator/releases/tag/v1.0.0) | 1.0.0 | 2025/11/24 15:00:48 | 5.63KB | 15 | [下载](https://github.com/HeTao-yz/llm-translator/releases/download/v1.0.0/llm-translator-v1.0.0.mcdr) |

