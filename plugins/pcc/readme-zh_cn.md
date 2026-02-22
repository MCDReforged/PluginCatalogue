[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## pcc

### 基本信息

- 插件 ID: `pcc`
- 插件名: ProxiedChatConnection
- 版本: 0.3.5
  - 元数据版本: 0.3.5
  - 发布版本: 0.3.5
- 总下载量: 713
- 作者: [zyxkad](https://github.com/zyxkad)
- 仓库: https://github.com/kmcsr/pcc_mcdr
- 仓库插件页: https://github.com/kmcsr/pcc_mcdr/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 允许你默默发送以及自动补全MCDR指令

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.14.0 |
| [kpi](/plugins/kpi/readme-zh_cn.md) | ~1.5.1 |
| [loginproxy](/plugins/loginproxy/readme-zh_cn.md) | ~0.9.0 |
| [packet_parser](/plugins/packet_parser/readme-zh_cn.md) | ~0.0.3 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍


- [English](https://github.com/kmcsr/pcc_mcdr/tree/main/README.MD)
- 中文

# PCC

一个允许你默默发送 MCDR 指令的插件.  
也允许你在游戏内自动补全 MCDR 指令

需要将 `loginproxy/config.json` 下的 `enable_packet_proxy` 选项设为 `true`

不支持小于 1.19.2 的版本

实测 1.19.2, 1.21.1 可用, 其他版本未知

## 特性

- 动态补全
- 完整的权限检查

## 依赖

| ID                                                      | 下载链接                                                 |
| ------------------------------------------------------- | ---------------------------------------------------- |
| [kpi](https://github.com/kmcsr/kpi_mcdr)                | <https://github.com/kmcsr/kpi_mcdr/releases>         |
| [loginproxy](https://github.com/kmcsr/login_proxy_mcdr) | <https://github.com/kmcsr/login_proxy_mcdr/releases> |

## 用法

本插件加载后会在玩家登录后将 MCDR 指令注册到 Minecraft 指令树内,
仅需使用 `/!!` 前缀自动补全 MCDR 指令.

PCC 假设所有以 `!!` 或 `/!!` 开头的文本为 MCDR 指令. 不以 `!!` 开头的 MCDR 指令无法被 PCC 正确代理.

## 选项

### `register_vanilla_command`

启用后, PCC 会在玩家登录后注册一个名为 `<!!MCDR-command>` 的动态指令节点以自动补全使用 Minecraft 指令形式发送的 MCDR 指令.  
默认启用

### `proxy_mcdr_chat_command`

启用后, PCC 会代理文本态的 MCDR 指令, 并阻止其被发送到服务端. 可能会导致部分旧版插件无法执行指令.  
默认启用

### `chat_preview_suggestion`

启用后, PCC 会要求客户端在打开聊天栏时动态发送聊天内容到服务端, 解析 MCDR 指令并返回建议选项.  
默认禁用

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ProxiedChatConnection-v0.3.5.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.5) | 0.3.5 | 2025/04/23 15:46:25 | 17.76KB | 337 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.5/ProxiedChatConnection-v0.3.5.mcdr) |
| [ProxiedChatConnection-v0.3.4.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.4) | 0.3.4 | 2025/04/15 16:34:15 | 17.76KB | 49 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.4/ProxiedChatConnection-v0.3.4.mcdr) |
| [ProxiedChatConnection-v0.3.3.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.3) | 0.3.3 | 2025/03/10 15:15:32 | 17.77KB | 110 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.3/ProxiedChatConnection-v0.3.3.mcdr) |
| [ProxiedChatConnection-v0.3.2.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.2) | 0.3.2 | 2025/02/08 04:57:20 | 17.04KB | 66 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.2/ProxiedChatConnection-v0.3.2.mcdr) |
| [ProxiedChatConnection-v0.3.1.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.1) | 0.3.1 | 2025/02/07 23:55:48 | 16.87KB | 28 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.1/ProxiedChatConnection-v0.3.1.mcdr) |
| [ProxiedChatConnection-v0.3.0.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.3.0) | 0.3.0 | 2025/02/07 15:37:44 | 18.95KB | 27 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.3.0/ProxiedChatConnection-v0.3.0.mcdr) |
| [ProxiedChatConnection-v0.2.0.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.2.0) | 0.2.0 | 2025/02/06 23:23:54 | 18.27KB | 68 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.2.0/ProxiedChatConnection-v0.2.0.mcdr) |
| [ProxiedChatConnection-v0.1.0.mcdr](https://github.com/kmcsr/pcc_mcdr/releases/tag/v0.1.0) | 0.1.0 | 2025/02/06 20:30:55 | 17.54KB | 28 | [下载](https://github.com/kmcsr/pcc_mcdr/releases/download/v0.1.0/ProxiedChatConnection-v0.1.0.mcdr) |

