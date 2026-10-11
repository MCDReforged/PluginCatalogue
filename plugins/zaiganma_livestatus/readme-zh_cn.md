[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## zaiganma_livestatus

### 基本信息

- 插件 ID: `zaiganma_livestatus`
- 插件名: ZaiGanMa (LiveStatus)
- 版本: 1.3.0
  - 元数据版本: 1.3.0
  - 发布版本: 1.3.0
- 总下载量: 145
- 作者: [man8in](https://github.com/man8in)
- 仓库: https://github.com/man8in/zaiganma-livestatus
- 仓库插件页: https://github.com/man8in/zaiganma-livestatus/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 允许玩家设置自己的状态标签，并显示在聊天框和 TAB 列表中

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | \>=1.6.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

<div align="center">

# ZaiGanMa (LiveStatus) for MCDReforged

[English](https://github.com/man8in/zaiganma-livestatus/tree/main//README.md) | [繁體中文](https://github.com/man8in/zaiganma-livestatus/tree/main//README.zh-TW.md)

[反馈问题](https://github.com/man8in/zaiganma-livestatus/issues) | [提供建议](https://github.com/man8in/zaiganma-livestatus/discussions)

</div>

> [!NOTE]
> ZaiGanMa (LiveStatus) 是一款轻量级 MCDR 插件，允许玩家设置自己的状态标签，并显示在聊天框和 TAB 列表中。基于 Minecraft 原版 Team 机制。

> [!IMPORTANT]
> **强烈建议使用 1.3.0 版本！** 1.3.0 全新增加**昵称模式**（管理员为玩家分配带颜色的昵称，替代状态标签），新增配置面板子指令、`!!zgm cle` 指令别名等特性，并修复了多项问题；旧版本可能存在兼容性问题，请务必升级到 [v1.3.0](https://github.com/man8in/zaiganma-livestatus/releases)。

## 📋 目录

- [功能特性](#-功能特性)
- [安装](#安装)
- [依赖](#依赖)
- [使用说明](#使用说明)
- [HTTP API](#-http-api)
- [配置说明](#配置说明)
- [支持的颜色](#支持的颜色)
- [开源协议](#开源协议)

## ✨ 功能特性

- ✅ 设置/清除手动状态 (`!!zgm set / clear`)
- ✅ 设置状态颜色 (`!!zgm color`)
- ✅ **预设状态** - 离线可见，上线自动生效 (`!!zgm preset / pending / cancel_pending`)
- ✅ 查询任意玩家状态（**支持离线玩家**）(`!!zgm <玩家名>`)
- ✅ **状态历史记录** 及隐私控制 (`!!zgm history`)
- ✅ 状态库管理 (`!!zgm lib`)
- ✅ 随机推荐状态 (`!!zgm suggest`)
- ✅ **HTTP API** 外部程序集成
- ✅ 自动识别假人 (`bot_` 前缀)
- ✅ 管理员配置面板 (`!!zgm config`)
- ✅ **昵称模式**（1.3.0 新增）- 管理员为玩家分配带颜色的昵称，替代状态标签 (`!!zgm give / take / list / nickcolor`)
- ✅ **状态黑名单** - 封禁指定玩家或状态词 (`!!zgm admin`)
- ✅ **自动检查更新 + 更新提示** - 发现新版本时向在线管理员推送可点击的一键更新提示（`[点击更新]` `[点击重载]` `[查看详情]`）
- ✅ 指令帮助菜单 (`!!zgm help`)

## 安装

在 MCDR 控制台执行：

```
!!MCDR plugin install zaiganma_livestatus
```

或者从 [Releases 页面](https://github.com/man8in/zaiganma-livestatus/releases) 下载 `.mcdr` 文件放入 `plugins` 文件夹。

> [!IMPORTANT]
> 强烈建议使用 **1.3.0** 版本。可在 Releases 页面或用 `!!MCDR plugin list` 确认当前版本，旧版本请及时升级。

## 依赖

| 依赖                 | 版本       | 必要性  |
| ------------------ | -------- | ---- |
| MCDR               | >= 2.0.0 | ✅ 必须 |
| minecraft_data_api | >= 1.6.0 | ✅ 必须 |

> [!NOTE]
> 插件会为每位玩家自动计算离线伪 UUID，无需安装额外的 UUID 插件。

## 使用说明

插件有两种模式：默认的**状态模式**和 1.3.0 新增的**昵称模式**（`nickname_mode`），不同模式下可用指令略有差异。

### 基本指令（两种模式通用）

| 指令                 | 说明               |
| ------------------ | ---------------- |
| `!!zgm`            | 查看自己的状态/昵称       |
| `!!zgm help`       | 查看所有指令（可点击使用）    |
| `!!zgm <玩家名>`      | 查看他人状态（**支持离线**） |
| `!!zgm info <玩家名>` | 查看他人状态（防指令冲突写法）  |
| `!!zgm update`     | 检查插件更新（仅限管理员）    |

### 状态模式指令（默认模式）

| 指令                                   | 说明               |
| ------------------------------------ | ---------------- |
| `!!zgm set <文字>`                     | 设置状态             |
| `!!zgm clear` / `!!zgm cle`          | 清除状态             |
| `!!zgm color/col <颜色>`               | 设置状态颜色           |
| `!!zgm clib`                         | 查看可用颜色           |
| `!!zgm suggest/sug`                  | 随机推荐状态           |
| `!!zgm preset <文字>`                  | 设置预设状态（下次上线自动生效） |
| `!!zgm pending`                      | 查看预设状态           |
| `!!zgm cancel_pending`               | 取消预设状态           |
| `!!zgm history [玩家名]`                | 查看状态历史（不填则查看自己）  |
| `!!zgm history privacy <true/false>` | 设置历史隐私           |
| `!!zgm lib`                          | 查看状态库（点击使用）      |
| `!!zgm lib add <文字>`                 | 添加状态到库           |
| `!!zgm lib remove/rem <文字>`          | 从库删除状态           |
| `!!zgm lib reload`                   | 从文件重载状态库         |
| `!!zgm lib reset`                    | 重置状态库为默认（仅限管理员）  |

### 昵称模式指令（1.3.0 新增）

| 指令                           | 说明                 |
| ---------------------------- | ------------------ |
| `!!zgm give <玩家名> <昵称>`      | 为指定玩家分配昵称（仅限管理员）   |
| `!!zgm take <玩家名>`           | 移除指定玩家的昵称（仅限管理员）   |
| `!!zgm list`                 | 查看所有昵称（仅限管理员）      |
| `!!zgm nickcolor <玩家名> <颜色>` | 设置指定玩家昵称的颜色（仅限管理员） |

### 管理员指令

| 指令                                           | 说明                   |
| -------------------------------------------- | -------------------- |
| `!!zgm config` / `!!zgm config panel`        | 查看配置面板（仅限管理员）        |
| `!!zgm config show_status <true/false>`      | 开关状态显示               |
| `!!zgm config allow_color <true/false>`      | 开关自定义颜色              |
| `!!zgm config default_status <文字>`           | 设置默认状态文字             |
| `!!zgm config max_length <数字>`               | 设置状态最大字数（1-20）       |
| `!!zgm config manual_status_timeout <分钟>`    | 设置手动状态超时（0 为永久）      |
| `!!zgm config library_entry_max_length <数字>` | 设置状态库条目最大字数（1-20）    |
| `!!zgm config nickname_mode <true/false>`    | 开关昵称模式（**切换后需重载插件**） |
| `!!zgm config op_permission_level <等级>`      | 设置管理员权限等级            |
| `!!zgm admin ban player <玩家>`                | 封禁玩家设置状态（仅限管理员）      |
| `!!zgm admin unban player <玩家>`              | 解封玩家（仅限管理员）          |
| `!!zgm admin ban status <词>`                 | 封禁状态词（仅限管理员）         |
| `!!zgm admin unban status <词>`               | 解封状态词（仅限管理员）         |
| `!!zgm admin banlist`                        | 查看黑名单（仅限管理员）         |

> [!TIP]
> 在 `!!zgm lib`、`!!zgm clib`、`!!zgm suggest`、`!!zgm config` 中点击状态可自动填入指令，按回车确认即可。

> [!TIP]
> 管理员可在 `!!zgm config` 面板中直接修改常用配置（`show_status`、`allow_color`、`default_status`、`max_length`、`manual_status_timeout`、`library_entry_max_length`、`nickname_mode`、`lib_reload_permission_level` 等），修改后自动保存到 config.json。

> [!NOTE]
> 切换 `nickname_mode` 会清空所有状态/昵称，且需要重载插件才能生效：`!!MCDR plugin reload zaiganma_livestatus`

## 🔌 HTTP API

ZaiGanMa 内置了一个 HTTP API 服务器，允许外部程序（如 QQ 机器人、Web 面板、手机 App 等）通过 HTTP 请求读写玩家状态。

API 服务器默认随插件一起启动，无需额外操作。插件加载成功时，MCDR 日志中会显示：

```
[ZaiGanMa] API 服务器已启动 http://0.0.0.0:8123
```

| 项目      | 值                               |
| ------- | ------------------------------- |
| 基础地址    | `http://你的服务器IP:8123`           |
| GET 接口  | `/api/status/get?uuid=<玩家UUID>` |
| POST 接口 | `/api/status/set`               |

> 监听地址和端口由[配置说明](#配置说明)中的 `api_host` / `api_port` 控制。

### 1️⃣ GET /api/status/get?uuid=<玩家UUID>

查询指定玩家的当前状态。

请求示例：

```bash
curl "http://127.0.0.1:8123/api/status/get?uuid=069a79f4-44e9-4726-a5be-fca90e38aaf5"
```

成功返回：

```json
{
  "success": true,
  "data": {
    "name": "man8in",
    "status": "挖矿中",
    "color": "gold",
    "has_pending": false,
    "updated_at": 1723705800
  }
}
```

| 字段          | 类型      | 说明          |
| ----------- | ------- | ----------- |
| name        | string  | 玩家名称        |
| status      | string  | 当前状态内容      |
| color       | string  | 状态颜色名称      |
| has_pending | boolean | 是否有待生效的预设状态 |
| updated_at  | integer | 状态更新时间戳     |

失败返回：

```json
{
  "success": false,
  "error": "Player not found"
}
```

### 2️⃣ POST /api/status/set

设置玩家的状态。

请求格式：

```
POST http://你的服务器IP:8123/api/status/set
Content-Type: application/json
```

请求参数：

| 参数      | 类型      | 必填  | 默认值   | 说明                   |
| ------- | ------- | --- | ----- | -------------------- |
| uuid    | string  | ✅ 是 | -     | 玩家 UUID              |
| name    | string  | ✅ 是 | -     | 玩家名称                 |
| status  | string  | ✅ 是 | -     | 状态内容                 |
| color   | string  | ❌ 否 | white | 颜色名称                 |
| pending | boolean | ❌ 否 | true  | true=预设状态，false=立即生效 |

请求示例（预设状态）：

```bash
curl -X POST http://127.0.0.1:8123/api/status/set \
  -H "Content-Type: application/json" \
  -d '{"uuid":"069a79f4-44e9-4726-a5be-fca90e38aaf5","name":"man8in","status":"去吃饭了","color":"yellow","pending":true}'
```

成功返回：

```json
{
  "success": true,
  "message": "Status set successfully",
  "pending": true
}
```

请求示例（立即生效）：

```bash
curl -X POST http://127.0.0.1:8123/api/status/set \
  -H "Content-Type: application/json" \
  -d '{"uuid":"069a79f4-44e9-4726-a5be-fca90e38aaf5","name":"man8in","status":"正在挖矿","color":"gold","pending":false}'
```

失败返回：

```json
{
  "success": false,
  "error": "Missing uuid"
}
```

### 🔒 安全建议

> [!WARNING]
> API 默认**没有身份验证**。如需公网访问，请根据实际情况配置安全措施。

**1. 限制监听地址**

如果只需要本地访问（如与 MCDR 同机运行的 QQ 机器人），将 `api_host` 改为 `127.0.0.1`，这样只有本机程序可以访问 API。

**2. 修改默认端口**

避免使用默认端口，降低被扫描的风险（如改为 `38123`）。

**3. 防火墙限制**

使用防火墙（如 iptables、ufw）限制只能特定 IP 访问：

```bash
# 只允许 192.168.1.100 访问 8123 端口
ufw allow from 192.168.1.100 to any port 8123
```

**4. 添加 Token 验证（高级）**

如果需要更高级的安全控制，可以自行在 API 处理器中添加 Token 验证。在 `StatusAPIHandler` 类的开头添加：

```python
API_TOKEN = "your_secret_token_here"

def do_GET(self):
    token = self.headers.get('Authorization', '').replace('Bearer ', '')
    if token != self.API_TOKEN:
        self._send_json(401, {'error': 'Unauthorized'})
        return
    # ... 原有代码
```

### 💻 集成示例

**Python（QQ 机器人）：**

```python
import requests

API_BASE = "http://127.0.0.1:8123"

def get_player_status(uuid):
    resp = requests.get(f"{API_BASE}/api/status/get", params={"uuid": uuid})
    return resp.json()

def set_player_status(uuid, name, status, color="white", pending=True):
    resp = requests.post(f"{API_BASE}/api/status/set", json={
        "uuid": uuid,
        "name": name,
        "status": status,
        "color": color,
        "pending": pending
    })
    return resp.json()
```

**JavaScript（Node.js）：**

```javascript
const axios = require('axios');

const API_BASE = 'http://127.0.0.1:8123';

async function getPlayerStatus(uuid) {
    const resp = await axios.get(`${API_BASE}/api/status/get`, { params: { uuid } });
    return resp.data;
}

async function setPlayerStatus(uuid, name, status, color = 'white', pending = true) {
    const resp = await axios.post(`${API_BASE}/api/status/set`, {
        uuid,
        name,
        status,
        color,
        pending
    });
    return resp.data;
}
```

### ❓ 常见问题

**Q1：API 请求返回 404？**

URL 路径错误或 API 服务器未启动。确认 MCDR 日志中有 `[ZaiGanMa] API 服务器已启动 http://...`，并确认请求的 URL 路径正确（区分大小写）。

**Q2：返回 `{"success": false, "error": "Player not found"}`？**

数据库中没有该 UUID 对应的玩家记录。玩家需要至少设置过一次状态，才会在数据库中有记录。

**Q3：如何获取玩家的 UUID？**

- 在游戏内使用 `!!zgm` 或查询历史（根据服务器配置可能显示）
- 插件会为每位玩家自动计算离线伪 UUID（`OfflinePlayer:玩家名` 的 MD5 值），无需额外插件
- 或直接查询数据库：

```bash
sqlite3 config/zaiganma_livestatus/zaigamma.db "SELECT uuid, name FROM player_status;"
```

**Q4：修改配置后 API 没有变化？**

需要重载插件：

```
!!MCDR reload ZaiGanMa
```

**Q5：API 可以跨域访问吗？**

可以。API 已在响应头中添加 `Access-Control-Allow-Origin: *`，支持跨域请求。

## 配置说明

首次运行自动生成 config.json：

| 配置项                         | 类型      | 默认值                  | 说明                               |
| --------------------------- | ------- | -------------------- | -------------------------------- |
| show_status                 | boolean | true                 | 状态显示总开关                          |
| show_in_tab                 | boolean | true                 | 是否在 TAB 列表中显示状态前缀（可选键，需要时可手动添加）  |
| nickname_mode               | boolean | false                | 昵称模式 - 用管理员分配的昵称替代状态标签（切换后需重载插件） |
| default_status              | string  | 在线                   | 默认状态文字                           |
| max_length                  | integer | 8                    | 状态最大字数                           |
| allow_color                 | boolean | true                 | 允许自定义颜色                          |
| manual_status_timeout       | integer | 180                  | 手动状态超时（分钟，0 为永久）                 |
| api_host                    | string  | 0.0.0.0              | HTTP API 监听地址                    |
| api_port                    | integer | 8123                 | HTTP API 端口                      |
| library_entry_max_length    | integer | 8                    | 状态库条目最大字数                        |
| op_permission_level         | integer | 3                    | 管理指令权限等级（配置面板、重置状态库等）            |
| lib_reload_permission_level | integer | 3                    | 状态库重载/重置所需权限等级                   |
| chat_prefix_style           | string  | text                 | 聊天前缀样式                           |
| auto_check_update           | boolean | true                 | 启动时自动检查更新，并向在线管理员推送可点击的更新提示      |
| update_check_interval       | integer | 86400                | 更新检查间隔（秒）                        |
| update_proxy                | string  | https://ghproxy.com/ | GitHub API 访问代理（用于检查更新）          |
| banned_players              | list    | []                   | 禁止设置状态的玩家黑名单                     |
| banned_statuses             | list    | []                   | 禁止使用的状态词黑名单（支持子串匹配）              |

## 支持的颜色

black、dark_blue、dark_green、dark_aqua、dark_red、dark_purple、gold、gray、dark_gray、blue、green、aqua、red、light_purple、yellow、white

也支持十六进制颜色，如 `#FF6B6B`。

## 开源协议

MIT

## 作者

man8in — [GitHub](https://github.com/man8in)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ZaiGanMa.LiveStatus.-v1.3.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/v1.3.0) | 1.3.0 | 2026/10/06 16:29:19 | 17.48KB | 6 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/v1.3.0/ZaiGanMa.LiveStatus.-v1.3.0.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.2.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.2.0) | 1.2.0 | 2026/09/27 10:36:56 | 16.12KB | 14 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.2.0/ZaiGanMa.LiveStatus.-v1.2.0.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.1.1.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.1.1) | 1.1.1 | 2026/08/29 06:08:22 | 14.11KB | 21 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.1.1/ZaiGanMa.LiveStatus.-v1.1.1.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.1.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.1.0) | 1.1.0 | 2026/08/16 08:06:02 | 14.23KB | 26 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.1.0/ZaiGanMa.LiveStatus.-v1.1.0.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.2.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.2) | 1.0.2 | 2026/08/06 07:32:13 | 8.7KB | 29 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.2/ZaiGanMa.LiveStatus.-v1.0.2.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.1.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.1) | 1.0.1 | 2026/08/04 18:16:46 | 9.12KB | 25 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.1/ZaiGanMa.LiveStatus.-v1.0.1.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.0) | 1.0.0 | 2026/08/04 06:41:52 | 7.73KB | 24 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.0/ZaiGanMa.LiveStatus.-v1.0.0.mcdr) |

