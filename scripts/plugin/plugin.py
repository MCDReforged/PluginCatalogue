import enum
import os
from json import JSONDecodeError
from typing import Optional, List, Dict, Union

from common import constants, log
from common.report import reporter
from common.translation import Text, BundledText, LANGUAGES, get_file_name, with_language
from meta.author import Author
from meta.misc import SchemaVersionHolder
from meta.plugin import PluginInfo, MetaInfo
from meta.release import ReleasePageCache, ReleaseSummary
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
	release_page_cache: Optional[ReleasePageCache] = None

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

	def is_disabled(self) -> bool:
		return self.__plugin_info.disable

	def get_disable_reason(self) -> str:
		return self.__plugin_info.disable_reason

	def fetch_introduction(self):
		external_introduction = self.__plugin_info.external_introduction
		introduction_translations = {}
		for lang in LANGUAGES:
			with with_language(lang):
				file_location = external_introduction.get(lang)
				if file_location is not None:
					try:
						file_content = self.get_repos_text(file_location)
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

	def is_data_fetched(self) -> bool:
		return self.__dataset.is_everything_fetched()

	@property
	def introduction(self) -> Text:
		return self.__introduction

	@property
	def latest_version(self) -> str:
		if self.release_summary.latest_version != 'N/A':
			return self.release_summary.latest_version
		return self.meta_info.version

	def __repr__(self):
		return 'Plugin[id={},repository={}]'.format(self.id, self.repos.repos_url)

	def get_repos_json(self, file_path: str, **kwargs) -> dict:
		resp = self.repos.request_repos_file(file_path, **kwargs)
		if resp.status_code != 200:
			raise Exception('status code {} (should be 200) when fetching json {} from {}'.format(resp.status_code, file_path, resp.url))
		try:
			return resp.json()
		except JSONDecodeError:
			raise Exception('Failed to decode json from response! url: {}, status_code {}: {}'.format(resp.url, resp.status_code, resp.content)) from None

	def get_repos_text(self, file_path: str, default: Optional[str] = None, **kwargs) -> str:
		resp = self.repos.request_repos_file(file_path, **kwargs)
		if resp.status_code != 200:
			if default is not None:
				return default
			else:
				raise Exception('status code {} (should be 200) when fetching text {} from {}'.format(resp.status_code, file_path, resp.url))
		return resp.text

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

	def fetch_meta(self) -> MetaInfo:
		self.meta_info = MetaInfo.fetch(self)
		log.info('Fetched meta info of {}'.format(self.id))
		self.__dataset |= _PluginDataSet.meta
		return self.meta_info

	def save_meta(self):
		if self.meta_info is None:
			log.info('Skipping {} during meta_info saving since meta_info is None'.format(self))
		else:
			file_utils.save_json(self.meta_info.serialize(), os.path.join(constants.META_FOLDER, self.id, 'meta.json'))

	@property
	def __release_info_file(self) -> str:
		return os.path.join(constants.META_FOLDER, self.id, 'release.json')

	@property
	def __release_page_cache_file(self) -> str:
		return os.path.join(constants.META_FOLDER, self.id, '.release_page_cache.json')

	def save_release_info(self):
		if self.release_summary is None:
			log.info('Skipping {} during release_summary saving since release_summary is None'.format(self))
		else:
			file_utils.save_json(self.release_summary.serialize(), self.__release_info_file)
		if self.release_page_cache is None:
			log.info('Skipping {} during release_page_cache saving since release_page_cache is None'.format(self))
		else:
			file_utils.save_json(self.release_page_cache.serialize(), self.__release_page_cache_file)

	def fetch_release(self) -> ReleaseSummary:
		prev: Optional[ReleaseSummary] = None
		try:
			release_info_object = file_utils.load_json(self.__release_info_file)
			holder = SchemaVersionHolder.deserialize(release_info_object, error_at_missing=True)
			if holder.schema_version != constants.RELEASE_INFO_SCHEMA_VERSION:
				log.warning('Ignoring previous release info due to different schema_version: {} -> {}'.format(holder.schema_version, constants.RELEASE_INFO_SCHEMA_VERSION))
				self.release_summary = None
			else:
				self.release_summary = prev = ReleaseSummary.deserialize(release_info_object, error_at_missing=True)
		except Exception as e:
			if not isinstance(e, FileNotFoundError):
				log.warning('Failed to deserialized existed release_summary for plugin {}: {} {}'.format(self, type(e), e))
				reporter.record_warning(self.id, 'Failed to deserialized existed release_summary', e)
			self.release_summary = None

		if self.release_summary is not None:  # load release page cache iif release summary is valid
			try:
				self.release_page_cache = ReleasePageCache.deserialize(file_utils.load_json(self.__release_page_cache_file))
			except Exception as e:
				if not isinstance(e, FileNotFoundError):
					log.warning('Failed to deserialized existed release_page_cache for plugin {}: {} {}'.format(self, type(e), e))
					reporter.record_warning(self.id, 'Failed to deserialized existed release_page_cache', e)
				self.release_page_cache = None

		if self.release_summary is not None and self.release_page_cache is not None:
			try:
				self.release_summary.sanity_check(self.release_page_cache)
			except Exception as e:
				log.warning('Failed to check release data sanity for plugin {}: {} {}, discarding existing data'.format(self, type(e), e))
				reporter.record_warning(self.id, 'Failed to check release info sanity', e)
				self.release_summary = None
				self.release_page_cache = None

		if self.release_summary is None:
			self.release_summary = ReleaseSummary()
		if self.release_page_cache is None:
			self.release_page_cache = ReleasePageCache()

		try:
			self.release_summary.update(self)
		except Exception as e:
			if prev is not None:
				self.release_summary = prev
				log.exception('Failed to fetch release info of {}, use the previous serialized one: {} {}'.format(self, type(e), e))
			else:
				raise e from None
		else:
			log.info('Fetched release info of {}, page num {}'.format(self.id, self.release_page_cache.page_amount))
			self.__dataset |= _PluginDataSet.releases
		return self.release_summary


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_meta()
