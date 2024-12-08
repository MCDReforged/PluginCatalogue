[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## hat

### 基本信息

- 插件 ID: `hat`
- 插件名: Hat
- 版本: 1.0.2
  - 元数据版本: 1.0.2
  - 发布版本: 1.0.2
- 总下载量: 18
- 作者: [shuangshun](https://github.com/shuangshun)
- 仓库: https://github.com/shuangshun/Hat
- 仓库插件页: https://github.com/shuangshun/Hat/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 将手中的物品戴到头上

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [minecraft_data_api](/plugins/minecraft_data_api/readme-zh_cn.md) | * |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

[![](https://socialify.git.ci/shuangshun/Hat/image?description=1&font=Raleway&forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Auto)](https://github.com/shuangshun/Hat)

# Hat

[![](https://img.shields.io/github/v/release/shuangshun/Hat)](https://github.com/shuangshun/Hat/releases)
[![](https://shields.io/github/downloads/shuangshun/Hat/total)](https://github.com/MrXiaoM/shuangshun/Hat)
[![](https://img.shields.io/github/stars/shuangshun/Hat)](https://github.com/shuangshun/Hat)

提供一个命令 `!!hat` , 允许玩家将手上的物品戴到头上

------

## 使用

- 安装前置 [Minecraft Data API](https://github.com/Fallen-Breath/MinecraftDataAPI)

- 安装 [Releases](https://github.com/shuangshun/Hat/releases/latest) 中的最新发行版

- 重启服务端或使用 `!!MCDR plugin reloadall` 命令重载所有插件

- 在游戏内拿着任意物品输入 `!!hat` 命令

## 配置说明

- `permission` 设置能够使用 `!!hat` 命令的最低权限等级
> 仅允许输入一个整数值, 详细请看 [权限概览](https://docs.mcdreforged.com/zh-cn/latest/permission.html#overview)

- `cooldown` 设置使用 `!!hat` 命令的冷却时间(单位: 秒)

```json5
{
    "permission": 1 // 默认为 1 , 即普通玩家
    "cooldown": 3 // 默认为 3 秒
}
```

------

> [!Note]
> 注意! 本插件现已基本兼容1.21之后的版本,
> 但还存在部分物品无法正常替换等问题(如: 不详旗帜),
> 请谨慎使用!!! (1.21 以下版本不受影响, 可放心使用)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [Hat-v1.0.2.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.0.2) | 1.0.2 | 2024/12/01 04:41:12 | 3.43KB | 18 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.0.2/Hat-v1.0.2.mcdr) |

