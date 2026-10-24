[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## leave_reason

### 基本信息

- 插件 ID: `leave_reason`
- 插件名: LeaveReason
- 版本: 1.3.0
  - 元数据版本: 1.3.0
  - 发布版本: 1.3.0
- 总下载量: 8
- 作者: [chuan_yi_awa](https://github.com/wellcy666)
- 仓库: https://github.com/wellcy666/leave_reason
- 仓库插件页: https://github.com/wellcy666/leave_reason/tree/main/src
- 标签: [`信息`](/labels/information/readme-zh_cn.md)
- 描述: 检测玩家异常退出（被踢、连接超时、被封禁、不在白名单）并在公屏广播原因

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# LeaveReason（退出原因）

检测玩家异常退出（被踢、超时、封禁、白名单），把原因广播到公屏。

> AZ 生电服同款插件，审核群 `1101978932`。

解析服务端日志，玩家退出时补上「为什么退出」。玩家「退出」这个动作本身由服务端或公屏转发插件显示，本插件只负责补原因。

## 能检测的原因

| 原因    | 公屏输出示例                                               |
| ----- | ---------------------------------------------------- |
| 被踢    | `xxx 退出游戏，原因：被踢出服务器（你已被移除）`                          |
| 连接超时  | `xxx 退出游戏，原因：连接超时`                                   |
| 被封禁   | `xxx 退出游戏，原因：被封禁`                                    |
| 不在白名单 | `xxx 退出游戏，原因：不在白名单内`                                 |
| 未归类   | `xxx 退出游戏，原因：Attempting to attack an invalid entity` |

文案都能改（见配置一节）。

## 工作原理

- 被踢 / 超时发生在游戏内，日志是 `<玩家> lost connection: <原因>`，能直接拿到玩家名。
- 封禁由原版 `banlist.json` 在登录阶段拦截，日志是 `Disconnecting <地址>: You are banned ...`。
- 白名单由原版 `whitelist.json` 在登录阶段拦截，日志是 `Disconnecting <地址>: You are not white-listed ...`。

> 封禁 / 白名单在登录阶段被拦下时，日志里通常没有玩家名，这时会改用 `message_no_name` 模板播报。这是后端日志本身不记名字，不是 bug。

## 安装

把 `leave_reason.mcdr` 丢进 MCDR 的 `plugins/` 目录，然后 `!!MCDR plugin load leave_reason.mcdr`（或重启）。

## 命令

| 命令                     | 说明   | 权限  |
| ---------------------- | ---- | --- |
| `!!lr`                 | 帮助   | 4   |
| `!!lr on` / `!!lr off` | 开关广播 | 4   |
| `!!lr reload`          | 重载配置 | 4   |
| `!!lr status`          | 查看状态 | 4   |

权限等级 4 = 拥有者 / 控制台。前缀 `!!lr` 在代码里的 `PREFIX` 常量定义。

## 配置

首次加载自动生成 `config/leave_reason/config.json`，改完 `!!lr reload` 生效。常用项：

| 字段                            | 作用                                                |
| ----------------------------- | ------------------------------------------------- |
| `enabled`                     | 总开关                                               |
| `message` / `message_no_name` | 消息格式，`{player}`=玩家名，`{reason}`=原因                 |
| `reason_text`                 | 四类原因的文案（`kick` / `timeout` / `ban` / `whitelist`） |
| `append_kick_detail`          | 被踢时是否附上原始理由                                       |
| `show_unknown`                | 没匹配到的原因是否也播报                                      |
| `dedup_seconds`               | 同一玩家同一原因去重秒数                                      |
| `keywords`                    | 归类关键词                                             |

最小配置：

```json
{
    "config_version": 2,
    "enabled": true,
    "message": "§7[§c!§7] §e{player} §7退出游戏，原因：§f{reason}",
    "message_no_name": "§7[§c!§7] §e有玩家 §7被拒绝加入，原因：§f{reason}",
    "reason_text": {
        "kick": "被踢出服务器",
        "timeout": "连接超时",
        "ban": "被封禁",
        "whitelist": "不在白名单内"
    }
}
```

从 1.2.x 升级：旧配置没有 `config_version`，会自动备份成 `config.json.bak` 再生成新格式。

## 调参

1. 先把 `debug` 设为 `true` 并 `!!lr reload`，用非白名单玩家和被封禁玩家各试一次，看控制台 `[leave_reason][debug]` 归类对不对。
2. 白名单拦截如果不是原版 `not white-listed` 而是插件自己踢人，把那段自定义文案的关键词加进 `keywords.whitelist`。
3. 正常断开（`Disconnected`）默认在 `keywords.ignore` 里被忽略，不刷屏，要检测就删掉它。

## 反馈

QQ：`2683654412`。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [leave_reason.mcdr](https://github.com/wellcy666/leave_reason/releases/tag/v1.3.0) | 1.3.0 | 2026/10/22 13:25:03 | 8.62KB | 8 | [下载](https://github.com/wellcy666/leave_reason/releases/download/v1.3.0/leave_reason.mcdr) |

