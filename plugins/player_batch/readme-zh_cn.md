[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## player_batch

### 基本信息

- 插件 ID: `player_batch`
- 插件名: PlayerBatch
- 版本: 1.0.6
  - 元数据版本: 1.0.7
  - 发布版本: 1.0.6
- 总下载量: 349
- 作者: [Eason120806](https://github.com/Eason120806)
- 仓库: https://github.com/Eason120806/player_batch-MCDR
- 仓库插件页: https://github.com/Eason120806/player_batch-MCDR/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: MCDR假人批量操作插件

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# PlayerBatch - MCDR假人批量操作插件

🎮 一个基于MCDReforged的插件，提供强大的Carpet假人批量操作功能

![License](https://img.shields.io/badge/License-GPLv3-blue)
![MCDR](https://img.shields.io/badge/MCDR-2.1.0%2B-blue)

## 📦 功能特性

- **批量基础操作**：同时控制多个假人执行任意指令
- **智能排列生成**：支持直线/方阵排列生成假人
- **初始化序列**：定制化生成+执行动作+自动清理流程
- **多维度配置**：可自定义假人命名规则和操作间隔
- **权限管理**：通过配置文件控制命令使用权限

## 🛠️ 安装方法

1. 确保已安装 [MCDReforged]
2. 下载最新版 `PlayerBatch.pyz`
3. 放入MCDR的plugins目录
4. 重启MCDR服务端

## ⚙️ 配置文件

路径：`config/player_batch.json`

```json
{
    "base_name": "bot_",
    "permission": 0,
    "interval": 1.0
}
```
## 🎯 命令列表

### 基础命令
```text
!!plb <名称> <起始> <结束> <动作>
!!playerbatch <名称> <起始> <结束> <动作>
```

### 直线生成
```text
!!plb l <名称> <起始> <长度> <方向> <间隔>
!!playerbatch l <名称> <起始> <长度> <方向> <间隔>
```

### 方阵生成
```text
!!plb s <名称> <起始> <长> <宽> <方向1> <方向2> <间隔>
!!playerbatch s <名称> <起始> <长> <宽> <方向1> <方向2> <间隔>
```

### 初始化序列
```text
!!plb init <名称> <起始> <长度> <间隔1> <间隔2> <x> <y> <z> <动作>
!!playerbatch init <名称> <起始> <长度> <间隔1> <间隔2> <x> <y> <z> <动作>
```

### 停止命令
```text
!!plb stop
!!playerbatch stop
```


## ⚠️ 注意事项

1. 需要安装Carpet Mod及其假人功能
2. 间隔时间影响服务器性能，请合理设置
3. 假人名称格式：前缀 + 自定义名 + 序号

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.6) | 1.0.6 | 2025/05/02 11:59:23 | 10.74KB | 174 | [下载](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.6/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.5) | 1.0.5 | 2025/05/02 09:59:45 | 10.68KB | 28 | [下载](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.5/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.4) | 1.0.4 | 2025/05/02 07:56:25 | 10.23KB | 26 | [下载](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.4/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.3) | 1.0.3 | 2025/04/30 17:24:58 | 10.2KB | 29 | [下载](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.3/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.2) | 1.0.2 | 2025/04/28 17:18:04 | 9.86KB | 31 | [下载](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.2/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.1) | 1.0.1 | 2025/04/25 10:51:49 | 3.23KB | 33 | [下载](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.1/player_batch.pyz) |
| [player_batch.pyz](https://github.com/Eason120806/player_batch-MCDR/releases/tag/1.0.0) | 1.0.0 | 2025/04/20 15:48:35 | 2.19KB | 28 | [下载](https://github.com/Eason120806/player_batch-MCDR/releases/download/1.0.0/player_batch.pyz) |

