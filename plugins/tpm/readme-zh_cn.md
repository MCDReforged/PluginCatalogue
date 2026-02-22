[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## tpm

### 基本信息

- 插件 ID: `tpm`
- 插件名: TpManager
- 版本: 0.5.4
  - 元数据版本: 0.5.4
  - 发布版本: 0.5.4
- 总下载量: 2959
- 作者: [zyxkad](https://github.com/zyxkad)
- 仓库: https://github.com/kmcsr/tpmanager_mcdr
- 仓库插件页: https://github.com/kmcsr/tpmanager_mcdr/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 一个Minecraft服务器传送管理

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.3.0 |
| [kpi](/plugins/kpi/readme-zh_cn.md) | ^1.5.2 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍


- [English](https://github.com/kmcsr/tpmanager_mcdr/tree/master/README.MD)
- 中文

# Tp Manager

*如果本插件有用, 请给个star吧 :)*

## 特性

- 玩家之间的传送
- 游戏内路径点传送

## TODO

- 与login_proxy联动?

## 依赖

| ID                                       | 下载链接                                         |
| ---------------------------------------- | -------------------------------------------- |
| [kpi](https://github.com/kmcsr/kpi_mcdr) | <https://github.com/kmcsr/kpi_mcdr/releases> |

## 指令

> [!TIP]
> 一些插件也注册了 `!!tp` 指令. 故此可使用 `!!tpm` 替换 `!!tp` 节点.

| 指令格式                                             | 介绍                     |
| ------------------------------------------------ | ---------------------- |
| `!!tp help`                                      | 显示帮助信息, `!!tp`同        |
| `!!tp pos <x> <y> <z>`                           | 传送到`<x>`, `<y>`, `<z>` |
| `!!tp ask <name>`                                | 请求传送到玩家, `!!tpa`同      |
| `!!tp askhere <name>`                            | 请求玩家传送到你, `!!tph`同     |
| `!!tp accept`                                    | 同意传送请求                 |
| `!!tp reject`                                    | 拒绝传送请求                 |
| `!!tp cancel`                                    | 取消传送请求                 |
| `!!tp warp <point>`                              | 传送到坐标点, `!!warp`同      |
| `!!tp warps list`                                | 列出所有坐标点                |
| `!!tp warps add <point> <x> <y> <z> <dimension>` | 添加或设置坐标点               |
| `!!tp warps remove <point>`                      | 删除坐标点                  |

## 配置文件

#### tpm/config.json

注意, 有些服务器执行 `teleport_xyz_command` 时会把在其他维度的玩家传送到主世界.  
将指令更改为 `execute at {name} run tp {name} {x} {y} {z}` 即可解决该问题

```javascript
{
    "minimum_permission_level": { // 指令权限
        "pos": 2,
        "ask": 1,
        "askhere": 1,
        "accept": 1,
        "reject": 0,
        "cancel": 0
    },
    "teleport_cooldown": 60, // 秒, 传送冷却
    "teleport_expiration": 10, // 秒, 传送请求过期时间
    "teleport_commands": [ // 用于传送到玩家的指令集
        "say Teleporting {src} to {dst} ...",
        "tp {src} {dst}",
    ],
    "teleport_xyz_command": "tp {name} {x} {y} {z}" // 用于传送到坐标的指令
}
```

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [TpManager-v0.5.4.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.5.4) | 0.5.4 | 2025/08/04 14:10:47 | 19.17KB | 204 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.5.4/TpManager-v0.5.4.mcdr) |
| [TpManager-v0.5.3.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.5.3) | 0.5.3 | 2025/03/12 14:23:08 | 19.16KB | 304 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.5.3/TpManager-v0.5.3.mcdr) |
| [TpManager-v0.5.2.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.5.2) | 0.5.2 | 2025/03/12 14:11:08 | 19.09KB | 54 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.5.2/TpManager-v0.5.2.mcdr) |
| [TpManager-v0.5.1.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.5.1) | 0.5.1 | 2025/02/01 20:07:10 | 18.76KB | 110 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.5.1/TpManager-v0.5.1.mcdr) |
| [TpManager-v0.5.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.5.0) | 0.5.0 | 2024/09/07 16:34:52 | 18.75KB | 331 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.5.0/TpManager-v0.5.0.mcdr) |
| [TpManager-v0.4.6.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.6) | 0.4.6 | 2024/03/09 21:53:20 | 17.01KB | 374 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.6/TpManager-v0.4.6.mcdr) |
| [TpManager-v0.4.5.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.5) | 0.4.5 | 2024/02/27 04:59:38 | 17.0KB | 85 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.5/TpManager-v0.4.5.mcdr) |
| [TpManager-v0.4.4.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.4) | 0.4.4 | 2024/02/05 00:16:45 | 17.02KB | 89 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.4/TpManager-v0.4.4.mcdr) |
| [TpManager-v0.4.3.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.3) | 0.4.3 | 2024/02/03 02:35:34 | 17.01KB | 97 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.3/TpManager-v0.4.3.mcdr) |
| [TpManager-v0.4.2.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.2) | 0.4.2 | 2024/02/03 02:33:06 | 17.01KB | 95 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.2/TpManager-v0.4.2.mcdr) |
| [TpManager-v0.4.1.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.1) | 0.4.1 | 2024/02/03 00:52:34 | 17.0KB | 96 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.1/TpManager-v0.4.1.mcdr) |
| [TpManager-v0.4.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.4.0) | 0.4.0 | 2024/02/03 00:35:46 | 17.0KB | 102 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.4.0/TpManager-v0.4.0.mcdr) |
| [TpManager-v0.3.4.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.4) | 0.3.4 | 2023/05/21 16:56:38 | 16.74KB | 345 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.4/TpManager-v0.3.4.mcdr) |
| [TpManager-v0.3.3.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.3) | 0.3.3 | 2023/02/26 17:42:05 | 16.63KB | 138 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.3/TpManager-v0.3.3.mcdr) |
| [TpManager-v0.3.2.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.2) | 0.3.2 | 2023/02/26 16:53:28 | 16.64KB | 76 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.2/TpManager-v0.3.2.mcdr) |
| [TpManager-v0.3.1.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.1) | 0.3.1 | 2023/02/26 16:52:51 | 16.65KB | 70 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.1/TpManager-v0.3.1.mcdr) |
| [TpManager-v0.3.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.3.0) | 0.3.0 | 2023/02/26 05:48:16 | 16.69KB | 73 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.3.0/TpManager-v0.3.0.mcdr) |
| [TpManager-v0.2.1.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.2.1) | 0.2.1 | 2022/11/28 02:31:44 | 16.41KB | 157 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.2.1/TpManager-v0.2.1.mcdr) |
| [TpManager-v0.2.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.2.0) | 0.2.0 | 2022/11/27 22:43:52 | 16.41KB | 78 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.2.0/TpManager-v0.2.0.mcdr) |
| [TpManager-v0.1.0.mcdr](https://github.com/kmcsr/tpmanager_mcdr/releases/tag/v0.1.0) | 0.1.0 | 2022/11/27 19:00:42 | 16.18KB | 81 | [下载](https://github.com/kmcsr/tpmanager_mcdr/releases/download/v0.1.0/TpManager-v0.1.0.mcdr) |

