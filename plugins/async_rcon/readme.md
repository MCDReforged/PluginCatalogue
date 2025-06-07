**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## async_rcon

### Basic Information

- Plugin ID: `async_rcon`
- Plugin Name: AsyncRconClient
- Version: 0.0.4
  - Metadata version: 0.0.4
  - Release version: 0.0.4
- Total downloads: 22
- Authors: [Mooling0602](https://github.com/Mooling0602)
- Repository: https://github.com/Mooling0602/AsyncRconClient
- Repository plugin page: https://github.com/Mooling0602/AsyncRconClient/tree/main
- Labels: [`API`](/labels/api/readme.md), [`Information`](/labels/information/readme.md)
- Description: A simple async rcon client.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.1 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [aiofiles](https://pypi.org/project/aiofiles) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [pydantic](https://pypi.org/project/pydantic) |  |

```
pip install aiofiles mcdreforged pydantic
```

### Introduction

# AsyncRconClient
A simple async rcon client.

## Usage
Run `async_rcon/__init__.py` directly.

### With MCDR
Install plugin from release.
> After plugin submitted to MCDR PluginCatalogue, you can install by  `!!MCDR plg install async_rcon [--confirm]`

Rcon client will start automatically when plugin is loading.

Use `@rcon <command>` to execute commands and get responses from target rcon server.

Use `@rcon connect` to start rcon client, use  `@rcon disconnect` to close it.

Use `@rcon reload` to reload plugin, equal to `!!MCDR plg reload async_rcon`

## API
Can be imported in MCDR plugins. If you want to use this module without MCDR, you should just import from `async_rcon/__init__.py`.
```python
import async_rcon.entry as rcon

from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, _prev_module):
    pass


async def main(server: PluginServerInterface):
    if rcon.rcon_task:
        response = rcon.loop.create_task(rcon.client.send_command("list"))
        await response
        server.logger.info(f"[Response] \n{response.result()}")

    # Following is some safe way to control rcon client
    server.execute_command("@rcon disconnect", ConsoleCommandSource) # Disconnect rcon client if you want.
    server.execute_command("@rcon connect", ConsoleCommandSource) # Reconnect rcon client if you want.
```

If you want to connect or disconnect rcon client by directly call the functions in async_rcon.entry, you should read source code carefully because it may dangerous.

And if any bugs found plz issue them, I'll be glad to fix.

## License & Credits
This project is licensed under the GPL-3.0 License.

Used projects:
- [RconConnection](https://docs.mcdreforged.com/zh-cn/latest/code_references/minecraft_tools.html#mcdreforged.minecraft.rcon.rcon_connection.RconConnection): LGPL-3.0
> A built-in module in MCDReforged.

Thanks the following projects for documentation support
- [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Mooling0602/AsyncRconClient)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [AsyncRconClient-v0.0.4.mcdr](https://github.com/Mooling0602/AsyncRconClient/releases/tag/0.0.4) | 0.0.4 | 2025/05/29 14:36:38 | 7.09KB | 7 | [Download](https://github.com/Mooling0602/AsyncRconClient/releases/download/0.0.4/AsyncRconClient-v0.0.4.mcdr) |
| [AsyncRconClient-v0.0.3.mcdr](https://github.com/Mooling0602/AsyncRconClient/releases/tag/0.0.3) | 0.0.3 | 2025/05/29 13:40:37 | 6.43KB | 4 | [Download](https://github.com/Mooling0602/AsyncRconClient/releases/download/0.0.3/AsyncRconClient-v0.0.3.mcdr) |
| [AsyncRconClient-v0.0.2.mcdr](https://github.com/Mooling0602/AsyncRconClient/releases/tag/0.0.2) | 0.0.2 | 2025/05/29 12:04:00 | 6.05KB | 4 | [Download](https://github.com/Mooling0602/AsyncRconClient/releases/download/0.0.2/AsyncRconClient-v0.0.2.mcdr) |
| [AsyncRconClient-v0.0.1.mcdr](https://github.com/Mooling0602/AsyncRconClient/releases/tag/0.0.1) | 0.0.1 | 2025/05/28 16:44:39 | 4.91KB | 7 | [Download](https://github.com/Mooling0602/AsyncRconClient/releases/download/0.0.1/AsyncRconClient-v0.0.1.mcdr) |

