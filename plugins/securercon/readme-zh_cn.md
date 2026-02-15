[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## securercon

### 基本信息

- 插件 ID: `securercon`
- 插件名: SecureRCON
- 版本: 1.0.3
  - 元数据版本: 1.0.3
  - 发布版本: 1.0.3
- 总下载量: 89
- 作者: [wangyupu](https://github.com/wang-yupu)
- 仓库: https://github.com/wang-yupu/SecureRCON
- 仓库插件页: https://github.com/wang-yupu/SecureRCON/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 加密你的RCON连接

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |
| [python](/plugins/python/readme-zh_cn.md) | \>=3.10.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [cryptography](https://pypi.org/project/cryptography) | \>=44.0.0 |
| [javaproperties](https://pypi.org/project/javaproperties) | \>=0.8.0 |
| [pydantic](https://pypi.org/project/pydantic) | \>=2.10.0 |
| [pyyaml](https://pypi.org/project/pyyaml) | \>=6.0.0 |

```
pip install "cryptography>=44.0.0" "javaproperties>=0.8.0" "pydantic>=2.10.0" "pyyaml>=6.0.0"
```

### 介绍


# SecureRCON

一个MCDR插件，加密你的RCON访问，扩展RCON功能

## Why?

原版的RCON是明文传输的（包括密钥与内容），因此加密RCON是有用的。扩展RCON后，可以执行MCDR指令和聊天。

## 加密方法和访问方法

此MCDR插件安装后会作为原始RCON的一个*代理*，替代鉴权部分，同时提供加密支持。  
安装此插件后，如果机器的任意端口都暴露到网络，请使用防火墙进行拦截(e.g. ufw / firewalled / iptables)，同时设定一个较强的RCON密码。本插件会自动读取RCON密码，并监听一个端口(默认25576)，此端口的协议兼容原始RCON，若依然使用原版RCON客户端，可以使用固定强密码或者动态密码。

### SecureMCRCON Python Package

> 执行 `pip install securemcrcon` 以安装，然后使用`smcrcon`命令  
> [Repo](https://github.com/wang-yupu/SecureMCRCON)  
> [PyPI](https://pypi.org/project/securemcrcon/)

CLI客户端

### MCRCON App

> Coming soon (第二优先级)

<!-- [GitHub](https://github.com/wang-yupu/)
此应用支持Windows / macOS(Coming Soon) / Linux(Coming Soon) / Android，可以用此应用进行加密RCON连接，本身也是一个不错的RCON图形化客户端 -->

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [SecureRCON-v1.0.3.mcdr](https://github.com/wang-yupu/SecureRCON/releases/tag/v1.0.3) | 1.0.3 | 2025/12/07 07:16:57 | 10.96KB | 17 | [下载](https://github.com/wang-yupu/SecureRCON/releases/download/v1.0.3/SecureRCON-v1.0.3.mcdr) |
| [SecureRCON-v1.0.2.mcdr](https://github.com/wang-yupu/SecureRCON/releases/tag/v1.0.2) | 1.0.2 | 2025/05/23 18:02:10 | 10.91KB | 37 | [下载](https://github.com/wang-yupu/SecureRCON/releases/download/v1.0.2/SecureRCON-v1.0.2.mcdr) |
| [SecureRCON-v1.0.1.mcdr](https://github.com/wang-yupu/SecureRCON/releases/tag/v1.0.1) | 1.0.1 | 2025/05/01 04:48:52 | 11.6KB | 35 | [下载](https://github.com/wang-yupu/SecureRCON/releases/download/v1.0.1/SecureRCON-v1.0.1.mcdr) |

