[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## delayexe

### 基本信息

- 插件 ID: `delayexe`
- 版本: *数据拉取失败*
- 总下载量: N/A
- 作者: [zyxkad](https://github.com/zyxkad)
- 仓库: https://github.com/kmcsr/delayexe_mcdr
- 仓库插件页: https://github.com/kmcsr/delayexe_mcdr/tree/master
- 标签: [`工具`](/labels/tool/readme-zh_cn.md), [`API`](/labels/api/readme-zh_cn.md)
- 描述: *数据拉取失败*

### 插件依赖

*数据拉取失败*

### 包依赖

*数据拉取失败*

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

*数据拉取失败*

