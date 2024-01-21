import asyncio
import time
from typing import TYPE_CHECKING, Optional, List

from common import log
from utils.serializer import Serializable

if TYPE_CHECKING:
	from plugin.cache import PluginRequestCacheManager
	from plugin.plugin import Plugin


class RepositoryInfo(Serializable):
	timestamp: int

	url: str
	name: str
	full_name: str
	description: Optional[str]
	archived: bool

	stargazers_count: int
	watchers_count: int
	forks_count: int

	readme: Optional[str]

	@classmethod
	async def create_for(cls, plugin: 'Plugin', plugin_cache_manager: 'PluginRequestCacheManager') -> 'RepositoryInfo':
		rsp = await plugin_cache_manager.fetch_repository_info()
		data = rsp.get_json()
		data['url'] = data['html_url']

		ri = RepositoryInfo.deserialize(data)
		ri.timestamp = int(time.time())
		await ri.__fetch_readmes(plugin)
		return ri

	async def __fetch_readmes(self, plugin: 'Plugin'):
		self.readme = None
		tasks: List[asyncio.Task] = []

		async def fetch_readme(file: str, what_readme: str, in_plugin_relative: bool):
			rsp = await plugin.repos.request_repos_file(file, in_plugin_relative=in_plugin_relative)
			if rsp.status_code == 200:
				self.readme = rsp.text
				log.info('({}) Fetched {} readme from file {!r}'.format(plugin.id, what_readme, file))
				for task in tasks:
					task.cancel()

		readme_candidates = ['readme.md', 'README.MD', 'README.md', 'readme.MD']
		async with asyncio.TaskGroup() as tg:
			for candidate in readme_candidates:
				tasks.append(tg.create_task(fetch_readme(candidate, 'plugin', True)))
		if self.readme is None and plugin.repos.related_path != '.':
			tasks.clear()
			async with asyncio.TaskGroup() as tg:
				for candidate in readme_candidates:
					tasks.append(tg.create_task(fetch_readme(candidate, 'repos', False)))

		if self.readme is None:
			log.warning('({}) Failed to fetch readme from repository, related path: {!r}'.format(plugin.id, plugin.repos.related_path))
