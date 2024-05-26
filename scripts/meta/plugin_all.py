from typing import Optional

from meta.plugin import MetaInfo, PluginInfo
from meta.release import ReleaseSummary
from meta.repos import RepositoryInfo
from utils.serializer import Serializable


class AllOfAPlugin(Serializable):
	"""
	/<plugin_id>/all.json
	"""
	meta: Optional[MetaInfo]
	plugin: PluginInfo
	release: Optional[ReleaseSummary]
	repository: Optional[RepositoryInfo]
