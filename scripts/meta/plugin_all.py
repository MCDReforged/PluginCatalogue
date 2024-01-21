from meta.plugin import MetaInfo, PluginInfo
from meta.release import ReleaseSummary
from meta.repos import RepositoryInfo
from utils.serializer import Serializable


class AllOfAPlugin(Serializable):
	"""
	/<plugin_id>/all.json
	"""
	timestamp: int
	meta: MetaInfo
	plugin: PluginInfo
	release: ReleaseSummary
	repository: RepositoryInfo
