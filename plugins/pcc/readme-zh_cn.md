[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## pcc

### 基本信息

- 插件 ID: `pcc`
- 版本: *数据拉取失败*
- 总下载量: N/A
- 作者: [zyxkad](https://github.com/zyxkad)
- 仓库: https://github.com/kmcsr/pcc_mcdr
- 仓库插件页: https://github.com/kmcsr/pcc_mcdr/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: *数据拉取失败*

### 插件依赖

*数据拉取失败*

### 包依赖

*数据拉取失败*

### 介绍


- [English](https://github.com/kmcsr/pcc_mcdr/tree/main/README.MD)
- 中文

# PCC

一个允许你默默发送 MCDR 指令的插件.  
也允许你在游戏内自动补全 MCDR 指令

需要将 `loginproxy/config.json` 下的 `enable_packet_proxy` 选项设为 `true`

不支持小于 1.19.2 的版本

实测 1.19.2, 1.21.1 可用, 其他版本未知

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

*数据拉取失败*

