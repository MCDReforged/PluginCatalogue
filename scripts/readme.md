## How to use

1. Install requirement

```
cd ./scripts
pip install -r requirements.txt
```

2. Start

Run the scrip in the `scripts/` folder

```
python manager.py
python manager.py check
```

## Environment variable

| name | description |
| --- | --- |
| http_proxy | the address for http proxy for `requests` lib. e.g. `127.0.0.1081` |
| github_api_token | The token used in github REST API querying, used in github action |

