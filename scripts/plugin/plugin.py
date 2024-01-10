import enum
import os
from json import JSONDecodeError
from typing import Optional, List, Dict, Union

from common import constants, log
from common.report import reporter
from common.translation import Text, BundledText, LANGUAGES, get_file_name, with_language
from meta.author import Author
from meta.plugin import PluginInfo, MetaInfo
from meta.release import ReleaseSummary
from plugin.cache import RequestCacheManager
from plugin.label import Label, get_label_set
from utils import file_utils, markdown_utils
from utils.repos import GithubRepository
from utils.serializer import Serializable


class _PluginDataSet(enum.Flag):
	info = enum.auto()
	introduction = enum.auto()
	meta = enum.auto()
	releases = enum.auto()

	def is_everything_fetched(self) -> bool:
		for ds in _PluginDataSet:
			if ds not in self:
				return False
		return True


class _PluginInfoJson(Serializable):
	"""
	Content of plugin_info.json
	"""
	id: str
	authors: List[Union[str, Author]] = []
	repository: str
	branch: str
	related_path: str = '.'
	labels: List[str] = []
	introduction: Dict[str, str] = {}  # lang -> file path in repos


class _PluginInfoInner:
	id: str

	repos: GithubRepository
	branch: str
	related_path: Optional[str]

	labels: List[Label]
	authors: List[Author]
	external_introduction: Dict[str, str]

	disable: bool
	disable_reason: str

	def __init__(self, plugin_json: dict):
		info = _PluginInfoJson.deserialize(plugin_json)

		self.id = info.id
		self.repos = GithubRepository(info.repository, info.branch, info.related_path)

		self.authors = []
		for item in info.authors:
			assert isinstance(item, (str, Author)), 'author item should be str or Author, found {}'.format(type(item))
			if isinstance(item, str):
				author = Author()
				author.name = item
			else:
				author = item
			self.authors.append(author)

		# label
		self.labels = []
		for label_key in info.labels:
			label = get_label_set().get_label(label_key)
			if label is None:
				raise ValueError('Unknown label: {}'.format(label_key))
			else:
				self.labels.append(label)

		# introduction
		self.external_introduction = info.introduction

		# disable state
		self.disable = bool(plugin_json.get('disable'))
		self.disable_reason = str(plugin_json.get('disable_reason', 'unknown'))


