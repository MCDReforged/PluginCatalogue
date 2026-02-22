**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## connect_core

### Basic Information

- Plugin ID: `connect_core`
- Plugin Name: ConnectCore
- Version: 0.2.6
  - Metadata version: 0.2.6
  - Release version: 0.2.6
- Total downloads: 620
- Authors: [zhongbai233](https://github.com/zhongbai2333)
- Repository: https://github.com/zhongbai2333/ConnectCore
- Repository plugin page: https://github.com/zhongbai2333/ConnectCore/tree/master
- Labels: [`API`](/labels/api/readme.md), [`Management`](/labels/management/readme.md)
- Description: Connect your Minecraft Server together and control it.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [cryptography](https://pypi.org/project/cryptography) |  |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [prompt_toolkit](https://pypi.org/project/prompt_toolkit) |  |
| [psutil](https://pypi.org/project/psutil) |  |
| [PyYAML](https://pypi.org/project/PyYAML) |  |
| [websockets](https://pypi.org/project/websockets) |  |

```
pip install cryptography mcdreforged prompt_toolkit psutil PyYAML websockets
```

### Introduction

# ConnectCore

This is a plugin for MCDReforged that can also be used independently. It allows you to set up your server as a plugin control group, primarily used for communication between plugins across different sub-servers, such as providing APIs and communication support for cross-server chat. It offers high security and easy configuration, making it suitable for various server environments.

English | [简中](https://github.com/zhongbai2333/ConnectCore/tree/master/README_zh.md)

## Usage

### Standalone Usage

1. Place the `ConnectCore.pyz` file in an empty folder.
2. Run the following command in the terminal:
   `python ConnectCore.pyz server` or `python ConnectCore.pyz client` to start the server or client.
3. Follow the prompts to configure.

### Usage as an MCDR Plugin

1. Place the `ConnectCore.pyz` file in the MCDR plugin directory (usually the `plugins` folder).
2. Start the MCDR server, then use the `!!connectcore init` command to enable the initialization process.
3. Follow the prompts to configure.

## Development

- A detailed English development documentation can be found on the [WIKI](https://github.com/zhongbai2333/ConnectCore/wiki/%5BDevelop%5D-API).
- For sample plugins, please visit [ExamplePlugin](https://github.com/zhongbai2333/ExamplePlugin).

## Notes

- Ensure that your server and client can properly connect to the network.
- A group of servers has only one server-side instance, but multiple clients can connect.
- If you encounter any issues, please refer to the [WIKI](https://github.com/zhongbai2333/ConnectCore/wiki) or contact the developer.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ConnectCore-v0.2.6.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.2.6) | 0.2.6 | 2025/06/26 09:27:16 | 58.69KB | 48 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.2.6/ConnectCore-v0.2.6.pyz) |
| [ConnectCore-v0.2.4.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.2.4) | 0.2.4 | 2025/05/04 17:14:44 | 57.72KB | 47 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.2.4/ConnectCore-v0.2.4.pyz) |
| [ConnectCore-v0.2.3.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.2.3) | 0.2.3 | 2025/05/04 05:11:58 | 57.64KB | 34 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.2.3/ConnectCore-v0.2.3.pyz) |
| [ConnectCore-v0.2.2.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.2.2) | 0.2.2 | 2025/05/03 06:38:07 | 55.16KB | 34 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.2.2/ConnectCore-v0.2.2.pyz) |
| [ConnectCore-v0.2.1.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.2.1) | 0.2.1 | 2025/04/30 23:18:03 | 54.71KB | 35 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.2.1/ConnectCore-v0.2.1.pyz) |
| [ConnectCore-v0.2.0.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.2.0) | 0.2.0 | 2025/04/29 11:59:17 | 54.69KB | 37 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.2.0/ConnectCore-v0.2.0.pyz) |
| [ConnectCore-v0.1.10.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.10) | 0.1.10 | 2025/04/28 15:09:25 | 54.48KB | 37 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.10/ConnectCore-v0.1.10.pyz) |
| [ConnectCore-v0.1.9.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.9) | 0.1.9 | 2025/04/27 14:41:51 | 54.48KB | 36 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.9/ConnectCore-v0.1.9.pyz) |
| [ConnectCore-v0.1.8.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.8) | 0.1.8 | 2025/04/26 09:59:29 | 54.11KB | 37 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.8/ConnectCore-v0.1.8.pyz) |
| [ConnectCore-v0.1.7.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.7) | 0.1.7 | 2025/04/25 23:15:09 | 53.67KB | 32 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.7/ConnectCore-v0.1.7.pyz) |
| [ConnectCore-v0.1.6.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.6) | 0.1.6 | 2025/02/07 08:21:06 | 53.61KB | 43 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.6/ConnectCore-v0.1.6.pyz) |
| [ConnectCore-v0.1.5.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.5) | 0.1.5 | 2025/02/06 15:15:40 | 53.58KB | 32 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.5/ConnectCore-v0.1.5.pyz) |
| [ConnectCore-v0.1.4.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.4) | 0.1.4 | 2025/02/04 14:44:35 | 53.3KB | 35 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.4/ConnectCore-v0.1.4.pyz) |
| [ConnectCore-v0.1.3.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.3) | 0.1.3 | 2025/02/04 07:24:02 | 52.66KB | 31 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.3/ConnectCore-v0.1.3.pyz) |
| [ConnectCore-v0.1.2.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.2) | 0.1.2 | 2025/02/04 01:30:25 | 51.13KB | 33 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.2/ConnectCore-v0.1.2.pyz) |
| [ConnectCore-v0.1.1.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.1) | 0.1.1 | 2025/02/03 15:25:34 | 50.58KB | 32 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.1/ConnectCore-v0.1.1.pyz) |
| [ConnectCore-v0.1.0.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.0) | 0.1.0 | 2025/01/26 02:57:59 | 47.95KB | 37 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.0/ConnectCore-v0.1.0.pyz) |

