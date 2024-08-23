import os

PLUGIN_INFO_SCHEMA_VERSION = 1
META_INFO_SCHEMA_VERSION = 4
RELEASE_INFO_SCHEMA_VERSION = 8

# https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#list-releases
MAX_RELEASE_PER_PAGE = 100

REQUEST_MAX_CONCURRENCY = 32

MCDR_LINK = 'https://github.com/Fallen-Breath/MCDReforged'
CATALOGUE_LINK = 'https://github.com/MCDReforged/PluginCatalogue'

HERE = os.path.dirname(__file__)
SCRIPT_ROOT = os.path.abspath(os.path.join(HERE, '..'))
REPOS_ROOT = os.path.abspath(os.path.join(SCRIPT_ROOT, '..'))

RESOURCES_FOLDER = os.path.join(SCRIPT_ROOT, 'resources')
TEMPLATE_FOLDER = os.path.join(RESOURCES_FOLDER, 'templates')
TRANSLATION_FOLDER = os.path.join(RESOURCES_FOLDER, 'lang')
PLUGINS_FOLDER = os.path.join(REPOS_ROOT, 'plugins')
LABEL_FILE = os.path.join(RESOURCES_FOLDER, 'labels.json')
CATALOGUE_FOLDER = os.path.join(REPOS_ROOT, 'catalogue')
META_FOLDER = os.path.join(REPOS_ROOT, 'meta')


class DEBUG:
	REQUEST_GET = False
	SHOW_RATE_LIMIT = False