class Plugin:
	__plugin_info: _PluginInfoInner
	meta_info: Optional[MetaInfo] = None
	release_summary: Optional[ReleaseSummary] = None

	def __init__(self, plugin_id: str):
		self.__introduction: Optional[BundledText] = None

		self.__info_directory = os.path.join(constants.PLUGINS_FOLDER, plugin_id)
		if not os.path.isdir(self.__info_directory):
			raise FileNotFoundError('Directory {} not found'.format(self.__info_directory))

		plugin_json = file_utils.load_json(os.path.join(self.__info_directory, 'plugin_info.json'))
		self.__plugin_info = _PluginInfoInner(plugin_json)
		if self.id != plugin_id:
			raise ValueError('Inconsistent plugin id, found {} in plugin_info.json but {} expected'.format(self.id, plugin_id))

		self.__dataset = _PluginDataSet.info
		self.__cache = RequestCacheManager(self, self.__request_cache_file)
		self.__cache.load()

	# ========================= property && getter =========================

	@property
	def id(self) -> str:
		return self.__plugin_info.id

	@property
	def repos(self) -> GithubRepository:
		return self.__plugin_info.repos

	@property
	def authors(self) -> List[Author]:
		return self.__plugin_info.authors

	@property
	def labels(self) -> List[Label]:
		return self.__plugin_info.labels

	@property
	def introduction(self) -> Text:
		return self.__introduction

	@property
	def latest_version(self) -> str:
		if self.release_summary.latest_version is not None:
			return self.release_summary.latest_version
		return self.meta_info.version

	def is_disabled(self) -> bool:
		return self.__plugin_info.disable

	def get_disable_reason(self) -> str:
		return self.__plugin_info.disable_reason

	def is_data_fetched(self) -> bool:
		return self.__dataset.is_everything_fetched()

	def __repr__(self):
		return 'Plugin[id={},repository={}]'.format(self.id, self.repos.repos_url)

	# ========================= utils =========================

	async def get_repos_json(self, file_path: str, **kwargs) -> dict:
		resp = await self.repos.request_repos_file(file_path, **kwargs)
		if resp.status_code != 200:
			raise Exception('status code {} (should be 200) when fetching json {} from {}'.format(resp.status_code, file_path, resp.url))
		try:
			return resp.json()
		except JSONDecodeError:
			raise Exception('Failed to decode json from response! url: {}, status_code {}: {}'.format(resp.url, resp.status_code, resp.content)) from None

	async def get_repos_text(self, file_path: str, default: Optional[str] = None, **kwargs) -> str:
		resp = await self.repos.request_repos_file(file_path, **kwargs)
		if resp.status_code != 200:
			if default is not None:
				return default
			else:
				raise Exception('status code {} (should be 200) when fetching text {} from {}'.format(resp.status_code, file_path, resp.url))
		return resp.text

	# ========================= Introduction =========================

	async def fetch_introduction(self):
		external_introduction = self.__plugin_info.external_introduction
		introduction_translations = {}
		for lang in LANGUAGES:
			with with_language(lang):
				file_location = external_introduction.get(lang)
				if file_location is not None:
					try:
						file_content = await self.get_repos_text(file_location)
					except Exception as e:
						log.exception('Failed to get custom introduction file in language {} from {} in {}'.format(lang, file_location, self))
						reporter.record_failure(self.id, 'Fetch custom introduction file in language {} from {} failed'.format(lang, file_location), e)
						introduction_translations[lang] = '*{}*'.format(Text('data_fetched_failed'))
					else:
						if file_location.lower().endswith('.md'):
							file_content = markdown_utils.rewrite_markdown(
								file_content,
								repos_url=self.repos.get_page_url_base(),
								raw_url=self.repos.get_raw_url_base(),
							)
						introduction_translations[lang] = file_content
				introduction_tr_file_path = os.path.join(self.__info_directory, get_file_name('introduction.md'))
				if os.path.isfile(introduction_tr_file_path):
					with file_utils.open_for_read(introduction_tr_file_path) as file_handler:
						introduction_translations[lang] = file_handler.read()
		self.__introduction = BundledText(introduction_translations)
		self.__dataset |= _PluginDataSet.introduction
		log.info('({}) Introduction fetched'.format(self.id))

	# ========================= PluginInfo =========================

	def generate_formatted_plugin_info(self) -> PluginInfo:
		if (_PluginDataSet.info | _PluginDataSet.introduction) not in self.__dataset:
			raise RuntimeError('not enough info. current dataset: {}'.format(self.__dataset))
		info = PluginInfo()
		info.id = self.id
		info.authors = [author.name for author in self.__plugin_info.authors]
		info.repository = self.repos.repos_url
		info.branch = self.repos.branch
		info.related_path = self.repos.related_path
		info.labels = [label.id for label in self.__plugin_info.labels]
		info.introduction = self.__introduction.get_mapping().copy()
		return info

	def save_formatted_plugin_info(self):
		info = self.generate_formatted_plugin_info()
		file_utils.save_json(info.serialize(), os.path.join(constants.META_FOLDER, self.id, 'plugin.json'))

	# ========================= MetaInfo =========================

	async def fetch_meta(self):
		self.meta_info = await MetaInfo.fetch_from_repos(self)
		self.__dataset |= _PluginDataSet.meta
		log.info('({}) MetaInfo fetched'.format(self.id))

	def save_meta(self):
		if self.meta_info is not None:
			file_utils.save_json(self.meta_info.serialize(), os.path.join(constants.META_FOLDER, self.id, 'meta.json'))

	# ========================= Release & Cache =========================

	async def fetch_release(self):
		self.release_summary = await ReleaseSummary.create_for(self, self.__cache)
		self.__dataset |= _PluginDataSet.releases
		log.info('({}) Release fetched'.format(self.id))

	@property
	def __release_info_file(self) -> str:
		return os.path.join(constants.META_FOLDER, self.id, 'release.json')

	@property
	def __request_cache_file(self) -> str:
		return os.path.join(constants.META_FOLDER, self.id, '.request_cache.json')

	def save_release_info(self):
		if self.release_summary is not None:
			file_utils.save_json(self.release_summary.serialize(), self.__release_info_file, with_gz=True)

	def save_request_cache(self):
		file_utils.save_json(self.__cache.dump_for_save(), self.__request_cache_file)


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_meta()
