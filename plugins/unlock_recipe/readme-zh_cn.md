[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## unlock_recipe

### 基本信息

- 插件 ID: `unlock_recipe`
- 插件名: UnlockRecipe
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 64
- 作者: [uerhu](https://uerhu.cn)
- 仓库: https://github.com/uerhu/MCDR-UnlockRecipe
- 仓库插件页: https://github.com/uerhu/MCDR-UnlockRecipe/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 允许玩家使用!!recipe解锁配方

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# UnlockRecipe
[English](https://github.com/uerhu/MCDR-UnlockRecipe/tree/master/README.md)

---
## 简介
* JEI, REI等mod查看配方时，可能无法查看未解锁的配方
* 使用该插件可以使非op玩家解锁配方
---
## 命令
* `!!recipe`解锁自己的所有配方（仅限玩家）
---
## 配置文件
config.json （默认配置文件）
```json5
{
    "permission": 1,  // 玩家权限等级
    "announce": true,  // 是否在玩家进入游戏时通知玩家
    "announce_once": true  // 是否只通知一次
}
```
announced_players.json (记录已通知的玩家)
```json5
{
  "announced_players": [
    "player1",
    "player2"
    ]
}
```

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [UnlockRecipe-1.0.0.mcdr](https://github.com/uerhu/MCDR-UnlockRecipe/releases/tag/1.0.0) | 1.0.0 | 2025/08/22 09:35:59 | 4.02KB | 64 | [下载](https://github.com/uerhu/MCDR-UnlockRecipe/releases/download/1.0.0/UnlockRecipe-1.0.0.mcdr) |

