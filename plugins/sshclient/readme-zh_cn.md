[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## sshclient

### 基本信息

- 插件 ID: `sshclient`
- 插件名: SSHClient
- 版本: 0.0.1
  - 元数据版本: 0.0.1
  - 发布版本: 0.0.1
- 总下载量: 9
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/SSHClient-MCDR
- 仓库插件页: https://github.com/Mooling0602/SSHClient-MCDR/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一个MCDR的SSH客户端实例

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [paramiko](https://pypi.org/project/paramiko) |  |

```
pip install paramiko
```

### 介绍

# SSHClient-MCDR
MCDR的一个SSH客户端实现，仅供娱乐。

请注意，本插件设计时未考虑任何安全问题，请勿在生产环境下使用！

Not support English yet, translate yourself.

## 用法
使用`!!ssh connect <地址> <用户名> <密码> <端口（可选）>`连接到ssh会话

连接成功后，即可使用`!!ssh "<可带空格的命令>"`执行命令并获取执行结果

不用了可使用`!!ssh disconnect`退出ssh会话

查看详细帮助可使用`!!ssh help`

## 当前局限
- ssh连接是全局共享的，所有人都能访问
- 未成功建立连接的ssh会话，也需要断开后才能再次建立连接
- 暂不支持使用密钥文件登录，只能使用密码
- 玩家在游戏内尝试连接，将会公屏暴露主机连接信息和用户名密码

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [SSHClient-v0.0.1.mcdr](https://github.com/Mooling0602/SSHClient-MCDR/releases/tag/0.0.1) | 0.0.1 | 2024/09/21 07:21:45 | 2.09KB | 9 | [下载](https://github.com/Mooling0602/SSHClient-MCDR/releases/download/0.0.1/SSHClient-v0.0.1.mcdr) |

