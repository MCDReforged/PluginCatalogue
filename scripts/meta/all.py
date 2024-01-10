from typing import Dict

from meta.author import AuthorSummary
from meta.plugin import MetaInfo, PluginInfo
from meta.release import ReleaseSummary
from utils.serializer import Serializable


class PluginMetaSummary(Serializable):
	"""
	/plugins.json
	"""
	plugin_amount: int
	plugins: Dict[str, MetaInfo]
	plugin_info: Dict[str, PluginInfo]


class EverythingOfAPlugin(Serializable):
	meta: MetaInfo
	plugin: PluginInfo
	release: ReleaseSummary


class Everything(Serializable):
	"""
	/everything.json
	"""
	authors: AuthorSummary
	plugins: Dict[str, EverythingOfAPlugin]
