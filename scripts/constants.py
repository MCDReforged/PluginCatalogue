import os

RELEASE_INFO_SCHEMA_VERSION = 1

THREAD_POOL_WORKER = 32

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

RESOURCES_FOLDER = os.path.join(HERE, 'resources')
TEMPLATE_FOLDER = os.path.join(RESOURCES_FOLDER, 'templates')
TRANSLATION_FOLDER = os.path.join(RESOURCES_FOLDER, 'lang')
PLUGINS_FOLDER = os.path.join(ROOT, 'plugins')
LABEL_FILE = os.path.join(PLUGINS_FOLDER, 'labels.json')
CATALOGUE_FOLDER = os.path.join(ROOT, 'catalogue')
META_FOLDER = os.path.join(ROOT, 'meta')
META_CACHE_FOLDER = os.path.join(META_FOLDER, '%cache')

PROXIES = None
if 'http_proxy' in os.environ:
	http_proxy = os.environ['http_proxy']  # e.g. 127.0.0.1:1082
	PROXIES = {
		'http': http_proxy,
		'https': http_proxy
	}
