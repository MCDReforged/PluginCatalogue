import json
import os
from typing import Optional, List

import requests
from requests import Response

import constants
import utils
from label import Label, get_label_set
from text import Text


class Plugin:
	id: str
	repository: str
	branch: str
	related_path: Optional[str]
	labels: List[Label]
	authors: List[str]
	name: str
	readme: Text

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

	def __get_file(self, file_path: str) -> Response:
		repos_path = utils.remove_prefix(self.repository, 'https://github.com/')
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/next/mcdreforged.plugin.json
		url_base = f'https://raw.githubusercontent.com/{repos_path}/{self.branch}/{self.related_path}/'
		return requests.get(url_base + file_path)

	def get_json(self, file_path: str):
		return self.__get_file(file_path).json()

	def check_repository(self):
		metadata = self.get_json('mcdreforged.plugin.json')
		assert metadata['id'] == self.id


def get_plugin_list() -> List[Plugin]:
	plugin_list = []
	for folder in os.listdir(constants.PLUGINS_FOLDER):
		if os.path.isdir(os.path.join(constants.PLUGINS_FOLDER, folder)):
			print('Found plugin {}'.format(folder))
			plugin_list.append(Plugin(folder))
	plugin_list.sort(key=lambda plg: plg.id.lower())
	return plugin_list


if __name__ == '__main__':
	Plugin('quick_backup_multi').check_repository()
