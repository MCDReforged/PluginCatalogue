[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## g0d_of_heads

### 基本信息

- 插件 ID: `g0d_of_heads`
- 插件名: G0d of Heads
- 版本: 2.1.0
  - 元数据版本: 2.1.0
  - 发布版本: 2.1.0
- 总下载量: 673
- 作者: [FRUITS_CANDY](https://github.com/FRUITS-CANDY), [Seeu_SAMA](https://github.com/SeeU-SAMA)
- 仓库: https://github.com/Passion-Never-Dissipate/G0d-of-Heads
- 仓库插件页: https://github.com/Passion-Never-Dissipate/G0d-of-Heads/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 获取任意玩家的任意数量的头颅，适配全版本

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.6.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# G0d of Heads

在 Minecraft 聊天栏输入 `!!head <玩家名> [数量]`，领取指定玩家的头颅。省略数量时领取 1 个。插件会按领取者的 MCDReforged 权限等级检查是否允许使用，并记录每人每天的领取数量。

## 安装

1. 使用 MCDReforged 2.6.0 或更新版本运行 Minecraft Java 服务端。
2. 下载本仓库的 `G0d-of-Heads-v2.1.0.mcdr`，放入 MCDR 的 `plugins` 目录。
3. 启动 MCDR。首次加载后会自动生成 `config/g0d_of_heads/config.json`；按需修改配置，再重载插件。

已有安装可直接替换 `.mcdr` 文件，然后在 MCDR 控制台执行 `!!MCDR plg reload g0d_of_heads`。升级前建议备份现有配置目录；当天的领取记录保存在同目录的 `usage.json` 中。

## 使用方法

| 玩家聊天命令           | 结果                          |
| ---------------- | --------------------------- |
| `!!head Steve`   | 领取 1 个 Steve 的头颅            |
| `!!head Steve 3` | 领取 3 个 Steve 的头颅，并计入自己的当日额度 |

玩家名只接受 1 到 16 位英文字母、数字或下划线。`[数量]` 必须是正整数。控制台不能领取；被禁用的 MCDR 权限等级、额度为 0 的玩家和超出剩余额度的请求都会被拒绝。

## 配置每日额度和权限

编辑 `config/g0d_of_heads/config.json`。首次加载生成的配置允许所有 MCDR 权限等级领取，每名玩家默认每天最多 64 个。下面的示例单独提高了 Steve 的额度，并禁止 guest 和 admin 等级领取：

```json
{
  "default_daily_limit": 64,
  "player_daily_limits": {
    "Steve": 128
  },
  "allowed_permission_levels": {
    "guest": false,
    "user": true,
    "helper": true,
    "admin": false,
    "owner": true
  }
}
```

配置项说明：

| 配置项                         | 含义                                                                                                         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `default_daily_limit`       | 未单独配置的玩家每天可领取的头颅总数；设为 `0` 可禁止其领取。                                                                          |
| `player_daily_limits`       | 按**领取者**的玩家名覆盖默认额度，大小写不敏感；值可以为 `0`。配置 Steve 的额度不会改变其他玩家领取 Steve 头颅的额度。                                     |
| `allowed_permission_levels` | 分别控制 MCDR 的 guest (0)、user (1)、helper (2)、admin (3)、owner (4) 是否能领取。每一级独立设置为 `true` 或 `false`，没有设置的等级默认允许。 |

仓库中的 [config.example.json](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/tree/master/config.example.json) 可作为填写模板。修改配置后执行 `!!MCDR plg reload g0d_of_heads`。若配置或用量文件损坏，插件会拒绝加载，避免意外清空额度。

每日用量保存在 `config/g0d_of_heads/usage.json`，按运行 MCDR 的机器的本地日期计算；日期变化时重新计数，插件重载不会清空当天记录。请勿在插件运行时手工修改此文件。

## 兼容性与注意事项

- 插件根据 Minecraft Java 版本生成 `/give` 命令：1.20.5 及以后使用 `minecraft:profile` 物品组件，较早版本使用 `SkullOwner`。
- 在 26.3 服务端的测试中，玩家聊天命令仍可触发插件并成功领取头颅。此次真实玩家测试使用 26.1 客户端经 ViaProxy 转译连接，并非原生 26.3 客户端测试。26.3 服务端给加入和离开消息加上的 `System chat:` 前缀不影响本插件的聊天命令，但 MCDR 2.15.7 的 VanillaHandler 未将这些消息识别为加入和离开事件。
- 从 Minecraft Java 1.21.9 起，仅提供玩家名的 `minecraft:profile` 可能在客户端显示时才解析皮肤；刚领取时可能短暂显示默认皮肤。
- 插件会先保存领取用量，再向服务端提交 `/give`。MCDR 不返回该命令的执行结果，因此“已提交”不代表服务端确认发放。若服务端拒绝命令，本次额度仍可能被计入，请由管理员核对日志。

## 从源码打包与测试

在本仓库根目录执行：

```powershell
python -m unittest discover -s tests -v
python -m mcdreforged pack -i . -o . --ignore-file .packignore
```

打包结果为 `G0d-of-Heads-v2.1.0.mcdr`。`.packignore` 会排除测试、Git 元数据和临时文件。

## 版本记录

- 2.1.0：加入按玩家配置的每日额度、按 MCDR 权限等级控制领取，并保存每日用量。
- 2.0.0：适配 Minecraft Java 1.20.5 的物品组件格式，重构命令实现。

项目采用 [GPL-3.0 许可证](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/tree/master/LICENSE)。作者：SeeU_SAMA、FRUITS_CANDY。

PND 原版技术生存群组服的 QQ 交流群：417086159。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [G0d-of-Heads-v2.1.0.mcdr](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/tag/2.1.0) | 2.1.0 | 2026/09/24 08:19:57 | 15.43KB | 6 | [下载](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/download/2.1.0/G0d-of-Heads-v2.1.0.mcdr) |
| [G0d-of-Heads-v2.0.1.mcdr](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/tag/2.0.1) | 2.0.1 | 2026/07/23 11:40:15 | 13.58KB | 80 | [下载](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/download/2.0.1/G0d-of-Heads-v2.0.1.mcdr) |
| [G0d-of-Heads-v2.0.0.mcdr](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/tag/2.0.0) | 2.0.0 | 2025/03/08 17:34:44 | 15.81KB | 419 | [下载](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/download/2.0.0/G0d-of-Heads-v2.0.0.mcdr) |
| [G0d-of-Heads-v1.1.0.mcdr](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/tag/1.1.0) | 1.1.0 | 2025/02/18 04:12:31 | 13.32KB | 84 | [下载](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/download/1.1.0/G0d-of-Heads-v1.1.0.mcdr) |
| [G0d-of-Heads-v1.0.0.mcdr](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/tag/1.0.0) | 1.0.0 | 2025/01/31 13:36:15 | 13.28KB | 84 | [下载](https://github.com/Passion-Never-Dissipate/G0d-of-Heads/releases/download/1.0.0/G0d-of-Heads-v1.0.0.mcdr) |

