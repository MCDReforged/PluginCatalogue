[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## mirror_mcsmcdr

### 基本信息

- 插件 ID: `mirror_mcsmcdr`
- 插件名: MirrorMcsmcdR
- 版本: 1.7.0
  - 元数据版本: 1.7.0
  - 发布版本: 1.7.0
- 总下载量: 1242
- 作者: [tanh_Heng](https://github.com/tanhHeng)
- 仓库: https://github.com/LazyAlienServer/MirrorMcsmcdR
- 仓库插件页: https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 一个多功能的完善的控制镜像服的MCDR插件

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.6.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [xxhash](https://pypi.org/project/xxhash) | \>=3 |

```
pip install "xxhash>=3"
```

### 介绍

# MirrorMcsmcdR

[![MCDR](https://img.shields.io/badge/MCDR-%E2%89%A52.6.0-blue)](https://github.com/Fallen-Breath/MCDReforged) [![许可证](https://img.shields.io/github/license/LazyAlienServer/MirrorMcsmcdR)](https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main/./LICENSE) [![下载量](https://img.shields.io/github/downloads/LazyAlienServer/MirrorMcsmcdR/total)](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases)

中文 · [English](https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main/./README_en.md)

> 最全面的 [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 镜像服控制插件！通过多种方式控制镜像服，并使用基于哈希的增删同步。

## 特性

- **多种方式控制与启停**：
  - 支持通过[MCSManager](https://github.com/MCSManager/MCSManager)控制镜像服（`MCSM-v9.9.0` `MCSM-v10.2.1+`）
  - 支持直接通过终端启动与停止镜像服（`Linux` `Windows`），并且新终端与父MCDR进程互不干扰，便于运维管理
    - Linux 通过`screen`控制镜像服
    - Windows 通过新命令行终端控制镜像服
  - 支持通过 RCON 停止镜像服
  - 支持通过`subprocess`在MCDR进程内启动镜像服子进程，并通过标准输入输出控制镜像服
  - 支持通过`!!mirror execute <command>`向镜像服发送指令
  - 支持多种控制方式的组合使用，例如：
    - 通过 Windows 终端 启动镜像服，通过 RCON 停止镜像服
    - 通过 MCDR 启动与停止镜像服，当镜像服进程异常时，通过 Linux 强制终止镜像服
- **完善的控制功能**：完善的**多镜像服**控制操作，获取运行状态/启动/停止/强制终止/同步操作
- **基于哈希的文件同步**：基于哈希的文件同步，只同步镜像服与源服务端不同的文件，提升速度并减少磁盘IO
- **高度可自定义的配置文件**：使用YAML格式，提供高可自定义的、配置友好配置文件，多个镜像服配置时只需要书写变化的值

> [!NOTE]
> 本插件不提供服务端创建/管理功能，请在镜像服创建完成并创建对应的MCSManager实例后再使用本插件。同样，本插件不提供镜像服启动/关闭成功的提示信息，建议搭配vchat等插件使用。

## 依赖

| 依赖                | 说明                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------ |
| Python            | `>=3.9`                                                                              |
| Python 包          | `xxhash>=3`                                                                          |
| Linux terminal 代理 | `proxy_type` 为 `linux` 或 `null` 时需要 [`screen`](https://www.gnu.org/software/screen/) |

## 指令

默认指令前缀为 `!!mirror`。

| 指令                                    | 说明                        |
| ------------------------------------- | ------------------------- |
| `!!mirror` / `!!mirror help`          | 显示指令帮助                    |
| `!!mirror status`                     | 查看镜像服状态                   |
| `!!mirror start`                      | 启动镜像服                     |
| `!!mirror stop`                       | 停止镜像服                     |
| `!!mirror kill`                       | 终止镜像服                     |
| `!!mirror kill -f`                    | 强制终止镜像服（仅 Linux terminal） |
| `!!mirror sync`                       | 同步文件                      |
| `!!mirror confirm`                    | 确认待执行操作                   |
| `!!mirror reload`                     | 热重载镜像服配置                  |
| `!!mirror history`                    | 查看同步历史                    |
| `!!mirror execute <command>`          | 通过 subprocess 代理发送指令      |
| `!!mirror log`                        | 查看 subprocess 控制台日志状态     |
| `!!mirror log enable|disable|<count>` | 启用、禁用或限制控制台日志输出           |

## 配置文件

> [!TIP]
> 配置文件较长，建议先阅读[快速开始](https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main/./docs/quickstart.md)，再将下文作为配置参考。

配置文件支持热重载和自动补全。新版本增加配置项时，插件会自动为旧配置补充默认值。

```yaml
"!!mirror":
  mcsm: # MCSManager配置
  terminal: # 通过命令行启动镜像服终端的配置
  rcon: # RCON配置
  sync: # 存档同步配置
  command:
    permission: # 指令权限配置
    action: # 指令行为配置
  display: # 显示配置
```

### 镜像服条目与继承

第一个镜像服条目是基础配置。后续条目会继承它的值，只需填写需要覆盖的配置。

**示例**

通过`!!mirror2`控制镜像服2，并设置`!!mirror2`的实例id为`abc123`，将`!!mirror2`的服务端名称改为`Mirror2`
```yaml
"!!mirror":
  # ...
"!!mirror2":
  mcsm:
    uuid: abc123
  display:
    server_name: Mirror2
```
你也可以借助YAML的特性来简化配置，例如：
```yaml
"!!mirror":
  # ...
"!!mirror2":
  mcsm.uuid: abc123
  display.server_name: Mirror2
```
其中，在`!!mirror2`中未设置的参数将会自动地从第一个设置的`!!mirror`中继承，例如`!!mirror2`中并未设置`mcsm`的`url`，那么它将继承自`!!mirror`中的`mcsm`的`url`，即`"http://127.0.0.1:23333/"`

完整的示例详见[多镜像服配置文件示例](#多镜像服配置文件示例)

<br>

### mcsm: MCSManager配置
此配置部分若有疑问，请参见[MCSManager官方文档](https://docs.mcsmanager.com/#/zh-cn/apis/readme)
```yaml
mcsm:
  enable: false,
  url: "http://127.0.0.1:23333/"
  uuid: 
  remote_uuid: 
  apikey: 
```
启用MCSM后，终端与RCON都会弃用。

**enable** `bool`
- 是否启用MCSM，你需要在配置完成此部分后将此选项设置为`true`。

**url** `str`
- MCSManager面板的访问地址，即请求api的地址。

**uuid** `str`
- 服务端实例的id，即实例显示的UID。

**remote_uuid** `str`
- 远程节点的id，即实例显示的GID。

**apikey** `str`
- 调用API接口必需的密钥，通常在用户界面可以查看。

<br>

### terminal: 通过命令行启动镜像服终端的配置
```yaml
terminal:
  enable: false
  launch_path: "./Mirror"
  launch_command: "python -m mcdreforged"
  port: 
  terminal_name: "Mirror"
  regex_strict: false
  is_mcdr: true
  proxy_type: 
  console_log: false
```
当`proxy_type`为`linux`时，插件会创建一个新的screen；为`windows`时，会创建一个新的命令行终端；为`subprocess`时，会在MCDR进程内启动镜像服子进程。镜像服停止后，Linux/Windows代理创建的screen/终端会自动关闭。

> [!NOTE]
> 如果你无法通过此命令启动镜像服，尝试按以下步骤检查。其中`terminal_name` `launch_command`都为配置文件中对应key的值
> 1. 在`launch_path`下执行`launch_command`，并确认能够使镜像服正常启动
> 2. Linux用户检查是否安装了`screen`，Windows用户检查终端中输入`python`是否能正常启动Python
> 3. 若以上两项都不能解决，则在当前服务端的MCDR根目录下执行Linux或Windows代理对应的完整命令，并检查命令回显
> - Linux `cd "{launch_path}"&&screen -dmS {terminal_name}&&screen -x -S {terminal_name} -p 0 -X stuff "{launch_command}&&exit\n"`
> - Windows `cd "{launch_path}"&&start cmd.exe cmd /C python -c "import os;os.system('title {terminal_name}');os.system('{launch_command}')"`

其中，`linux`代理通过screen控制镜像服；`windows`代理的`stop`会向监听镜像服端口的进程发送`SIGINT`（即`Ctrl+C`命令），`kill`会使用`taskkill`强制终止该进程；`subprocess`代理通过子进程标准输入输出进行控制。Linux/Windows代理需要正确配置`port`，subprocess代理无需配置`port`。MCSM或RCON仍可作为替代控制方式。

> [!WARNING]
> Windows代理下的 stop 命令为实验性功能，请自行承担使用风险。请尽可能配置 RCON，避免产生不必要的运维成本。

**enable** `bool`
- 是否启用终端，当MCSM未启用且此选项为`true`时将通过终端启动镜像服。

**launch_path** `str`
- 执行启动命令的路径，通常为镜像服所在的目录。

**launch_command** `str`
- 需要执行的启动命令，若简单的启动命令无法满足需求，你可以创建一个`.bat`（或`.sh`）文件，并将启动命令写在该文件中，然后执行该文件。

**port** `int | null`
- 镜像服运行的端口。Linux/Windows代理通过此端口检查状态并控制进程；subprocess代理无需配置此项。

**terminal_name** `str`
- 新命令行终端的标题、新screen的名称，或subprocess代理日志输出使用的前缀。

**regex_strict** `bool`
- Linux/Windows代理在通过端口检查镜像服运行状态时，是否在找到端口后继续验证进程名必须为`java.exe`。一般情况下无需开启。

**is_mcdr** `bool`
- 是否通过MCDReforged启动镜像服，默认为`true`。Linux代理设置为`true`时，`stop`和`kill`会向screen输入MCDR指令；设置为`false`时，`stop`会输入Minecraft的`stop`命令，`kill`会直接执行强制终止。subprocess代理设置为`true`时，`stop`会发送`!!MCDR server stop_exit`，设置为`false`时会发送Minecraft的`stop`命令，`kill`会直接终止子进程。Windows代理的`stop`使用`SIGINT`，`kill`使用`taskkill`强制终止监听端口的进程。

> [!IMPORTANT]
> `!!mirror kill -f`和`!!mirror kill --force`仅适用于Linux terminal或Windows/Linux+MCDR。它们会杀死配置端口的所有监听进程，再关闭screen；请确认`port`配置正确，避免终止其他服务。

**proxy_type** `str | null`
- 终端代理类型，替代旧版的`system`配置项。可选值为`linux`、`windows`和`subprocess`。设置为`null`时，将根据当前操作系统自动选择`linux`或`windows`。`subprocess`会在MCDR进程内启动镜像服子进程，不需要配置`port`，并支持通过`!!mirror execute`发送指令。

> [!NOTE]
> 使用 `subprocess` 代理启动镜像服 MCDR 实例时，请在镜像服 MCDR 的配置文件中将 `advanced_console` 设置为 `false`。

**console_log** `bool`
- 是否默认将`subprocess`代理的镜像服控制台日志输出到MCDR控制台。此配置仅对`subprocess`代理生效。

<br>

### rcon: RCON配置
```yaml
rcon:
  enable: false
  address: 
  port: 
  password: 
```
**enable** `bool`
- 是否启用RCON，当MCSM未启用时，插件将通过RCON执行`stop`指令和获取镜像服状态。若同时启用了RCON和终端，插件将优先通过检查RCON状态来获取镜像服状态，若RCON未连接，则将通过检查端口来获取状态。若RCON状态与端口状态不匹配将会提示。

**address** `str`
- RCON的连接地址，不包含端口。

**port** `int`
- RCON的连接端口

**password** `str`
- RCON的连接密码

<br>

### sync: 文件同步相关的配置文件
```yaml
sync:
  world:
    - "world"
  source: "./server"
  target:
    - "./Mirror/server"
  ignore_inexistent_target_path: false
  concurrency: 4
  ignore_files:
    - "session.lock"
```
在`sync`中，`./`即指服务端所在的`MCDReforged`根目录，一个可能的目录结构如下：

```
mcdr_root (./)
 ├─ config
 ├─ logs
 ├─ plugins
 ├─ server (./server)
 |   └─ world
 └─ Mirror
     └─ server (./Mirror/server)
         └─ world
```

**world** `list`
- 需要同步的目录，当存档有多个世界文件时需要添加

**source** `str`
- 源服务端目录，通常应为MCDR的[工作目录](https://mcdreforged.readthedocs.io/zh-cn/latest/configuration.html#working-directory)，即默认情况下的`server`目录。文件由`source/world` 同步至==> `target/world`

**target** `str, list`
- 目标服务端目录, 只有一个目录时可只写字符串, 多个目录需为列表。将会为每个目标目录都同步一份源目录的文件。默认情况下镜像服的MCDR工作目录位于当前MCDR的根目录下的`Mirror`目录。

**ignore_inexistent_target_path** `bool`
- 若某个目标服务端目录不存在，当设置为`false`时，将会跳过对该目录的同步。当设置为`true`时，将会新建该目录并继续同步

**concurrency** `int`
- 同步时进行哈希计算的线程数

**ignore_files** `list`
- 不进行同步的文件，若使用`carpet`模组和`plus-carpet-addition(PCA)`模组，建议添加`"carpet.conf"` `"pca.conf"`

<br>

### command: 指令配置
```yaml
command:
  permission: # 指令权限配置
  action: # 指令行为配置
```
<br>

### permission: 指令权限配置
```yaml
permission:
  status: 0
  start: 0
  stop: 2
  kill: 3
  sync: 2
  confirm: 0
  abort: 0
  log: "console"
  execute: "console"
```
`int | str`
- 执行各指令所需的最低MCDR权限等级，或设置为`console`以限制只允许控制台执行
  <br>

### action: 指令行为配置
```yaml
action:
  status:
    require_confirm: false
  start:
    require_confirm: false
  stop:
    require_confirm: true
  kill:
    require_confirm: true
  sync:
    require_confirm: true
    ensure_server_closed: true
    auto_server_restart: false
    check_status_interval: 5
    max_attempt_times: 3
    save_world:
      # 保存世界配置
      # ...
  history:
    require_confirm: false
    max_history_count: 5
  confirm:
    timeout: 30
    cancel_anymsg: true
  abort:
    operator: everyone
```


### 通用配置

**require_confirm** `bool`
- 当此选项为`true`时, 执行该指令后需要输入`!!mirror confirm`以确认操作

### sync配置
**ensure_server_closed** `bool`
- 当此选项为`true`时, 同步时将会检查镜像服是否已停止。当此选项为`false`时, 无论镜像服是否停止, 都将直接进行同步。

**auto_server_restart** `bool`
- 此选项仅在`ensure_server_closed`为`true`时生效。当此选项为`true`时, 如果同步时镜像服未停止, 那么将在尝试自动停止镜像服后进行同步, 并在同步完成后自动重启镜像服

**check_status_interval** `int`
- 此选项仅在`auto_server_restart`生效时生效。同步时停止镜像服后, 插件需确认镜像服是否已停止。此选项为检查镜像服状态的时间间隔

**max_attempt_times** `int`
- 此选项仅在`auto_server_restart`生效时生效。检查镜像服状态的尝试次数, 超过此尝试次数后将不再尝试检查镜像服状态, 并输出`自动关闭失败`及镜像服当前状态信息。等效于超时时间 `timeout = check_status_interval * max_attempt_times`

**save_world** 保存世界配置 *一般无需更改*
```yaml
save_world:
  turn_off_auto_save: true
  commands:
    save_all_worlds: save-all flush
    auto_save_off: save-off
    auto_save_on: save-on
  saved_world_regex: '^Saved the game$'
  save_world_max_wait_sec: 60
```
**turn_off_auto_save** `bool`
- 保存世界时关闭自动保存

**commands** 相关指令
- **save_all_worlds** `str`
  + 保存世界的指令
- **auto_save_off** `str`
  + 关闭自动保存的指令
- **auto_save_on** `str`
  + 开启自动保存的指令

**saved_world_regex** `str`
- 匹配服务端"世界保存完成"日志的正则表达式

**save_world_max_wait_sec** `int`
- 保存世界的最大等待时间(秒)，超时将会跳过世界保存并进行同步

### history配置

**max_history_count** `int`
- 最多保存多少条同步历史。设置为`-1`以不限制最大数量，设置为`0`以禁用同步历史功能。默认最多保存`5`条

### confirm配置
玩家只能确认自己执行的指令

**timeout** `int`
- 需确认的指令经过多少秒后超时取消。若执行某指令后超过`timeout`秒后, 该玩家未进行任何操作, 则此指令超时，自动取消

**cancel_anymsg** `bool`
- 若玩家执行某指令后发送了除`confirm`指令外的消息, 则此指令操作自动取消。除此之外, 若玩家执行了某指令后又执行了对应镜像服的其他指令, 则先前执行的指令自动取消

### abort配置
~此功能仍在开发~

<br>

### display: 显示配置
```yaml
display:
  server_name: Mirror
```
**server_name** `str`
- "镜像服"的名称，用以在显示时区分不同的镜像服

<br>

### 多镜像服配置文件示例


```yaml
'!!mirror':
  mcsm:
    enable: true
    url: http://127.0.0.1:23333/
    uuid: 71154??????????0a1a2f4dd90695609
    remote_uuid: 6e927??????????999f0e66bc404071b
    apikey: b8f???????????????????????????ade

  terminal:
    enable: false
    launch_path: ./Mirror
    launch_command: python -m mcdreforged
    port:
    terminal_name: Mirror
    regex_strict: false
    is_mcdr: true
    proxy_type:
    console_log: false

  rcon:
    enable: false
    address:
    port:
    password:

  sync:
    world:
    - world
    source: ./server
    target:
    - ./Mirror/server
    ignore_inexistent_target_path: false
    concurrency: 4
    ignore_files:
    - session.lock

  command:
    permission:
      status: 0
      start: 0
      stop: 2
      kill: 3
      sync: 2
      history: 0
      confirm: 0
      abort: 0
      log: console
      execute: console
    action:
      status:
        require_confirm: false
      start:
        require_confirm: false
      stop:
        require_confirm: true
      kill:
        require_confirm: true
      sync:
        require_confirm: true
        ensure_server_closed: true
        auto_server_restart: true
        check_status_interval: 5
        max_attempt_times: 3
        save_world:
          turn_off_auto_save: true
          commands:
            save_all_worlds: save-all flush
            auto_save_off: save-off
            auto_save_on: save-on
          saved_world_regex: ^Saved the game$
          save_world_max_wait_sec: 60
      history:
        require_confirm: false
        max_history_count: 5
      confirm:
        timeout: 30
        cancel_anymsg: true
      abort:
        operator: everyone

  display:
    server_name: Mirror

'!!mirror2':
  mcsm:
    uuid: 83011??????????49c1133fc08a41b80
  sync:
    target:
    - ./Mirror2/server
  display:
    server_name: Mirror2

'!!mirror3':
  mcsm.enable: false
  sync.target:
    - ./Mirror3/server
  terminal:
    enable: true
    launch_path: ./Mirror3
    port: 30002
    terminal_name: Mirror3
  rcon:
    enable: true
    address: 127.0.0.1
    port: 31002
    password: p@ssw0rd
  display.server_name: Mirror3
```

## 致谢

- 哈希比对思路 / [better_backup](https://github.com/z0z0r4/better_backup)
- 配置文件权限配置思路 / [PrimeBackup](https://github.com/TISUnion/PrimeBackup)
- 保存世界思路 / [QuickBackupM](https://github.com/TISUnion/QuickBackupM)

## ToDo

- [x] 指令执行确认
- [ ] 指令执行延迟
- [ ] 禁止同步`!!mirror sync enable/disable reason`
- [x] lang语言文件
- [ ] 指令禁用
- [x] RCON支持
- [x] 无MCSM下通过命令行启动服务端
- [x] Linux/Windows通过终端执行`kill`指令
- [x] 历史同步记录显示

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [MirrorMcsmcdR-v1.7.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.7.0) | 1.7.0 | 2026/09/04 14:20:12 | 47.34KB | 3 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.7.0/MirrorMcsmcdR-v1.7.0.mcdr) |
| [MirrorMcsmcdR-v1.6.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.6.0) | 1.6.0 | 2026/08/31 15:36:33 | 40.61KB | 5 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.6.0/MirrorMcsmcdR-v1.6.0.mcdr) |
| [MirrorMcsmcdR-v1.5.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.5.0) | 1.5.0 | 2026/08/19 15:50:02 | 36.8KB | 10 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.5.0/MirrorMcsmcdR-v1.5.0.mcdr) |
| [MirrorMcsmcdR-v1.4.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.4.1) | 1.4.1 | 2025/08/23 08:52:40 | 31.28KB | 302 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.4.1/MirrorMcsmcdR-v1.4.1.mcdr) |
| [MirrorMcsmcdR-v1.4.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.4.0) | 1.4.0 | 2025/05/23 17:10:05 | 27.64KB | 129 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.4.0/MirrorMcsmcdR-v1.4.0.mcdr) |
| [MirrorMcsmcdR-v1.3.6.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.6) | 1.3.6 | 2024/08/30 11:48:35 | 25.34KB | 176 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.6/MirrorMcsmcdR-v1.3.6.mcdr) |
| [MirrorMcsmcdR-v1.3.5.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.5) | 1.3.5 | 2024/08/01 11:11:24 | 25.34KB | 82 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.5/MirrorMcsmcdR-v1.3.5.mcdr) |
| [MirrorMcsmcdR-v1.3.4.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.4) | 1.3.4 | 2024/07/25 05:47:10 | 25.29KB | 60 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.4/MirrorMcsmcdR-v1.3.4.mcdr) |
| [MirrorMcsmcdR-v1.3.3.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.3) | 1.3.3 | 2024/07/24 09:16:40 | 25.29KB | 50 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.3/MirrorMcsmcdR-v1.3.3.mcdr) |
| [MirrorMcsmcdR-v1.3.2.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.2) | 1.3.2 | 2024/07/21 11:42:39 | 25.29KB | 53 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.2/MirrorMcsmcdR-v1.3.2.mcdr) |
| [MirrorMcsmcdR-v1.3.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.1) | 1.3.1 | 2024/07/02 09:06:19 | 25.25KB | 74 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.1/MirrorMcsmcdR-v1.3.1.mcdr) |
| [MirrorMcsmcdR-v1.2.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.2.1) | 1.2.1 | 2024/04/28 06:38:18 | 21.09KB | 96 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.2.1/MirrorMcsmcdR-v1.2.1.mcdr) |
| [MirrorMcsmcdR-v1.2.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.2.0) | 1.2.0 | 2024/04/28 05:46:54 | 21.1KB | 51 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.2.0/MirrorMcsmcdR-v1.2.0.mcdr) |
| [MirrorMcsmcdR-v1.1.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.1.0) | 1.1.0 | 2024/04/07 12:08:27 | 18.97KB | 45 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.1.0/MirrorMcsmcdR-v1.1.0.mcdr) |
| [MirrorMcsmcdR-v1.0.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.0.1) | 1.0.1 | 2024/04/06 09:05:50 | 18.19KB | 54 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.0.1/MirrorMcsmcdR-v1.0.1.mcdr) |
| [MirrorMcsmcdR-v0.1.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v0.1.0) | 0.1.0 | 2024/01/06 08:32:34 | 5.5KB | 52 | [下载](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v0.1.0/MirrorMcsmcdR-v0.1.0.mcdr) |

