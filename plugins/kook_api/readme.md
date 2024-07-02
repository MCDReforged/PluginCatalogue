**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## kook_api

### Basic Information

- Plugin ID: `kook_api`
- Plugin Name: Kook API
- Version: 0.1.3
  - Metadata version: 0.1.3
  - Release version: 0.1.3
- Total downloads: 18
- Authors: [Aimerny](https://github.com/Aimerny)
- Repository: https://github.com/Aimerny/KookAPI
- Repository plugin page: https://github.com/Aimerny/KookAPI/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: A bridge of MC and Kook

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [requests](https://pypi.org/project/requests) |  |

```
pip install requests
```

### Introduction

# KookAPI
> 一个连接Kook和MCDR的API插件,通过Kook机器人事件代理服务将Kook服务器(频道)的事件接入MCDR

## 功能介绍
1. 实现了Kook文本事件的解析与转发.下游插件通过订阅该插件事件进行处理.(参考插件 -> [KookIn](https://github.com/Aimerny/KookIn))
2. 实现发送频道消息的api,进行MC与Kook双向通信

## 如何开始
1. 启动Kook机器人事件代理服务[Elix](https://github.com/Aimerny/Elix)
2. MCDR服务器启动并加载本插件
3. 修改配置文件以连接到Elix服务

## 配置项
`$MCDR/config/kook_api/conf.json`

| 配置项       | 配置说明            | 示例        |
| --------- | --------------- | --------- |
| kook_host | kook机器人代理地址     | 127.0.0.1 |
| kook_port | kook机器人代理ws端口   | 9000      |
| api_port  | kook机器人代理http端口 | 9001      |

## 接入方式
下游插件通过订阅 `kook_api.on_message`接收事件, 得到对应的 `message` 字面内容 + 完整的`event`数据


### 示例代码:
```python
def on_load(server: PluginServerInterface, old_plg):
    server.register_event_listener('kook_api.on_message', on_message)

def on_message(server: PluginServerInterface, raw_content: str, event: Event):
    server.logger.info(f"kook message event received: {raw_content}, event: {event}")
```

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [KookAPI-v0.1.3.mcdr](https://github.com/Aimerny/KookAPI/releases/tag/v0.1.3) | 0.1.3 | 2024/05/27 13:32:04 | 36.13KB | 14 | [Download](https://github.com/Aimerny/KookAPI/releases/download/v0.1.3/KookAPI-v0.1.3.mcdr) |
| [KookAPI-v0.1.2.mcdr](https://github.com/Aimerny/KookAPI/releases/tag/v0.1.2) | 0.1.2 | 2024/05/13 16:30:51 | 36.0KB | 2 | [Download](https://github.com/Aimerny/KookAPI/releases/download/v0.1.2/KookAPI-v0.1.2.mcdr) |
| [KookAPI-v0.1.1.mcdr](https://github.com/Aimerny/KookAPI/releases/tag/v0.1.1) | 0.1.1 | 2024/05/11 16:24:57 | 35.27KB | 2 | [Download](https://github.com/Aimerny/KookAPI/releases/download/v0.1.1/KookAPI-v0.1.1.mcdr) |

