[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## iploc

### 基本信息

- 插件 ID: `iploc`
- 插件名: IPLocation
- 版本: 0.1.6
  - 元数据版本: 0.1.6
  - 发布版本: 0.1.6
- 总下载量: 476
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/IPLocation-MCDR
- 仓库插件页: https://github.com/Mooling0602/IPLocation-MCDR/tree/main
- 标签: [`信息`](/labels/information/readme-zh_cn.md)
- 描述: 使用多种API，在玩家上线时显示其IP归属地。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0-alpha.1 |
| [player_ip_logger](/plugins/player_ip_logger/readme-zh_cn.md) | \>=1.2.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [requests](https://pypi.org/project/requests) |  |

```
pip install requests
```

### 介绍

# IPLocation-MCDR
本插件适合中国大陆地区用户使用。

启用了此插件后，在玩家上线时，会使用淘宝IP地址库查询并显示其IP归属地。

后续可能会更新与之相关的更多功能。

## 用法
开箱即用。

## 依赖项
- 必需依赖：Pypi包request（多数情况下你的Python环境中已经安装好了）
- 必需依赖：MCDR插件[Player IP Logger](https://mcdreforged.com/zh-CN/plugin/player_ip_logger)（用于获取玩家的IP地址）
- 可选依赖：MCDR插件[MatrixSync](https://mcdreforged.com/zh-CN/plugin/matrix_sync)（可实现IP归属地广播到Matrix房间内）

## 效果
> 控制台效果：
> ![屏幕截图_20240930_224343](https://github.com/user-attachments/assets/2e36d77c-2237-48e9-a0bf-b5695574d375)
> 游戏内效果：
> ![Screenshot_20240930-225430_Minecraft](https://github.com/user-attachments/assets/42bad1a3-623f-4da2-9a36-6e6a0f32861d)



## 注意
若无法查询出IP归属地，可以尝试增加配置（config/iploc/config.json）中的retry数，默认查询3次应该足以查询出结果了。

目前没有找到可用的获取淘宝IP地址库的访问密钥（accessKey）的方法，因此暂不提供配置，使用通用方案，如果你有可用性更好的访问密钥可以修改源代码并使用。

## 局限性
使用的接口：淘宝IP地址库、百度，精准度和可用性难以保证。

提示语句暂不能自定义，计划于后续进行支持。

## 其他
目前尚无相关的同类MCDR插件，而Spigot插件EssentialsX GeoIP配置比较繁琐且有时提供的信息不完整，因此开发此插件。

如果您有更好的方案，可以自行开发并进行完善，当有更好用的项目出现后，本项目可能会考虑存档并停止更新。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [IPLocation-v0.1.6.mcdr](https://github.com/Mooling0602/IPLocation-MCDR/releases/tag/0.1.6) | 0.1.6 | 2024/12/24 05:52:36 | 17.32KB | 234 | [下载](https://github.com/Mooling0602/IPLocation-MCDR/releases/download/0.1.6/IPLocation-v0.1.6.mcdr) |
| [IPLocation-v0.1.4.mcdr](https://github.com/Mooling0602/IPLocation-MCDR/releases/tag/0.1.4) | 0.1.4 | 2024/12/07 15:40:19 | 17.19KB | 42 | [下载](https://github.com/Mooling0602/IPLocation-MCDR/releases/download/0.1.4/IPLocation-v0.1.4.mcdr) |
| [IPLocation-v0.1.3.mcdr](https://github.com/Mooling0602/IPLocation-MCDR/releases/tag/0.1.3) | 0.1.3 | 2024/11/18 14:44:19 | 17.26KB | 50 | [下载](https://github.com/Mooling0602/IPLocation-MCDR/releases/download/0.1.3/IPLocation-v0.1.3.mcdr) |
| [IPLocation-v0.1.2.mcdr](https://github.com/Mooling0602/IPLocation-MCDR/releases/tag/0.1.2) | 0.1.2 | 2024/11/17 11:00:06 | 17.17KB | 29 | [下载](https://github.com/Mooling0602/IPLocation-MCDR/releases/download/0.1.2/IPLocation-v0.1.2.mcdr) |
| [IPLocation-v0.1.1.mcdr](https://github.com/Mooling0602/IPLocation-MCDR/releases/tag/0.1.1) | 0.1.1 | 2024/11/09 11:42:17 | 17.22KB | 29 | [下载](https://github.com/Mooling0602/IPLocation-MCDR/releases/download/0.1.1/IPLocation-v0.1.1.mcdr) |
| [IPLocation-v0.1.0.mcdr](https://github.com/Mooling0602/IPLocation-MCDR/releases/tag/0.1.0) | 0.1.0 | 2024/11/05 13:34:33 | 17.4KB | 37 | [下载](https://github.com/Mooling0602/IPLocation-MCDR/releases/download/0.1.0/IPLocation-v0.1.0.mcdr) |
| [IPLocation-v0.0.1.mcdr](https://github.com/Mooling0602/IPLocation-MCDR/releases/tag/0.0.1) | 0.0.1 | 2024/10/14 06:33:59 | 2.42KB | 55 | [下载](https://github.com/Mooling0602/IPLocation-MCDR/releases/download/0.0.1/IPLocation-v0.0.1.mcdr) |

