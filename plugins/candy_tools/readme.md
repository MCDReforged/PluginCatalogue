**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## candy_tools

### Basic Information

- Plugin ID: `candy_tools`
- Plugin Name: Candy Tools
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 8
- Authors: [FRUITS_CANDY](https://github.com/FRUITS-CANDY)
- Repository: https://github.com/Passion-Never-Dissipate/candy_tools
- Repository plugin page: https://github.com/Passion-Never-Dissipate/candy_tools/tree/main
- Labels: [`API`](/labels/api/readme.md)
- Description: The prerequisite API for the MCDR plugin of FRUITS_CANDY

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.7.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.7.0 |

```
pip install "mcdreforged>=2.7.0"
```

### Introduction

# Candy Tools

## 概述

本插件主要作为前置api用于FRUITS_CANDY开发的MCDR插件，如果你有兴趣使用可以下载源码查看完整功能。

**⚠️ 重要警告：所有 API 函数都不能在任务执行者 (TaskExecutor) 线程中调用，否则会抛出 `RuntimeError` 异常！**

**注意：部分功能需要安装 Carpet mod 才能使用**

## 功能特性

- ✅ 执行任意命令并根据正则表达式匹配结果
- ✅ 监听服务器输出中的特定消息
- ✅ 支持返回完整字符串或正则匹配对象
- ✅ 获取在线玩家列表（支持筛选假人）
- ✅ 检测服务端上是否加载了 Carpet mod
- ✅ 获取指定坐标范围内所有玩家的 NBT 属性
- ✅ 获取指定坐标范围内所有玩家列表
- ✅ 线程安全，支持插件热重载

## 安装

### 前置要求

- MCDReforged >= 2.7.0
- Minecraft 服务器（支持 Fabric 服务端）（可选）

### 安装步骤

将插件放入 MCDR 的 `plugins` 目录 或使用指令 `!!MCDR plugin install candy_tools` 来安装插件

## API 使用指南

### 基本导入

```python
import candy_tools
# 或者只导入需要的函数
from candy_tools import execute_and_wait, listen_and_wait
```

### 核心功能

#### 1. 执行命令并等待结果

##### 1.1 返回完整字符串

```python
# 获取玩家列表
result = candy_tools.execute_and_wait_str(
    command="list",
    pattern=r"There are \d+ of a max of \d+ players online:.*",
    timeout=5.0
)

if result:
    print(f"服务器返回: {result}")
else:
    print("命令执行超时")
```

##### 1.2 返回正则匹配对象（提取分组）

```python
# 获取世界时间并提取时间值
match = candy_tools.execute_and_wait_match(
    command="time query daytime",
    pattern=r"The time is (\d+)",
    timeout=3.0
)

if match:
    world_time = match.group(1)  # 获取匹配的分组
    print(f"世界时间: {world_time}")
```

##### 1.3 使用命名分组（更清晰）

```python
match = candy_tools.execute_and_wait_match(
    command="list",
    pattern=r"There are (?P<current>\d+) of a max of (?P<max>\d+) players online:(?P<players>.*)",
    timeout=5.0
)

if match:
    current_players = match.group('current')  # 当前在线玩家数
    max_players = match.group('max')         # 最大玩家数
    player_list = match.group('players')     # 玩家名字列表
    print(f"在线: {current_players}/{max_players}")
    print(f"玩家列表: {player_list}")
```

#### 2. 监听服务器消息

##### 2.1 监听特定事件

```python
# 监听玩家加入消息
message = candy_tools.listen_and_wait_str(
    pattern=r"Player (\w+) joined the game",
    timeout=30.0
)

if message:
    print(f"有玩家加入: {message}")

# 监听服务器启动完成
match = candy_tools.listen_and_wait_match(
    pattern=r"Done \((\d+\.\d+)s\)! For help, type \"help\"",
    timeout=60.0
)

if match:
    startup_time = match.group(1)
    print(f"服务器启动完成，耗时: {startup_time}秒")
```

### 3. 其他功能（部分需要 Carpet mod）

#### 3.1 检测 Carpet 模组

```python
# 检测服务器是否加载了 Carpet 模组
has_carpet = candy_tools.query_carpet()
print(f"服务器是否安装 Carpet 模组: {has_carpet}")

```

#### 3.2 获取在线玩家列表（需要 Carpet mod）

```python
# 获取所有在线玩家（包括真人和假人）
players = candy_tools.get_online_players(timeout=5.0)

if players is None:
    print("查询超时")
elif len(players) == 0:
    print("没有在线玩家")
else:
    print(f"在线玩家 ({len(players)}): {players}")

# 仅获取假人玩家
fake_players = candy_tools.get_online_fake_players(timeout=5.0)

if fake_players is None:
    print("查询超时")
elif len(fake_players) == 0:
    print("没有在线假人")
else:
    print(f"在线假人 ({len(fake_players)}): {fake_players}")
```

#### 3.3 获取区域内的玩家信息（需要 Carpet mod）

##### 3.3.1 定义区域字典

```python
# 区域定义示例
regions = {
    # 原版维度使用简写名称
    'overworld': [
        {'x1': -100, 'x2': 100, 'y1': 0, 'y2': 255, 'z1': -100, 'z2': 100},
        {'x1': 200, 'x2': 300, 'z1': 200, 'z2': 300}  # y坐标可省略，表示全高度
    ],
    'the_nether': [
        {'x1': -50, 'x2': 50, 'y1': 0, 'y2': 127, 'z1': -50, 'z2': 50}
    ],
    # 非原版维度使用完整名称
    'twilightforest:twilight_forest': [
        {'x1': -50, 'x2': 50}  # 可只定义x，z，y坐标中的一个
    ]
}
```

##### 3.3.2 获取玩家 NBT 属性

```python
# 获取区域内玩家的UUID
players = candy_tools.get_players_nbt_in_regions(
    region_dict=regions,
    nbt_attribute='uuid',  # 可以是 'uuid', 'health', 'gamemode', 'name' 等
    timeout=10.0
)

if players is None:
    print("查询超时")
elif players == {}:  # 空字典
    print("区域内没有玩家")
else:
    for player_name, uuid in players.items():
        print(f"{player_name}: {uuid}")
```

##### 3.3.3 仅获取玩家名称

```python
# 使用辅助函数获取区域内玩家名称列表
players = candy_tools.get_online_players_in_regions(
    region_dict=regions,
    timeout=10.0
)

if players is None:
    print("查询超时")
elif len(players) == 0:
    print("区域内没有玩家")
else:
    print(f"区域内玩家 ({len(players)}): {players}")
```

##### 3.3.4 获取其他 NBT 属性

```python
# 获取玩家游戏模式
players_gamemode = candy_tools.get_players_nbt_in_regions(
    region_dict=regions,
    nbt_attribute='gamemode',  # 0=生存, 1=创造, 2=冒险, 3=旁观
    timeout=10.0
)

if players_gamemode:
    for player_name, gamemode in players_gamemode.items():
        print(f"{player_name}: 游戏模式={gamemode}")

# 获取玩家生命值
players_health = candy_tools.get_players_nbt_in_regions(
    region_dict=regions,
    nbt_attribute='health',
    timeout=10.0
)

if players_health:
    for player_name, health in players_health.items():
        print(f"{player_name}: 生命值={health}")
```

## 错误处理

### 主线程调用异常

```python
try:
    # 错误：在任务执行者线程中调用
    result = candy_tools.execute_and_wait_str("list", r"players online")
except RuntimeError as e:
    print(f"错误: {e}")
    # 错误信息会是: "Cannot invoke execute_and_wait on the task executor thread"
```

### 正确的线程管理

```python
# 使用MCDR的 @new_thread 装饰器
@new_thread("query-thread")
def safe_query():
    result = candy_tools.execute_and_wait_str("list", r"players online")
    return result

# 使用 Python threading模块
import threading
def safe_query_2():
    def query():
        result = candy_tools.execute_and_wait_str("list", r"players online")
        # 处理结果...

    threading.Thread(target=query, daemon=True).start()
```

### 超时处理

所有 API 函数都有 `timeout` 参数，超时会返回 `None`：

```python
result = candy_tools.execute_and_wait_str("list", r"players online", timeout=2.0)
if result is None:
    print("命令执行超时")
```

### 正则表达式错误

如果提供的正则表达式无效，会记录错误并返回 `None`：

```python
# 错误的正则表达式
result = candy_tools.execute_and_wait_str("list", r"invalid[regex", timeout=2.0)
# result 为 None，控制台会输出错误日志
```

## 故障排除

### 常见问题

1. **API 返回 None**
   - 检查命令是否正确执行
   - 使用的API可能依赖carpet mod
   - 检查正则表达式是否匹配命令输出
   - 增加超时时间

2. **插件加载失败**
   - 检查 MCDReforged 版本是否 >= 2.7.0
   - 检查插件文件是否完整
   - 查看 MCDR 日志中的错误信息

## 贡献与反馈

- 项目地址：https://github.com/Passion-Never-Dissipate/candy_tools
- 问题反馈：在 GitHub Issues 中提交问题
- 功能建议：欢迎提交 Pull Request

---



### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [Candy_Tools-v1.0.0.mcdr](https://github.com/Passion-Never-Dissipate/candy_tools/releases/tag/1.0.0) | 1.0.0 | 2026/02/06 14:28:48 | 19.84KB | 8 | [Download](https://github.com/Passion-Never-Dissipate/candy_tools/releases/download/1.0.0/Candy_Tools-v1.0.0.mcdr) |

