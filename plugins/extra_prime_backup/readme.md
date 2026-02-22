**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## extra_prime_backup

### Basic Information

- Plugin ID: `extra_prime_backup`
- Plugin Name: Extra Prime Backup
- Version: 0.0.2
  - Metadata version: 0.0.2
  - Release version: 0.0.2
- Total downloads: 120
- Authors: [esunyao](https://github.com/esunyao)
- Repository: https://github.com/GloryRedstoneUnion/MCDR-ExtraPrimeBackup
- Repository plugin page: https://github.com/GloryRedstoneUnion/MCDR-ExtraPrimeBackup/tree/master
- Labels: [`Management`](/labels/management/readme.md)
- Description: 一个简单的PrimeBackup拓展插件，用于在备份前监测机器是否开启

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.12.0 |
| [prime_backup](/plugins/prime_backup/readme.md) | \>=1.5 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | * |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# 🧱 ExtraPrimeBackup - Minecraft 机器状态备份管理器

<p align="center">
  <strong>✨ 确保您的红石机器在备份前正确关闭 ✨</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/MCDReforged-2.x-blue" alt="MCDReforged">
  <img src="https://img.shields.io/badge/PrimeBackup-Required-green" alt="PrimeBackup Required">
  <img src="https://img.shields.io/badge/minecraft__data__api-Required-orange" alt="minecraft_data_api Required">
</p>

## 🚀 概述

ExtraPrimeBackup 是一个强大的 MCDReforged 插件，专为 Minecraft 服务器管理员设计。它扩展了 PrimeBackup 的功能，通过智能监控方块状态，确保在执行备份前所有重要红石机器都已正确关闭。

~~这是一个全部由AI写的项目~~

> 💡 **核心价值**：防止备份包含正在运行的机器，避免恢复后出现物品复制或机器故障问题

## 🌟 功能亮点

- 🗂️ **树状检查点管理** - 支持多级分组结构
- 🌍 **多维度支持** - 主世界、下界、末地全覆盖
- 📊 **可视化状态检查** - 精美树状格式显示状态详情
- ⚡ **无缝集成** - 完美兼容 PrimeBackup
- 🔄 **自动迁移** - 无缝升级旧版本数据
- ⏱️ **智能检测** - 自动识别玩家所在维度
- 🛡️ **双重模式** - 线程守护/事件触发可选
- 🚨 **异常预警** - 实时广播未关机机器

## 📦 安装要求

- [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 2.x 或更高版本
- [PrimeBackup](https://github.com/TISUnion/PrimeBackup) 插件
- [minecraft_data_api](https://github.com/Fallen-Breath/MinecraftDataAPI) 插件

## ⚙️ 配置说明

```json
// config/check_point.json
{
  "tree": {
    "factory": {
      "type": "group",
      "description": "主要工厂区域",
      "children": {
        "redstone": {
          "type": "group",
          "description": "红石机器",
          "children": {
            "piston_door": {
              "type": "checkpoint",
              "x": 150,
              "y": 64,
              "z": 250,
              "world": "overworld",
              "block": "minecraft:piston",
              "data": {"extended": "false"}
            }
          }
        }
      }
    }
  },
  "override_mode": "event",
  "check_point": {},
  "groups": {}
}
```

### 🔧 配置选项

| 参数              | 类型     | 默认值       | 说明                                                             |
| --------------- | ------ | --------- | -------------------------------------------------------------- |
| `override_mode` | string | `"event"` | PrimeBackup 覆写模式：<br>`"thread"` - 线程守护模式<br>`"event"` - 事件触发模式 |
| `tree`          | object | `{}`      | 树状结构存储检查点和分组                                                   |
| `check_point`   | object | `{}`      | 旧版检查点数据（兼容）                                                    |
| `groups`        | object | `{}`      | 旧版分组数据（兼容）                                                     |

## ⌨️ 指令大全

### 🆘 帮助指令
| 指令                       | 说明         |
| ------------------------ | ---------- |
| `!!pb cp help`           | 显示完整帮助信息   |
| `!!pb cp help <command>` | 显示特定指令详细帮助 |

### 🌳 树状管理
| 指令             | 说明        |
| -------------- | --------- |
| `!!pb cp list` | 显示检查点树状结构 |
| `!!pb cp ls`   | 列表形式显示检查点 |

### 📍 检查点操作
| 指令                                       | 说明      |
| ---------------------------------------- | ------- |
| `!!pb cp add <x> <y> <z> <name> [world]` | 添加根级检查点 |
| `!!pb cp status <name>`                  | 查看检查点状态 |
| `!!pb cp update <name>`                  | 更新检查点状态 |
| `!!pb cp del <name>`                     | 删除检查点   |

### 📂 分组管理
| 指令                                                      | 说明        |
| ------------------------------------------------------- | --------- |
| `!!pb cp add g <group_path>`                            | 创建新分组     |
| `!!pb cp add g <group_path> <x> <y> <z> <name> [world]` | 在分组中添加检查点 |

### ⚡ 备份操作
| 指令                 | 说明           |
| ------------------ | ------------ |
| `!!pb make [备注]`   | 正常备份（检查机器状态） |
| `!!pb ignore [备注]` | 强制备份（忽略机器状态） |

## 🎯 使用示例

### 创建检查点
```bash
# 自动检测维度添加检查点
!!pb cp add 100 64 200 wheat_farm

# 指定下界维度添加检查点
!!pb cp add 50 80 -100 nether_portal the_nether
```

### 创建分组结构
```bash
# 创建主分组
!!pb cp add g industrial_area

# 创建子分组
!!pb cp add g industrial_area.factories

# 在子分组中添加检查点
!!pb cp add g industrial_area.factories 120 65 180 auto_smelter
```

### 检查状态
```bash
# 列出所有检查点
!!pb cp list

# 查看具体检查点状态
!!pb cp status industrial_area.factories.auto_smelter

# 更新检查点状态
!!pb cp update industrial_area.factories.auto_smelter
```

### 执行备份
```bash
# 正常备份（检查机器状态）
!!pb make "每日例行备份"

# 强制备份（忽略机器状态）
!!pb ignore "紧急故障修复备份"
```

## 🌐 支持的世界

| 世界名称         | 对应维度 | 备注   |
| ------------ | ---- | ---- |
| `overworld`  | 主世界  | 默认维度 |
| `the_nether` | 下界   | 地狱维度 |
| `the_end`    | 末地   | 末地维度 |

## 🔍 状态显示示例

```
§a=== 检查点状态：factory.redstone.piston ===
§6├─ 🧭 基本信息
§7│  ├─ 📍 坐标: §e(150, 64, 250)
§7│  ├─ 🌍 世界: §eoverworld
§7│  └─ ✅ 获取状态: §a成功
§6├─ ⚙️ 配置数据
§7│  ├─ 🧱 方块类型: §eminecraft:piston
§7│  └─ 🔧 方块属性:
§7│     └─ §bextended§7: §efalse
§6├─ 🔍 实际数据
§7│  ├─ 🧱 方块类型: §eminecraft:piston
§7│  └─ 🔧 方块属性:
§7│     └─ §bextended§7: §efalse
§6├─ 📊 状态分析
§7│  ├─ 🧱 方块类型匹配: §a✔️ 是
§7│  ├─ 🔧 方块属性匹配: §a✔️ 是
§7│  └─ 💡 整体状态: §a🛑 机器已关闭
§6└─ ⚡ 操作选项
§7   🔴 [删除] 🟡 [更新]
```

## ⚠️ 注意事项

1. 确保已安装所有依赖插件
2. 方块状态检查需要服务器支持 `/info block` 命令
3. 建议在服务器低负载时更新检查点
4. 强制备份会在备注中标注未关机机器
5. 首次使用会自动迁移旧版数据

## 📜 开源许可

本项目采用 [GNU General Public License v3.0](https://github.com/GloryRedstoneUnion/MCDR-ExtraPrimeBackup/tree/master/LICENSE) 开源

## 🤝 贡献指南

欢迎通过以下方式参与项目：
1. 提交 Issue 报告问题或建议
2. 发起 Pull Request 贡献代码
3. 分享使用经验和配置技巧

---

**让您的每一次备份都安心无忧！** 🛡️

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [ExtraPrimeBackup-v0.0.2.mcdr](https://github.com/GloryRedstoneUnion/MCDR-ExtraPrimeBackup/releases/tag/v0.0.2) | 0.0.2 | 2025/07/11 04:59:38 | 10.84KB | 120 | [Download](https://github.com/GloryRedstoneUnion/MCDR-ExtraPrimeBackup/releases/download/v0.0.2/ExtraPrimeBackup-v0.0.2.mcdr) |

