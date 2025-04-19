**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## bedrock_liteloader_handler

### Basic Information

- Plugin ID: `bedrock_liteloader_handler`
- Plugin Name: BedrockLiteloaderHandler
- Version: 1.2.1
  - Metadata version: 1.2.1
  - Release version: 1.2.1
- Total downloads: 66
- Authors: [Elec glacier](https://github.com/Elec-Glacier), [jiangyan](https://github.com/jiangyan03)
- Repository: https://github.com/Elec-Glacier/liteloader_handler
- Repository plugin page: https://github.com/Elec-Glacier/liteloader_handler/tree/main
- Labels: [`Handler`](/labels/handler/readme.md)
- Description: A handler which allows BDS(bedrock dedicated server) to use MCDR

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.13.2 |

```
pip install "mcdreforged>=2.13.2"
```

### Introduction

**English** | [中文](https://github.com/Elec-Glacier/liteloader_handler/blob/main/README_cn.md)

# Bedrock Liteloader Handler
A handler which allows BDS(bedrock dedicated server) to use MCDR and its plugins.

## Before you use
Vanilla BDS does not have the function to print out player chat log.
So it is recommended to use a behavior pack or modify BDS to std out your chat log

## Usage
1. Download the latest version from [releases](https://github.com/Elec-Glacier/liteloader_handler/releases)
2. Place this plugin in your MCDR "plugins" directory
3. Start MCDR
4. Change and choose the handler in mcdreforged "config" directory
5. reload the config

## Notice
After LeviLamina@1.0.0, Popen() can't get stdout after server being modded. You can use a pty terminal as bridge. You can see more details in [this issue](https://github.com/Elec-Glacier/liteloader_handler/issues/13)
After version 1.2.0, this handler has adapted to PrimeBackup. You can turn it off in config.

## MCDR plugins installation notice
Since Bedrock and Java edition are different in many aspects, so read the introductions of other MCDR plugins you want to use and make sure them would work correctly before you place them into plugins directory.

## Attentions
Due to a [BDS bug](https://bugs.mojang.com/browse/BDS-3791), you might need to use some server modified plugins to let MCDR work correctly, such as [UnicodeFixer](https://www.minebbs.com/resources/unicodefixer.6991/).

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [BedrockLiteloaderHandler-v1.2.1.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.2.1) | 1.2.1 | 2025/03/14 17:56:17 | 6.04KB | 15 | [Download](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.2.1/BedrockLiteloaderHandler-v1.2.1.mcdr) |
| [BedrockLiteloaderHandler-v1.2.0.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.2.0) | 1.2.0 | 2025/01/31 13:07:18 | 6.0KB | 8 | [Download](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.2.0/BedrockLiteloaderHandler-v1.2.0.mcdr) |
| [BedrockLiteloaderHandler-v1.1.2.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.1.2) | 1.1.2 | 2025/01/05 05:21:18 | 5.69KB | 16 | [Download](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.1.2/BedrockLiteloaderHandler-v1.1.2.mcdr) |
| [BedrockLiteloaderHandler-v1.1.1.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.1.1) | 1.1.1 | 2024/12/14 11:34:03 | 4.32KB | 10 | [Download](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.1.1/BedrockLiteloaderHandler-v1.1.1.mcdr) |
| [BedrockLiteloaderHandler-v1.0.0.mcdr](https://github.com/Elec-Glacier/liteloader_handler/releases/tag/1.0.0) | 1.0.0 | 2024/12/07 20:36:24 | 6.91KB | 17 | [Download](https://github.com/Elec-Glacier/liteloader_handler/releases/download/1.0.0/BedrockLiteloaderHandler-v1.0.0.mcdr) |

