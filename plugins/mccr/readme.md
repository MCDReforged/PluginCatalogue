**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mccr

### Basic Information

- Plugin ID: `mccr`
- Plugin Name: MCDR Command Completer Reforged
- Version: 1.1.1
  - Metadata version: 1.1.1
  - Release version: 1.1.1
- Total downloads: 201
- Authors: [DancingSnow](https://github.com/DancingSnow0517), [ZhuRuoLing](https://github.com/ZhuRuoLing)
- Repository: https://github.com/DancingSnow0517/MCDRCommandCompleterReforged
- Repository plugin page: https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/tree/master
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: MCDR Command Completer

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>2.14.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [fastapi](https://pypi.org/project/fastapi) |  |
| [uvicorn](https://pypi.org/project/uvicorn) |  |

```
pip install fastapi uvicorn
```

### Introduction

<div align="center">

# MCDRCommandCompletion Reforged
_✨ Another wonderful implementation of client-side MCDR command completion ✨_

</div>

[Readme zh_CN](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/tree/master//README.md)

> [!WARNING]  
> Requires [FabricMod-MCDRCommandCompletionReforged-Mod](https://github.com/ZhuRuoLing/MCDRCommandCompletionReforged-Mod) to work

## Usage
- Download the latest release of this plugin from [Release](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases) and install it.
- Ensure that the server you join has this mod and the corresponding plugin installed.
- Use `!` in the chat bar to trigger completion.

## Configuration
Configuration file can be found at `config/mccr/config.json`

* ### http_port
  #### `http_port` represents the port used by the HTTP server, this value will be automatically configured to the `server mod` by the command
  - Type: `int`
  - Any integer between `1-65535`
  - Default value: `8080`

## License
This project follows the GNU LGPL V3 license

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MCDRCommandCompleterReforged-v1.1.1.mcdr](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/tag/1.1.1) | 1.1.1 | 2025/03/20 02:29:54 | 4.67KB | 140 | [Download](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/download/1.1.1/MCDRCommandCompleterReforged-v1.1.1.mcdr) |
| [MCDRCommandCompleterReforged-v1.1.0.mcdr](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/tag/1.1.0) | 1.1.0 | 2025/03/19 11:32:09 | 4.65KB | 28 | [Download](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/download/1.1.0/MCDRCommandCompleterReforged-v1.1.0.mcdr) |
| [MCDRCommandCompleterReforged-v1.0.0.mcdr](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/tag/1.0.0) | 1.0.0 | 2025/03/18 18:13:33 | 4.63KB | 33 | [Download](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/download/1.0.0/MCDRCommandCompleterReforged-v1.0.0.mcdr) |

