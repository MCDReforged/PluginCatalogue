[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## color_me

### 基本信息

- 插件 ID: `color_me`
- 插件名: ColorMe
- 版本: 1.1.0
  - 元数据版本: 1.1.0
  - 发布版本: 1.1.0
- 总下载量: 114
- 作者: [Apricityx_](https://github.com/Apricityx)
- 仓库: https://github.com/Apricityx/ColorMe
- 仓库插件页: https://github.com/Apricityx/ColorMe/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 让玩家自行更改名字颜色！

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | ~=2.15.7 |

```
pip install mcdreforged~=2.15.7
```

### 介绍

[中文] | [[英文]](https://github.com/Apricityx/ColorMe/tree/master/introduction/./introduction.md)

### ColorMe

一个让玩家自行选择名字颜色的简单插件：

```
!!color <color>
```

原理是让玩家加入 16 个原版计分板队伍（每种聊天颜色一个队伍），
同时支持 Minecraft 1.12.x 和 1.13+。

启用插件后，先初始化一次队伍：

```
!!color install
```

不再需要此插件时，删除队伍：

```
!!color uninstall
```

其他命令：`!!color list` 列出所有颜色；`install` 和 `uninstall` 需要
MCDReforged 权限等级 2（helper）或更高。

注意：一名玩家同一时间只能属于一个队伍，因此本插件可能与其他使用原版队伍
实现前后缀/权限的系统冲突。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [ColorMe-v1.1.0.mcdr](https://github.com/Apricityx/ColorMe/releases/tag/v1.1.0) | 1.1.0 | 2026/09/13 04:53:35 | 15.42KB | 8 | [下载](https://github.com/Apricityx/ColorMe/releases/download/v1.1.0/ColorMe-v1.1.0.mcdr) |
| [ColorMe-v1.1.0.mcdr](https://github.com/Apricityx/ColorMe/releases/tag/1.1.0) | 1.1.0 | 2026/09/13 04:54:52 | 15.42KB | 13 | [下载](https://github.com/Apricityx/ColorMe/releases/download/1.1.0/ColorMe-v1.1.0.mcdr) |
| [ColorMe-v1.0.2.mcdr](https://github.com/Apricityx/ColorMe/releases/tag/1.0.2) | 1.0.2 | 2025/10/28 15:14:00 | 17.83KB | 93 | [下载](https://github.com/Apricityx/ColorMe/releases/download/1.0.2/ColorMe-v1.0.2.mcdr) |

