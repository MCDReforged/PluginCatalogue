[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## kook_api

### 基本信息

- 插件 ID: `kook_api`
- 插件名: Kook API
- 版本: 0.1.3
  - 元数据版本: 0.1.3
  - 发布版本: 0.1.3
- 总下载量: 18
- 作者: [Aimerny](https://github.com/Aimerny)
- 仓库: https://github.com/Aimerny/KookAPI
- 仓库插件页: https://github.com/Aimerny/KookAPI/tree/main
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 打通kook机器人与mc

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [requests](https://pypi.org/project/requests) |  |

```
pip install requests
```

### 介绍

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

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [KookAPI-v0.1.3.mcdr](https://github.com/Aimerny/KookAPI/releases/tag/v0.1.3) | 0.1.3 | 2024/05/27 13:32:04 | 36.13KB | 14 | [下载](https://github.com/Aimerny/KookAPI/releases/download/v0.1.3/KookAPI-v0.1.3.mcdr) |
| [KookAPI-v0.1.2.mcdr](https://github.com/Aimerny/KookAPI/releases/tag/v0.1.2) | 0.1.2 | 2024/05/13 16:30:51 | 36.0KB | 2 | [下载](https://github.com/Aimerny/KookAPI/releases/download/v0.1.2/KookAPI-v0.1.2.mcdr) |
| [KookAPI-v0.1.1.mcdr](https://github.com/Aimerny/KookAPI/releases/tag/v0.1.1) | 0.1.1 | 2024/05/11 16:24:57 | 35.27KB | 2 | [下载](https://github.com/Aimerny/KookAPI/releases/download/v0.1.1/KookAPI-v0.1.1.mcdr) |

