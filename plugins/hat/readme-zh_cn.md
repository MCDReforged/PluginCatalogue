[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## hat

### 基本信息

- 插件 ID: `hat`
- 插件名: Hat
- 版本: 1.1.5
  - 元数据版本: 1.1.5
  - 发布版本: 1.1.5
- 总下载量: 447
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
| [nbtlib](https://pypi.org/project/nbtlib) | \>=2.0.4 |

```
pip install "nbtlib>=2.0.4"
```

### 介绍

# Hat

[![](https://img.shields.io/github/v/release/shuangshun/Hat)](https://github.com/shuangshun/Hat/releases)
[![](https://shields.io/github/downloads/shuangshun/Hat/total)](https://github.com/MrXiaoM/shuangshun/Hat)
[![](https://img.shields.io/github/stars/shuangshun/Hat)](https://github.com/shuangshun/Hat)

[English](https://github.com/shuangshun/Hat/tree/main/README.md) | **中文**

提供一个命令 `!!hat` , 允许玩家将手上的物品戴到头上

------

## 使用

- 安装好插件及所需的全部依赖

- 在游戏内拿着任意物品输入 `!!hat` 命令

## 配置说明

- `permission` 设置能够使用 `!!hat` 命令的最低权限等级
> 仅允许输入一个整数值, 详细请看 [权限概览](https://docs.mcdreforged.com/zh-cn/latest/permission.html#overview)

- `cooldown` 设置使用 `!!hat` 命令的冷却时间(单位: 秒)

```json5
{
    "permission": 1, // 默认为 1, 即普通玩家
    "cooldown": 3 // 默认为 3 秒
}
```

------

> [!Note]
> 注意! 本插件仅适用于 [1.17+](https://zh.minecraft.wiki/w/%E5%91%BD%E4%BB%A4/item#%E5%8E%86%E5%8F%B2)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [Hat-v1.1.5.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.5) | 1.1.5 | 2025/05/02 07:10:41 | 4.05KB | 55 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.1.5/Hat-v1.1.5.mcdr) |
| [Hat-v1.1.4.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.4) | 1.1.4 | 2025/01/22 12:44:46 | 3.63KB | 199 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.1.4/Hat-v1.1.4.mcdr) |
| [Hat-v1.1.3.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.3) | 1.1.3 | 2025/01/21 14:34:27 | 3.63KB | 12 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.1.3/Hat-v1.1.3.mcdr) |
| [Hat-v1.1.2.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.2) | 1.1.2 | 2025/01/17 15:06:08 | 3.4KB | 32 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.1.2/Hat-v1.1.2.mcdr) |
| [Hat-v1.1.1.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.1) | 1.1.1 | 2025/01/11 10:48:48 | 3.4KB | 43 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.1.1/Hat-v1.1.1.mcdr) |
| [Hat-v1.1.0.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.1.0) | 1.1.0 | 2024/12/29 04:18:30 | 3.4KB | 54 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.1.0/Hat-v1.1.0.mcdr) |
| [Hat-v1.0.2.mcdr](https://github.com/shuangshun/Hat/releases/tag/v1.0.2) | 1.0.2 | 2024/12/01 04:41:12 | 3.43KB | 52 | [下载](https://github.com/shuangshun/Hat/releases/download/v1.0.2/Hat-v1.0.2.mcdr) |

