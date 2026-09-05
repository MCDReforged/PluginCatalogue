[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## batch_bot_spawn

### 基本信息

- 插件 ID: `batch_bot_spawn`
- 插件名: BatchBotSpawn
- 版本: 0.2.0
  - 元数据版本: 0.2.0
  - 发布版本: 0.2.0
- 总下载量: 31
- 作者: [oneIdler](https://github.com/oneIdler)
- 仓库: https://github.com/SDK-Minecraft-Server/BatchBotSpawn
- 仓库插件页: https://github.com/SDK-Minecraft-Server/BatchBotSpawn/tree/release
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: A plugin for batch managing Carpet fake players

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.0.0 |

```
pip install "mcdreforged>=2.0.0"
```

### 介绍

# BatchBotSpawn

[English](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/tree/release/README_en.md) | 简体中文

一款用于 **批量管理 Carpet 假人** 的 MCDR 插件，支持自定义名称前缀/后缀、在线状态检测、命令限流与生成结果验证，让假人生成、丢弃物品、下线等操作更高效便捷。

---

## 💡 灵感来源

本项目的灵感与思路参考自 [Walkersifolia/FastBotSpawn](https://github.com/Walkersifolia/FastBotSpawn)。

---

## ✨ 主要功能

- **批量生成**：按指定序号范围批量生成假人，支持自定义名称前缀和后缀。
- **智能跳过**：自动检测已在线的假人并跳过生成，避免重复。
- **操作限流**：批量指令按可配置的间隔逐条发送，避免刷爆服务端命令队列。
- **结果验证**：生成后可等待一段时间并验证实际上线数量。
- **离线跳过**：`drop` / `kill` 只对在线假人发送指令，避免服务端报错。
- **灵活配置**：可设置单次操作数量上限、默认数量、发送间隔等，并持久化保存。
- **在线列表**：`!!b list` 列出当前匹配命名规则的在线假人，点击可直接填入下线指令。
- **多语言支持**：内置中文（zh_CN）和英文（en_US）命令界面。

---

## 📦 依赖

- **MCDR** ≥ 2.0.0
- **Carpet Mod**（服务端需安装，并提供 `/player` 命令）
- **minecraft_data_api**（可选但推荐。安装后通过 `/list` 准确获取在线玩家列表；未安装时插件使用 MCDR 的玩家进出事件维护在线列表，服务端启动前已在线的玩家可能无法被识别）

---

## 🚀 安装

1. 将插件文件夹放入 MCDR 的 `plugins` 目录。
2. 建议同时安装 `minecraft_data_api` 插件。
3. 重启 MCDR 或执行 `!!MCDR reload plg` 加载插件。

---

## 🔧 命令列表

所有命令以 `!!b` 开头，仅玩家可用（控制台暂不支持）。其中 `pre / suf / limit / def_num / clear` 为配置命令，需要 **管理员（admin）** 及以上权限。

| 命令                         | 说明                        | 示例                    |
| -------------------------- | ------------------------- | --------------------- |
| `!!b pre <前缀>`             | 设置假人名称前缀（推荐与 Carpet 同步）   | `!!b pre bot_`        |
| `!!b suf <后缀>`             | 设置假人名称后缀（推荐与 Carpet 同步）   | `!!b suf _fake`       |
| `!!b limit <数量>`           | 设置单次操作假人数量上限              | `!!b limit 20`        |
| `!!b def_num <数量>`         | 设置默认召唤数量（需 ≤ limit）       | `!!b def_num 5`       |
| `!!b clear`                | 清除前缀和后缀设置                 | `!!b clear`           |
| `!!b spawn [名字] [最小] [最大]` | 批量生成假人（默认 1~def_num）      | `!!b spawn test 1 10` |
| `!!b drop [名字] [最小] [最大]`  | 批量让假人丢弃全部物品（默认 1~def_num） | `!!b drop test 1 5`   |
| `!!b kill [名字] [最小] [最大]`  | 批量让假人下线（默认 1~def_num）     | `!!b kill test 1 5`   |
| `!!b list [名字]`            | 列出在线且匹配命名规则的假人            | `!!b list test`       |

> **参数说明**：
> - `[名字]`、`[最小]`、`[最大]` 均为可选参数，具体组合如下：
>   - 不填参数：按默认范围 `1~def_num` 操作；
>   - 1 个数字：只操作该序号；
>   - 2 个数字：按序号范围操作；
>   - `名字` 放在最前面时：1 个数字 = 该名字的单个序号，2 个数字 = 该名字的序号范围。
> - `[名字]` 需为 1-16 位字母、数字或下划线，且最终假人名称（`前缀 + 名字/序号 + 后缀`）总长度不超过 16 字符。

---

## ⚙️ 配置

配置文件位于 `config/batch_bot_spawn/config.json`（首次运行自动生成，也可通过游戏内命令修改）。

```json
{
  "prefix": "bot_",
  "suffix": "",
  "limit": 10,
  "def_num": 10,
  "interval": 0.05,
  "verify": true,
  "verify_delay": 2.0
}
```

| 配置项            | 默认值    | 说明                                 |
| -------------- | ------ | ---------------------------------- |
| `prefix`       | `""`   | 假人名称前缀                             |
| `suffix`       | `""`   | 假人名称后缀                             |
| `limit`        | `10`   | 单次操作假人数量上限（spawn / drop / kill 共用） |
| `def_num`      | `10`   | 默认召唤数量，加载时自动钳制到不超过 `limit`         |
| `interval`     | `0.05` | 发送每条指令的间隔（秒），设为 0 可关闭限流            |
| `verify`       | `true` | 生成后是否等待并验证实际上线数量                   |
| `verify_delay` | `2.0`  | 生成后等待验证的秒数                         |

> 提示：`prefix` / `suffix` 需与 Carpet 的 `player` 命令实际名称一致，否则 `list` 无法正确匹配。

---

## 🧪 开发与测试

运行单元测试（需在安装有 MCDR 的 Python 环境中执行）：

```bash
python -m unittest discover -s tests -v
```

构建发布包：

```bash
python -m mcdreforged pack -i . -o releases
```

---

## 📄 许可证

本项目基于 [MIT License](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/tree/release/LICENSE) 开源。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [BatchBotSpawn-v0.2.0.mcdr](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/releases/tag/v0.2.0) | 0.2.0 | 2026/08/01 12:09:33 | 9.17KB | 31 | [下载](https://github.com/SDK-Minecraft-Server/BatchBotSpawn/releases/download/v0.2.0/BatchBotSpawn-v0.2.0.mcdr) |

