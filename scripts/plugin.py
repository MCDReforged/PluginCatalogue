import json
import os
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Optional, List, Dict

import requests
from requests import Response

import constants
import utils
from label import Label, get_label_set
from text import Text


class MetaInfo:
	version: str
	dependencies: Dict[str, str]
	requirements: List[str]

	def __init__(self, version: str, dependencies: Dict[str, str], requirements: List[str]):
		self.version = version
		self.dependencies = dependencies
		self.requirements = requirements


class Plugin:
	id: str
	repository: str
	branch: str
	related_path: Optional[str]
	labels: List[Label]
	authors: List[str]
	name: str
	readme: Text

	meta_info: Optional[MetaInfo]

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

	def __get_repos_file(self, file_path: str) -> Response:
		repos_path = utils.remove_prefix(self.repository, 'https://github.com/')
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/next/mcdreforged.plugin.json
		url_base = f'https://raw.githubusercontent.com/{repos_path}/{self.branch}/{self.related_path}/'
		return requests.get(url_base + file_path, proxies=constants.PROXIES)

	def get_repos_json(self, file_path: str) -> dict:
		return self.__get_repos_file(file_path).json()

	def get_repos_text(self, file_path: str, default=None) -> str:
		resp = self.__get_repos_file(file_path)
		if resp.status_code != 200:
			return default
		return resp.text

	def fetch_metadata(self):
		metadata = self.get_repos_json('mcdreforged.plugin.json')
		assert metadata['id'] == self.id
		version = metadata.get('version')
		dependencies = metadata.get('dependencies', {})
		requirements = self.get_repos_text('requirements.txt', default='').strip().splitlines()
		self.meta_info = MetaInfo(version, dependencies, requirements)
		print('Fetched meta info of {}'.format(self.id))

	def fetch_release(self):
		pass


class PluginList(List[Plugin]):
	def __init__(self):
		super().__init__()
		for folder in os.listdir(constants.PLUGINS_FOLDER):
			if os.path.isdir(os.path.join(constants.PLUGINS_FOLDER, folder)):
				print('Found plugin {}'.format(folder))
				self.append(Plugin(folder))

		print('Loaded {} plugins'.format(len(self)))
		self.sort(key=lambda plg: plg.id.lower())

	def fetch_meta(self):
		print('Fetching meta info')
		futures = []
		with ThreadPoolExecutor(max_workers=16) as executor:
			for plugin in self:
				futures.append(executor.submit(plugin.fetch_metadata))
			for future in futures:
				future.result()

		print('Meta info fetched')


_plugin_list = PluginList()


def get_plugin_list() -> PluginList:
	return _plugin_list


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_metadata()
