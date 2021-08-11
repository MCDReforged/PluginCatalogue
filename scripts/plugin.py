import json
import os
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Optional, List, Dict, Callable, Any

import requests
from requests import Response

import constants
import utils
from label import Label, get_label_set
from serializer import Serializable
from text import Text


class MetaInfo(Serializable):
	id: str
	name: str
	version: str
	repository: str
	labels: List[str]
	authors: List[str]
	dependencies: Dict[str, str]
	requirements: List[str]


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
		# plugin_id-v1.2.3
		# v1.2.3
		# 1.2.3

		version = self.tag_name
		if version.startswith(plugin_id + '-'):
			version = utils.remove_prefix(version, plugin_id + '-')
		if len(version) == 0:
			return version
		if version.isdigit():
			return version
		elif version[0].lower() == 'v':
			return version.lstrip('vV')
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


class Plugin:
	id: str
	repository: str
	branch: str
	related_path: Optional[str]
	labels: List[Label]
	authors: List[str]
	name: str
	readme: Text

	# Available after fetch_data()
	meta_info: Optional[MetaInfo]
	release_summary: Optional[ReleaseSummary]

	def __init__(self, plugin_id: str):
		self.directory = os.path.join(constants.PLUGINS_FOLDER, plugin_id)
		if not os.path.isdir(self.directory):
			raise FileNotFoundError('Directory {} not found'.format(self.directory))
		with open(os.path.join(self.directory, 'info.json'), 'r') as file_handler:
			js: dict = json.load(file_handler)

		self.id = js.get('id', None)
		if self.id != plugin_id:
			raise ValueError('Inconsistent plugin id, found {} in info.json but {} expected'.format(self.id, plugin_id))
		self.name = js.get('name', self.id)
		self.repository = js['repository'].rstrip('/')
		if not self.repository.startswith('https://github.com/'):
			raise ValueError('Github repository with https url is required, found: {}'.format(self.repository))
		self.branch = js['branch']
		self.related_path = js.get('related_path', '.').strip('/')
		self.authors = js.get('author', [])
		if isinstance(self.authors, str):
			self.authors = [self.authors]
		self.labels = []
		for label_key in js['labels']:
			label = get_label_set().get_label(label_key)
			if label is None:
				print('Unknown label: {}'.format(label_key))
			else:
				self.labels.append(label)

		# readme
		with open(os.path.join(self.directory, 'readme.md'), 'r') as file_handler:
			readme_en = file_handler.read()
		readme_cn_file = os.path.join(self.directory, 'readme.md')
		if os.path.isfile(readme_cn_file):
			with open(readme_cn_file, 'r') as file_handler:
				readme_cn = file_handler.read()
		else:
			readme_cn = None
		self.readme = Text(readme_en, readme_cn)

		self.meta_info = None
		self.release_summary = None

	@property
	def latest_version(self) -> str:
		if self.release_summary.latest_version != 'N/A':
			return self.release_summary.latest_version
		return self.meta_info.version

	@property
	def repos_path(self) -> str:
		# TISUnion/QuickBackupM
		return utils.remove_prefix(self.repository, 'https://github.com/')

	def __get_repos_file(self, file_path: str) -> Response:
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/next/mcdreforged.plugin.json
		url_base = f'https://raw.githubusercontent.com/{self.repos_path}/{self.branch}/{self.related_path}/'
		return requests.get(url_base + file_path, proxies=constants.PROXIES)

	def get_repos_json(self, file_path: str) -> dict:
		return self.__get_repos_file(file_path).json()

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
		self.meta_info.labels = list(map(str, self.labels))
		self.meta_info.authors = self.authors
		self.meta_info.dependencies = metadata.get('dependencies', {})
		self.meta_info.requirements = self.get_repos_text('requirements.txt', default='').strip().splitlines()
		print('Fetched meta info of {}'.format(self.id))
		return self.meta_info

	def save_meta(self):
		utils.save_json(self.meta_info.serialize(), os.path.join(constants.META_FOLDER, self.id, 'meta.json'))

	@property
	def __release_info_file(self) -> str:
		return os.path.join(constants.META_FOLDER, self.id, 'release.json')

	def save_release_info(self):
		utils.save_json(self.release_summary.serialize(), self.__release_info_file)

	def fetch_release(self) -> ReleaseSummary:
		try:
			self.release_summary = ReleaseSummary.deserialize(utils.load_json(self.__release_info_file))
		except:
			self.release_summary = ReleaseSummary()
		self.release_summary.fetch_from_api(self)
		print('Fetched release info of {}'.format(self.id))
		return self.release_summary


class PluginList(List[Plugin]):
	def __init__(self):
		super().__init__()
		self.__inited = False
		self.__data_fetched = False

	def init(self):
		if self.__inited:
			return
		self.clear()
		for folder in os.listdir(constants.PLUGINS_FOLDER):
			if os.path.isdir(os.path.join(constants.PLUGINS_FOLDER, folder)):
				print('Found plugin {}'.format(folder))
				self.append(Plugin(folder))

		print('Found {} plugins in total'.format(len(self)))
		self.sort(key=lambda plg: plg.id.lower())
		self.__inited = True

	def __fetch(self, func: Callable[[Plugin], Any]):
		with ThreadPoolExecutor(max_workers=16) as executor:
			futures = []
			for plugin in self:
				futures.append(executor.submit(func, plugin))
			for future in futures:
				future.result()

	def fetch_data(self, meta: bool = True, release: bool = True):
		if self.__data_fetched:
			return
		print('Fetching data')
		if meta:
			self.__fetch(lambda plg: plg.fetch_meta())
		if release:
			self.__fetch(lambda plg: plg.fetch_release())
		self.__data_fetched = True

	def store_data(self):
		print('Storing data')
		meta_summary = PluginMetaSummary()
		meta_summary.plugin_amount = len(self)
		meta_summary.plugins = {}
		for plugin in self:
			plugin.save_meta()
			plugin.save_release_info()
			meta_summary.plugins[plugin.id] = plugin.meta_info
		utils.save_json(meta_summary.serialize(), os.path.join(constants.META_FOLDER, 'plugins.json'))


_plugin_list = PluginList()


def get_plugin_list() -> PluginList:
	_plugin_list.init()
	return _plugin_list


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_meta()
