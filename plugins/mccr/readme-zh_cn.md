[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mccr

### 基本信息

- 插件 ID: `mccr`
- 插件名: MCDR Command Completer Reforged
- 版本: 1.1.1
  - 元数据版本: 1.1.1
  - 发布版本: 1.1.1
- 总下载量: 201
- 作者: [DancingSnow](https://github.com/DancingSnow0517), [ZhuRuoLing](https://github.com/ZhuRuoLing)
- 仓库: https://github.com/DancingSnow0517/MCDRCommandCompleterReforged
- 仓库插件页: https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: MCDR Command Completer

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>2.14.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [fastapi](https://pypi.org/project/fastapi) |  |
| [uvicorn](https://pypi.org/project/uvicorn) |  |

```
pip install fastapi uvicorn
```

### 介绍

<div align="center">

# MCDRCommandCompletion Reforged
_✨ 另一种奇妙实现的客户端MCDR命令补全 ✨_

</div>

[Readme en_US](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/tree/master//README_en.md)

> [!WARNING]  
> 需要搭配 [FabricMod-MCDRCommandCompletionReforged-Mod](https://github.com/ZhuRuoLing/MCDRCommandCompletionReforged-Mod) 使用

## 使用
- 从 [Release](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases) 处下载本插件的最新发布版并安装。
- 确保阁下加入的服务器安装了本模组以及本模组配套插件
- 在聊天栏中使用`!`触发补全。

## 配置
配置文件从 `config/mccr/config.json` 找到

* ### http_port
  #### `http_port` 代表着 http 服务器所使用的端口, 该值会自动使用命令自动配置到 `服务端mod` 上
  - 类型: `int`
  - 任意 `1-65535` 的整数
  - 默认值: `8080`

## 许可
本项目遵循 GNU LGPL V3 许可

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MCDRCommandCompleterReforged-v1.1.1.mcdr](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/tag/1.1.1) | 1.1.1 | 2025/03/20 02:29:54 | 4.67KB | 140 | [下载](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/download/1.1.1/MCDRCommandCompleterReforged-v1.1.1.mcdr) |
| [MCDRCommandCompleterReforged-v1.1.0.mcdr](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/tag/1.1.0) | 1.1.0 | 2025/03/19 11:32:09 | 4.65KB | 28 | [下载](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/download/1.1.0/MCDRCommandCompleterReforged-v1.1.0.mcdr) |
| [MCDRCommandCompleterReforged-v1.0.0.mcdr](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/tag/1.0.0) | 1.0.0 | 2025/03/18 18:13:33 | 4.63KB | 33 | [下载](https://github.com/DancingSnow0517/MCDRCommandCompleterReforged/releases/download/1.0.0/MCDRCommandCompleterReforged-v1.0.0.mcdr) |

