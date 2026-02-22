[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## ftp_backup

### 基本信息

- 插件 ID: `ftp_backup`
- 插件名: ftp Backup
- 版本: 0.0.4
  - 元数据版本: 0.0.4
  - 发布版本: 0.0.4
- 总下载量: 154
- 作者: [yhy-yangyang](https://github.com/yhy-yangyang)
- 仓库: https://github.com/yhy-yangyang/mcdr-ftpbackup
- 仓库插件页: https://github.com/yhy-yangyang/mcdr-ftpbackup/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: A backup plugin for MCDR

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.7.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [chardet](https://pypi.org/project/chardet) |  |
| [paramiko](https://pypi.org/project/paramiko) |  |
| [apscheduler](https://pypi.org/project/apscheduler) |  |

```
pip install mcdreforged chardet paramiko apscheduler
```

### 介绍

# MCDR-FTPBackup

一个为 Minecraft 服务器提供备份与 FTP 远程同步功能的 MCDReforged 插件。

---

## 功能特性
- **一键备份**：自动压缩服务器文件并支持断连保护
- **远程同步**：将备份文件上传至远程FTP/SFTP服务器
- **匹配编码**：自动匹配FTP服务器的编码
- **智能清理**：保留指定数量的本地备份文件
- **安全模式**：关闭服务器后再执行备份（可在配置文件内修改）
- **权限管理**：可配置不同命令的权限等级

---

## 安装指南
1. 将插件文件放置于 MCDR 的 `plugins` 目录
2. 首次运行会自动生成配置文件 `config/config.json`
3. 根据服务器环境修改配置文件（配置说明见下文）

---

## 配置说明
```
{
    "stop_server": true,                // 是否在备份前停服
    "protocol": "ftp",                  // 选择协议 大小写均可
    "host": "ftp.example.com",          // FTP/SFTP 服务器地址
    "port": 21,                         // FTP/SFTP 端口
    "timeout": 10,                      // 超时时间  
    "username": "anonymous",            // 登录用户名
    "private_key_path": "",             // SFTP服务器秘钥路径
    "password": "",                     // 登录密码
    "prefix": "!!fb",                   // 命令前缀
    "server_dir": "./server",           // 服务器目录
    "keep_local_backups": 3,            // 本地保留备份数量
    "required_permission": 3,           // 操作所需权限等级
    "exclude_patterns": [               // 需要排除的文件
        "logs",
        "*.tmp",
        "*.lock"
    ]
    remote_path : str = '/'             // 指定远程备份路径
    local_path: str = './backups'       // 指定本地备份路径
    auto_backup: bool = False           // 是否开启定时备份功能
    cron_expression: str = '0 0 * * *'  // 定时备份时间
}
```

---

## 命令列表
<font size="3">注意:本文档假定你使用`!!fb`作为 MCDR 命令的前缀</font>

- `!!fb` - 显示帮助信息
- `!!fb test` - 测试与FTP服务器的连接
- `!!fb make` - 创建一个备份并上传到FTP服务器
- `!!fb inquire` - 查询备份进度
- `!!fb reload` - 热重载配置
- `!!fb abort` - 终止备份
---

## 注意事项
1. 首次使用前需要在`config.json`文件中修改FTP/SFTP服务器有关设置
2. 备份完毕后会在`backups`文件夹内保留备份，保留数量可在配置文件内修改
3. 排除的文件以unix shell风格匹配
4. 定时备份表达式为一个 crontab 字符串，可以使用 <https://crontab.guru/> 来创建一个 crontab 字符串

---

## 许可证
本项目基于 Apache License 2.0 发布

---

## 贡献
欢迎提交 Issue 和 Pull Request！

---

## TODO
- [x] 支持sftp协议
- [x] 添加定时备份功能
- [x] 使用`@new_thread`实现多线程(~~不仔细看文档的后果~~)

---

## 友商项目
- [八宝粥 (多)MC服务端管理面板](https://github.com/babaozhouO/BBZ-MCServers-Manager)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ftp_backup-v0.0.4.mcdr](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/tag/v0.0.4) | 0.0.4 | 2025/05/01 07:33:30 | 22.67KB | 68 | [下载](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/download/v0.0.4/ftp_backup-v0.0.4.mcdr) |
| [ftp_backup-v0.0.3.mcdr](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/tag/v0.0.3) | 0.0.3 | 2025/04/19 12:07:08 | 7.58KB | 32 | [下载](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/download/v0.0.3/ftp_backup-v0.0.3.mcdr) |
| [ftp_backup-v0.0.2.mcdr](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/tag/v0.0.2) | 0.0.2 | 2025/04/19 07:14:00 | 7.01KB | 28 | [下载](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/download/v0.0.2/ftp_backup-v0.0.2.mcdr) |
| [ftp_backup.mcdr](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/tag/v0.0.1) | 0.0.1 | 2025/04/13 08:11:24 | 12.95KB | 26 | [下载](https://github.com/yhy-yangyang/mcdr-ftpbackup/releases/download/v0.0.1/ftp_backup.mcdr) |

