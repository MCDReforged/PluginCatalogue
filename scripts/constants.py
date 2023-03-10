import os

PLUGIN_INFO_SCHEMA_VERSION = 1
META_INFO_SCHEMA_VERSION = 2
RELEASE_INFO_SCHEMA_VERSION = 6
MAX_RELEASE_PER_PAGE = 100

THREAD_POOL_WORKER = 32
MCDR_LINK = 'https://github.com/Fallen-Breath/MCDReforged'

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))

RESOURCES_FOLDER = os.path.join(HERE, 'resources')
TEMPLATE_FOLDER = os.path.join(RESOURCES_FOLDER, 'templates')
TRANSLATION_FOLDER = os.path.join(RESOURCES_FOLDER, 'lang')
PLUGINS_FOLDER = os.path.join(ROOT, 'plugins')
LABEL_FILE = os.path.join(RESOURCES_FOLDER, 'labels.json')
CATALOGUE_FOLDER = os.path.join(ROOT, 'catalogue')
META_FOLDER = os.path.join(ROOT, 'meta')

PROXIES = None
if 'http_proxy' in os.environ:
	http_proxy = os.environ['http_proxy']  # e.g. 127.0.0.1:1082
	PROXIES = {
		'http': http_proxy,
		'https': http_proxy
	}


class DEBUG:
	REQUEST_GET = False
	SHOW_RATE_LIMIT = False
