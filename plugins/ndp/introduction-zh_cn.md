# No Danger Player Project MCDR Client (NDP-MCDR) - 多服务器联合封禁系统

中文|[English](https://github.com/No-Danger-Player-Project/NDP-MCDR/blob/main/README.md)

## 项目概述
**No Danger Player Project MCDR Client (NDP-MCDR)** 是一款开源的跨服务器封禁插件，旨在实时同步多个服务器之间的封禁名单，防止恶意玩家进入任何已连接的服务器。通过集中管理玩家封禁数据，显著提升服务器网络的安全性和管理效率。

## 核心功能
**实时封禁同步**
 - 当玩家在一个服务器被封禁时，该封禁会立即同步到所有安装了NDP插件/模组的服务器
 - 强制绑定**IP地址**和**玩家名称**，防止通过小号或代理逃避封禁

## 工作原理
玩家加入服务器A → 插件检查本地/中央封禁名单 → 如果被封禁则拒绝访问 → 将封禁同步至服务器B/C/D...

## 快速开始
**安装**
   - 下载对应版本的MCDR文件到服务器的`plugins`文件夹
   - 重启服务器生成`ndp_config.json`配置文件

**命令**
- `!!ndp help 显示帮助信息`
- `!!ndp ban <玩家> <原因> 请求封禁玩家`
- `!!ndp pardon <玩家> 请求解封玩家`
- `!!ndp sync 同步封禁数据`
- `!!ndp status 查看系统状态`
