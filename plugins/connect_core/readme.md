**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## connect_core

### Basic Information

- Plugin ID: `connect_core`
- Version: *Data fetching failed*
- Total downloads: N/A
- Authors: [zhongbai233](https://github.com/zhongbai2333)
- Repository: https://github.com/zhongbai2333/ConnectCore
- Repository plugin page: https://github.com/zhongbai2333/ConnectCore/tree/master
- Labels: [`API`](/labels/api/readme.md), [`Management`](/labels/management/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

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

*Data fetching failed*

