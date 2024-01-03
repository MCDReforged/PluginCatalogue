import os
import traceback
from json import JSONDecodeError
from typing import Optional, List

import requests

import constants
import log
import utils
from label import Label, get_label_set
from report import reporter
from schema import Author, MetaInfo, ReleaseSummary, ReleasePageCache, PluginInfo, FormattedPluginInfo, SchemaVersionHolder
from translation import Text, BundledText, LANGUAGES, get_file_name, with_language


class Plugin:
	plugin_json: dict

	id: str = 'N/A'
	repository: str = 'N/A'
	branch: str
	related_path: Optional[str]
	labels: List[Label]
	authors: List[Author]
	__introduction: Text

	# Available after fetch_data()
	meta_info: Optional[MetaInfo] = None
	release_summary: Optional[ReleaseSummary] = None
	release_page_cache: Optional[ReleasePageCache] = None

	def __init__(self, plugin_id: str):
		self.directory = os.path.join(constants.PLUGINS_FOLDER, plugin_id)
		if not os.path.isdir(self.directory):
			raise FileNotFoundError('Directory {} not found'.format(self.directory))

		self.__introduction: Optional[BundledText] = None
		js: dict = utils.load_json(os.path.join(self.directory, 'plugin_info.json'))
		self.load_from_json(js)

		if self.id != plugin_id:
			raise ValueError('Inconsistent plugin id, found {} in plugin_info.json but {} expected'.format(self.id, plugin_id))

		self.meta_info = None
		self.release_summary = None
		self.release_page_cache = None

	def is_disabled(self) -> bool:
		return bool(self.plugin_json.get('disable'))

	def get_disable_reason(self) -> str:
		return str(self.plugin_json.get('disable_reason', 'unknown'))

	def load_from_json(self, js: dict):
		info = PluginInfo.deserialize(js)
		self.plugin_json = js

		self.id = info.id
		self.repository = info.repository.rstrip('/')
		if not self.repository.startswith('https://github.com/'):
			raise ValueError('Github repository with https url is required, found: {}'.format(self.repository))
		self.branch = info.branch
		self.related_path = info.related_path.strip('/')

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
		external_introduction = info.introduction
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
							file_content = utils.rewrite_markdown(
								file_content,
								repos_url=self.__get_repos_page_base(),
								raw_url=self.__get_repos_raw_base(),
							)
						introduction_translations[lang] = file_content
				introduction_tr_file_path = os.path.join(self.directory, get_file_name('introduction.md'))
				if os.path.isfile(introduction_tr_file_path):
					with utils.read_file(introduction_tr_file_path) as file_handler:
						introduction_translations[lang] = file_handler.read()
		self.__introduction = BundledText(introduction_translations)

	def is_data_fetched(self) -> bool:
		return self.meta_info is not None and self.release_summary is not None

	@property
	def introduction(self) -> Text:
		return self.__introduction

	@property
	def latest_version(self) -> str:
		if self.release_summary.latest_version != 'N/A':
			return self.release_summary.latest_version
		return self.meta_info.version

	@property
	def repos_path(self) -> str:
		# TISUnion/QuickBackupM
		return utils.remove_prefix(self.repository, 'https://github.com/')

	@property
	def repository_plugin_page(self) -> str:
		# https://github.com/TISUnion/QuickBackupM/tree/master
		# https://github.com/Myself/MyPlugin/tree/main/path/to/plugin
		url = f'{self.repository}/tree/{self.branch}'
		if self.related_path != '.':
			url += '/' + self.related_path
		return url

	def str(self):
		try:
			return self.id
		except:
			return repr(self)

	def __repr__(self):
		return 'Plugin[id={},repository={}]'.format(self.id, self.repository)

	def __get_repos_page_base(self, tag: Optional[str] = None) -> str:
		# https://github.com/TISUnion/QuickBackupM/blob/master/
		url_base = f'https://github.com/{self.repos_path}/blob/{tag or self.branch}/'
		if self.related_path != '.':
			url_base += self.related_path + '/'
		return url_base

	def __get_repos_raw_base(self, tag: Optional[str] = None) -> str:
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/master/
		url_base = f'https://raw.githubusercontent.com/{self.repos_path}/{tag or self.branch}/'
		if self.related_path != '.':
			url_base += self.related_path + '/'
		return url_base

	def __get_repos_raw_file_path(self, file_path: str, *, tag: Optional[str] = None) -> str:
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/master/mcdreforged.plugin.json
		return self.__get_repos_raw_base(tag=tag) + file_path

	def __request_repos_file(self, file_path: str, *, tag: Optional[str] = None) -> requests.Response:
		return utils.request_get(self.__get_repos_raw_file_path(file_path, tag=tag))

	def get_repos_json(self, file_path: str, **kwargs) -> dict:
		response = self.__request_repos_file(file_path, **kwargs)
		try:
			return response.json()
		except JSONDecodeError:
			raise Exception('Failed to decode json from response! url: {}, status_code {}: {}'.format(response.url, response.status_code, response.content)) from None

	def get_repos_text(self, file_path: str, default: Optional[str] = None, **kwargs) -> str:
		resp = self.__request_repos_file(file_path, **kwargs)
		if resp.status_code != 200:
			if default is not None:
				return default
			else:
				raise Exception('status code {} (should be 200) when fetching {} from {}'.format(resp.status_code, file_path, resp.url))
		return resp.text

	def generate_formatted_plugin_info(self) -> FormattedPluginInfo:
		info = FormattedPluginInfo()
		info.id = self.id
		info.authors = [author.name for author in self.authors]
		info.repository = self.repository
		info.branch = self.branch
		info.related_path = self.related_path
		info.labels = [label.id for label in self.labels]
		info.introduction = self.__introduction.get_mapping().copy()
		return info

	def save_formatted_plugin_info(self):
		info = self.generate_formatted_plugin_info()
		utils.save_json(info.serialize(), os.path.join(constants.META_FOLDER, self.id, 'plugin.json'))

	def fetch_meta(self) -> MetaInfo:
		self.meta_info = MetaInfo.fetch(self)
		log.info('Fetched meta info of {}'.format(self.id))
		return self.meta_info

	def save_meta(self):
		if self.meta_info is None:
			log.info('Skipping {} during meta_info saving since meta_info is None'.format(self))
		else:
			utils.save_json(self.meta_info.serialize(), os.path.join(constants.META_FOLDER, self.id, 'meta.json'))

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
			utils.save_json(self.release_summary.serialize(), self.__release_info_file)
		if self.release_page_cache is None:
			log.info('Skipping {} during release_page_cache saving since release_page_cache is None'.format(self))
		else:
			utils.save_json(self.release_page_cache.serialize(), self.__release_page_cache_file)

	def fetch_release(self) -> ReleaseSummary:
		prev: Optional[ReleaseSummary] = None
		try:
			release_info_object = utils.load_json(self.__release_info_file)
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
				self.release_page_cache = ReleasePageCache.deserialize(utils.load_json(self.__release_page_cache_file))
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
		return self.release_summary


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_meta()
