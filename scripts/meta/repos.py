from typing import TYPE_CHECKING, Optional

from utils.serializer import Serializable

if TYPE_CHECKING:
	from plugin.cache import PluginRequestCacheManager


class RepositoryInfo(Serializable):
	url: str
	name: str
	full_name: str
	description: Optional[str]
	archived: bool

	stargazers_count: int
	watchers_count: int
	forks_count: int

	@classmethod
	async def create_for(cls, plugin_cache_manager: 'PluginRequestCacheManager') -> 'RepositoryInfo':
		rsp = await plugin_cache_manager.fetch_repository_info()
		data = rsp.get_json()
		data['url'] = data['html_url']

		return RepositoryInfo.deserialize(data)
