[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## backup_to_nas

### 基本信息

- 插件 ID: `backup_to_nas`
- 插件名: Backup To Nas
- 版本: 0.1.4
  - 元数据版本: 0.1.4
  - 发布版本: 0.1.4
- 总下载量: 22
- 作者: [renzaifei](https://github.com/ren-zaifei)
- 仓库: https://github.com/SDK-Minecraft-Server/BackupToNas
- 仓库插件页: https://github.com/SDK-Minecraft-Server/BackupToNas/tree/release
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 将存档打包为 ZIP，并通过 SFTP 传输到远程 NAS。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.10.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.10.0 |
| [paramiko](https://pypi.org/project/paramiko) | \>=3.4.0 |

```
pip install "mcdreforged>=2.10.0" "paramiko>=3.4.0"
```

### 介绍

# Backup To Nas

[English](https://github.com/SDK-Minecraft-Server/BackupToNas/tree/release/README.md)

Backup To Nas 是一个 MCDR 插件，用于将 Minecraft 世界备份到远程 NAS。插件会生成 ZIP 压缩包，并通过 SFTP 传输到目标目录。

## 功能

- 按配置备份一个或多个世界并上传压缩包。
- 按固定间隔自动备份。
- 手动上传临时目录中已有的 `.zip` 文件。
- 查询 SFTP 上传进度。
- 配置 MCDR 权限等级和 SFTP 连接参数。

## 安装

插件要求 MCDR 2.10.0 或更高版本，并依赖 Paramiko：

```bash
pip install -r requirements.txt
```

如果 MCDR 通过 pipx 安装，请将 Paramiko 注入 MCDR 环境：

```bash
pipx inject mcdreforged paramiko
```

插件首次加载时会生成：

```text
config/backup_to_nas/config.json
```

## 配置

```json
{
    "permissions": {
        "help": 0,
        "make": 3,
        "interval": 3,
        "status": 0,
        "upload": 3
    },
    "interval": "",
    "temp": "./backup_to_nas",
    "turn_off_auto_save": true,
    "server_path": "./server",
    "world_names": ["world"],
    "ignore_session_lock": true,
    "sftp": {
        "host": "192.168.1.100",
        "port": 22,
        "username": "root",
        "password_file": "/etc/mcdr/backup_to_nas/sftp_password",
        "private_key_file": "",
        "remote_dir": "/minecraft-backups",
        "timeout": 30,
        "auto_add_host_key": false
    }
}
```

`server_path`、`temp` 和 `world_names` 用于确定本地世界目录。相对路径相对于 MCDR 工作目录，生产环境建议使用绝对路径。`world_names` 可以填写多个世界目录。

SFTP 认证方式二选一：

- `password_file` 指向只包含密码的文件，文件末尾的换行会被忽略。
- `private_key_file` 指向 SSH 私钥文件。

两项不能同时配置。凭据从文件读取，不会直接保存在 JSON 配置中。`auto_add_host_key` 默认是 `false`，需要先将 NAS 主机密钥加入运行 MCDR 用户的 `known_hosts`。只有在明确接受自动信任未知主机的风险时才设置为 `true`。

`interval` 为空表示关闭自动备份，也可以使用 `1s`、`30s`、`1h` 或 `1d` 等格式。修改配置后重载插件即可生效。

## 命令

默认命令前缀是 `!!btn`：

| 命令                          | 作用                              |
| --------------------------- | ------------------------------- |
| `!!btn`                     | 显示帮助信息                          |
| `!!btn make`                | 立即创建并上传一次备份                     |
| `!!btn interval <interval>` | 设置自动备份间隔，例如 `!!btn interval 6h` |
| `!!btn interval off`        | 禁用自动备份                          |
| `!!btn status`              | 查询当前或最近一次 SFTP 上传状态             |
| `!!btn upload`              | 上传临时目录顶层已有的 `.zip` 文件           |

备份和手动上传不能同时执行。上传失败的 ZIP 文件会保留在临时目录中，可以使用 `!!btn upload` 重试。

## 权限

权限值表示执行命令所需的最低 MCDR 权限等级：

|  等级 | 身份   |
| --: | ---- |
|   0 | 所有人  |
|   1 | 普通用户 |
|   2 | 协助者  |
|   3 | 管理员  |
|   4 | 所有者  |

`permissions.help`、`permissions.make`、`permissions.interval`、`permissions.status` 和 `permissions.upload` 分别控制对应命令。根命令的 `help` 权限也会限制子命令访问。


## 许可证

本项目使用 LGPL-3.0，详见 [LICENSE](https://github.com/SDK-Minecraft-Server/BackupToNas/tree/release/LICENSE)。

备份部分参考了 [PermanentBackup](https://github.com/TISUnion/PermanentBackup)。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BackupToNas-0.1.4.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.4) | 0.1.4 | 2026/09/22 10:30:24 | 11.28KB | 5 | [下载](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.4/BackupToNas-0.1.4.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.3) | 0.1.3 | 2026/09/22 02:23:05 | 8.41KB | 5 | [下载](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.3/BackupToNas.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.2) | 0.1.2 | 2026/09/22 02:13:57 | 11.26KB | 4 | [下载](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.2/BackupToNas.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.1) | 0.1.1 | 2026/09/22 01:21:32 | 8.63KB | 4 | [下载](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.1/BackupToNas.mcdr) |
| [BackupToNas.mcdr](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/tag/0.1.0) | 0.1.0 | 2026/09/22 01:10:48 | 8.59KB | 4 | [下载](https://github.com/SDK-Minecraft-Server/BackupToNas/releases/download/0.1.0/BackupToNas.mcdr) |

