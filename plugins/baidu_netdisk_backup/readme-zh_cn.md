[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## baidu_netdisk_backup

### 基本信息

- 插件 ID: `baidu_netdisk_backup`
- 插件名: 百度网盘备份
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: N/A
- 总下载量: 0
- 作者: [Moran0710](https://github.com/moran0710)
- 仓库: https://github.com/moran0710/MinecraftServer_BaiduNetdisk_backup
- 仓库插件页: https://github.com/moran0710/MinecraftServer_BaiduNetdisk_backup/tree/master/baidu_netdisk_backup
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 用于备份服务器数据并使用ByPy上传到百度网盘的MCDR插件。将会备份整个服务端（包括用户数据和插件数据），和MCDR插件及配置

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# 百度网盘备份插件

## 介绍
这是一个基于[ByPy](https://github.com/houtianze/bypy)来~~白嫖~~用来利用百度网盘的免费空间来备份整个服务端的插件

支持自动保存和指令`!!baidu_backup`保存，自动上传到百度网盘，不占用本地空间

支持多槽位，超出槽位个数的百度网盘备份将被删除

## 安装

1. 前往release下载.mcdr文件
2. 丢进你的mcdr plugin文件夹
3. 你需要安装以下依赖，直接执行以下命令
```
pip install bypy
pip install APScheduler
```
4. 第一次运行时，Bypy会要求你登录百度网盘，请根据bypy在命令行的提示登录（点击提供的链接，并复制授权码到命令行）
5. done

## 配置&使用
插件会在./config下释放配置文件文件夹`./config/baidu_netdisk_backup/baidu_netdisk_backup_config.yaml`，
按照说明填写即可

使用`!!baidu_backup`手动备份

备份时会重启服务器

## 反馈
请在issue提供

## 鸣谢
1. [ByPy](https://github.com/houtianze/bypy)
2. [MCDReforged](https://github.com/MCDReforged/MCDReforged)

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |

