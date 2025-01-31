from pathlib import Path

PLUGIN_INFO_SCHEMA_VERSION = 1
META_INFO_SCHEMA_VERSION = 4
RELEASE_INFO_SCHEMA_VERSION = 8

# https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#list-releases
MAX_RELEASE_PER_PAGE = 100

REQUEST_MAX_CONCURRENCY = 32

MCDR_LINK = 'https://github.com/Fallen-Breath/MCDReforged'
CATALOGUE_LINK = 'https://github.com/MCDReforged/PluginCatalogue'

HERE = Path(__file__).absolute().parent
SCRIPT_ROOT = HERE.parent
REPOS_ROOT = SCRIPT_ROOT.parent

RESOURCES_FOLDER = SCRIPT_ROOT / 'resources'
TEMPLATE_FOLDER = RESOURCES_FOLDER / 'templates'
TRANSLATION_FOLDER = RESOURCES_FOLDER / 'lang'
PLUGINS_FOLDER = REPOS_ROOT / 'plugins'
LABEL_FILE = RESOURCES_FOLDER / 'labels.json'
CATALOGUE_FOLDER = REPOS_ROOT / 'catalogue'
META_FOLDER = REPOS_ROOT / 'meta'


class DEBUG:
	REQUEST_GET = False
	SHOW_RATE_LIMIT = False
