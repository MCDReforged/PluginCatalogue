[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## delayexe

### 基本信息

- 插件 ID: `delayexe`
- 插件名: Delay Exe
- 版本: 1.4.1
  - 元数据版本: 1.4.1
  - 发布版本: 1.4.1
- 总下载量: 733
- 作者: [zyxkad](https://github.com/zyxkad)
- 仓库: https://github.com/kmcsr/delayexe_mcdr
- 仓库插件页: https://github.com/kmcsr/delayexe_mcdr/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`API`](/labels/api/readme-zh_cn.md)
- 描述: 延迟执行命令, 直到所有玩家都离开游戏

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.14.0 |
| [kpi](/plugins/kpi/readme-zh_cn.md) | ~1.5.0 |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |

### 介绍


- [English](https://github.com/kmcsr/delayexe_mcdr/tree/master/README.MD)
- 中文

# Delay ExE

- 一个延迟直到服务器**没有玩家**后执行指定命令的插件
- 可以当做*API*用
- ~~原理非常简单, 就不多介绍了~~

### API示例

```python

import delayexe

def a_method():
	delayexe.add_delay_task('say There are no player online') # 执行minecraft命令
	delayexe.add_delay_task('kill @a') # 不会有任何东西被杀死, 在任何时候
	delayexe.add_delay_task(lambda: print('There are no player online')) # 可以执行python无参函数

	# ...

	delayexe.clear_delay_task() # 清除所有任务

# ...

a_method()

# ...

```

### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [DelayExe-v1.4.1.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.4.1) | 1.4.1 | 2025/02/01 20:19:10 | 4.92KB | 17 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.4.1/DelayExe-v1.4.1.mcdr) |
| [DelayExe-v1.4.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.4.0) | 1.4.0 | 2025/02/01 20:18:20 | 4.91KB | 4 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.4.0/DelayExe-v1.4.0.mcdr) |
| [DelayExe-v1.3.2.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.3.2) | 1.3.2 | 2023/08/27 01:27:19 | 4.77KB | 149 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.3.2/DelayExe-v1.3.2.mcdr) |
| [DelayExe-v1.3.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.3.0) | 1.3.0 | 2022/11/25 07:59:57 | 4.77KB | 226 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.3.0/DelayExe-v1.3.0.mcdr) |
| [DelayExe-v1.2.2.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.2.2) | 1.2.2 | 2022/10/23 06:19:23 | 4.78KB | 50 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.2.2/DelayExe-v1.2.2.mcdr) |
| [DelayExe-v1.2.1.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.2.1) | 1.2.1 | 2022/09/18 02:03:14 | 4.77KB | 49 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.2.1/DelayExe-v1.2.1.mcdr) |
| [DelayExe-v1.2.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.2.0) | 1.2.0 | 2022/09/18 00:48:47 | 4.76KB | 19 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.2.0/DelayExe-v1.2.0.mcdr) |
| [DelayExe-v1.1.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.1.0) | 1.1.0 | 2022/05/09 23:51:26 | 4.87KB | 130 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.1.0/DelayExe-v1.1.0.mcdr) |
| [DelayExe-v1.0.3.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.3) | 1.0.3 | 2022/01/07 05:38:57 | 3.59KB | 39 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.3/DelayExe-v1.0.3.mcdr) |
| [DelayExe-v1.0.2.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.2) | 1.0.2 | 2022/01/07 01:30:16 | 3.58KB | 15 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.2/DelayExe-v1.0.2.mcdr) |
| [DelayExe-v1.0.1.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.1) | 1.0.1 | 2022/01/05 23:36:47 | 3.37KB | 16 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.1/DelayExe-v1.0.1.mcdr) |
| [DelayExe-v1.0.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.0) | 1.0.0 | 2022/01/05 22:42:57 | 3.32KB | 19 | [下载](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.0/DelayExe-v1.0.0.mcdr) |

