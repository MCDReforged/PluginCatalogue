[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## zaiganma_livestatus

### 基本信息

- 插件 ID: `zaiganma_livestatus`
- 插件名: ZaiGanMa (LiveStatus)
- 版本: 1.1.1
  - 元数据版本: 1.1.1
  - 发布版本: 1.1.1
- 总下载量: 67
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

## 安装

在 MCDR 控制台执行：

```
!!MCDR plugin install zaiganma_livestatus
```

或者从 [Releases 页面](https://github.com/man8in/zaiganma-livestatus/releases) 下载 `.mcdr` 文件放入 `plugins` 文件夹。

## 依赖

| 依赖                 | 版本       | 必要性  |
| ------------------ | -------- | ---- |
| MCDR               | >= 2.0.0 | ✅ 必须 |
| minecraft_data_api | >= 1.6.0 | ✅ 必须 |
| uuid_api           | >= 1.0.0 | ⭕ 可选 |

> [!TIP]
> `uuid_api` 为可选依赖：安装后可改善离线玩家的 UUID 解析，未安装时插件会自动降级，不影响核心功能。

## 使用说明

| 指令                                   | 说明               |
| ------------------------------------ | ---------------- |
| `!!zgm`                              | 查看自己的状态          |
| `!!zgm <玩家名>`                        | 查看他人状态（**支持离线**） |
| `!!zgm set <文字>`                     | 设置状态             |
| `!!zgm clear`                        | 清除状态             |
| `!!zgm color <颜色>`                   | 设置状态颜色           |
| `!!zgm clib`                         | 查看可用颜色           |
| `!!zgm preset <文字>`                  | 设置预设状态（下次上线自动生效） |
| `!!zgm pending`                      | 查看预设状态           |
| `!!zgm cancel_pending`               | 取消预设状态           |
| `!!zgm history [玩家名]`                | 查看状态历史（不填则查看自己）  |
| `!!zgm history privacy <true/false>` | 设置历史隐私           |
| `!!zgm lib`                          | 查看状态库（点击使用）      |
| `!!zgm lib add <文字>`                 | 添加状态到库           |
| `!!zgm lib remove <文字>`              | 从库删除状态           |
| `!!zgm lib reload`                   | 从文件重载状态库         |
| `!!zgm lib reset`                    | 重置状态库为默认（仅限管理员）  |
| `!!zgm suggest`                      | 随机推荐状态           |
| `!!zgm config`                       | 查看配置面板（仅限管理员）    |

> [!TIP]
> 在 `!!zgm lib`、`!!zgm clib`、`!!zgm suggest`、`!!zgm config` 中点击状态可自动填入指令，按回车确认即可。

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
- 使用 uuid_api 插件：

```python
uuid_api = server.get_plugin_instance('uuid_api')
uuid = uuid_api.get_uuid('man8in')
```

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

| 配置项                      | 类型      | 默认值     | 说明                    |
| ------------------------ | ------- | ------- | --------------------- |
| show_status              | boolean | true    | 状态显示总开关               |
| default_status           | string  | 在线      | 默认状态文字                |
| max_length               | integer | 8       | 状态最大字数                |
| allow_color              | boolean | true    | 允许自定义颜色               |
| manual_status_timeout    | integer | 180     | 手动状态超时（分钟，0 为永久）      |
| api_host                 | string  | 0.0.0.0 | HTTP API 监听地址         |
| api_port                 | integer | 8123    | HTTP API 端口           |
| library_entry_max_length | integer | 8       | 状态库条目最大字数             |
| op_permission_level      | integer | 3       | 管理指令权限等级（配置面板、重置状态库等） |

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
| [ZaiGanMa.LiveStatus.-v1.1.1.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.1.1) | 1.1.1 | 2026/08/29 06:08:22 | 14.11KB | 4 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.1.1/ZaiGanMa.LiveStatus.-v1.1.1.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.1.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.1.0) | 1.1.0 | 2026/08/16 08:06:02 | 14.23KB | 16 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.1.0/ZaiGanMa.LiveStatus.-v1.1.0.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.2.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.2) | 1.0.2 | 2026/08/06 07:32:13 | 8.7KB | 20 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.2/ZaiGanMa.LiveStatus.-v1.0.2.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.1.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.1) | 1.0.1 | 2026/08/04 18:16:46 | 9.12KB | 13 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.1/ZaiGanMa.LiveStatus.-v1.0.1.mcdr) |
| [ZaiGanMa.LiveStatus.-v1.0.0.mcdr](https://github.com/man8in/zaiganma-livestatus/releases/tag/1.0.0) | 1.0.0 | 2026/08/04 06:41:52 | 7.73KB | 14 | [下载](https://github.com/man8in/zaiganma-livestatus/releases/download/1.0.0/ZaiGanMa.LiveStatus.-v1.0.0.mcdr) |

