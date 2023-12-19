# 📝 Join MOTD Reforged

又一个为 MCDR MOTD 消息插件。

![Built for MCDR 2.10+](./为%20MCDR%202.10+%20开发-57728b.svg)

## 📜 功能

显示一个包含欢迎信息，服务器开服时间和子服务器列表的 MOTD 消息。

## 📖 命令

- `!!motd`: 显示 MOTD 和子服务器列表。
- `!!motd reload`: 重新加载配置文件。
- `!!server`: 显示子服务器列表。

## ⚙️ 依赖

- Python 3.9 或更高版本（低版本可能可以运行，但未经测试）
- MCDReforged 2.10.0 或更高版本
- NBTLib 2.0.0 或更高版本
- [DayCount NBT](https://github.com/alex3236/daycount-NBT) 2.2.1 或兼容版本

## 📥 安装

> [!IMPORTANT]
> 本插件**仅**应安装在后端服务器（即通过代理服务器（如 BungeeCord 或 Velocity）连接的服务器）上，
> 而**不应**安装在代理服务器上。

1. 使用 pip 安装 NBTLib：

    ```shell
    pip install nbtlib
    ```

2. 下载并将 [DayCount NBT](https://github.com/alex3236/daycount-NBT) 插件放置到 MCDR 插件文件夹中。
3. 下载并将本插件放置到 MCDR 插件文件夹中。
4. 在 `config/joinmotd_reforged/config.json` 中按照下面的指南配置本插件。

## 📖 配置

```json5
{
    "server_name": "Minecraft Server", // 服务器组的名称。
    "current_server_name": "Survival Server", // 当前连接的服务器的名称。
    "server_list": [
        {
            // 服务器组中的一个服务器的名称。该名称是 `/server` 命令后使用的名称。
            // 该名称通过代理服务器的配置文件进行配置。
            "name": "survival",
            // 使用上面的名称的服务器的描述。
            "description": "Survival Server"
        },
        {
            // 同上。
            "name": "creative",
            "description": "Creative Server"
        },
        {
            // 同上。
            "name": "mirror",
            "description": "Mirror Server"
        }
        // 本列表可按需添加更多服务器。
    ],
    "permission": {
        "motd": 0,    // 执行 `!!motd` 命令所需的权限等级。
        "server": 0,  // 执行 `!!server` 命令所需的权限等级。
        "reload": 3   // 执行 `!!motd reload` 命令所需的权限等级。
    }
}
```
