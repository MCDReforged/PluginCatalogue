[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## snapshot_follower

### 基本信息

- 插件 ID: `snapshot_follower`
- 插件名: Snapshot Follower
- 版本: 1.2.0
  - 元数据版本: 1.2.0
  - 发布版本: 1.2.0
- 总下载量: 14
- 作者: [Fallen_Breath](https://github.com/Fallen-Breath)
- 仓库: https://github.com/Fallen-Breath/SnapshotFollower
- 仓库插件页: https://github.com/Fallen-Breath/SnapshotFollower/tree/master
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: Keep your Minecraft server up-to-date with the latest snapshot

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install mcdreforged requests
```

### 介绍

# Snapshot Follower

[English](https://github.com/Fallen-Breath/SnapshotFollower/tree/master/README.md) | **中文**

让你的 Minecraft 服务器始终保持最新快照版本

该插件会定期从 [Mojang API](https://launchermeta.mojang.com/mc/game/version_manifest.json) 查询最新的 Minecraft 快照版本。
当发现有新的快照时，它会依次进行：下载快照的 `server.jar`、停止正在运行的服务器、替换掉现有的 `server.jar`、
使用最新的 Minecraft 快照 jar 启动服务器

> [!NOTE]
> 当插件加载或服务器启动时，插件会通过读取 `server.jar` 文件中的 `version.json` 来尝试检测当前 Minecraft 版本，
> 从而判断当前运行的 Minecraft 版本是否与最新的快照匹配
> 
> 如果检测失败，插件会假定当前的 Minecraft 版本就是最新的快照版本

可选地，在更新完成后，插件可发起一个 HTTP POST 的 webhook

## Configuration

配置文件路径：`config/snapshot_follower/config.json`

```json5
{
    "enabled": true,  // 插件开关，默认为 true

    "check_interval": 60.0,  // 每次检查的间隔时间
    "server_jar_path": "server/server.jar",  // 服务端 jar 文件的路径，需要可写以便进行更新
    "keep_downloaded_jar": true,  // 更新后是否保留下载的 server.jar 文件。下载的 jar 文件将位于 `config/snapshot_follower/jars`
    "version_blacklist": [],  // 版本黑名单。位于里面的版本号会被忽略。如果你希望跳过某些快照版本，就可以用这个黑名单

    "http_proxy": "http://127.0.0.1:1081",  // 可选项，HTTP 请求时使用的 HTTP 代理 URL
    "https_proxy": "http://127.0.0.1:1081",  // 可选项，HTTP 请求时使用的 HTTPS 代理 URL
    "request_timeout": 10.0,  // HTTP 请求超时时间，单位为秒

    "webhook": {
        "enabled": true,  // Webhook 功能开关。插件会在更新完成后会发送一个 HTTP POST 请求
        "use_http_proxy": false,  // Webhook 的 HTTP 请求是否使用上面定义的 HTTP 代理
        "url": "http://127.0.0.1:8080/my/callback",  // webhook 的 URL
        "headers": {  // Webhook 的 HTTP 请求头，可为空
            "Authorization": "Bearer foobar"
        },
        "body": "服务器已更新到 {{version}}"  // Webhook 请求体。占位符 {{version}} 将被替换为更新后的版本号（例如 24w39a）
    }
}
```

## TODO

- [ ] 更新前进行游戏内广播 + 倒计时 + 用户延迟更新支持
- [ ] 更新前备份存档（借助其他插件）

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [SnapshotFollower-v1.2.0.mcdr](https://github.com/Fallen-Breath/SnapshotFollower/releases/tag/v1.2.0) | 1.2.0 | 2025/04/02 19:02:45 | 7.54KB | 2 | [下载](https://github.com/Fallen-Breath/SnapshotFollower/releases/download/v1.2.0/SnapshotFollower-v1.2.0.mcdr) |
| [SnapshotFollower-v1.1.0.mcdr](https://github.com/Fallen-Breath/SnapshotFollower/releases/tag/v1.1.0) | 1.1.0 | 2024/10/01 17:59:34 | 7.35KB | 12 | [下载](https://github.com/Fallen-Breath/SnapshotFollower/releases/download/v1.1.0/SnapshotFollower-v1.1.0.mcdr) |

