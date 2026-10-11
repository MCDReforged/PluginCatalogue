[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## secure_shell

### 基本信息

- 插件 ID: `secure_shell`
- 插件名: Secure Shell
- 版本: 2.1.0
  - 元数据版本: 2.1.0
  - 发布版本: 2.1.0
- 总下载量: 9
- 作者: ZhangZuoqian
- 仓库: https://github.com/ZhangZuoqian/secure_shell
- 仓库插件页: https://github.com/ZhangZuoqian/secure_shell/tree/main
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 跨平台Shell执行器（执行引擎为可选扩展包），带安全白名单与日志审计

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.0.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍

# Secure Shell

[English](https://github.com/ZhangZuoqian/secure_shell/tree/main/README.md) | **简体中文**

一个给面板服用的 MCDReforged 插件，帮你跑 shell 命令——从 MCDR 控制台跑，游戏聊天框里也能跑（但要自己开）。带权限等级门槛、黑白名单和审计日志。

面板服只给你一个网页控制台，敲进去的东西直接进游戏服务端。没有 root，没有 SSH，也没有系统终端。想看磁盘占了多少、哪个进程在吃内存？没地方敲。这插件就是干这个的——我自己就跑在简幻欢上，日常这些检查全靠它。

## 前置

```
mcdreforged>=2.0.0
```

插件代码自身需要 Python 3.7+（`subprocess` 用到了 `text=True` 参数，更老的 Python 不认识它）。实际下限跟着 MCDR 走——比如 MCDR 2.15+ 就要求 Python 3.9。开发实测环境：MCDR 2.15.7 / Python 3.12。

## 功能

- 控制台优先：默认只有 MCDR 控制台能执行命令，游戏内执行是可选项
- 游戏内双重门槛：`allow_player_execution` 开关要打开，玩家还得有 MCDR 4 级权限（`required_permission` 可调）
- 不经过 shell：输入用 `shlex` 拆分后直接启动程序，管道、重定向、通配符、`$()` 一概不通
- 危险命令黑名单常开，另有可选的白名单-only 模式
- 每次执行和拒绝都写进 `logs/secure_shell.log`
- 跨平台（Linux / macOS / Windows），单条命令超时强杀
- 引擎可插拔：shell 执行引擎本身做成签名的扩展包——默认不存在，装不装全凭管理员一句话

## 用法

默认只有 MCDR 控制台能执行，游戏内是禁用的（v2.0.2 起）。想让游戏里也能用，把配置里的 `allow_player_execution` 改成 `true`——就算开了，玩家还得有 MCDR 权限等级 `required_permission`（默认 4），两道门都过才放行。开关关着的时候，玩家尝试会被拒绝并记进日志。

```
!!shell "<命令>"                    执行命令
!!sh "<命令>"                       !!sh 是 !!shell 的别名
!!shell --timeout=10 "<命令>"       单条命令临时改超时
!!shellstatus                       查看当前各开关状态
```

插件能跑在 Linux、macOS 和 Windows 上，但能执行什么命令取决于宿主系统：

**Linux**

```
!!shell "df -h"                    磁盘占用
!!shell "free -h"                  内存
!!shell "ps aux"                   进程
!!shell "cd /home/container"       然后：!!shell "ls"
```

**macOS** —— 大部分跟 Linux 一样，但没有 `free`，看内存用 `vm_stat` 或 `top -l 1`：

```
!!shell "df -h"
!!shell "vm_stat"
!!shell "ping -c 4 8.8.8.8"
```

**Windows** —— 插件不经 shell、直接启动程序，所以 `dir`、`copy`、`del` 这类 cmd 内置命令跑不了，得用真正的可执行文件。另外 Windows 的 `ping` 用 `-n` 不是 `-c`：

```
!!shell "tasklist"                 进程
!!shell "ipconfig /all"            网络配置
!!shell "systeminfo"
!!shell "netstat -an"
!!shell "cd C:\MCDR"               然后：!!shell "tree /F"
```

`cd` 和 `pwd` 在三个系统上都由插件自己处理，工作目录会跟着走，重载插件后恢复原样。

返回内容依次是：一行执行信息（当前 `cwd` 和超时）、流式输出、一行退出码。`[OK] 退出码 0 (exit 0)` 是成功，`[FAIL] 退出码 N (exit N)` 是失败——回复语都是中英双语，中文在前。stderr 会并进输出。被拦下的命令不会执行，提示 `[FAIL] 安全拦截 (blocked): <原因>`；超时的会被强杀，提示 `[FAIL] 命令超时 (timeout >Ns)，已强制终止 (killed)`；引号没闭合这类格式错误直接不执行。以上这些——包括拒绝记录——都会写进 `logs/secure_shell.log`。

`!!shellstatus` 会显示白名单是否强制、游戏内执行开没开，还会提醒你黑名单始终兜底。

## 配置

配置文件在 `config/secure_shell/config.json`，首次加载自动生成：

| 键                        | 默认值           | 说明                                                           |
| ------------------------ | ------------- | ------------------------------------------------------------ |
| `required_permission`    | `4`           | 执行命令需要的 MCDR 权限等级                                            |
| `allow_player_execution` | `false`       | `false`：仅 MCDR 控制台。`true`：玩家也能执行，但仍需满足 `required_permission` |
| `default_timeout`        | `60`          | 超时时间（秒）                                                      |
| `enforce_allowlist`      | `false`       | `true` 时只放行白名单里的程序                                           |
| `allowlist`              | （一组常用的安全命令）   | 条目按程序名（命令的第一个词）匹配                                            |
| `blacklist`              | （危险命令）        | 优先于白名单，始终生效                                                  |
| `ext_download_url`       | （本仓库 release） | `install_ext` 拉取引擎包的地址                                       |
| `ext_expected_sha256`    | （空 = 源码内置锚）   | 自建扩展包时必填你自己的哈希                                               |
| `ext_password_pbkdf2`    | （空 = 关闭）      | 二次密码哈希，用 `hash_password` 生成                                  |

匹配对象是拆分后的真实程序名（首词全等）：白名单里的 `git status` 放行的是 `git`，黑名单里的 `rm -rf /` 拦的是 `rm`。黑名单永远兜底，白名单只在 `enforce_allowlist` 为 `true` 时生效。自带的 `allowlist` 是按 Linux 写的——Windows 和 macOS 用户请按自己的系统改（比如 Windows 下的 `tasklist`、`ipconfig`）。

## 扩展包

v2.1.0 起，真正的 shell 引擎是独立的可选包。主插件不自带、不下载、不加载——必须由控制台管理员主动安装。所有 `!!secure_shell` 管理命令**仅限控制台**，游戏内玩家无论什么权限一律拒绝。

```
!!secure_shell install_ext [密码]     下载、校验（SHA256）并安装扩展包
!!secure_shell check_ext              查看引擎是否已安装/已启用及版本
!!secure_shell enable_ext             启用已安装的引擎（故意设计成第二步）
!!secure_shell disable_ext            停用引擎但保留文件
!!secure_shell uninstall_ext [密码]   删除引擎文件
!!secure_shell hash_password <密码>   生成 PBKDF2 哈希，贴进配置用（想要二次密码时）
```

完整性校验是强制的：下载的包必须命中插件源码内置（或你在 `ext_expected_sha256` 里设置的）SHA-256，对不上就不落盘。想自建分发源、想要比哈希更强的保证，以后可以再加 RSA 签名——正常使用哈希就够了。配置里设置了密码（PBKDF2 哈希，不是明文，更不在源码里）之后，`install_ext` 和 `uninstall_ext` 都要附加密码参数。

## 安全说明

从 v2.0.1 起，命令不再经过 shell。输入先拆成程序名和参数（`shlex.split`），然后直接启动程序——管道 `|`、重定向 `>`、通配符 `*`、`;`、`&&`、`$()`、反引号都不再生效。普通命令加普通参数不受影响。真需要管道、重定向，就写个脚本放到服务器上，把脚本加进白名单。

把 `allow_player_execution` 改成 `true` 之前想清楚：能用 `!!shell` 的人就是在你主机上跑真实命令。黑名单和白名单只是模式匹配，不是沙箱。只开给自己的服主账号——MCDR 的 4 级权限来自 `permission.yml`，玩家默认一个都没有——也别为了让某个人用起来就把 `required_permission` 调低。

bash、sh、zsh、python、perl、powershell 这类解释器别放进白名单。解释器自己就能跑任意命令，放一个进去等于白名单作废。插件不会拦你——配置是你的事。白名单老老实实放 ping、df、free、uptime、systemctl 这类单纯工具。

每次执行都会记录到 `logs/secure_shell.log`，含时间、玩家、命令和结果——拒绝记录也在内。

扩展包有两点要想明白：MCDR 控制台的权限等于主机本身，能碰控制台的人就能装引擎——这才是真正的信任边界，二次密码防的是手滑不是内鬼。自己打包的话，把你的哈希填到 `ext_expected_sha256` 就行。

## 安装

从 [Releases](https://github.com/ZhangZuoqian/secure_shell/releases) 下载 `secure_shell.mcdr`，丢进 `plugins/` 目录，然后：

```
!!MCDR reload plugin
```

## 许可

MIT，见 [LICENSE](https://github.com/ZhangZuoqian/secure_shell/tree/main/LICENSE)。

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [secure_shell-v2.1.0.mcdr](https://github.com/ZhangZuoqian/secure_shell/releases/tag/v2.1.0) | 2.1.0 | 2026/10/05 05:44:09 | 17.13KB | 3 | [下载](https://github.com/ZhangZuoqian/secure_shell/releases/download/v2.1.0/secure_shell-v2.1.0.mcdr) |
| [secure_shell-v2.0.3.mcdr](https://github.com/ZhangZuoqian/secure_shell/releases/tag/v2.0.3) | 2.0.3 | 2026/10/05 23:19:34 | 13.05KB | 3 | [下载](https://github.com/ZhangZuoqian/secure_shell/releases/download/v2.0.3/secure_shell-v2.0.3.mcdr) |
| [secure_shell-v2.0.2.mcdr](https://github.com/ZhangZuoqian/secure_shell/releases/tag/v2.0.2) | 2.0.2 | 2026/10/05 23:19:32 | 11.66KB | 3 | [下载](https://github.com/ZhangZuoqian/secure_shell/releases/download/v2.0.2/secure_shell-v2.0.2.mcdr) |

