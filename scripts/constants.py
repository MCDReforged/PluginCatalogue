import os

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

TEMPLATE = os.path.join(HERE, 'templates')
PLUGINS_FOLDER = os.path.join(ROOT, 'plugins')
LABEL_FILE = os.path.join(PLUGINS_FOLDER, 'labels.json')
GENERATED_FOLDER = os.path.join(ROOT, 'generated')

PROXIES = None
if 'http_proxy' in os.environ:
	http_proxy = os.environ['http_proxy']  # e.g. 127.0.0.1:1082
	PROXIES = {
		'http': http_proxy,
		'https': http_proxy
	}
