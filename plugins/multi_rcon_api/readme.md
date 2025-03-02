**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## multi_rcon_api

### Basic Information

- Plugin ID: `multi_rcon_api`
- Version: *Data fetching failed*
- Total downloads: N/A
- Authors: [YehowahLiu](https://github.com/YehowahLiu)
- Repository: https://github.com/FAS-Server/MultiRconAPI
- Repository plugin page: https://github.com/FAS-Server/MultiRconAPI/tree/main
- Labels: [`Tool`](/labels/tool/readme.md), [`API`](/labels/api/readme.md)
- Description: *Data fetching failed*

### Dependencies

*Data fetching failed*

### Requirements

*Data fetching failed*

### Introduction

# Multi Rcon API

![MCDReforged](https://img.shields.io/badge/dynamic/json?label=MCDReforged&query=dependencies.mcdreforged&url=https%3A%2F%2Fraw.githubusercontent.com%2FFAS-Server%2FMultiRconAPI%2Fmaster%2Fmcdreforged.plugin.json&style=plastic) ![license](https://img.shields.io/github/license/FAS-Server/MultiRconAPI?style=plastic) ![build status](https://img.shields.io/github/workflow/status/FAS-Server/MultiRconAPI/CI%20for%20MCDR%20Plugin?label=build&style=plastic) ![Release](https://img.shields.io/github/v/release/FAS-Server/MultiRconAPI?style=plastic) ![total download](https://img.shields.io/github/downloads/FAS-Server/MultiRconAPI/total?label=total%20download&style=plastic)

[English](https://github.com/FAS-Server/MultiRconAPI/tree/main/README_EN.md) | 简体中文

一个使用rcon来做到对群组服进行简单操作的api

## 配置

1. 配置文件

`broadcast `: 是否将特定事件通过rcon进行广播, 其中 `startup`为服务器启动事件,  `stop` 为服务器关闭事件

`self_server`: 存储此子服务器名称, 用于在通过rcon广播事件时作为标识

`data_file`: 数据文件存放的地址

示例配置文件如下:

```json
{
    "broadcast": {
        "startup": true,
        "stop": false
    },
    "self_server": "Survival",
    "data_file": "config/MultiRconAPI_ServerList.json"
}
```

2. 数据文件

`servers` : 存储群组服务器中所有的rcon信息, 键为服务器名, 建议与跨服中的名称保持一致；值为rcon的 地址/端口/ 密码 等信息

`groups`: 存储自定义服务器分组信息

示例数据文件如下:

```json
{
    "servers": {
        "Survival": {
            "address": "localhost",
            "port": "25565",
            "password": "default_password_please_change"
        },
        "Creative": {
            "address": "localhost",
            "port": "25566",
            "password": "default_password_please_change"
        },
        "Mirror": {
            "address": "localhost",
            "port": "25567",
            "password": "default_password_please_change"
        }
    },
    "groups": {
        "g_creative": ["Creative", "Mirror"]
    }
}
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

*Data fetching failed*

