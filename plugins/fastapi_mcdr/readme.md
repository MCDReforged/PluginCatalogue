**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## fastapi_mcdr

### Basic Information

- Plugin ID: `fastapi_mcdr`
- Plugin Name: FastAPI MCDR
- Version: 1.0.0
  - Metadata version: 1.0.0
  - Release version: 1.0.0
- Total downloads: 55
- Authors: [Andy Zhang](https://github.com/AnzhiZhang)
- Repository: https://github.com/AnzhiZhang/MCDReforgedPlugins
- Repository plugin page: https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/fastapi_mcdr
- Labels: [`API`](/labels/api/readme.md)
- Description: Provides HTTP API.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [fastapi](https://pypi.org/project/fastapi) |  |
| [uvicorn](https://pypi.org/project/uvicorn) |  |

```
pip install fastapi uvicorn
```

### Introduction

# FastAPI

[简体中文](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/fastapi_mcdr/readme_cn.md)

> Provides HTTP API

## Quick Start

In general, there are two things you need to do in your plugin:

1. Check FastAPI's status when loading. If it's ready for registration, directly register the API.
2. Register a listener for the ACCEPT event to register the API when it becomes acceptable.

Specifically, you need to add the following code:

```python
def on_load(server, prev_module):
    # register if fastapi_mcdr is ready
    fastapi_mcdr = server.get_plugin_instance('fastapi_mcdr')
    if fastapi_mcdr is not None and fastapi_mcdr.is_ready():
        register_apis(server)

    # register event listener
    server.register_event_listener(
        "fastapi_mcdr.accept",
        register_apis
    )

def register_apis(server):
    # save plugin id and fastapi_mcdr instance
    id_ = server.get_self_metadata().id
    fastapi_mcdr = server.get_plugin_instance('fastapi_mcdr')

    # register api
    fastapi_mcdr.add_api_route(
        id_,
        path="/test",
        endpoint=test,
        response_model=Dict[str, str],
        methods=["GET"],
    )

async def test():
    return "Hello, world!"
```

Visit <http://localhost:8080/docs> to view the API documentation.

## Technical Details

### Loading

In theory, providing an HTTP API externally should be a soft dependency. That's why checking FastAPI's status and registering an ACCEPT event listener are necessary. The following diagram illustrates the process of loading FastAPI and custom plugins:

Load FastAPI first, then load custom plugins:

```mermaid
sequenceDiagram
    participant FastAPI
    participant Test

    Note right of FastAPI: FastAPI Load
    Note right of FastAPI: FastAPI Dispatch ACCEPT Event

    Note left of Test: Test Load

    Test ->> FastAPI: Loaded?
    FastAPI ->> Test: Yes!
    Test ->> FastAPI: is_ready?
    FastAPI ->> Test: Yes!
    Test ->> FastAPI: Register API

    Note left of Test: Test Register ACCEPT Event
```

Load custom plugins first, then load FastAPI:

```mermaid
sequenceDiagram
    participant FastAPI
    participant Test

    Note left of Test: Test Load

    Test ->> FastAPI: Loaded?
    FastAPI ->> Test: No!

    Note left of Test: Test Register ACCEPT Event

    Note right of FastAPI: FastAPI Load

    FastAPI ->> Test: Dispatch ACCEPT Event
    Test ->> FastAPI: Register API
```

With this design, you can achieve soft plugin dependency without worrying about the order of plugin loading. The following diagram shows the scenario of any plugin being reloaded:

```mermaid
sequenceDiagram
    participant FastAPI
    participant Test

    Note right of FastAPI: FastAPI Reload

    FastAPI ->> Test: Dispatch ACCEPT Event
    Test ->> FastAPI: Register API

    Note left of Test: Test Reload

    Test ->> FastAPI: Loaded?
    FastAPI ->> Test: Yes!
    Test ->> FastAPI: is_ready?
    FastAPI ->> Test: Yes!
    Test ->> FastAPI: Register API

    Note left of Test: Test Register ACCEPT Event
```

## Standards

### ACCEPT Event

Event name: `fastapi_mcdr.accept`

An instance of `PluginEvent` for this event is also exposed as `ACCEPT_EVENT`.

### Public Functions

#### is_ready

The plugin's status for accepting registration. If forcefully registered, it will raise a `RuntimeError`.

#### add_api_route

Accepts parameters almost identical to the `add_api_route` function of the fastapi library. However, the first parameter `plugin_id` should be the plugin id, so that the plugin id is used as a prefix when registering the path.

In other words, if the id parameter is `test` and the path parameter is `/test`, then the registered path is `/test/test`.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [FastAPIMCDR-v1.0.0.mcdr](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/tag/fastapi_mcdr-v1.0.0) | 1.0.0 | 2023/12/21 16:38:12 | 2.29KB | 55 | [Download](https://github.com/AnzhiZhang/MCDReforgedPlugins/releases/download/fastapi_mcdr-v1.0.0/FastAPIMCDR-v1.0.0.mcdr) |

