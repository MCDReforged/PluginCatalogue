[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## ender_pearl_tp

### 基本信息

- 插件 ID: `ender_pearl_tp`
- 版本: *数据拉取失败*
- 总下载量: N/A
- 作者: [Mooling0602](https://github.com/Mooling0602)
- 仓库: https://github.com/Mooling0602/Ender-Pearl-TP-MCDR
- 仓库插件页: https://github.com/Mooling0602/Ender-Pearl-TP-MCDR/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: *数据拉取失败*

### 插件依赖

*数据拉取失败*

### 包依赖

*数据拉取失败*

### 介绍

- [English](https://github.com/Mooling0602/Ender-Pearl-TP-MCDR/blob/main/README.md)

# Ender Pearl TP-MCDR
花费一定数量的末影珍珠传送到任何你想去的地方，可指定到坐标或者其他玩家。

本插件理论上适用于所有MCDR支持的服务端。

## Usage
使用 `!!etp <玩家名>` 以传送到其他玩家。
> 目前使用Rcon或OnlinePlayerAPI判定玩家是否在线，若两种方法都无法检测到要传送到的目标玩家是否在线，则插件会拒绝进行传送。
> 可能会在后续增加`!!etp confirm <玩家名>`使玩家可以强制运行传送，但仍然建议配置好MCDR环境。

使用 `!!etp pos <x> <y> <z>` 以传送到指定坐标。

使用 `!!etp back` 以返回传送前所在的位置，但已经花费的末影珍珠不会退还。

## Config
服主可在配置文件`config/ender_pearl_tp/config.json`中将"cost"设置为整数以决定玩家该花多少末影珍珠以传送到他们想去的地方。

默认的花费设置为4末影珍珠。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

*数据拉取失败*

