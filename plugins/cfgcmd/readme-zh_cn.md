[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## cfgcmd

### 基本信息

- 插件 ID: `cfgcmd`
- 插件名: configCommand
- 版本: 1.3.3
  - 元数据版本: 1.3.3
  - 发布版本: 1.3.3
- 总下载量: 270
- 作者: [wangyupu](https://github.com/wang-yupu)
- 仓库: https://github.com/wang-yupu/configCommand
- 仓库插件页: https://github.com/wang-yupu/configCommand/tree/main
- 标签: [`管理`](/labels/management/readme-zh_cn.md)
- 描述: 使用MCDR指令修改配置文件

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [pyyaml](https://pypi.org/project/pyyaml) |  |
| [toml](https://pypi.org/project/toml) |  |
| [requests](https://pypi.org/project/requests) |  |

```
pip install pyyaml toml requests
```

### 介绍


# configCommand / cfgcmd

[English](https://github.com/wang-yupu/configCommand/tree/main//README_en.md)  
[Link](https://cfgcmd.wangyupu.com)

在游戏内使用MCDR命令修改其它插件/Mod的配置！

**`1.3.1`版本支持在线编辑器!**

## 权限

目前插件对所有配置内允许的玩家允许使用(MCDR 4级权限)。此插件可以修改**运行MCDR进程的用户有权修改的所有文件**(尤其是`root`)，因此**请控制好权限或者将服务端放入容器运行**。

## 命令

- `!!cfg env <路径，以MCDR根路径开始，可用绝对/相对路径> <配置文件> [可选: 读写器类型]`: 将执行者修改的目标文件设置为对应文件
- `!!cfg quit`: 清空执行者的目标文件
- `!!cfg write`: 写入目标文件
- `!!cfg reload`: 重载目标文件(会覆盖已经进行的所有修改)
- `!!cfg info`: 查看文件信息

---  

- `!!cfg set <key> <value>`: 设置键值对，`<key>`中`.`分割的键将被当做配置树的路径解释(具体见下文示例)，此命令的`key`不支持`..`此类相对路径。类型见下方类型章节
- `!!cfg setTyped <key> <type> <value>`: 具体见下方类型章节。若值无法被解释为指定的类型，则使用`STRING`
- `!!cfg rm <key>`: 删除键对应的内容
- `!!cfg mv <sourceKey> <destKey>`: 移动，也可以当重命名使用
- `!!cfg cp <sourceKey> <destKey>`: 复制粘贴
- `!!cfg cd <key>`: 因为配置文件是树状结构，所以就提供一个类似文件系统操作的`cd`指令。在读写器为`plain`时不可用
- `!!cfg ls [可选: page] [需要前项存在: key]`: 查看当前Object内容。在读写器为`plain`时打印全文。每10行算一页
- `!!cfg lsLong [必选: page] [可选: linePerPage] [需要前项存在: key]`: 同上

---  

- `!!cfg lsDir <路径>`: 以MCDR目录为根目录查看文件列表
- `!!cfg rmFile <文件>`: 删除文件 (**无法撤销**)
- `!!cfg touchFile <文件>`: 创建**空**文件

---  

- `!!cfg editor`: 打开当前文件的在线编辑器，需要配置`enableCloud`为`true`
- `!!cfg editorApply`: 从云端同步已经修改的配置文件
- `!!cfg editorDelete`: 删除云端的会话

> 从`1.3.1`版本以下升级过来的，需要手动为配置文件添加`enableCloud`为`true`才能使用在线编辑器

---  

> 执行`!!cfg env ...`后，不会占用文件  
> 执行`!!cfg info`给出当前文件信息  
> 执行`!!cfg ls`打印指针所在Object的内容  
> 读写器根据文件后缀名判断。没有后缀名或者未知后缀名的会选择使用`plain`读写器  
> 若读写器为`plain`，`<key>`参数指定的就是行号  
> 若`<key>`包含空格且后面还有参数，用英文双引号把它括住。用`\`可以转义。具体见[QuotableText](https://docs.mcdreforged.com/zh-cn/latest/code_references/command.html#mcdreforged.command.builder.nodes.arguments.QuotableText)

### 数值类型

`setTyped`可以指定数值的类型，以下类型可用，部分类型有特殊的行为:

- `STRING`: 基本的字符串
- `INT`: 数字，包含浮点数(`float`)
- `BOOL`: 布尔值，数值大小写不敏感，但是输入必须为`T``True`(解析为真)、`F``False`(解析为假)
- `LIST`: 列表
- `OBJECT`: JS的`Object`，Python的`dict`，YAML的`mapping`
- `AUTO`: 用这个类型 = 直接用`set`子命令

#### `LIST`与`OBJECT`的特殊行为

##### `LIST`

它会将输入的值用英文逗号分开，可以使用`\`转义逗号避免错误的分割。被分割后的项目会自动进行类型推导并创建一个列表。若值是空的，则创建一个空列表

##### `OBJECT`

类似`LIST`，它会将输入的值用英文逗号分开，然后再用`:`分割键值对。可以使用`\`转义逗号避免错误的分割。被分割后的项目会自动进行类型推导(无论是键还是值)并创建一个`OBJECT`。若值是空的，则创建一个空`OBJECT`
> 实际不推荐使用`setTyped OBJECT ...`，因为它会遇到聊天框输入限制。推荐用于创建空的`OBJECT`

#### 类型推导

所有被推导的类型共享一个逻辑:

1. 判断原先值是否不存在或值为`None`(大小写敏感) ? 开始自动推导 : 原有类型可用则以原有类型继续，否则开始自动推导
2. 将数值转换为纯大写后是否为[`T`,`TRUE`,`F`,`FALSE`]中的一项 ? 是布尔值，结束 : 继续
3. 包含非数字字符(小数点、负号、双引号除外) ? 是一个字符串，结束 : 是一个数字，跳到第4步
4. 判断值被双引号括住 ? 是一个字符串式的数字，且去掉开头与结尾的双引号并进行5步的转换，结束 : 继续判断
5. 全是数字(以及可能包含的小数点和开头符号) ? 是数字(小数点取最靠后的那个)，结束 : 这是一个字符串

> `LIST`与`OBJECT`不参与此推导过程，因此自动推导不可能推出`LIST`与`OBJECT`

### 示例

原始配置文件:

```json
1  {
2      "foo": 123,
3      "bar": {
4          "barFoo": "?",
5          "barBar": {
6              "barBarFoo": 456
7          }
8      },
9      "buzz": [
10         "wangyupu","zzfx1166"
11     ]
12 }
```

命令(有顺序):

1. `!!cfg env "config/foo/" bar.json`: 打开文件
2. `!!cfg set foo 1231`: 设置第2行的值为1231
3. `!!cfg set bar.barFoo "!"`: 设置第4行的值为"!"
4. `!!cfg rm buzz.1`: 删除第10行列表的第二项 (0-based index)
5. `!!cfg cd bar.barBar`: 切换目前指针到第5行的Object
6. `!!cfg set barBarFoo 789`: 修改第6行的值为789
7. `!!cfg write`: 写入文件
8. `!!cfg quit`: 离开文件

修改后配置文件:

```json
1  {
2      "foo": 1231,
3      "bar": {
4          "barFoo": "!",
5          "barBar": {
6              "barBarFoo": 789
7          }
8      },
9      "buzz": [
10         "wangyupu"
11     ]
12 }
```

## 插件配置

```yaml
ownerPlayer: 玩家名称
cfgCmdPermission: 4
allowModifyConfig: true
allowOutBound: false
enableLog: true
onlyOwnerPlayer: false
enableCloud: true
```

`ownerPlayer`指定的玩家绕过所有安全控制措施。将其留空以对所有有权限的玩家进行权限控制  
`allowModifyConfig`指定是否允许修改**本插件(`cfgcmd`)的配置**  
`allowOutBound`指定是否允许离开`MCDR`根路径，为`false`时只能访问`MCDR`路径下的文件  
`enableLog`指定是否启用记录功能，记录保存于*MCDR根路径*`/logs/cfgcmdLogs/<YYYY>-<mm>-<dd>_<COUNT>.log`  
`onlyOwnerPlayer`指定是否只允许被指定的`ownerPlayer`才能使用此插件

> `allowModifyConfig`默认为`true`是为了管理员于无法访问后台的情况下也能对插件进行安全配置，建议安装后手动将其改为`false`  
> `enableCloud`在`1.3.1`版本前不存在，因此升级到`1.3.1+`版本时需要自行添加此配置以允许编辑器会话

## 支持的配置文件格式

- `json`
- `yaml`(`yml`)
- `toml`
- 纯文本

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [configCommand-v1.3.3.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.3.3) | 1.3.3 | 2025/04/28 15:26:02 | 19.99KB | 56 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.3.3/configCommand-v1.3.3.mcdr) |
| [configCommand-v1.3.2.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.3.2) | 1.3.2 | 2025/04/17 17:44:29 | 19.83KB | 31 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.3.2/configCommand-v1.3.2.mcdr) |
| [cfgcmd-v1.2.6.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.6) | 1.2.6 | 2025/04/05 03:04:34 | 16.35KB | 24 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.2.6/cfgcmd-v1.2.6.mcdr) |
| [cfgcmd-v1.2.5.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.5) | 1.2.5 | 2025/04/02 13:58:44 | 16.35KB | 26 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.2.5/cfgcmd-v1.2.5.mcdr) |
| [cfgcmd-v1.2.4.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.4) | 1.2.4 | 2025/04/02 11:20:09 | 16.35KB | 24 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.2.4/cfgcmd-v1.2.4.mcdr) |
| [cfgcmd-v1.2.3.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.3) | 1.2.3 | 2025/03/30 16:34:22 | 16.25KB | 27 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.2.3/cfgcmd-v1.2.3.mcdr) |
| [cfgcmd-v1.2.0.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.0) | 1.2.0 | 2025/03/28 15:50:19 | 15.34KB | 27 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.2.0/cfgcmd-v1.2.0.mcdr) |
| [configCommand-v1.1.0.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.1.0) | 1.1.0 | 2025/03/27 03:11:05 | 12.79KB | 29 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.1.0/configCommand-v1.1.0.mcdr) |
| [configCommand-v1.0.1.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.0.1) | 1.0.1 | 2025/03/26 06:38:16 | 12.58KB | 26 | [下载](https://github.com/wang-yupu/configCommand/releases/download/v1.0.1/configCommand-v1.0.1.mcdr) |

