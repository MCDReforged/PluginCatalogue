**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## gugubot

### Basic Information

- Plugin ID: `gugubot`
- Plugin Name: GUGUbot
- Version: 1.8.7
  - Metadata version: 1.8.7
  - Release version: 1.8.7
- Total downloads: 482
- Authors: [XueK66](https://github.com/XueK66), [LoosePrince](https://github.com/LoosePrince)
- Repository: https://github.com/LoosePrince/PF-GUGUBot
- Repository plugin page: https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot
- Labels: [`Information`](/labels/information/readme.md), [`Management`](/labels/management/readme.md)
- Description: A QQ bot connect MC and QQ

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [cq_qq_api](/plugins/cq_qq_api/readme.md) | \>=1.0.0 |
| [online_player_api](/plugins/online_player_api/readme.md) | \>=1.0.0 |
| [player_ip_logger](/plugins/player_ip_logger/readme.md) | \>=1.1.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [pygame](https://pypi.org/project/pygame) |  |
| [Requests](https://pypi.org/project/Requests) |  |
| [ruamel.yaml](https://pypi.org/project/ruamel.yaml) |  |

```
pip install pygame Requests ruamel.yaml
```

### Introduction

# PF-QQchat（支持离线服务器）

> PFingan服务器MCDRQQ机器人插件

[![页面浏览量计数](https://badges.toozhao.com/badges/01H98QXADB4DYZBRC2EHSEJ4HW/green.svg)](https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot//) 
[![查看次数起始时间](https://img.shields.io/badge/查看次数统计起始于-2023%2F9%2F2-1?style=flat-square)](https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot//)
[![仓库大小](https://img.shields.io/github/repo-size/LoosePrince/PF-GUGUBot?style=flat-square&label=仓库占用)](https://github.com/LoosePrince/PF-GUGUBot/tree/main/GUGUbot//) 
[![最新版](https://img.shields.io/github/v/release/LoosePrince/PF-GUGUBot?style=flat-square&label=最新版)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest/download/GUGUbot.mcdr)
[![议题](https://img.shields.io/github/issues/LoosePrince/PF-GUGUBot?style=flat-square&label=Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues) 
[![已关闭issues](https://img.shields.io/github/issues-closed/LoosePrince/PF-GUGUBot?style=flat-square&label=已关闭%20Issues)](https://github.com/LoosePrince/PF-GUGUBot/issues?q=is%3Aissue+is%3Aclosed)
[![下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/total?style=flat-square&label=下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases)
[![最新发布下载量](https://img.shields.io/github/downloads/LoosePrince/PF-GUGUBot/latest/total?style=flat-square&label=最新版本下载量)](https://github.com/LoosePrince/PF-GUGUBot/releases/latest)

> [!NOTE]
> 由于 **GUGUbot** 和 **WebUI** 项目庞大，但迄今为止仅有开发者一名，所以我们从现在开始招募有志者加入我们！<br>
> 有意者请加 QQ1377820366 或 QQ群726741344

> [!TIP]
> 【腾讯文档】GUGUbot文档
> 
> 访问文档查看更详细的说明: https://docs.qq.com/aio/DTFlheGZKY0RvYnRi

## 快速导航

- [依赖配置](#依赖配置)
- [快速开始](#安装)
- [功能列表](#功能列表)
  - [基本功能](#基本功能)
  - [游戏内指令](#游戏内指令)
  - [群聊功能](#群聊功能)
  - [管理功能](#管理功能)
- [详细配置](#配置)
  - [前置cq\_qq\_api配置](#前置cq_qq_api配置)
  - [GUGUbot机器人配置](#gugubot机器人配置)
- [有BUG或是新的IDEA](#有bug或是新的idea)
- [TODO](#todo)
- [贡献](#贡献)

## 依赖配置

**Python 包:** 请确保已安装 [Python™](https://www.python.org/) 和 [pip](https://pypi.org/project/pip/) (pip通常在安装完python后会默认安装)。

**Python 模块:** 参考插件目录内的 `requirements.txt` 文件，使用命令 `pip install -r requirements.txt` 进行安装。

#### 前置插件
- [cq_qq_api](https://github.com/XueK66/PF-cq_qq_api/releases)
- [player_ip_logger](https://github.com/LoosePrince/PF-player_ip_logger)
- [online_player_api](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/online_player_api)
- [whitelist_api](https://github.com/Aimerny/MCDRPlugins/tree/main/src/whitelist_api)
#### 可选插件
- [PF-MCDR-WebUI](https://github.com/LoosePrince/PF-MCDR-WebUI) : 在 2.0.0 版本后将是必选前置插件

## 安装
#### MCDR快捷安装:
1. MCDR服务端输入 `!!MCDR plugin install gugubot`
2. 加载后，在`/config/cq_qq_api/config.json`中配置接收api
3. 加载后，在`/config/GUGUbot/config.yml`中配置机器人
4. 重载 cq_qq_api: `!!MCDR plugin reload cq_qq_api`

#### github下载安装:
1. 下载[前置插件](#前置插件)并放入`/plugins`
2. 前往[Release](https://github.com/LoosePrince/PF-GUGUBot/releases)下载GUGUbot.mcdr放入`/plugins`
3. 加载后，在`/config/cq_qq_api/config.json`中配置服务
4. 加载后，在`/config/GUGUbot/config.yml`中配置机器人
5. 重载 cq_qq_api: `!!MCDR plugin reload cq_qq_api`

### 必要配置
*机器人*
- **正向websocket服务端口:** 接收数据上报的端口，例如`8080`
- **消息上报格式:** 机器人基于CQ码进行解析

*CQ-qq-api*
- **host:** 接收数据上报的地址，默认 `127.0.0.1`
- **port:** 对应数据上报的端口，默认`8080`

*GUGUbot*
- **admin_id:** 管理员QQ号 默认拥有GUGUbot管理员权限(仅私聊)
- **group_id:** 聊天转发的群

> [!IMPORTANT]
> 注: 如果您在安装完成后启动提示没有配置文件请下载[config_default.yml](https://github.com/LoosePrince/PF-GUGUBot/blob/main/config_default.yml)重名名为`config.yml`放入`/config/GUGUbot/config.yml`再运行<br>
> 请注意，以上仅为必要配置项，如果您想要更加私有的体验，请完整的阅读可选配置项！

## 功能列表
> QQ部分帮助，向QQ机器人发送，可以私聊也可以群聊发送 `#帮助`

#### 基本功能

- **聊天互相转发:** 支持 MCDR 与 QQ 群组/私聊之间的消息互通。
- **白名单绑定:** 支持在QQ群内进行白名单绑定，退群自动解绑；支持离线服务器或者正版与离线的混合服务器。

#### 游戏内指令

```
!!klist','显示游戏内关键词
!!qq <msg>', '向QQ群发送消息(可以触发qq关键词)
!!add <关键词> <回复>','添加游戏内关键词回复
!!del <关键词>','删除指定游戏关键词
@ <QQ名/号> <消息>','让机器人在qq里@
```

#### 群聊功能

```
命令帮助如下:
#玩家                -> 获取在线玩家列表
#假人                -> 获取在线假人列表
#服务器              -> 同时获取在线玩家和假人列表
#绑定 <游戏ID>       -> 绑定你的游戏ID
#mc <消息>           -> 向游戏内发送消息（可以触发游戏内关键词）
#风格                -> 机器人风格帮助
#游戏关键词 列表     -> 显示现有游戏内关键词列表
#删除假人 <假人名字> -> 删除游戏内指定假人

关键词相关: 
#添加 <关键词> <回复> -> 添加游戏内关键词回复
#添加图片 <关键词>    -> 添加关键词图片
#删除 <关键词>        -> 删除关键词
#列表                 -> 获取关键词回复列表
#帮助                 -> 查看关键词相关帮助
```

<details>
<summary>机器人回复风格</summary>

机器人回复风格切换 `#风格`
```
#风格 列表   -> 风格列表
#风格 <风格> -> 切换至指定风格
```
内置模式: `正常` `傲娇`
AI生成后内置的模式: `雌小鬼` `御姐` `萝莉` `波奇酱` `病娇` `中二病`

</details>

#### 管理功能

```
管理员命令帮助如下
#绑定   -> 查看绑定相关帮助
#白名单 -> 查看白名单相关帮助
#启动指令 -> 查看启动指令相关帮助
#违禁词 -> 查看违禁词相关帮助
#关键词 -> 查看关键词相关帮助
#游戏内关键词 -> 查看游戏内关键词相关帮助
#uuid   -> 查看uuid 匹配相关帮助
#名字   -> 查看机器人名字相关帮助
#审核   -> 协助审核功能
#执行 <command> -> 执行指令
#重启 -> 重载机器人
```

> <details>
>  <summary>绑定详细说明</summary>
> 
> ```
> #绑定 列表            -> 查看绑定列表
> #绑定 查询 <QQ号>     -> 查询绑定ID
> #绑定 解绑 <QQ号>     -> 解除绑定
> #绑定 <QQ号> <游戏ID> -> 绑定新ID
> #绑定 清空 -> 清空绑定名单 + 白名单（需二次确认）
> ```
> 记录玩家mc内ID,转发到游戏内会显示绑定时的ID<br>
> 在群聊中使用 `#绑定 xxx` 来绑定<br>
> 在管理员/管理群中,可以对玩家绑定进行 增删查改 操作
> </details>

> <details>
>  <summary>白名单详细说明</summary>
> 
> ```
> #白名单 添加 <target> -> 添加白名单成员
> #白名单 列表 -> 列出白名单成员
> #白名单 关   -> 关闭白名单
> #白名单 开   -> 开启白名单
> #白名单 重载 -> 重载白名单
> #白名单 删除 <target> -> 删除白名单成员 <target> 可以是玩家名/目标选择器/UUID
> ```
> 管理员权限专属,可以通过此功能 增删查改 服务器白名单
> </details>

> <details>
>  <summary>启动指令详细说明</summary>
> 
> ```
> #启动指令 添加 <名称> <指令> -> 添加启动指令
> #启动指令 删除 <名称>        -> 删除指定启动指令
> #启动指令 列表 -> 查看现有启动指令
> #启动指令 开   -> 开启开服指令
> #启动指令 关   -> 关闭开服指令
> #启动指令 执行 -> 执行一遍开服指令
> #启动指令 重载 -> 重载开服指令
> ```
> 有些指令想服务器启动时自动执行? 添加启动指令!<br>
> 机器人会在服务器启动时,自动指令添加的指令.<br>
> 或许会有意想不到的效果捏
> </details>

> <details>
>  <summary>违禁词详细说明</summary>
> 
> ```
> #违禁词 添加 <违禁词> <违禁理由> -> 添加违禁词
> #违禁词 列表 -> 显示违禁词列表及理由
> #违禁词 删除 <违禁词> -> 删除指定违禁词
> #违禁词 开   -> 开启违禁词
> #违禁词 关   -> 关闭违禁词
> #违禁词 重载 -> 重载违禁词
> ```
> 熊孩子多?容易吵架?腐竹天天被催女装?<br>
> 聊天中出现违禁词(句中一部分也算),机器人自动撤回 + 提示<br>
> 注: 需要机器人有群管理员权限
> </details>

> <details>
>  <summary>关键词详细说明</summary>
> 
> ```
> #关键词 开   -> 开启关键词
> #关键词 关   -> 关闭关键词
> #关键词 重载 -> 重载关键词
> #关键词 列表 -> 显示关键词列表
> #添加 <关键词> <回复> -> 添加关键词
> #删除 <关键词> -> 删除指定关键词
> ```
> 想要复读机?关键信息记录(服务器种子)?<br>
> 添加关键词! 发送绑定的关键词就会回复记录的内容.<br>
> 支持图片,请使用 `#添加图片 <关键词>` 进行添加
> </details>

> <details>
>  <summary>游戏内关键词详细说明</summary>
> 
> ```
> #游戏关键词 开   -> 开启游戏内关键词
> #游戏关键词 关   -> 关闭游戏内关键词
> #游戏关键词 重载 -> 重载游戏内关键词
> #游戏关键词 列表 -> 显示游戏内关键词列表
> #游戏关键词添加 <关键词> <回复> -> 添加游戏内关键词
> #游戏关键词删除 <关键词> -> 删除指定游戏内关键词
> ```
> MC游戏内可触发的关键词<br>
> 记录坐标小帮手
> </details>

> <details>
>  <summary>风格详细说明</summary>
> 
> ```
> #风格        -> 风格帮助
> #风格 列表   -> 风格列表
> #风格 <风格> -> 切换至指定风格
> ```
> 机器人回复风格<br>
> 可以给机器人换一个性格
> 
> 支持自定义风格:
> * 在`./config/GUGUbot/` 中创建 `extra_style.json`
> * 在`./config/GUGUbot/config.yml` 中设定上一步的路径 `extra_style_path`
> * 重载gugubot `!!MCDR plugin reload gugubot`
>   开始切换叭!
> 
> <details>
>  <summary>自定义说明</summary>
> 
> **{} 的数量需要一致**
> 
> **缺少的回复会自动使用正常格式回复**
> ```  
> {
>  '正常' : {
>    'add_cancel': '图片保存已取消',
>    'add_existed': '已存在该关键词~',
>    'add_image_instruction': '请发送要添加的图片~',
>    'add_image_fail': '图片保存失败~',
>    'add_image_previous_no_done': '上一个关键词还未绑定，添加哒咩！',
>    'add_success':'添加成功！',
>    'authorization_pass': '已通过{}的申请awa',
>    'authorization_reject': '已拒绝{}的申请awa',
>    'authorization_request': '{} 申请进群, 请审核',
>    'ban_word_find':'回复包含违禁词请修改后重发，维护和谐游戏人人有责。\n违禁理由: {}',
>    'bound_add_whitelist': '已将您添加到服务器白名单',
>    'bound_exist': '您已绑定ID: {}, 请联系管理员修改',
>    'bound_success': '已成功绑定',
>    'command_success' : '指令执行成功',
>    'delete_success':'删除成功！',
>    'del_no_exist': '该关键词不存在',
>    'del_whitelist_when_quit': '{}已退群，白名单同步删除',
>    'key_word_exist': '已有指定关键词,请删除(#删除 <关键词>)后重试 awa',
>    'lack_parameter': '缺少参数，请参考 #帮助 里的说明',
>    'list': '列表如下: \n{}',
>    'no_player_ingame': f"现在没人游玩服务器",
>    'no_word': '列表空空的',
>    'player_api_fail': '未能捕获服务器日志（推荐开启rcon精准获取玩家信息）',
>    'player_list':'在线玩家共{}人，{}列表: {}',
>    'player_notice_join': '{} 加入了游戏',
>    'player_notice_leave': '{} 离开了游戏',
>    'reload_success': '重载成功',
>    'server_start':'服务器已启动',
>    'server_stop': '服务器已关闭'
>  }
> }
> ```
> </details>
> </details>

> <details>
>  <summary>uuid匹配详细说明</summary>
> 
> ```
> #uuid        -> 查看uuid相关帮助
> #uuid 列表   -> 查看uuid绑定表
> #uuid 重载 -> 重新匹配uuid
> #uuid 更新 <老ID> <新ID> -> 改白名单的名字
> ```
> 在白名单开启时,自动使用更新的mc名称进行转发
> </details>

> <details>
>  <summary>机器人名字详细说明</summary>
> 
> ```
> #名字 -> 查看名字相关帮助
> #名字 开 -> 机器人名字显示为在线人数
> #名字 关 -> 机器人名字为特殊空白名字
> ```
> 机器人群内名字自动显示服务器内人数<br>
> 仅限单服使用,多服会随机显示其中一个服务器的人数
> </details>

> <details>
>  <summary>审核名单详细说明</summary>
> 
> ```
> #审核 开 -> 开启自动审核
> #审核 关 -> 关闭自动审核
> #审核 添加 <QQ号> <别名> -> 添加审核员的别名(匹配用)
> #审核 删除 <QQ号> -> 删除审核员
> #审核 列表 -> 审核员列表
> ```
> 具体功能效果自行测试(才不是咕咕咕)
> </details>

> <details>
>  <summary>指令详细说明</summary>
> 
> ```
> #指令 <command> -> 执行指令
> ```
> 执行服务器指令<br>
> 在私聊或者管理群中使用 `#指令 <command>` 来执行<br>
> 机器人会返回执行结果
> </details>


## 配置

### 机器人的必要配置
| 配置项 | 默认值 | 说明 |
| - | - | - |
| 正向websocket服务端口 | `8080` | 接收数据上报的端口 |
| 消息上报格式 | CQ码 | 机器人基于CQ码进行解析 |

### 前置cq_qq_api配置

| 配置项 | 默认值 | 说明 |
| - | - | - |
| host | `127.0.0.1` | 接收数据上报的地址 |
| port | `8080` | 对应数据上报的端口 | 
| post_path | "" | 对应数据上报的终点名 |
| token | "" | 对应数据上报的token，用于加密信息 |

```
{
    "host": "127.0.0.1",
    "port": 8080,
    "post_path": "",
    "token": ""
}
```

以上为正向websocket

### GUGUbot机器人配置
> [!IMPORTANT]
> 非常建议看看[默认的配置文件](https://github.com/LoosePrince/PF-GUGUBot/blob/main/config_default.yml)<br>

**QQ相关设置 - 必要项**
- admin_id: 管理员QQ号 默认拥有GUGUbot管理员权限(仅私聊)
- group_id: 聊天转发的群

**QQ相关设置 - 可选项**
> <details>
> <summary>QQ相关设置</summary>
> 
> - admin_group_id: 管理群群号,群内所有人都有管理权限(仅限该群内)
> - is_main_server: 是否为主服务器,分服请设置成`false`
> - server_name: 服务器名称前缀, mc转发到QQ时显示
> 
> </details>

> <details>
> <summary>指令开关</summary>
> 
> - bound_notice: 是否进行绑定提示
> - ban_word: 违禁词撤回开关
> - execute_command: 执行指令开关
> - group_admin: 群指令（只能被咱们的管理员执行）
> - ingame_key_word: 游戏内关键词开关
> - key_word: 群聊关键词开关
> - list: 玩家列表查询开关
> - mc: #mc指令开关(非转发开关)
> - name: 机器人名字显示为服务器在线人数开关
> - qq: !!qq指令开关(非转发开关)
> - shenhe: 审核功能开关(咕咕咕)
> - start_command: 启动指令系统开关
> - whitelist: 白名单开关
> </details>

> <details>
> <summary>转发设置</summary>
> 
> - farward_other_bot: 转发官方机器人回复
> - keep_raw_image_link: 转发图片链接(适用于ChatImage)
> - mc_to_qq: MC转发到QQ开关
> - mc_to_qq_command: 服务器指令(!!/@)转发到QQ
> - player_notice: 玩家上下线通知
> - qq_to_mc: QQ转发到mc开关
> - show_group_notice: 上线显示最新群公告
> 
> </details>

> <details>
> <summary>路径</summary>
> 
> - command_prefix: 群聊指令前缀识别
> 
> **在dict_address底下**
> **都是路径,不要跟上面的搞混了**
> 
> - ban_word_dict: 违禁词储存路径
> - bound_image_path: 绑定图片储存路径
> - extra_style_path: 自定义风格储存路径
> - font_path: 字体储存路径
> - key_word_dict: 群聊关键词储存路径
> - key_word_ingame_dict: 游戏内关键词储存路径
> - shenhe_log: 审核日志储存路径
> - shenheman: 审核管理员储存路径
> - start_command_dict: 启动指令储存路径
> - uuid_qqid: uuid储存路径
> - whitelist: 服务器白名单路径
> 
> </details>

> <details>
> <summary>其他设置</summary>
> 
> - font_limit: 文字超长转图片 （默认大于150字转图片, 设置-1关闭）
> - max_bound: 一个玩家可以绑定多少个名称
> - show_message_in_console: 展示上报消息
> - style: （可选）机器人回复风格 #风格 查看风格帮助
> - style_cooldown: 风格切换冷却(单位: 秒)
> - whitelist_add_with_bound: 绑定时是否自动添加白名单
> - whitelist_remove_with_leave: 退群时是否自动移除白名单
> 
> </details>


# 有BUG或是新的IDEA
如果需要更多联动或提交想法和问题请提交 [issues](https://github.com/LoosePrince/PF-GUGUBot/issues) 或 QQ [1377820366](http://wpa.qq.com/msgrd?v=3&uin=1377820366&site=qq&menu=yes) 提交！ <br />
如需要帮助或者交流请通过 QQ群 [726741344](https://qm.qq.com/q/TqmRHmTmcU) 进行询问或者交流 <br />
视情况添加，请勿联系他人（开发者: [雪开](https://github.com/XueK66)）

# TODO
- [ ] [多服聚合](https://github.com/LoosePrince/PF-GUGUBot/issues/106)
- [ ] [联动WebUI](https://github.com/LoosePrince/PF-GUGUBot/issues/107) & [WebUI的饼](https://github.com/LoosePrince/PF-MCDR-WebUI/issues/8)

# 贡献

代码贡献: [QQChat](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/qq_chat) | [AnzhiZhang](https://github.com/AnzhiZhang)

技术支持: [XueK__](https://github.com/XueK66)

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [GUGUbot-v1.8.7.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.7) | 1.8.7 | 2024/12/09 06:32:41 | 11.66MB | 24 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.7/GUGUbot-v1.8.7.mcdr) |
| [GUGUbot-v1.8.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.6) | 1.8.6 | 2024/11/25 16:44:06 | 11.66MB | 50 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.6/GUGUbot-v1.8.6.mcdr) |
| [GUGUbot-v1.8.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.5) | 1.8.5 | 2024/11/25 16:38:10 | 11.66MB | 4 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.5/GUGUbot-v1.8.5.mcdr) |
| [GUGUbot-v1.8.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.4) | 1.8.4 | 2024/11/16 06:43:51 | 11.66MB | 34 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.4/GUGUbot-v1.8.4.mcdr) |
| [GUGUbot-v1.8.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.3) | 1.8.3 | 2024/11/01 00:25:26 | 11.66MB | 31 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.3/GUGUbot-v1.8.3.mcdr) |
| [GUGUbot-v1.8.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.2) | 1.8.2 | 2024/10/28 02:31:41 | 11.66MB | 14 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.2/GUGUbot-v1.8.2.mcdr) |
| [GUGUbot-v1.8.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.1) | 1.8.1 | 2024/10/26 21:17:31 | 11.66MB | 7 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.1/GUGUbot-v1.8.1.mcdr) |
| [GUGUbot-v1.8.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.8.0) | 1.8.0 | 2024/10/20 19:33:18 | 11.66MB | 18 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.8.0/GUGUbot-v1.8.0.mcdr) |
| [GUGUbot-v1.7.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.5) | 1.7.5 | 2024/10/05 05:12:29 | 11.66MB | 22 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.5/GUGUbot-v1.7.5.mcdr) |
| [GUGUbot-v1.7.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.4) | 1.7.4 | 2024/10/04 02:06:53 | 11.66MB | 6 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.4/GUGUbot-v1.7.4.mcdr) |
| [GUGUbot-v1.7.3.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.3) | 1.7.3 | 2024/10/03 17:42:45 | 11.66MB | 7 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.3/GUGUbot-v1.7.3.mcdr) |
| [GUGUbot-v1.7.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.2) | 1.7.2 | 2024/09/22 16:20:10 | 11.66MB | 55 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.2/GUGUbot-v1.7.2.mcdr) |
| [GUGUbot-v1.7.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.7.1) | 1.7.1 | 2024/09/22 14:12:52 | 11.66MB | 8 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.7.1/GUGUbot-v1.7.1.mcdr) |
| [GUGUbot-v1.1.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.6) | 1.1.6 | 2024/09/18 17:55:55 | 11.65MB | 19 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.6/GUGUbot-v1.1.6.mcdr) |
| [GUGUbot-v1.1.5.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.5) | 1.1.5 | 2024/09/17 04:47:21 | 11.65MB | 13 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.5/GUGUbot-v1.1.5.mcdr) |
| [GUGUbot-v1.1.4.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.4) | 1.1.4 | 2024/08/27 05:26:45 | 11.65MB | 78 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.4/GUGUbot-v1.1.4.mcdr) |
| [GUGUbot-v1.1.2.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.2) | 1.1.2 | 2024/08/18 00:31:47 | 11.65MB | 35 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.2/GUGUbot-v1.1.2.mcdr) |
| [GUGUbot-v1.1.1.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.1) | 1.1.1 | 2024/08/17 14:05:21 | 11.65MB | 5 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.1/GUGUbot-v1.1.1.mcdr) |
| [GUGUbot-v1.1.0.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.1.0) | 1.1.0 | 2024/08/14 16:02:43 | 11.65MB | 13 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.1.0/GUGUbot-v1.1.0.mcdr) |
| [GUGUbot-v1.0.6.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.6) | 1.0.6 | 2024/08/13 15:55:00 | 11.65MB | 14 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.6/GUGUbot-v1.0.6.mcdr) |
| [GUGUbot.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.5) | 1.0.5 | 2023/08/30 11:34:34 | 23.25MB | 16 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.5/GUGUbot.mcdr) |
| [GUGUbot.mcdr](https://github.com/LoosePrince/PF-GUGUBot/releases/tag/v1.0.4) | 1.0.4 | 2023/08/29 05:25:28 | 23.25MB | 9 | [Download](https://github.com/LoosePrince/PF-GUGUBot/releases/download/v1.0.4/GUGUbot.mcdr) |

