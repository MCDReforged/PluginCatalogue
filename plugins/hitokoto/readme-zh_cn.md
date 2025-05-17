[English](readme.md) | **中文**

\>\>\> [回到索引](/readme-zh_cn.md)

## hitokoto

### 基本信息

- 插件 ID: `hitokoto`
- 插件名: hitokoto
- 版本: 1.0.0
  - 元数据版本: 1.0.0
  - 发布版本: 1.0.0
- 总下载量: 10
- 作者: [gubai](https://github.com/gubaiovo)
- 仓库: https://github.com/gubaiovo/MCDR_hitokoto
- 仓库插件页: https://github.com/gubaiovo/MCDR_hitokoto/tree/main/hitokoto
- 标签: [`API`](/labels/api/readme-zh_cn.md), [`工具`](/labels/tool/readme-zh_cn.md)
- 描述: 自动推送一言至你的服务器

### 插件依赖

| 插件 ID | 依赖需求 |
| --- | --- |

### 包依赖

| Python 包 | 依赖需求 |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) |  |
| [re](https://pypi.org/project/re) |  |
| [urllib](https://pypi.org/project/urllib) |  |
| [time](https://pypi.org/project/time) |  |
| [json](https://pypi.org/project/json) |  |

```
pip install mcdreforged re urllib time json
```

### 介绍

# Hitokoto
调用[Hitokoto](https://hitokoto.cn/)接口，并自动输出到服务器

### 配置文件

```json
{
    "interval": "10s",
    "parameters": {},
    "base_url": "https://v1.hitokoto.cn/",
    "from_where": true
}
```

- `interval` : 获取间隔，支持单位：s、m、h。最少10s
- `base_url` : api地址
- `parameters` : 调用参数，参考 [#接口说明](https://developer.hitokoto.cn/sentence/#%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E)
- `from_where` : 是否显示来源

示例配置文件

```json
{
    "interval": "1m",
    "parameters": {
        "c": ["a", "c"],
        "max_length": 10
    },
    "base_url": "https://v1.hitokoto.cn/",
    "from_where": true
}
```



### API 调用

插件提供 `get_hitokoto()` 函数调用api

使用示例

```python
import hitokoto

message = hitokoto.get_hitokoto()
print(message)
```


### 下载

> [!IMPORTANT]
> 使用插件之前，先阅读仓库中的 README。

| 文件 | 版本 | 上传时间 (UTC) | 大小 | 下载数 | 操作 |
| --- | --- | --- | --- | --- | --- |
| [hitokoto.mcdr](https://github.com/gubaiovo/MCDR_hitokoto/releases/tag/v1.0.0) | 1.0.0 | 2025/03/19 13:25:50 | 10.57KB | 10 | [下载](https://github.com/gubaiovo/MCDR_hitokoto/releases/download/v1.0.0/hitokoto.mcdr) |

