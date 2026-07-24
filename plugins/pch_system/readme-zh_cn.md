[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## pch_system

### 基本信息

- 插件 ID: `pch_system`
- 插件名: PCH System
- 版本: 0.8.0
  - 元数据版本: 0.8.0
  - 发布版本: 0.8.0
- 总下载量: 23
- 作者: [YuShen](https://github.com/YuShenLiu06)
- 仓库: https://github.com/YuShenLiu06/PCHSystem
- 仓库插件页: https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`信息`](/labels/information/readme-zh_cn.md)
- 描述: 材料协作收集与项目进度管理，联动 Web 后台

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.0 |
| [uuid_api_remake](/plugins/uuid_api_remake/readme-zh_cn.md) | * |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | * |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [requests](https://pypi.org/project/requests) | \>=2.31 |

```
pip install "requests>=2.31"
```

### 介绍

# HTCMC Project Contribution & Honor System

> 面向白名单生电社区服的**项目制工程贡献与荣誉体系**。把「工程项目协作 + 积分激励」搬进 Minecraft：玩家在游戏里协作完成工程项目，系统跟踪每位参与者的贡献，完结后归档沉淀，（将来）按贡献结算积分与称号。流程全自动。

> ⚠️ **仍在开发中**：当前已交付身份主锚（Web 账号绑多身份）/ 项目协作（含协管员角色）/ 归档 / 通知 / 一键部署；积分、称号等核心玩法尚未落地。见[开发状态](#开发状态)。

---

## 功能特性

### 特性

- **后端分离**：游戏内端与后端完全分离（不强制绑定MCDR），后端可独立部署，游戏内端仅作为客户端。由于前后端分离，在未来可以甚至实现以下功能：
  - 跨服务器同步数据：多个服务器的 MCDR 指向同一个后端，无缝同步
  - 更好的多平台支持：由于后端所有操作由 FASTAPI 封装，你可以以很少的代码完成其他平台的开发（如fabric，forge，neoforge，的客户端开发，或者 Bukkit、Spigot等平台的开发）
  - 不强制依赖 MCDR：由于前后端分离，你甚至可以在服主不添加该插件的前提下进行部署，如 2b2t 等无政府服务器等的组织备货
- **独立前端**：提供独立的 Web 前端，玩家可在 Web 端查看项目进度、编辑材料清单、上传投影 / 蓝图等，不进游戏也能协作；游戏端或 MCDR 重启时，Web 端仍可独立访问
- **兼容性强**：基于MCDR的强大兼容性，可以在几乎所有的我的世界版本上面运行

### 功能（已实现）

- **游戏内登录后台**：`!!PCH login` 一键生成登录链接，点击直接进入 web 页面方便操作
- **项目协作（在线表格）**：完整的项目材料清单协作——认领材料、多人累计上交、交付确认、打回返工、解除锁定，Web 端与游戏端**对等操作**
  - 一键提交：支持一键扫描背包（支持潜影盒内物品）上报进度。
  - 投影 / 蓝图一键建表：上传 `.litematic` 投影或机械动力 `.nbt` 蓝图，自动解析方块、翻译成中文名、生成材料清单（支持原版与 Create 模组物品）（仅 web 端支持）
  - 子物品：一键通过倍数（支持小数）来直接生成子一级的合成物品的清单
  - 快捷命令：游戏内大量命令已经通过可点击的方式来达到便携化，尽可能的减少手打命令的状况
  - 智能数量换算：自动将数量换算成可读性更高的 个/组/盒 （正在考虑加入箱盒）
  - 游戏内快速读取手持 `registry-id` 直接更改所需的物品 id，新增物品，去除手打物品 id 的苦恼
  - Web 端行编辑：在线编辑材料行（名称 / 数量 / `registry-id`），与游戏端操作对等
- **项目归档**：项目完结自动生成归档文档 + 贡献占比饼图，精确记录每位参与者的贡献
- **通知投递**：认领 / 交付 / 打回 / 项目状况变化 / 上交等事件游戏内自动通知，离线期间的通知上线补推

![一览](https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/main/McdrPlugin/../McdrPlugin/docs/img/sheet-mc.png)

### 规划中（尚未实现）

- **积分体系**：提供统一积分层，管理相关内容
  - 提供统一积分入账层
  - 提供统一积分出账层
  - 提供积分排行榜
  - 完善项目归档自动结算积分
- **指数增长称号**：积分达标自动解锁，聊天前缀差异化，高阶全服公告
- **项目协作（施工阶段）**：真正校验建造放置（当前施工阶段为占位）
  - 提供实时的计分板进度显示
- **Wiki 归档同步**：归档内容双向同步到 wiki.js
  - 项目权限继承：将项目拥有者，admin，自动拥有该篇归档 wiki 的编辑权限

---

## 部署

### 一键脚本（推荐）

面向服主，一条命令完成 Docker 安装、国内网络镜像自适应、配置生成、起服务、数据库迁移、前端构建、`pch_system` 插件部署与 token 双写：

```bash
git clone https://github.com/YuShenLiu06/PCHSystem.git
cd PCHSystem
bash Scripts/install.sh    # 首次安装（交互式，幂等）
bash Scripts/update.sh     # 之后日常更新
```

完整选项（镜像策略、排错、密钥轮换、禁用前端容器等）见 [`Scripts/README.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Scripts/README.md)。

### 手动（docker compose）

```bash
cp .env.example .env       # 按需改密钥
docker compose up -d       # 起 postgres + backend + web（前端默认由 web 容器托管）
curl http://localhost:8000/healthz
```

> `.env` 的 `COMPOSE_PROFILES=web` 默认启用前端 web 容器（nginx 托管 `dist` + 反代 `/api`）；清空即禁用，改由自有 nginx 托管。详见 [`Docs/RUNBOOK.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Docs/RUNBOOK.md)。

> 本项目**不含 Minecraft 服务端**：MCDReforged 由你持有，插件经 HTTP 与后端通信。MCDR 插件本身的部署见 [`McdrPlugin/README.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././McdrPlugin/README.md)。

---

## 架构

三端分离：**后端（FastAPI + PostgreSQL）** 是唯一数据拥有者；**Web 端（Vue3）** 是浏览器后台；**游戏端（MCDR 插件）** 是纯客户端，不直连数据库，只经 HTTP 与后端通信。前端默认由 compose 的 web 容器（nginx）托管。

![architecture](https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/main/McdrPlugin/../Image/architecture.png)

完整架构图、ADR、跨服务流程见 [`Docs/architecture.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Docs/architecture.md)。

---

## 开发状态

| 状态    | 模块                                                                       |
| ----- | ------------------------------------------------------------------------ |
| ✅ 已交付 | 登录鉴权（Web 账号绑多身份 + 密码登录）、项目协作（在线表格 + 协管员角色）、投影 / 蓝图解析、材料上交、项目归档、通知投递、一键部署 |
| 🚧 规划中 | 积分结算、指数称号、施工方块检测、Wiki 同步、风控告警                                            |

详见 [`TODO.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././TODO.md) 与 [`CHANGELOG.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CHANGELOG.md)。

---

## 开发与贡献

- 部署 / 排错 / 回滚：[`Docs/RUNBOOK.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Docs/RUNBOOK.md)
- 分支 / Commit / 发布规范：[`CONTRIBUTING.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CONTRIBUTING.md)
- 根规范（红线、命名）：[`CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CLAUDE.md)
- 各端开发指引：[`Backend/CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Backend/CLAUDE.md) · [`Frontend/CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Frontend/CLAUDE.md) · [`McdrPlugin/CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././McdrPlugin/CLAUDE.md)

提 PR 前请先读 [`CONTRIBUTING.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CONTRIBUTING.md) 与 [`CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CLAUDE.md) §3 红线；涉及 MCDR 的改动须先联网核实 API（根 [`CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CLAUDE.md) §0 S-1）。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [pch_system-v0.8.0.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.8.0) | 0.8.0 | 2026/07/20 13:30:51 | 57.62KB | 6 | [下载](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.8.0/pch_system-v0.8.0.mcdr) |
| [pch_system-v0.7.1.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.7.1) | 0.7.1 | 2026/07/14 04:24:44 | 51.67KB | 8 | [下载](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.7.1/pch_system-v0.7.1.mcdr) |
| [pch_system-v0.7.0.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.7.0) | 0.7.0 | 2026/07/12 13:04:16 | 51.54KB | 9 | [下载](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.7.0/pch_system-v0.7.0.mcdr) |

