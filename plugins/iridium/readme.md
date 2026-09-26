**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## iridium

### Basic Information

- Plugin ID: `iridium`
- Plugin Name: Iridium
- Version: 26.9.14
  - Metadata version: 26.9.14
  - Release version: 26.9.14
- Total downloads: 5
- Authors: [云镜之端/SKYMirror](https://github.com/HzSKYMirror)
- Repository: https://github.com/HzSKYMirror/Iridium
- Repository plugin page: https://github.com/HzSKYMirror/Iridium/tree/main
- Labels: [`Tool`](/labels/tool/readme.md)
- Description: Item share / hat / player head / calculator / join MOTD

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.6.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction

# Iridium

MCDReforged 插件：物品展示 / 戴头 / 获取头颅 / 游戏内计算器 / 进服 MOTD。

|     |                              |
| --- | ---------------------------- |
| 版本  | **26.9.14**                  |
| 作者  | 云镜之端/SKYMirror               |
| 许可  | **GPL-3.0**                  |
| 前置  | MCDReforged `>= 2.6.0`       |
| MC  | **1.7.10+**（按版本分支；不支持的功能会提示） |
| 依赖  | 无第三方 Python 包                |

## 功能一览

| 功能                | 说明                            |
| ----------------- | ----------------------------- |
| `!!share`         | 展示主手物品：聊天栏显示物品名，悬停查看完整数据      |
| `!!hat`           | 主手与头部装备互换                     |
| `!!head [player]` | 给自己或指定玩家 **1 个** 头颅；有冷却       |
| `!!c <表达式>`       | 四则运算 + 括号：`+ - * / // % ** ^` |
| 进服 MOTD           | 开服天数、自定义行、可点击链接、`§` 颜色        |
| 进服命令提示            | 可点击填入聊天框                      |

## 安装

### 方式 A：使用发布包

1. 下载 `Iridium.mcdr`
2. 放入 MCDR 的 `plugins/` 目录
3. `!!MCDR reload plugin` 或重启 MCDR

### 方式 B：从源码打包

```bash
./pack.sh
# 或
zip -r Iridium.mcdr iridium lang mcdreforged.plugin.json LICENSE
```

### 使用 `!!hat` / 无 RCON 的 `!!share`

在 `server.properties` 中启用 RCON，并在 MCDR 配置里填好连接信息：

```properties
enable-rcon=true
rcon.port=25575
rcon.password=your_password
```

| 功能        | 无 RCON               | 有 RCON |
| --------- | -------------------- | ------ |
| `!!share` | 可用（解析控制台回包，空手可能超时提示） | 推荐     |
| `!!hat`   | 不可用（会提示）             | 必需     |

## 命令

| 命令                | 权限（默认）       | 说明          |
| ----------------- | ------------ | ----------- |
| `!!share`         | `permission` | 展示主手物品      |
| `!!hat`           | `permission` | 手与头盔交换      |
| `!!head`          | `permission` | 给自己一个头颅     |
| `!!head <player>` | `permission` | 给自己一个该玩家的头颅 |
| `!!c <表达式>`       | `permission` | 计算并私聊回复结果   |

帮助列表可用 `!!help` 查看（已注册 help message）。

## 版本能力

| 功能          | 1.7.10 |   1.8–1.12   | 1.13–1.16  | 1.17–1.20.4 |   1.20.5+    |
| ----------- | :----: | :----------: | :--------: | :---------: | :----------: |
| `!!c`       |   ✅    |      ✅       |     ✅      |      ✅      |      ✅       |
| `!!head`    |   ✅    |      ✅       |     ✅      |      ✅      | ✅ profile 组件 |
| `!!share`   |  ❌ 提示  | ✅ entitydata | ✅ data get |      ✅      |      ✅       |
| `!!hat`     |  ❌ 提示  |    ✅ RCON    |   ✅ RCON   |   ✅ RCON    |    ✅ RCON    |
| MOTD / 进服提示 |   ✅    |      ✅       |     ✅      |      ✅      |      ✅       |

无法检测版本时会提示；可在配置中设置 `force_version`（如 `"1.12.2"`）。

## 配置

路径：`config/iridium/iridium.yml`（YAML，`#` 注释；首次加载自动生成；旧的 `config/iridium.json` / `config/iridium/iridium.json` 会自动迁移）

```yaml
permission: 1
head_cooldown_seconds: 60
hat_cooldown_seconds: 3
share_sound: true
force_version: ""
join_tip: true
join_tip_delay_seconds: 1.5
motd_enabled: true
motd_start_day: "2026-09-14"
motd_lines:
  - "§6欢迎 §e{player}§6 加入服务器！"
  - "§7服务器已开服 §b{days}§7 天"
  - "§7官网: {link:§b点击打开官网|https://www.skymirror.top}"
  - "§7QQ群: {link:§f985402607|https://skymirror.top/qq}"
```

| 字段                       | 默认     | 说明                                   |
| ------------------------ | ------ | ------------------------------------ |
| `permission`             | `1`    | 各命令最低权限（0 控制台 / 1 普通玩家 / 2 OP）       |
| `head_cooldown_seconds`  | `60`   | `!!head` 冷却；`0` 不限制                  |
| `hat_cooldown_seconds`   | `3`    | `!!hat` 冷却；`0` 不限制                   |
| `share_sound`            | `true` | `!!share` 是否播放提示音                    |
| `force_version`          | `""`   | 强制 MC 版本；留空自动检测                      |
| `join_tip`               | `true` | 进服是否提示可用命令                           |
| `join_tip_delay_seconds` | `1.5`  | 进服消息延迟；`0` 立即                        |
| `motd_enabled`           | `true` | 是否发送 MOTD                            |
| `motd_start_day`         | 生成配置当天 | 开服日期 `YYYY-MM-DD`（当天算第 1 天）；可改成真实开服日 |
| `motd_lines`             | 见上     | MOTD 文本行                             |

修改配置后执行 `!!MCDR reload plugin` 生效。

### MOTD 语法

| 语法                      | 含义                     |
| ----------------------- | ---------------------- |
| `{player}`              | 进服玩家名（已清洗）             |
| `{days}` / `{day}`      | 开服天数                   |
| `{online}`              | 在线人数，拿不到为 `?`          |
| `{link:文字|https://url}` | 可点击链接                  |
| `{link:https://url}`    | 可点击链接，显示完整 URL         |
| `§`                     | 原版颜色/样式（§a §e §l §r 等） |

仅当 `motd_lines` 中**没有** `{days}`/`{day}` 时，才会在末尾自动追加「开服第 N 天」。

## 常见问题

**`!!hat` 说需要 RCON？**  
未开启 RCON，或 MCDR 未配置 RCON 连接。见上文「使用 !!hat」。

**进服没有 MOTD？**  
检查 `motd_enabled`、`join_tip_delay_seconds`；若延迟 >0，消息会在进服后约 1.5 秒出现。

**版本检测失败？**  
等待 VersionDetector 完成，或配置 `force_version`。

**`!!share` 超时？**  
多为无 RCON 且空手（控制台无 `SelectedItem` 回包）。可开 RCON 或先手持物品再试。

**如何关闭进服提示？**  
`join_tip` 与 `motd_enabled` 可分别设为 `false`。

## 安全说明

- 计算器：字符 + AST 白名单，不执行任意 Python；指数上限 64。
- 玩家名进入游戏命令前统一清洗为 `[A-Za-z0-9_]`（最长 32）。
- 控制台命令会去掉换行，避免拆成多行执行。
- MOTD 链接仅 `http(s)`。
- `!!head` 每次固定 1 个，并受冷却限制。

## 开发与测试

```bash
python3 tests/test_pure.py
```

无需启动 Minecraft；覆盖命令拼装、NBT 解析、计算器、MOTD 与清洗逻辑。

## 版权

Copyright (c) 2026 云镜之端/SKYMirror.

本项目采用 **GNU GPL v3.0** 许可，详见 [LICENSE](https://github.com/HzSKYMirror/Iridium/tree/main/LICENSE)。  
This project is licensed under the **GNU GPL v3.0**. See [LICENSE](https://github.com/HzSKYMirror/Iridium/tree/main/LICENSE).

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [Iridium.mcdr](https://github.com/HzSKYMirror/Iridium/releases/tag/v26.9.14) | 26.9.14 | 2026/09/14 16:43:11 | 31.84KB | 5 | [Download](https://github.com/HzSKYMirror/Iridium/releases/download/v26.9.14/Iridium.mcdr) |

