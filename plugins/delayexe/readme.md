**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## delayexe

### Basic Information

- Plugin ID: `delayexe`
- Plugin Name: Delay Exe
- Version: 1.4.1
  - Metadata version: 1.4.1
  - Release version: 1.4.1
- Total downloads: 733
- Authors: [zyxkad](https://github.com/zyxkad)
- Repository: https://github.com/kmcsr/delayexe_mcdr
- Repository plugin page: https://github.com/kmcsr/delayexe_mcdr/tree/master
- Labels: [`Tool`](/labels/tool/readme.md), [`API`](/labels/api/readme.md)
- Description: Delay execute command until all player have left

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | ^2.14.0 |
| [kpi](/plugins/kpi/readme.md) | ~1.5.0 |

### Requirements

| Python package | Requirement |
| --- | --- |

### Introduction


- English
- [中文](https://github.com/kmcsr/delayexe_mcdr/tree/master/README_zh.MD)

# Delay ExE

- A plugin for delay execute command until all player have left
- You can use it as a API

### Example for API

```python

import delayexe

def a_method():
	delayexe.add_delay_task('say There are no player online') # run minecraft command
	delayexe.add_delay_task('kill @a') # Must nothing to kill
	delayexe.add_delay_task(lambda: print('There are no player online')) # run python method

	# ...

	delayexe.clear_delay_task() # clear all delay tasks, the top of three commands will never run, if any player is online

# ...

a_method()

# ...

```


### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [DelayExe-v1.4.1.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.4.1) | 1.4.1 | 2025/02/01 20:19:10 | 4.92KB | 17 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.4.1/DelayExe-v1.4.1.mcdr) |
| [DelayExe-v1.4.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.4.0) | 1.4.0 | 2025/02/01 20:18:20 | 4.91KB | 4 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.4.0/DelayExe-v1.4.0.mcdr) |
| [DelayExe-v1.3.2.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.3.2) | 1.3.2 | 2023/08/27 01:27:19 | 4.77KB | 149 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.3.2/DelayExe-v1.3.2.mcdr) |
| [DelayExe-v1.3.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.3.0) | 1.3.0 | 2022/11/25 07:59:57 | 4.77KB | 226 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.3.0/DelayExe-v1.3.0.mcdr) |
| [DelayExe-v1.2.2.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.2.2) | 1.2.2 | 2022/10/23 06:19:23 | 4.78KB | 50 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.2.2/DelayExe-v1.2.2.mcdr) |
| [DelayExe-v1.2.1.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.2.1) | 1.2.1 | 2022/09/18 02:03:14 | 4.77KB | 49 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.2.1/DelayExe-v1.2.1.mcdr) |
| [DelayExe-v1.2.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.2.0) | 1.2.0 | 2022/09/18 00:48:47 | 4.76KB | 19 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.2.0/DelayExe-v1.2.0.mcdr) |
| [DelayExe-v1.1.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.1.0) | 1.1.0 | 2022/05/09 23:51:26 | 4.87KB | 130 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.1.0/DelayExe-v1.1.0.mcdr) |
| [DelayExe-v1.0.3.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.3) | 1.0.3 | 2022/01/07 05:38:57 | 3.59KB | 39 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.3/DelayExe-v1.0.3.mcdr) |
| [DelayExe-v1.0.2.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.2) | 1.0.2 | 2022/01/07 01:30:16 | 3.58KB | 15 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.2/DelayExe-v1.0.2.mcdr) |
| [DelayExe-v1.0.1.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.1) | 1.0.1 | 2022/01/05 23:36:47 | 3.37KB | 16 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.1/DelayExe-v1.0.1.mcdr) |
| [DelayExe-v1.0.0.mcdr](https://github.com/kmcsr/delayexe_mcdr/releases/tag/v1.0.0) | 1.0.0 | 2022/01/05 22:42:57 | 3.32KB | 19 | [Download](https://github.com/kmcsr/delayexe_mcdr/releases/download/v1.0.0/DelayExe-v1.0.0.mcdr) |

