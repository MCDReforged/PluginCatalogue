## How to use

1. Install requirement

```bash
cd ./scripts
pip3 install -r requirements.txt
```

2. Start

Run the script in the `scripts/` folder

```bash
# show help of the scripts
python3 main.py --help
# show help of the check subcommand
python3 main.py check --help
# trigger the fetch subcommand
python3 main.py fetch
```

## Environment variable

| name             | description                                                                            |
|------------------|----------------------------------------------------------------------------------------|
| http_proxy       | the address for http proxy for `requests` lib. e.g. `127.0.0.1:1081`                   |
| github_api_token | The token used in github REST API querying. It's automatically filled in github action |


## Plugin disabling

Some time you need to disable some plugins during the category generating due to the plugin information is no longer valid, and here's the way to do that

Added these 2 fields in the `plugin_info.json`

```json
    "disable": true,
    "disable_reason": "(optional) why it's disable",
```

That's it, the scripts will ignore these plugins marked as disabled
