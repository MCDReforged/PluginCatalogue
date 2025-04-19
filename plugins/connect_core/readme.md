**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## connect_core

### Basic Information

- Plugin ID: `connect_core`
- Plugin Name: ConnectCore
- Version: 0.1.6
  - Metadata version: 0.1.6
  - Release version: 0.1.6
- Total downloads: 32
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
| [cryptography](https://pypi.org/project/cryptography) | \>=44.0.0 |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.4 |
| [prompt_toolkit](https://pypi.org/project/prompt_toolkit) | \>=3.0.50 |
| [psutil](https://pypi.org/project/psutil) | \>=6.1.1 |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0.2 |
| [websockets](https://pypi.org/project/websockets) | \>=14.2 |

```
pip install "cryptography>=44.0.0" "mcdreforged>=2.14.4" "prompt_toolkit>=3.0.50" "psutil>=6.1.1" "PyYAML>=6.0.2" "websockets>=14.2"
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
| [ConnectCore-v0.1.6.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.6) | 0.1.6 | 2025/02/07 08:21:06 | 53.61KB | 13 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.6/ConnectCore-v0.1.6.pyz) |
| [ConnectCore-v0.1.5.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.5) | 0.1.5 | 2025/02/06 15:15:40 | 53.58KB | 2 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.5/ConnectCore-v0.1.5.pyz) |
| [ConnectCore-v0.1.4.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.4) | 0.1.4 | 2025/02/04 14:44:35 | 53.3KB | 5 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.4/ConnectCore-v0.1.4.pyz) |
| [ConnectCore-v0.1.3.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.3) | 0.1.3 | 2025/02/04 07:24:02 | 52.66KB | 2 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.3/ConnectCore-v0.1.3.pyz) |
| [ConnectCore-v0.1.2.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.2) | 0.1.2 | 2025/02/04 01:30:25 | 51.13KB | 2 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.2/ConnectCore-v0.1.2.pyz) |
| [ConnectCore-v0.1.1.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.1) | 0.1.1 | 2025/02/03 15:25:34 | 50.58KB | 2 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.1/ConnectCore-v0.1.1.pyz) |
| [ConnectCore-v0.1.0.pyz](https://github.com/zhongbai2333/ConnectCore/releases/tag/v0.1.0) | 0.1.0 | 2025/01/26 02:57:59 | 47.95KB | 6 | [Download](https://github.com/zhongbai2333/ConnectCore/releases/download/v0.1.0/ConnectCore-v0.1.0.pyz) |

