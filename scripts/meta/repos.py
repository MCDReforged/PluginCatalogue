import asyncio
from typing import TYPE_CHECKING, Optional, List

from common import log
from utils import markdown_utils, request_utils
from utils.serializer import Serializable

if TYPE_CHECKING:
	from plugin.cache import PluginRequestCacheManager
	from plugin.plugin import Plugin


class RepositoryInfo(Serializable):
	url: str
	name: str
	full_name: str
	html_url: str
	description: Optional[str]
	archived: bool

	stargazers_count: int
	watchers_count: int
	forks_count: int

	readme: Optional[str] = None
	readme_url: Optional[str] = None

	@classmethod
	async def create_for(cls, plugin: 'Plugin', plugin_cache_manager: 'PluginRequestCacheManager') -> 'RepositoryInfo':
		rsp = await plugin_cache_manager.fetch_repository_info()
		data = rsp.get_json()
		data['url'] = data['html_url']

		ri = RepositoryInfo.deserialize(data)
		await ri.__fetch_readmes(plugin)
		return ri

	async def __fetch_readmes(self, plugin: 'Plugin'):
		self.readme = None
		self.readme_url = None
		tasks: List[asyncio.Task] = []

		async def fetch_readme(file: str, what_readme: str, in_plugin_relative: bool):
			url = plugin.repos.resolve_raw(file, in_plugin_relative=in_plugin_relative)
			rsp = await request_utils.request_get(url)
			if rsp.status_code == 200:
				log.info('({}) Fetched {} readme from file {!r}, rel {}'.format(plugin.id, what_readme, file, in_plugin_relative))
				readme = rsp.text
				try:
					readme = markdown_utils.rewrite_markdown(
						rsp.text,
						repos_url=plugin.repos.get_page_url_base(in_plugin_relative=in_plugin_relative),
						raw_url=plugin.repos.get_raw_url_base(in_plugin_relative=in_plugin_relative),
					)
				except Exception:
					log.exception('{} Failed to rewrite markdown for, use original content, file: {!r}, rel: {}'.format(plugin.id, file, in_plugin_relative))

				self.readme = readme
				self.readme_url = url
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
