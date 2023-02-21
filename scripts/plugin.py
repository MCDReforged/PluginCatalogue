import os
import traceback
from json import JSONDecodeError
from typing import Optional, List, Dict

import requests
from mcdreforged.plugin.meta.metadata import Metadata
from mcdreforged.plugin.meta.version import Version

import constants
import utils
from label import Label, get_label_set
from serializer import Serializable
from translation import Text, BundledText, LANGUAGES, get_file_name, with_language, DEFAULT_LANGUAGE


class MetaInfo(Serializable):
	id: str
	name: str
	version: str
	repository: str
	labels: List[str]
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
			text = utils.format_markdown(text)
		return text


class AssetInfo(Serializable):
	name: str
	size: int
	download_count: int
	created_at: str
	browser_download_url: str


class ReleaseInfo(Serializable):
	url: str
	name: str
	tag_name: str
	created_at: str
	assets: List[AssetInfo]
	description: str
	prerelease: bool
	parsed_version: str

	def __parse_version(self, plugin_id: str) -> Optional[str]:
		# Possible tag names
		#   plugin_id-v1.2.3
		#   plugin_id-1.2.3
		#   v1.2.3
		#   1.2.3

		def test_and_return(version_str: str) -> Optional[str]:
			try:
				Version(version_str, allow_wildcard=False)
			except:
				return None
			else:
				return version_str

		version = self.tag_name
		if version.startswith(plugin_id + '-'):
			version = utils.remove_prefix(version, plugin_id + '-')
		if len(version) == 0:
			return version
		if version[0].isdigit():
			return test_and_return(version)
		elif version[0].lower() == 'v':
			return test_and_return(version[1:])
		else:
			return None

	def parse_version(self, plugin_id: str) -> Optional[str]:
		self.parsed_version = self.__parse_version(plugin_id)
		return self.parsed_version

	def get_mcdr_assets(self) -> List[AssetInfo]:
		return [asset for asset in self.assets if asset.name.endswith('.mcdr') or asset.name.endswith('.pyz')]


class ReleasePage(Serializable):
	index: int = -1
	etag: str = ''
	releases: List[ReleaseInfo]
	empty: bool

	@classmethod
	def fetch_page(cls, plugin: 'Plugin', page_index: int, old_etag: str) -> Optional['ReleasePage']:
		"""
		:return: (page, is_empty)
		"""
		url = f'https://api.github.com/repos/{plugin.repos_path}/releases'
		resp, new_etag = utils.request_github_api(url, etag=old_etag, params={'page': page_index, 'per_page': constants.MAX_RELEASE_PER_PAGE})
		if resp is None:
			return None

		page = ReleasePage(index=page_index, etag=new_etag)
		page.releases = []
		for item in resp:
			item['url'] = item['html_url']
			item['description'] = item['body'] or 'N/A'
			try:
				r_info = ReleaseInfo.deserialize(item)
			except Exception as e:
				print('Failed to deserialize ReleaseInfo from {}: {}'.format(item, e))
				continue
			if cls.check_release(plugin, r_info):
				page.releases.append(r_info)
		page.empty = len(resp) == 0
		return page

	@classmethod
	def check_release(cls, plugin: 'Plugin', r_info: ReleaseInfo) -> bool:
		if r_info.parse_version(plugin.id) is None:
			return False
		if r_info.prerelease:
			return False
		return len(r_info.get_mcdr_assets()) > 0


class ReleaseSummaryVersionHolder(Serializable):
	schema_version: int


class ReleaseSummary(Serializable):
	schema_version: int = None
	id: str
	latest_version: str
	releases: List[ReleaseInfo] = []
	release_pages: List[ReleasePage] = []

	def update(self, plugin: 'Plugin'):
		self.schema_version = constants.RELEASE_INFO_SCHEMA_VERSION
		self.id = plugin.id
		page_map: Dict[int, ReleasePage] = {page.index: page for page in self.release_pages}

		# GitHub: Only the first 10000 results are available.
		# 10000 results == 100 pages
		for i in range(100):  # i in [0, 99]
			idx = i + 1  # idx in [1, 100]
			if idx in page_map:
				old_etag = page_map[idx].etag
			else:
				old_etag = ''
			page = ReleasePage.fetch_page(plugin, idx, old_etag)
			if page is not None:  # page updated
				page_map[idx] = page
			if page_map[idx].empty:  # not that many releases
				break

		self.release_pages = list(page_map.values())
		self.release_pages.sort(key=lambda p: p.index)
		self.releases = []
		for page in self.release_pages:
			self.releases.extend(page.releases)
		self.latest_version = self.releases[0].parsed_version if len(self.releases) > 0 else 'N/A'

	@property
	def page_amount(self) -> int:
		return len(self.release_pages) - 1

	def get_latest_release(self) -> Optional[ReleaseInfo]:
		if len(self.releases) > 0:
			return self.releases[0]
		return None

	def get_total_downloads(self) -> int:
		total = 0
		for release in self.releases:
			for asset in release.get_mcdr_assets():
				total += asset.download_count
		return total


