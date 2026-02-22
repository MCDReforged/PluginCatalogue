[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## cq_qq_api

### 基本信息

- 插件 ID: `cq_qq_api`
- 插件名: cq_qq_api
- 版本: 1.6.0
  - 元数据版本: 1.6.0
  - 发布版本: 1.6.0
- 总下载量: 1461
- 作者: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- 仓库: https://github.com/XueK66/PF-cq_qq_api
- 仓库插件页: https://github.com/XueK66/PF-cq_qq_api/tree/master/src
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 处理QQ通信的websocket应用

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [websocket-client](https://pypi.org/project/websocket-client) | \>=1.4.0 |

```
pip install "websocket-client>=1.4.0"
```

### 介绍


# PF-cq_qq_api

[![仓库大小](https://img.shields.io/github/repo-size/XueK66/PF-cq_qq_api?style=flat-square&label=仓库占用)](https://github.com/XueK66/PF-cq_qq_api/tree/master/src//)
[![最新版](https://img.shields.io/github/v/release/XueK66/PF-cq_qq_api?style=flat-square&label=最新版)](https://github.com/XueK66/PF-cq_qq_api/releases/latest/download/YourRepoName.mcdr)
[![Issues](https://img.shields.io/github/issues/XueK66/PF-cq_qq_api?style=flat-square&label=Issues)](https://github.com/XueK66/PF-cq_qq_api/issues)
[![已关闭issues](https://img.shields.io/github/issues-closed/XueK66/PF-cq_qq_api?style=flat-square&label=已关闭%20Issues)](https://github.com/XueK66/PF-cq_qq_api/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/XueK66/PF-cq_qq_api/total?style=flat-square&label=下载量)](https://github.com/XueK66/PF-cq_qq_api/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/XueK66/PF-cq_qq_api/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/XueK66/PF-cq_qq_api/releases/latest)


> PFingan服务器MCDRQQ机器人插件
> 
> 基于CQ码的**正向Websocket**QQ连接机器人
> 
> 提供MCDR机器人插件接口，方便聊天类机器人的构建

技术支持：XueK__ [前往主页](https://github.com/XueK66)

使用方式：
* 将Release里面的cq_qq_api.mcdr放入`/plugins`
* 加载后，在`/config/cq_qq_api/config.yml`中配置机器人
* 与机器人连接请参考文档：[PF系列插件官方文档 - CQ-QQ-API - 机器人食用指南](https://pf-doc.pfingan.com/main.html?path=PF-cq-api%2F%E6%9C%BA%E5%99%A8%E4%BA%BA%E9%A3%9F%E7%94%A8%E6%8C%87%E5%8D%97%2FREADME.md)

## 依赖
#### Python
- [Python™](https://www.python.org/)
#### Python模块
- 已存储在插件对应的文件夹内的 [requirements.txt](https://github.com/XueK66/PF-cq_qq_api/tree/master/src/requirements.txt) 中, 可以使用 `pip install -r requirements.txt` 安装

基本功能：聊天互相转发

## 使用方式

#### 调用机器人
```
bot = server.get_plugin_instance("cq_qq_api").get_bot()
```

#### 调用例子 - 发送群聊消息
更多接口详情可查看`bot.py`或查看[Onebot_11_API_标准](https://github.com/botuniverse/onebot-11/blob/master/api/public.md)
```
bot = server.get_plugin_instance("cq_qq_api").get_bot()
bot.send_group_msg(group_id, message)
```


## 配置

#### 服务端配置 - Server
- config.json

> | 配置项 | 默认值 | 说明 |
> | - | - | - |
> | host | `127.0.0.1` | 接收数据上报的地址 |
> | port | `8080` | 对应数据上报的端口 | 
> | post_path | "" | 对应数据上报的终点名 |
> | token | "" | 对应数据上报的token，用于加密信息 |
> | language | "zh" | 语言包[zh/en] |
> | max_wait_time | 10 | 最长等待QQAPI的时间（秒） |
```
{
    "host": "127.0.0.1",
    "port": 8080,
    "post_path": "",
    "token": "",
    "language": "zh",
    "max_wait_time": 10
}
```

#### QQ机器人配置
**以下为必要配置！**
> | 配置项 | 默认值 | 说明 |
> | - | - | - |
> | 正向websocket服务端口 | `8080` | 接收数据上报的端口 |
> | 消息上报格式 | CQ码 | 机器人基于CQ码进行解析 |

# 有BUG或是新的IDEA
如果需要更多联动或提交想法和问题请提交 [issues](https://github.com/LoosePrince/PF-GUGUBot/issues) 或 QQ [1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 提交！ <br />
视情况添加，请勿联系他人（开发者：[雪开](https://github.com/XueK66)）

# 致谢
- 消息格式参考 from [go-cqhttp](https://docs.go-cqhttp.org/)
- 接口参考 from [Onebot_11_API](https://github.com/botuniverse/onebot-11/blob/master/api/public.md)
- 消息解析参考 from [qq_api](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/6049c6a6808383b2d5fb219598a79b975905fa84/qq_api) 作者 [AnzhiZhang](https://github.com/AnzhiZhang)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [cq_qq_api-v1.6.0.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.6.0) | 1.6.0 | 2025/10/09 03:44:52 | 29.94KB | 132 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.6.0/cq_qq_api-v1.6.0.mcdr) |
| [cq_qq_api-v1.5.0.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.5.0) | 1.5.0 | 2025/08/20 01:54:20 | 27.88KB | 149 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.5.0/cq_qq_api-v1.5.0.mcdr) |
| [cq_qq_api-v1.4.0.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.4.0) | 1.4.0 | 2025/08/10 21:17:52 | 27.84KB | 64 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.4.0/cq_qq_api-v1.4.0.mcdr) |
| [cq_qq_api-v1.3.0.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.3.0) | 1.3.0 | 2025/06/14 23:40:03 | 27.68KB | 180 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.3.0/cq_qq_api-v1.3.0.mcdr) |
| [cq_qq_api-v1.2.2.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.2.2) | 1.2.2 | 2025/06/14 05:40:00 | 27.52KB | 47 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.2.2/cq_qq_api-v1.2.2.mcdr) |
| [cq_qq_api-v1.2.1.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.2.1) | 1.2.1 | 2025/02/11 06:55:35 | 10.99KB | 234 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.2.1/cq_qq_api-v1.2.1.mcdr) |
| [cq_qq_api-v1.1.0.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.1.0) | 1.1.0 | 2025/01/06 04:03:12 | 24.72KB | 150 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.1.0/cq_qq_api-v1.1.0.mcdr) |
| [cq_qq_api-v1.0.5.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.0.5) | 1.0.5 | 2024/11/08 05:11:50 | 10.09KB | 150 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.0.5/cq_qq_api-v1.0.5.mcdr) |
| [cq_qq_api-v1.0.4.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.0.4) | 1.0.4 | 2024/11/01 00:16:07 | 10.08KB | 48 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.0.4/cq_qq_api-v1.0.4.mcdr) |
| [cq_qq_api-v1.0.3.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/v1.0.3) | 1.0.3 | 2024/10/05 18:24:19 | 9.75KB | 80 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/v1.0.3/cq_qq_api-v1.0.3.mcdr) |
| [cq_qq_api-v1.0.2.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/1.0.2) | 1.0.2 | 2024/09/18 16:46:20 | 9.61KB | 80 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/1.0.2/cq_qq_api-v1.0.2.mcdr) |
| [cq_qq_api-v1.0.1.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/1.0.1) | 1.0.1 | 2024/08/17 23:52:09 | 8.87KB | 96 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/1.0.1/cq_qq_api-v1.0.1.mcdr) |
| [cq_qq_api-v1.0.0.mcdr](https://github.com/XueK66/PF-cq_qq_api/releases/tag/1.0.0) | 1.0.0 | 2024/08/15 16:19:41 | 8.77KB | 51 | [下载](https://github.com/XueK66/PF-cq_qq_api/releases/download/1.0.0/cq_qq_api-v1.0.0.mcdr) |

