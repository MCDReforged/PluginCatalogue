## How to use

1. Install requirement

```
cd ./scripts
pip install -r requirements.txt
```

2. Start

Run the script in the `scripts/` folder

```
python main.py --help
python main.py check
```

## Environment variable

| name | description |
| --- | --- |
| http_proxy | the address for http proxy for `requests` lib. e.g. `127.0.0.1081` |
| github_api_token | The token used in github REST API querying, used in github action |


## Plugin disabling

Some time you need to disable some plugins during the category generating due to the plugin information is no longer valid, and here's the way to do that

Added these 2 fields in the `plugin_info.json`

```json
    "disable": true,
    "disable_reason": "(optional) why it's disable",
```

That's it, the scripts will ignore these plugins marked as disabled
