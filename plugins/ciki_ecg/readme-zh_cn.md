[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## ciki_ecg

### 基本信息

- 插件 ID: `ciki_ecg`
- 插件名: Ciki ECG
- 版本: 2.1.0
  - 元数据版本: 2.1.0
  - 发布版本: 2.1.0
- 总下载量: 72
- 作者: [Crystal0404](https://github.com/Crystal0404)
- 仓库: https://github.com/Crystal0404/CikiECG
- 仓库插件页: https://github.com/Crystal0404/CikiECG/tree/master
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 在停电时关闭你的服务器!

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.7 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.15.7 |
| [pydantic](https://pypi.org/project/pydantic) | \>=2.13.3 |
| [cryptography](https://pypi.org/project/cryptography) | \>=48.0.0 |
| [colorlog](https://pypi.org/project/colorlog) | \>=6.10.1 |
| [ping3](https://pypi.org/project/ping3) | \>=5.1.5 |

```
pip install "mcdreforged>=2.15.7" "pydantic>=2.13.3" "cryptography>=48.0.0" "colorlog>=6.10.1" "ping3>=5.1.5"
```

### 介绍

# Ciki ECG

Ciki的服务器心电监护仪

一个针对入门级UPS的低成本停电检测插件

用于在停电时在UPS有限的供电时间内关闭服务器防止数据损坏

![image](https://raw.githubusercontent.com/Crystal0404/CikiECG/master/doc/image/power_off.png)

## 先决条件

**使用此插件需物理硬件支持, 使用前请务必确认你拥有以下设备**

### UPS(不间断电源)

在停电后依然可以为服务器短暂供电, 使此插件有时间检测供电状态和关闭你的服务器

### 路由器(或其它可以响应Ping请求的设备)

连接在公共电网上, 当插件无法Ping到此设备, 即视为停电

## MCDR事件
此插件会分发一些事件, 其它插件可以通过监听这些事件来实现一些自定义功能

### `ciki_ecg.power_off`
检测到停电时会分发此事件

### `ciki_ecg.power_on`
恢复供电时会分发此事件

### `ciki_ecg.server_stop`
由此插件关闭服务器时会分发此事件

## 更多信息

请阅读[README](https://github.com/Crystal0404/CikiECG)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [CikiECG-v2.1.0.pyz](https://github.com/Crystal0404/CikiECG/releases/tag/2.1.0) | 2.1.0 | 2026/06/30 14:05:17 | 20.42KB | 19 | [下载](https://github.com/Crystal0404/CikiECG/releases/download/2.1.0/CikiECG-v2.1.0.pyz) |
| [CikiECG-v2.0.0-beta.2.pyz](https://github.com/Crystal0404/CikiECG/releases/tag/2.0.0-beta.2) | 2.0.0-beta.2 | 2026/05/11 10:05:31 | 19.79KB | 53 | [下载](https://github.com/Crystal0404/CikiECG/releases/download/2.0.0-beta.2/CikiECG-v2.0.0-beta.2.pyz) |

