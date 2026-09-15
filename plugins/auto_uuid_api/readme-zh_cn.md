[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## auto_uuid_api

### 基本信息

- 插件 ID: `auto_uuid_api`
- 插件名: Auto UUID API
- 版本: 0.1.0
  - 元数据版本: 0.1.0
  - 发布版本: 0.1.0
- 总下载量: 7
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/Auto-UUID-API-MCDR
- 仓库插件页: https://github.com/Mooling0602/Auto-UUID-API-MCDR/tree/main/src
- 标签: [`API`](/labels/api/readme-zh_cn.md)
- 描述: 使用本地数据或联网API自动检索玩家的档案信息。

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.14.0 |
| [python](/plugins/python/readme-zh_cn.md) | \>=3.12 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.14.0 |

```
pip install "mcdreforged>=2.14.0"
```

### 介绍

# Auto-UUID-API-MCDR
使用本地数据或联网API自动检索玩家的档案信息。

这是一个供下游使用的API插件，尽管如此，仍提供了一些内置的命令以方便普通用户用于查询信息。

> 此项目当前仍处于开发阶段，目前本地检索功能已开发完毕。

## 注意
在同一服务器使用多个身份验证服务时，请自行解决玩家重名问题。

## 改进
- 通过“白名单（whitelist.json） > 用户缓存（usercache.json） > 联网API（微软&Mojang或第三方皮肤站提供的接口）”来逐级地获取玩家的档案信息，确保结果的准确度和可靠性。
> 数据源的使用顺序可在插件配置中修改，也可以使用插件命令进行快速切换；你可以指定特定的玩家名仅使用特定的数据源，具体请查看文档。
- 自动缓存使用联网API得到的结果。
- 自动识别服务端目录位置。
> 请确保在MCDR的配置中正确填写了`working_directory`项，尽管插件仍会尝试通过服务端的PID来定位服务端目录位置（但这是最终的后备解决方案）。
- 通过[MeowtiWhitelist](https://mcdreforged.com/zh-CN/plugin/meowtiwhitelist)支持外置登录（第三方皮肤站）的服务器。
> 这是一个可选功能，若没有安装该插件，则不会启用。

## 当前缺陷
目前没有考虑纯离线情况，插件不能保证在这种条件下能够正确工作。
> 理论来说，本地查询方案应已足够精准，但如果检索不出结果，则插件将始终返回None。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [AutoUUIDAPI-v0.1.0.mcdr](https://github.com/Mooling0602/Auto-UUID-API-MCDR/releases/tag/0.1.0) | 0.1.0 | 2025/09/20 13:42:36 | 6.81KB | 7 | [下载](https://github.com/Mooling0602/Auto-UUID-API-MCDR/releases/download/0.1.0/AutoUUIDAPI-v0.1.0.mcdr) |

