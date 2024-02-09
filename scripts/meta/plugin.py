from typing import List, Dict, Optional, TYPE_CHECKING

from mcdreforged.plugin.meta.metadata import Metadata

from common import constants
from common.translation import BundledText, Text, DEFAULT_LANGUAGE
from utils import markdown_utils
from utils.serializer import Serializable

if TYPE_CHECKING:
	from plugin.plugin import Plugin


class PluginInfo(Serializable):
	"""
	/<plugin_id>/plugin.json
	"""
	schema_version: int = constants.PLUGIN_INFO_SCHEMA_VERSION
	id: str
	authors: List[str]  # author names
	repository: str
	branch: str
	related_path: str
	labels: List[str]
	introduction: Dict[str, str]  # lang -> content


class MetaInfo(Serializable):
	"""
	/<plugin_id>/meta.json
	"""
	schema_version: int = constants.META_INFO_SCHEMA_VERSION
	id: str
	name: str
	version: str
	link: Optional[str]
	authors: List[str]
	dependencies: Dict[str, str]
	requirements: List[str]
	description: Dict[str, str]

	@property
	def translated_description(self) -> str:
		text = BundledText(self.description).get()
		if text is None:
			text = '*{}*'.format(Text('none'))
		else:
			text = markdown_utils.format_markdown(text)
		return text

	@classmethod
	def of(cls, metadata_json: dict, requirements_str: str) -> 'MetaInfo':
		metadata = Metadata(metadata_json)
		meta_info = MetaInfo()
		meta_info.id = metadata.id
		meta_info.name = metadata.name
		meta_info.version = str(metadata.version)
		meta_info.link = metadata.link
		meta_info.authors = metadata.author or []
		meta_info.dependencies = dict(map(
			lambda t: (str(t[0]), str(t[1])),
			metadata.dependencies.items()
		))
		meta_info.requirements = list(filter(
			lambda l: len(l) > 0, map(
				lambda l: l.split('#', 1)[0].strip(),
				requirements_str.splitlines()
			)
		))
		if isinstance(metadata.description, str):
			meta_info.description = {DEFAULT_LANGUAGE: metadata.description}
		elif isinstance(metadata.description, dict):
			meta_info.description = metadata.description
		else:
			meta_info.description = {}
		return meta_info

	@classmethod
	async def fetch_from_repos(cls, plugin: 'Plugin', *, tag: Optional[str] = None) -> 'MetaInfo':
		metadata_json = await plugin.get_repos_json('mcdreforged.plugin.json', tag=tag)
		requirements_str = await plugin.get_repos_text('requirements.txt', default='', tag=tag)
		meta_info = cls.of(metadata_json, requirements_str)

		if meta_info.id != plugin.id:
			raise AssertionError('wrong plugin id in mcdreforged.plugin.json, expected {} but found {}'.format(plugin.id, meta_info.id))
		return meta_info
