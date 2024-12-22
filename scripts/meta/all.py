from typing import Dict

from meta.author import AuthorSummary
from meta.plugin import MetaInfo, PluginInfo
from meta.plugin_all import AllOfAPlugin
from utils.serializer import Serializable


class PluginMetaSummary(Serializable):
	"""
	/plugins.json
	"""
	plugin_amount: int
	plugins: Dict[str, MetaInfo]
	plugin_info: Dict[str, PluginInfo]


class Everything(Serializable):
	"""
	/everything.json
	"""
	timestamp: int
	authors: AuthorSummary
	plugins: Dict[str, AllOfAPlugin]
