**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## pch_system

### Basic Information

- Plugin ID: `pch_system`
- Plugin Name: PCH System
- Version: 0.10.2
  - Metadata version: 0.10.2
  - Release version: 0.10.2
- Total downloads: 143
- Authors: [YuShen](https://github.com/YuShenLiu06)
- Repository: https://github.com/YuShenLiu06/PCHSystem
- Repository plugin page: https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin
- Labels: [`Tool`](/labels/tool/readme.md), [`Information`](/labels/information/readme.md)
- Description: 材料协作收集与项目进度管理，联动 Web 后台

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.0 |
| [uuid_api_remake](/plugins/uuid_api_remake/readme.md) | * |
| [minecraft_data_api](/plugins/minecraft_data_api/readme.md) | * |
| [chest_scanner_lib](/plugins/chest_scanner_lib/readme.md) | \>=1.0.1 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [requests](https://pypi.org/project/requests) | \>=2.31 |

```
pip install "requests>=2.31"
```

### Introduction



<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/Assets/logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/Assets/logo.svg">
  <img alt="PCHSystem" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/Assets/logo.svg" width="280">
</picture>

# HTCMC Project Contribution & Honor System

**面向生电社区服的项目管理与贡献系统**

玩家在游戏里协作完成工程项目，系统跟踪每位参与者的贡献，完结后归档沉淀，（将来）提供积分兑换。流程全自动。

<p>
  <a href="https://github.com/YuShenLiu06/PCHSystem/releases">
    <img alt="Release" src="https://shields.io/github/v/release/YuShenLiu06/PCHSystem?display_name=tag&sort=semver&color=22C55E">
  </a>
  <a href="https://github.com/YuShenLiu06/PCHSystem">
    <img alt="Stars" src="https://shields.io/github/stars/YuShenLiu06/PCHSystem?color=22C55E">
  </a>
  <img alt="Clones" src="https://shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/main/.github/clone-stats.json&query=$.clones&label=clones&color=22C55E">
  <a href="LICENSE">
    <img alt="License" src="https://shields.io/github/license/YuShenLiu06/PCHSystem?color=22C55E">
  </a>
  <a href="https://github.com/YuShenLiu06/PCHSystem/commits">
    <img alt="Last Commit" src="https://shields.io/github/last-commit/YuShenLiu06/PCHSystem?color=22C55E">
  </a>
  <a href="https://yushenliu06.github.io/PCHSystem-wiki/">
    <img alt="Wiki" src="https://shields.io/badge/Wiki-文档-22C55E?logo=github&logoColor=white">
  </a>
</p>

<img alt="PCHSystem Web 端预览" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/Assets/hero-site.png" width="800">

</div>

> **仍在开发中**：归档自动结算、称号等核心玩法尚未落地。见[开发状态](#开发状态)。
> 
> **Wiki 文档**：完整使用文档与玩法指引见 [**PCHSystem Wiki**](https://yushenliu06.github.io/PCHSystem-wiki/)（搭建中，内容持续补充）。

---

## 功能特性

### 核心特性

- **后端分离** — 游戏内端与后端完全分离（不强制绑定 MCDR），后端可独立部署，游戏内端仅作为客户端
- **独立前端** — 提供独立 Web 前端，玩家不进游戏也能查看项目进度、编辑材料清单、上传投影 / 蓝图；游戏端或 MCDR 重启时，Web 端仍可独立访问
- **兼容性强** — 基于 MCDR 的强大兼容性，可在几乎所有 Minecraft 版本上运行

### 已实现功能

#### 登录鉴权

- `!!PCH login` 一键生成登录链接，点击直接进入 Web 页面

#### 项目协作（在线表格）

完整的项目材料清单协作——认领材料、多人累计上交、交付确认、打回返工、解除锁定，Web 端与游戏端**对等操作**。

- **一键提交**：支持扫描背包（含潜影盒内物品）上报进度，提供双维度抽象层方便二次开发
- **投影 / 蓝图一键建表**：上传 `.litematic` 投影或 Create `.nbt` 蓝图，自动解析方块、翻译中文名、生成材料清单（支持原版与模组物品；多份投影合并为同一项目；单投影倍数设置）（仅 Web 端）
- **子物品**：通过倍数（支持小数）直接生成子一级合成物品清单
- **快捷命令**：游戏内大量命令支持可点击交互，减少手打
- **智能换算**：自动将数量换算为可读性更高的 个 / 组 / 盒
- **手持读取**：游戏内读取手持物品 `registry-id`，直接更改 / 新增所需物品，免去手打 ID
- **Web 端行编辑**：在线编辑材料行（名称 / 数量 / `registry-id`），与游戏端对等

#### 项目协作（施工阶段）

完成施工阶段对不同参与者的贡献统计。

- **开放统计层**：提供面向客户端 / 服务端两种鉴权方式的 API，复用 `JWT` 与 `service-token`
- **默认服务端统计层**：轮询玩家 `json` 文件进行 `diff`，汇报项目相关数据
- **多种图表**：提供多种图表直观、准确地显示项目进度，前端已预留接口随时切换

#### 项目归档

项目完结自动生成归档文档 + 贡献占比饼图，精确记录每位参与者的贡献。

#### 积分管理

- **积分记账**：批量入账 / 出账，流水不可篡改、每笔附记账后余额，可完整审计回溯；支持防重复提交与透支开关
- **管理员调分**：管理员 / 拥有者调增调减玩家积分，原因必填、可附备注，记入审计日志
- **管理面板**：「积分管理」页双 tab——积分流水筛选、玩家余额排名（负余额红标）、调分弹窗、账号流水下钻抽屉
- **积分通知**：记账 / 调分附带站内通知，游戏内即时收到变动提醒

#### 通知投递

认领 / 交付 / 打回 / 项目状况变化 / 上交等事件游戏内自动通知，离线期间通知上线补推。

### 效果一览

<table>
  <tr>
    <td align="center"><b>游戏内 · 材料清单</b></td>
    <td align="center"><b>Web 端 · 施工贡献图表</b></td>
  </tr>
  <tr>
    <td><img alt="游戏内材料清单" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/sheet-mc.png"></td>
    <td><img alt="施工贡献图表" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/construction.png"></td>
  </tr>
</table>

<details>
<summary><b>查看更多截图</b></summary>
<table>
  <tr>
    <td align="center"><b>Web 端 · 在线表格</b></td>
    <td align="center"><b>游戏内 · 登录链接</b></td>
  </tr>
  <tr>
    <td><img alt="Web 端在线表格" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/sheet-web.png"></td>
    <td><img alt="游戏内登录" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/login.png"></td>
  </tr>
  <tr>
    <td align="center"><b>游戏内 · 数量换算</b></td>
    <td align="center"><b>Web 端 · 子物品提交</b></td>
  </tr>
  <tr>
    <td><img alt="数量换算" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/sheet-mc-amounts.png"></td>
    <td><img alt="子物品提交" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/sheet-web-sub.gif"></td>
  </tr>
  <tr>
    <td align="center"><b>项目归档</b></td>
    <td align="center"><b>通知投递</b></td>
  </tr>
  <tr>
    <td><img alt="归档" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/archived.png"></td>
    <td><img alt="通知" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/McdrPlugin/docs/img/notify-1.png"></td>
  </tr>
</table>
</details>

### 规划中

- **积分闭环** — 项目归档自动结算（settle）+ 玩家消耗积分 + 公开榜单
- **指数增长称号** — 积分达标自动解锁，聊天前缀差异化，高阶全服公告
- **施工阶段** — 真正校验建造放置（主体已完成）+ 实时计分板进度
- **Wiki 归档同步** — 归档内容双向同步到 wiki.js + 项目权限继承
- **管理员面板** — 服务器管理面板

---

## 快速开始

### 一键脚本（推荐）

面向服主，一条命令完成 Docker 安装、国内网络镜像自适应、配置生成、起服务、数据库迁移、前端构建、`pch_system` 插件部署与 token 双写：

```bash
git clone https://github.com/YuShenLiu06/PCHSystem.git

# 或使用 Gitee 镜像
git clone https://gitee.com/yushenliu03/PCHSystem.git

cd PCHSystem
bash Scripts/install.sh    # 首次安装（交互式、幂等）
bash Scripts/update.sh     # 日常更新
```

> 完整选项（镜像策略、排错、密钥轮换、禁用前端容器等）见 [`Scripts/README.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Scripts/README.md)。

### 手动（Docker Compose）

```bash
cp .env.example .env       # 按需改密钥
docker compose up -d       # 起 postgres + backend + web（前端默认由 web 容器托管）
curl http://localhost:8000/healthz
```

> `.env` 的 `COMPOSE_PROFILES=web` 默认启用前端 web 容器（nginx 托管 `dist` + 反代 `/api`）；清空即禁用，改由自有 nginx 托管。详见 [`Docs/runbook.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Docs/runbook.md)。

> 本项目**不含 Minecraft 服务端**：MCDReforged 由你持有，插件经 HTTP 与后端通信。MCDR 插件本身的部署见 [`McdrPlugin/README.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././McdrPlugin/README.md)。

---

## 架构

三端分离：**后端（FastAPI + PostgreSQL）** 是唯一数据拥有者；**Web 端（Vue3）** 是浏览器后台；**游戏端（MCDR 插件）** 是纯客户端，不直连数据库，只经 HTTP 与后端通信。

<div align="center">

<img alt="PCHSystem 架构图" src="https://raw.githubusercontent.com/YuShenLiu06/PCHSystem/refs/heads/main/Assets/architecture.png" width="720">

</div>

完整架构图、ADR、跨服务流程见 [`Docs/architecture.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Docs/architecture.md)。

---

## 开发状态

| 状态  | 模块                                                                                                          |
| :-: | ----------------------------------------------------------------------------------------------------------- |
| 已交付 | 登录鉴权（Web 账号绑多身份 + 密码登录）、项目协作（在线表格 + 协管员角色）、投影 / 蓝图解析、材料上交、**施工进度追踪/上报**、项目归档、**积分记账 / 调分 / 管理面板**、通知投递、一键部署 |
| 规划中 | 归档自动结算、指数称号、Wiki 管理                                                                                         |

详见 [`CHANGELOG.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CHANGELOG.md)。

---

## 开发与贡献

| 文档                                                                                                                                                                                                                                                                                                                                              | 说明                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [PCHSystem Wiki](https://yushenliu06.github.io/PCHSystem-wiki/)                                                                                                                                                                                                                                                                                 | 使用文档与玩法指引（搭建中）     |
| [`Docs/runbook.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Docs/runbook.md)                                                                                                                                                                                                                                         | 部署 / 排错 / 回滚       |
| [`CONTRIBUTING.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CONTRIBUTING.md)                                                                                                                                                                                                                                         | 分支 / Commit / 发布规范 |
| [`CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CLAUDE.md)                                                                                                                                                                                                                                                     | 根规范（红线、命名）         |
| [`Backend/CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Backend/CLAUDE.md) · [`Frontend/CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././Frontend/CLAUDE.md) · [`McdrPlugin/CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././McdrPlugin/CLAUDE.md) | 各端开发指引             |

提 PR 前请先读 [`CONTRIBUTING.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CONTRIBUTING.md) 与 [`CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CLAUDE.md) §3 红线；涉及 MCDR 的改动须先联网核实 API（根 [`CLAUDE.md`](https://github.com/YuShenLiu06/PCHSystem/tree/main/McdrPlugin/.././CLAUDE.md) §0 S-1）。

---

<div align="center">

<sub>Built for the HTCMC community</sub>

</div>

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [pch_system-v0.10.2.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.10.2) | 0.10.2 | 2026/08/31 14:21:48 | 81.18KB | 2 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.10.2/pch_system-v0.10.2.mcdr) |
| [pch_system-v0.10.1.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.10.1) | 0.10.1 | 2026/08/22 07:37:56 | 80.69KB | 7 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.10.1/pch_system-v0.10.1.mcdr) |
| [pch_system-v0.10.0.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.10.0) | 0.10.0 | 2026/08/19 10:28:27 | 80.69KB | 7 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.10.0/pch_system-v0.10.0.mcdr) |
| [pch_system-v0.9.3.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.9.3) | 0.9.3 | 2026/08/19 10:34:04 | 86.38KB | 2 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.9.3/pch_system-v0.9.3.mcdr) |
| [pch_system-v0.9.2.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.9.2) | 0.9.2 | 2026/08/08 01:21:38 | 83.95KB | 14 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.9.2/pch_system-v0.9.2.mcdr) |
| [pch_system-v0.9.1.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.9.1) | 0.9.1 | 2026/08/06 12:15:04 | 76.24KB | 23 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.9.1/pch_system-v0.9.1.mcdr) |
| [pch_system-v0.9.0.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.9.0) | 0.9.0 | 2026/07/28 17:13:39 | 76.19KB | 15 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.9.0/pch_system-v0.9.0.mcdr) |
| [pch_system-v0.8.2.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.8.2) | 0.8.2 | 2026/07/25 06:11:52 | 57.74KB | 17 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.8.2/pch_system-v0.8.2.mcdr) |
| [pch_system-v0.8.1.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.8.1) | 0.8.1 | 2026/07/25 03:49:02 | 57.74KB | 15 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.8.1/pch_system-v0.8.1.mcdr) |
| [pch_system-v0.8.0.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.8.0) | 0.8.0 | 2026/07/20 13:30:51 | 57.62KB | 14 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.8.0/pch_system-v0.8.0.mcdr) |
| [pch_system-v0.7.1.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.7.1) | 0.7.1 | 2026/07/14 04:24:44 | 51.67KB | 18 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.7.1/pch_system-v0.7.1.mcdr) |
| [pch_system-v0.7.0.mcdr](https://github.com/YuShenLiu06/PCHSystem/releases/tag/pch_system-v0.7.0) | 0.7.0 | 2026/07/12 13:04:16 | 51.54KB | 9 | [Download](https://github.com/YuShenLiu06/PCHSystem/releases/download/pch_system-v0.7.0/pch_system-v0.7.0.mcdr) |

