**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## ciki_ecg

### Basic Information

- Plugin ID: `ciki_ecg`
- Plugin Name: Ciki ECG
- Version: 2.1.0
  - Metadata version: 2.1.0
  - Release version: 2.1.0
- Total downloads: 72
- Authors: [Crystal0404](https://github.com/Crystal0404)
- Repository: https://github.com/Crystal0404/CikiECG
- Repository plugin page: https://github.com/Crystal0404/CikiECG/tree/master
- Labels: [`Management`](/labels/management/readme.md)
- Description: Shut down your server during a power outage!

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.15.7 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.15.7 |
| [pydantic](https://pypi.org/project/pydantic) | \>=2.13.3 |
| [cryptography](https://pypi.org/project/cryptography) | \>=48.0.0 |
| [colorlog](https://pypi.org/project/colorlog) | \>=6.10.1 |
| [ping3](https://pypi.org/project/ping3) | \>=5.1.5 |

```
pip install "mcdreforged>=2.15.7" "pydantic>=2.13.3" "cryptography>=48.0.0" "colorlog>=6.10.1" "ping3>=5.1.5"
```

### Introduction

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

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [CikiECG-v2.1.0.pyz](https://github.com/Crystal0404/CikiECG/releases/tag/2.1.0) | 2.1.0 | 2026/06/30 14:05:17 | 20.42KB | 19 | [Download](https://github.com/Crystal0404/CikiECG/releases/download/2.1.0/CikiECG-v2.1.0.pyz) |
| [CikiECG-v2.0.0-beta.2.pyz](https://github.com/Crystal0404/CikiECG/releases/tag/2.0.0-beta.2) | 2.0.0-beta.2 | 2026/05/11 10:05:31 | 19.79KB | 53 | [Download](https://github.com/Crystal0404/CikiECG/releases/download/2.0.0-beta.2/CikiECG-v2.0.0-beta.2.pyz) |

