[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## player_watchdog

### 基本信息

- 插件 ID: `player_watchdog`
- 插件名: Watch_dog_online_players_with_coords_and_dim
- 版本: 1.0.2
  - 元数据版本: 1.0.2
  - 发布版本: 1.0.2
- 总下载量: 57
- 作者: [LinHouyu](https://github.com/LinHouYu)
- 仓库: https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim
- 仓库插件页: https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md), [`信息`](/labels/information/readme-zh_cn.md)
- 描述: *无*

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | * |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# Player Watchdog

一个基于 [MCDReforged](https://mcdreforged.com/) 的插件，用于定时记录在线玩家的坐标、维度和物品信息，并保存为 CSV 文件，方便用 Excel 查看和分析。

## 功能特性
- **自动记录在线玩家信息**  
  每隔固定时间（默认 5 秒）获取所有在线玩家的：
  - 坐标（X, Y, Z）
  - 所在维度（主世界 / 地狱 / 末地）
  - 物品栏（Inventory）
- **CSV 格式输出**
  - 文件体积小，长期保存无压力
  - 可直接用 Excel 打开，支持筛选、排序、统计
  - 字段：时间、玩家、维度、X、Y、Z、物品
  - <img width="1620" height="393" alt="image" src="https://github.com/user-attachments/assets/10fd545f-f901-4d63-9106-b265f3822aba" />

## 使用方法
1. 将本插件文件夹放入 `plugins/` 目录
2. 确保已安装并启用 [Minecraft Data API](https://mcdreforged.com/zh-CN/plugin/minecraft_data_api) 插件
3. 在 MCDR 的 Python 环境中安装依赖：
   ```bash
   pip install hjson
   ```

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [player_watchdog.mcdr](https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim/releases/tag/v1.0.2) | 1.0.2 | 2025/08/30 05:53:28 | 90.05KB | 38 | [下载](https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim/releases/download/v1.0.2/player_watchdog.mcdr) |
| [player_watchdog.mcdr](https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim/releases/tag/v1.0.1) | 1.0.1 | 2025/08/25 04:08:28 | 5.67KB | 11 | [下载](https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim/releases/download/v1.0.1/player_watchdog.mcdr) |
| [player_watchdog.mcdr](https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim/releases/tag/v1.0.0) | 1.0.0 | 2025/08/25 03:46:34 | 5.64KB | 8 | [下载](https://github.com/LinHouYu/Watch_dog_online_players_with_coords_and_dim/releases/download/v1.0.0/player_watchdog.mcdr) |

