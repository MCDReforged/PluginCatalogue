import os
import shutil
import traceback
from typing import Callable, Any, List, Collection, Optional

import constants
import utils
from plugin import Plugin
from report import reporter
from schema import PluginMetaSummary, AuthorSummary
from serializer import serialize
from thread_pools import worker_pool


class PluginList(List[Plugin]):
	def __init__(self):
		super().__init__()
		self.__inited = False
		self.__meta_fetched = False
		self.__release_fetched = False

	def init(self, target_ids: Optional[Collection[str]]):
		if self.__inited:
			return
		self.clear()
		futures = []
		for folder in os.listdir(constants.PLUGINS_FOLDER):
			if os.path.isdir(os.path.join(constants.PLUGINS_FOLDER, folder)):
				if target_ids is None or folder in target_ids:
					print('Found plugin {}'.format(folder))
					futures.append((folder, worker_pool.submit(Plugin, folder)))
				else:
					print('Skipping plugin {}'.format(folder))
		for folder, future in futures:
			try:
				plugin = future.result()
				if plugin.is_disabled():
					print('Plugin {} is disabled due to "{}"'.format(plugin, plugin.get_disable_reason()))
					reporter.record_plugin_disabled(plugin.id, plugin.get_disable_reason())
				else:
					self.append(plugin)
			except Exception as e:
				print('[Error] Failed to initialize plugin in folder "{}"'.format(folder))
				reporter.record_failure(folder, 'Initialize plugin in folder {} failed'.format(folder), e)
				traceback.print_exc()
				raise

		print('Found {} plugins in total'.format(len(self)))
		self.sort(key=lambda plg: plg.id.lower())
		self.__inited = True

	def __fetch(self, fetch_target_name: str, func: Callable[[Plugin], Any], fail_hard: bool):
		futures = []
		for plugin in self:
			futures.append((plugin, worker_pool.submit(func, plugin)))
		for plugin, future in futures:
			try:
				future.result()
			except Exception as e:
				print('[Error] Failed to fetch {} of plugin {}'.format(fetch_target_name, plugin))
				reporter.record_failure(plugin.id, 'Fetch {} failed'.format(fetch_target_name), e)
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

		# prepare folder
		if os.path.isdir(constants.META_FOLDER):
			shutil.rmtree(constants.META_FOLDER)
		os.makedirs(constants.META_FOLDER)
		shutil.copy(os.path.join(constants.TEMPLATE_FOLDER, 'meta_readme.md'), os.path.join(constants.META_FOLDER, 'readme.md'))

		# store info for each plugin
		for plugin in self:
			try:
				plugin.save_meta()
				plugin.save_release_info()
				plugin.save_formatted_plugin_info()
			except Exception as e:
				print('[Error] Storing info for plugin {}'.format(plugin))
				reporter.record_failure(plugin.id, 'Store plugin info', e)
				traceback.print_exc()

		# make and store plugin summary
		meta_summary = PluginMetaSummary()
		meta_summary.plugin_amount = len(self)
		meta_summary.plugins = {}
		for plugin in self:
			meta_summary.plugins[plugin.id] = plugin.meta_info
		utils.save_json(serialize(meta_summary), os.path.join(constants.META_FOLDER, 'plugins.json'), compact=True)

		# make and store author summary
		author_storage = AuthorSummary()
		for plugin in self:
			for author in plugin.authors:
				author_storage.add_author(author.copy(), plugin.id)
		author_storage.finalize()
		utils.save_json(serialize(author_storage), os.path.join(constants.META_FOLDER, 'authors.json'))


_plugin_list = PluginList()


def get_plugin_list(target_ids: Optional[Collection[str]] = None) -> PluginList:
	_plugin_list.init(target_ids)
	return _plugin_list