class PluginMetaSummary(Serializable):
	plugin_amount: int
	plugins: Dict[str, MetaInfo]


class Author(Serializable):
	name: str
	link: str = None

	def to_markdown(self) -> str:
		if self.link is None:
			return self.name
		return '[{}]({})'.format(self.name, self.link)


class Plugin:
	plugin_json: dict

	id: str = 'N/A'
	repository: str = 'N/A'
	branch: str
	related_path: Optional[str]
	labels: List[Label]
	authors: List[Author]
	introduction: Text

	# Available after fetch_data()
	meta_info: Optional[MetaInfo] = None
	release_summary: Optional[ReleaseSummary] = None

	def __init__(self, plugin_id: str):
		self.directory = os.path.join(constants.PLUGINS_FOLDER, plugin_id)
		if not os.path.isdir(self.directory):
			raise FileNotFoundError('Directory {} not found'.format(self.directory))
		js: dict = utils.load_json(os.path.join(self.directory, 'plugin_info.json'))
		self.load_from_json(js)

		if self.id != plugin_id:
			raise ValueError('Inconsistent plugin id, found {} in plugin_info.json but {} expected'.format(self.id, plugin_id))

		self.meta_info = None
		self.release_summary = None

	def is_disabled(self) -> bool:
		return bool(self.plugin_json.get('disable'))

	def get_disable_reason(self) -> str:
		return str(self.plugin_json.get('disable_reason', 'unknown'))

	def load_from_json(self, js: dict):
		self.plugin_json = js

		self.id = js.get('id', None)
		self.repository = js['repository'].rstrip('/')
		if not self.repository.startswith('https://github.com/'):
			raise ValueError('Github repository with https url is required, found: {}'.format(self.repository))
		self.branch = js['branch']
		self.related_path = js.get('related_path', '.').strip('/')

		authors = js.get('authors', [])
		self.authors = []
		for item in authors:
			author = Author()
			if isinstance(item, str):
				author.name = item
			else:
				assert isinstance(item, dict)
				author.update_from(item)
			self.authors.append(author)

		# label
		self.labels = []
		for label_key in js['labels']:
			label = get_label_set().get_label(label_key)
			if label is None:
				raise ValueError('Unknown label: {}'.format(label_key))
			else:
				self.labels.append(label)

		# introduction
		external_introduction = js.get('introduction', {})
		introduction_translations = {}
		for lang in LANGUAGES:
			with with_language(lang):
				file_location = external_introduction.get(lang)
				if file_location is not None:
					try:
						introduction_translations[lang] = self.get_repos_text(file_location)
					except:
						print('Failed to get custom introduction file from {} in language {} in {}'.format(file_location, lang, self))
						traceback.print_exc()
						introduction_translations[lang] = '*{}*'.format(Text('data_fetched_failed'))
				introduction_tr_file_path = os.path.join(self.directory, get_file_name('introduction.md'))
				if os.path.isfile(introduction_tr_file_path):
					with utils.read_file(introduction_tr_file_path) as file_handler:
						introduction_translations[lang] = file_handler.read()
		self.introduction = BundledText(introduction_translations)

	def is_data_fetched(self) -> bool:
		return self.meta_info is not None and self.release_summary is not None

	@property
	def latest_version(self) -> str:
		if self.release_summary.latest_version != 'N/A':
			return self.release_summary.latest_version
		return self.meta_info.version

	@property
	def repos_path(self) -> str:
		# TISUnion/QuickBackupM
		return utils.remove_prefix(self.repository, 'https://github.com/')

	def str(self):
		try:
			return self.id
		except:
			return repr(self)

	def __repr__(self):
		return 'Plugin[id={},repository={}]'.format(self.id, self.repository)

	def __get_repos_file(self, file_path: str) -> requests.Response:
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/next/mcdreforged.plugin.json
		url_base = f'https://raw.githubusercontent.com/{self.repos_path}/{self.branch}/{self.related_path}/'
		return utils.request_get(url_base + file_path)

	def get_repos_json(self, file_path: str) -> dict:
		response = self.__get_repos_file(file_path)
		try:
			return response.json()
		except JSONDecodeError:
			print('Failed to decode json from response! url: {}, status_code {}: {}'.format(response.url, response.status_code, response.content))
			raise

	def get_repos_text(self, file_path: str, default: Optional[str] = None) -> str:
		resp = self.__get_repos_file(file_path)
		if resp.status_code != 200:
			if default is not None:
				return default
			else:
				raise Exception('status code {} != 200 when fetching file {} from {}'.format(resp.status_code, file_path, resp.url))
		return resp.text

	def fetch_meta(self) -> MetaInfo:
		metadata_json = self.get_repos_json('mcdreforged.plugin.json')
		metadata = Metadata(metadata_json)
		assert metadata.id == self.id
		self.meta_info = MetaInfo()
		self.meta_info.id = metadata.id
		self.meta_info.name = metadata.name
		self.meta_info.version = str(metadata.version)
		self.meta_info.repository = self.repository
		self.meta_info.labels = list(map(lambda l: l.id, self.labels))
		self.meta_info.authors = list(map(lambda a: a.name, self.authors))
		self.meta_info.dependencies = dict(map(
			lambda t: (str(t[0]), str(t[1])),
			metadata.dependencies.items()
		))
		self.meta_info.requirements = list(filter(
			lambda l: len(l) > 0, map(
				lambda l: l.split('#', 1)[0].strip(),
				self.get_repos_text('requirements.txt', default='').splitlines()
			)
		))
		if isinstance(metadata.description, str):
			self.meta_info.description = {DEFAULT_LANGUAGE: metadata.description}
		elif isinstance(metadata.description, dict):
			self.meta_info.description = metadata.description
		else:
			self.meta_info.description = {}
		if isinstance(self.meta_info.description, str):
			self.meta_info.description = {DEFAULT_LANGUAGE: self.meta_info.description}
		print('Fetched meta info of {}'.format(self.id))
		return self.meta_info

	def save_meta(self):
		if self.meta_info is None:
			print('Skipping {} during meta_info saving since meta_info is None'.format(self))
		else:
			utils.save_json(self.meta_info.serialize(), os.path.join(constants.META_FOLDER, self.id, 'meta.json'))

	@property
	def __release_info_file(self) -> str:
		return os.path.join(constants.META_FOLDER, self.id, 'release.json')

	def save_release_info(self):
		if self.release_summary is None:
			print('Skipping {} during release_summary saving since release_summary is None'.format(self))
		else:
			utils.save_json(self.release_summary.serialize(), self.__release_info_file)

	def fetch_release(self) -> ReleaseSummary:
		prev: Optional[ReleaseSummary] = None
		try:
			release_info_object = utils.load_json(self.__release_info_file)
			holder = ReleaseSummaryVersionHolder.deserialize(release_info_object, error_at_missing=True)
			if holder.schema_version != constants.RELEASE_INFO_SCHEMA_VERSION:
				print('Ignoring previous release info due to different schema_version: {} -> {}'.format(holder.schema_version, constants.RELEASE_INFO_SCHEMA_VERSION))
				self.release_summary = None
			else:
				self.release_summary = prev = ReleaseSummary.deserialize(release_info_object, error_at_missing=True)
		except Exception as e:
			if not isinstance(e, FileNotFoundError):
				print('Failed to deserialized existed release_summary for plugin {}: {} {}'.format(self, type(e), e))
			self.release_summary = None
		if self.release_summary is None:
			self.release_summary = ReleaseSummary()
		try:
			self.release_summary.update(self)
		except Exception as e:
			if prev is not None:
				self.release_summary = prev
				print('Failed to fetch release info of {}, use the previous serialized one: {} {}'.format(self, type(e), e))
			else:
				raise e from None
		else:
			print('Fetched release info of {}, page num {}'.format(self.id, self.release_summary.page_amount))
		return self.release_summary


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_meta()
