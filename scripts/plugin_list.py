import os
import shutil
import traceback
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Callable, Any, List

import constants
import utils
from plugin import PluginMetaSummary, Plugin


class PluginList(List[Plugin]):
	def __init__(self):
		super().__init__()
		self.__inited = False
		self.__meta_fetched = False
		self.__release_fetched = False

	def init(self):
		if self.__inited:
			return
		self.clear()
		for folder in os.listdir(constants.PLUGINS_FOLDER):
			if os.path.isdir(os.path.join(constants.PLUGINS_FOLDER, folder)):
				print('Found plugin {}'.format(folder))
				try:
					self.append(Plugin(folder))
				except:
					print('Failed to initialize plugin in folder "{}"'.format(folder))
					traceback.print_exc()
					raise

		print('Found {} plugins in total'.format(len(self)))
		self.sort(key=lambda plg: plg.id.lower())
		self.__inited = True

	def __fetch(self, name: str, func: Callable[[Plugin], Any], fail_hard: bool):
		with ThreadPoolExecutor(max_workers=16) as executor:
			futures = []
			for plugin in self:
				futures.append(executor.submit(func, plugin))
			for future in futures:
				try:
					future.result()
				except Exception as e:
					print('Failed to fetch {} of plugin {}'.format(name, plugin))
					if fail_hard:
						raise
					else:
						print('{}: {}'.format(type(e), e))
					traceback.print_exc()

	def fetch_data(self, meta: bool = True, release: bool = True, *, fail_hard: bool):
		print('Fetching data')
		if meta and not self.__meta_fetched:
			self.__fetch('meta', lambda plg: plg.fetch_meta(), fail_hard=fail_hard)
			self.__meta_fetched = True
		if release and not self.__release_fetched:
			self.__fetch('release', lambda plg: plg.fetch_release(), fail_hard=fail_hard)
			self.__release_fetched = True

	def store_data(self):
		print('Storing data into meta folder')
		if os.path.isdir(constants.META_FOLDER):
			shutil.rmtree(constants.META_FOLDER)
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
