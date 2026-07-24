[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## unified_handler

### 基本信息

- 插件 ID: `unified_handler`
- 插件名: Unified Handler
- 版本: 0.2.1
  - 元数据版本: 0.2.1
  - 发布版本: 0.2.1
- 总下载量: 40
- 作者: [Alex3236](https://github.com/Alex3236)
- 仓库: https://github.com/alex3236/UnifiedHandler
- 仓库插件页: https://github.com/alex3236/UnifiedHandler/tree/master
- 标签: [`服务端处理器`](/labels/handler/readme-zh_cn.md)
- 描述: ✨ YAML 驱动的万能服务端处理器，简单、易用、可扩展

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.13.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

**中文** | [`English`](https://github.com/alex3236/UnifiedHandler/tree/master/README_en.md)

# ✨ Unified Handler

一个用于 MCDReforged 的服务端处理器插件——用 YAML 驱动的 profile 来适配各种 Minecraft 服务端，再也不用为了不同服务端装一堆 handler 插件啦。

## 为什么需要它？

MCDR 的插件 handler 机制有个不小的遗憾：

- **同一时间只有一个插件 handler 能生效**。如果服务器插件 A 提供了「命令方块执行 MCDR 命令」的功能，插件 B 提供了「称号前缀解析」的功能——你只能选一个。
- **插件 handler 无法优雅地继承当前 handler**。如果你想提供一个提供增强的 handler，需要做一些不优雅的检测。

Unified Handler 用一套简单的 **Base ⊕ Features** 架构解决这两个问题。

## 怎么做到的？

```
Handler = Base（服务端类型，选一个）⊕ Features（额外功能，随便叠）
```

- **Base** 决定"这是什么服务端"。内置支持 Vanilla / Forge / Bukkit / Velocity / Bedrock BDS，还包括 Cleanroom、Leaves 等特殊分支的适配。
- **Features** 提供可叠加的增强——**多个 Feature 可以同时启用、自由组合**。命令方块识别、称号前缀解析、子服消息路由……像搭积木一样需要哪个就加哪个。

所有行为都由 **YAML profile** 定义——清晰可读、易于修改、升级无忧。

### 为什么不采用 Hook / Mixin 模式？

起初此项目考虑过开放钩子，让其他插件在消息处理时插入逻辑。但最终没有走这条路：

- **效率更高。** Profile 在加载时一次性编译为预处理的 regex 结构，运行时无需在插件间来回跳转、动态查找回调。每条日志行直接匹配，没有额外的分发开销。

- **更容易上手。** 写 YAML 比写 Python 门槛低得多。不需要懂编程、不需要了解 MCDR API——只要照着日志写几行正则就能适配自己的服务端。内置 profile 就是最好的例子：Cleanroom 和 Leaves 的适配都只用了十几行 YAML。

- **一个 handler 就够了。** MCDR 本身只允许一个插件 handler 生效。Base ⊕ Features 的组合已经能覆盖绝大多数场景。与其让多个插件在运行时互相协调，不如把功能收敛到一处，在早期阶段解决问题。

## 快速开始

> [!IMPORTANT]
> **不要和其他 handler 插件一起使用。** MCDR 同时存在多个插件 handler 时，究竟采用哪一个是没有定义的。
> 如果你已经在用其他 handler 插件，请先卸载它们，再把 UnifiedHandler 配置好。

### 📦 安装

在 MCDR 控制台执行：

```
!!MCDR plugin install unified_handler
```

插件会自动生成 `config/unified_handler/config.yml` 并释放内置 profiles，无需手动重载。

也可以手动安装：把 `.mcdr` 文件放进 `plugins/` 目录，然后重载 MCDR。

### ⚙️ 配置

> [!NOTE]  
> 配置完成后，建议按照 [Handler 工作状态验证指南](https://github.com/alex3236/UnifiedHandler/tree/master/doc/handler_troubleshooting.md) 跑一遍检查，确认所有项目都正常。

编辑 `config/unified_handler/config.yml`

<details open>
<summary><strong>✅ 情况一：MCDR 自带的 handler 能处理你的服务端</strong></summary>

如果由 [MCDR 自带的 handler](https://docs.mcdreforged.com/zh-cn/latest/configuration.html#handler) 能覆盖大部分情况，而你只需要一些扩展（比如处理 Team 前缀）：

1. 保留 MCDR 配置文件中原有的 `handler` 字段
2. 把 `base_handler` 设为 `"auto"`
3. 在 `features` 中添加你需要的功能

```yaml
base_handler: "auto"

features:
  - chat_prefixes     # 支持 Team 前缀和称号前缀的玩家消息
  - commandblock      # 可以多加几个，随意组合
```

</details>

<details>
<summary><strong>🔧 情况二：MCDR 自带的 handler 无法处理你的服务端</strong></summary>

比如 BDS、Leaves 等，使用本插件内置的 profile：

1. 把 `base_handler` 设为对应的 profile 名称
2. 按需添加 `features`

```yaml
base_handler: "bedrock_bds"    # 详见“内置 Profile”一节

features:
  - commandblock
```

如果内置 profile 还不够用，你也可以[自己写一个](https://github.com/alex3236/UnifiedHandler/tree/master/doc/custom_profile.md)：

```yaml
base_handler: "my_custom_server"
```

</details>

其他配置项：

```yaml
command_prefix: "!!uh" # 命令前缀
admin_permission: 3    # UnifiedHandler 的命令权限
debug: false           # 设为 true 开启调试输出
```

## 内置 Profile

UnifiedHandler 内置了一些常见的处理情景。感谢这些开发者的付出。

由于未在真实服务端上全部测试，部分 profile 可能存在问题。若使用过程中发现无法处理其标称功能，请在 Issue 中提出。

### Base

| 名称              | 文件                       | 适用于                      | 原始作者                                                                             |
| --------------- | ------------------------ | ------------------------ | -------------------------------------------------------------------------------- |
| `cleanroom`     | `base/cleanroom.yml`     | Cleanroom MC             | [`Cmmmmmm`](https://github.com/CmmmmmmLau/CleanroomHandler)                      |
| `leaves`        | `base/leaves.yml`        | LeavesMC                 | [`Mooling0602`](https://github.com/Mooling0602/LeavesHandler-MCDR)               |
| `lbs_subserver` | `base/lbs_subserver.yml` | Velocity 子服消息识别          | [`Ra1ny_Yuki`](https://github.com/Lazy-Bing-Server/LBSVelocityHandler-MCDR)      |
| `bedrock_bds`   | `base/bedrock_bds.yml`   | Bedrock Dedicated Server | [`Elec glacier`](https://github.com/Elec-Glacier/liteloader_handler), `jiangyan` |

### Features

| 名称              | 文件                           | 作用                                | 原始作者                                                                                                                            |
| --------------- | ---------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `commandblock`  | `features/commandblock.yml`  | `[@]` 和 `[Server]` 消息也能触发 MCDR 命令 | [`Dainsleif`](https://github.com/Dainsleif233/MCDR-Commandblock-Handler)                                                        |
| `chat_prefixes` | `features/chat_prefixes.yml` | 解析 `<[Team]Name>` 格式和称号前缀         | [`DCS`](https://github.com/ayuan94/TitlePrefixHandler), [`Mooling0602`](https://github.com/Mooling0602/VanillaTeamHandler-MCDR) |

## 自定义 Profile

想适配自己的服务端？只需要写几行 YAML。我们有完整的 [JSON Schema](https://github.com/alex3236/UnifiedHandler/tree/master/profile.schema.json) 帮你自动补全和校验。

详见 [自定义 Profile 指南](https://github.com/alex3236/UnifiedHandler/tree/master/doc/custom_profile.md)。

## 贡献你的 Profile

如果你写的 profile 有通用场景（某个服务端的适配、某个常见功能的增强），欢迎通过 PR 提交。提交前请确认：

- 文件放在 `resources/builtin_profiles/base/` 或 `features/` 下
- 包含 `name`、`version`、`changelog`、`description` 字段
- 若适配的是已有插件的 handler，在 PR 中注明原始作者

## 命令

*所有 `!!uh` 命令均需管理员权限。*

| 命令                    | 作用                         |
| --------------------- | -------------------------- |
| `!!uh`                | 查看当前使用的 Base 和启用的 Features |
| `!!uh status`         | 同上                         |
| `!!uh reload`         | 重载配置和 profiles             |
| `!!uh debug [on|off]` | 切换调试输出                     |
| `!!uh update`         | 更新并覆盖过期的内置 profile         |

## 兼容性

- MCDReforged >= 2.13.0
- 零 MCDR 核心修改

## 许可

[FreeBSD License](https://github.com/alex3236/UnifiedHandler/tree/master/LICENSE)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [UnifiedHandler-v0.2.1.mcdr](https://github.com/alex3236/UnifiedHandler/releases/tag/v0.2.1) | 0.2.1 | 2026/05/29 12:56:23 | 23.88KB | 40 | [下载](https://github.com/alex3236/UnifiedHandler/releases/download/v0.2.1/UnifiedHandler-v0.2.1.mcdr) |

