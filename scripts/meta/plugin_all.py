from meta.plugin import MetaInfo, PluginInfo
from meta.release import ReleaseSummary
from meta.repos import RepositoryInfo
from utils.serializer import Serializable


class AllOfAPlugin(Serializable):
	"""
	/<plugin_id>/all.json
	"""
	meta: MetaInfo
	plugin: PluginInfo
	release: ReleaseSummary
	repository: RepositoryInfo
