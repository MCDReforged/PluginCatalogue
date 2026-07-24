[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## title_prefix_handler

### 基本信息

- 插件 ID: `title_prefix_handler`
- 插件名: Title Prefix Handler
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 65
- 作者: [DCS](https://github.com/ayuan94/)
- 仓库: https://github.com/ayuan94/TitlePrefixHandler
- 仓库插件页: https://github.com/ayuan94/TitlePrefixHandler/tree/master
- 标签: [`服务端处理器`](/labels/handler/readme-zh_cn.md)
- 描述: MCDR handler plugin that fixes player name parsing when title prefixes are added by Team prefixes.

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.0 |

```
pip install "mcdreforged>=2.14.0"
```

### 介绍

# Title Prefix Handler

A lightweight MCDReforged handler designed to fix player name parsing when the `DCSTitleManager` plugin applies title prefixes via Minecraft `Team` prefixes.

## Why use this handler

`DCSTitleManager` adds title prefixes to player names by modifying `Team` prefixes. In some handler configurations, this can cause player names to be mis-parsed when chat messages contain multiple bracketed prefixes.

This handler removes the extra title prefix from the raw server output before MCDR parses the player name, allowing the title manager plugin to work correctly without breaking chat parsing.

## Features

- Removes the third title prefix segment from server output
- Preserves the actual player name and chat content
- Compatible with MCDReforged >= 2.14.0
- Minimal, single-file handler implementation

## Installation

1. Download the handler package and place it in your MCDR plugin directory.
2. Ensure `mcdreforged` is installed in your Python environment.
3. Enable the handler in the MCDR configuration.

## Usage

Add the handler to your MCDR configuration and enable it before loading `DCSTitleManager`.

```python
import re
from mcdreforged.handler.impl import VanillaHandler

PLUGIN_METADATA = {
    'id': 'title_prefix_handler',
    'version': '1.0.0',
}

class TitlePrefixHandler(VanillaHandler):
    def get_name(self) -> str:
        return 'title_prefix_handler'

    def pre_parse_server_stdout(self, text: str):
        text = super().pre_parse_server_stdout(text)
        text = re.sub(
            r'^(.*?\[[^]]+\].*?\[[^]]+\].*?)\[[^]]+\]\s+',
            r'\1',
            text
        )
        return text

    def parse_server_stdout(self, text: str):
        info = super().parse_server_stdout(text)
        if info.player is None:
            m = re.fullmatch(r'<\[[^]]+](?P<name>[^>]+)> (?P<message>.*)', info.content)
            if m is not None:
                name = m['name'].strip()
                if self._verify_player_name(name):
                    info.player, info.content = name, m['message']
        return info


def on_load(server, prev_module):
    server.register_server_handler(TitlePrefixHandler())
```

## Notes

- Use this handler together with `DCSTitleManager`.
- Clear existing Minecraft `Team` state before enabling the handler to avoid prefix conflicts.

## License

This project is released under the GPL-3.0 License.

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [TitlePrefixHandler-v1.0.0.mcdr](https://github.com/ayuan94/TitlePrefixHandler/releases/tag/v1.0.0) | 1.0.0 | 2026/05/24 08:26:38 | 2.56KB | 65 | [下载](https://github.com/ayuan94/TitlePrefixHandler/releases/download/v1.0.0/TitlePrefixHandler-v1.0.0.mcdr) |

