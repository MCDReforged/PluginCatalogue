[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## tpm

### 基本信息

- 插件 ID: `tpm`
- 版本: *数据拉取失败*
- 总下载量: N/A
- 作者: [zyxkad](https://github.com/zyxkad)
- 仓库: https://github.com/kmcsr/tpmanager_mcdr
- 仓库插件页: https://github.com/kmcsr/tpmanager_mcdr/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: *数据拉取失败*

### 插件依赖

*数据拉取失败*

### 包依赖

*数据拉取失败*

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

| 指令格式                   | 介绍                     |
| ---------------------- | ---------------------- |
| `!!tp help`            | 显示帮助信息, `!!tp`同        |
| `!!tp pos <x> <y> <z>` | 传送到`<x>`, `<y>`, `<z>` |
| `!!tp ask <name>`      | 请求传送到玩家, `!!tpa`同      |
| `!!tp askhere <name>`  | 请求玩家传送到你, `!!tph`同     |
| `!!tp accept`          | 同意传送请求                 |
| `!!tp reject`          | 拒绝传送请求                 |
| `!!tp cancel`          | 取消传送请求                 |

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

*数据拉取失败*

