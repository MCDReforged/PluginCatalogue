import os
import traceback
from json import JSONDecodeError
from typing import Optional, List, Dict

import requests
from mcdreforged.plugin.meta.version import Version
from requests import Response

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
	def translated_description(self) -> Text:
		return BundledText(self.description)


class AssetInfo(Serializable):
	name: str
	size: int
	download_count: int
	created_at: str
	url: str


class ReleaseInfo(Serializable):
	url: str
	name: str
	tag_name: str
	created_at: str
	assets: List[AssetInfo]
	description: str
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


class ReleaseSummary(Serializable):
	id: str
	latest_version: str
	etag: str = ''
	releases: List[ReleaseInfo]

	def fetch_from_api(self, plugin: 'Plugin'):
		url = f'https://api.github.com/repos/{plugin.repos_path}/releases'
		resp: Optional[List[dict]]
		new_etag: str
		resp, new_etag = utils.request_github_api(url, etag=self.etag)
		self.id = plugin.id
		self.etag = new_etag
		if resp is not None:
			self.releases = []
			for item in resp:
				item['url'] = item['html_url']
				item['description'] = item['body']
				r_info = ReleaseInfo.deserialize(item)
				if r_info.parse_version(self.id) is not None:
					self.releases.append(r_info)
			self.latest_version = self.releases[0].parsed_version if len(self.releases) > 0 else 'N/A'


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
	id: str = 'N/A'
	repository: str = 'N/A'
	branch: str
	related_path: Optional[str]
	labels: List[Label]
	authors: List[Author]
	name: str
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

	def load_from_json(self, js: dict):
		self.id = js.get('id', None)
		self.name = js.get('name', self.id)
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
				author.deserialize_from(item)
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
				if lang in external_introduction:
					url = external_introduction[lang]
					try:
						response = requests.get(url, proxies=constants.PROXIES)
						assert response.status_code == 200, 'status code: {}'.format(response.status_code)
					except:
						print('Failed to get custom introduction file from {} in language {} in {}'.format(url, lang, self))
						traceback.print_exc()
						introduction_translations[lang] = '*{}*'.format(Text('data_fetched_failed'))
					else:
						introduction_translations[lang] = response.text
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

	def __repr__(self):
		return 'Plugin[id={},repository={}]'.format(self.id, self.repository)

	def __get_repos_file(self, file_path: str) -> Response:
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/next/mcdreforged.plugin.json
		url_base = f'https://raw.githubusercontent.com/{self.repos_path}/{self.branch}/{self.related_path}/'
		return requests.get(url_base + file_path, proxies=constants.PROXIES)

	def get_repos_json(self, file_path: str) -> dict:
		response = self.__get_repos_file(file_path)
		try:
			return response.json()
		except JSONDecodeError:
			print('Failed to decode json from response! status_code {}: {}'.format(response.status_code, response.content))
			raise

	def get_repos_text(self, file_path: str, default=None) -> str:
		resp = self.__get_repos_file(file_path)
		if resp.status_code != 200:
			return default
		return resp.text

	def fetch_meta(self) -> MetaInfo:
		metadata = self.get_repos_json('mcdreforged.plugin.json')
		assert metadata['id'] == self.id
		self.meta_info = MetaInfo()
		self.meta_info.id = self.id
		self.meta_info.name = self.name
		self.meta_info.version = metadata.get('version')
		self.meta_info.repository = self.repository
		self.meta_info.labels = list(map(lambda l: l.id, self.labels))
		self.meta_info.authors = list(map(lambda a: a.name, self.authors))
		self.meta_info.dependencies = metadata.get('dependencies', {})
		self.meta_info.requirements = self.get_repos_text('requirements.txt', default='').strip().splitlines()
		self.meta_info.description = metadata.get('description', {})
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
		try:
			self.release_summary = ReleaseSummary.deserialize(utils.load_json(self.__release_info_file))
		except:
			self.release_summary = ReleaseSummary()
		self.release_summary.fetch_from_api(self)
		print('Fetched release info of {}'.format(self.id))
		return self.release_summary


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_meta()
