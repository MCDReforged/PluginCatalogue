from typing import Optional, TYPE_CHECKING

from typing_extensions import Self

from common import log
from common.report import reporter
from utils import request_utils, value_utils

if TYPE_CHECKING:
	from meta.repos import RepositoryInfo


class GithubRepository:
	def __init__(self, repository: str, branch: str, related_path: str):
		value_utils.ensure_type(repository, str)
		value_utils.ensure_type(branch, str)
		value_utils.ensure_type(related_path, str)

		repository = repository
		if not repository.startswith('https://github.com/'):
			raise ValueError('GitHub repository with https url is required, found: {}'.format(repository))

		# no tailing '/'
		self.repos_url = repository.rstrip('/')
		self.repos_pair = value_utils.remove_prefix(self.repos_url, 'https://github.com/')  # TISUnion/QuickBackupM
		self.branch = branch  # master
		self.related_path = related_path.strip('/')

		if self.repos_pair.count('/') != 1:
			raise ValueError('Bad repository url {!r}'.format(self.repos_url))

	def __set_from(self, other: Self):
		self.repos_url = other.repos_url
		self.repos_pair = other.repos_pair
		self.branch = other.branch
		self.related_path = other.related_path

	def get_raw_url_base(self, tag: Optional[str] = None, in_plugin_relative: bool = True) -> str:
		"""
		No tailing '/'

		Example return values:
		- https://raw.githubusercontent.com/Myself/MyPlugin/master
		- https://raw.githubusercontent.com/Myself/MyPlugin/main/path/to/plugin
		"""
		url_base = f'https://raw.githubusercontent.com/{self.repos_pair}/{tag or self.branch}'
		if in_plugin_relative and self.related_path != '.':
			url_base += '/' + self.related_path
		return url_base

	def get_page_url_base(self, tag: Optional[str] = None, in_plugin_relative: bool = True) -> str:
		"""
		No tailing '/'

		For files, GitHub will perform an auto redirect to "blob" path, so it's ok

		Example return values:
		- https://github.com/Myself/MyPlugin/tree/master
		- https://github.com/Myself/MyPlugin/tree/main/path/to/plugin
		"""
		url_base = f'{self.repos_url}/tree/{tag or self.branch}'
		if in_plugin_relative and self.related_path != '.':
			url_base += '/' + self.related_path
		return url_base

	def resolve_raw(self, path: str, tag: Optional[str] = None, in_plugin_relative: bool = True) -> str:
		# https://raw.githubusercontent.com/TISUnion/QuickBackupM/master/mcdreforged.plugin.json
		return self.get_raw_url_base(tag=tag, in_plugin_relative=in_plugin_relative) + '/' + path

	def resolve_page(self, path: str, tag: Optional[str] = None) -> str:
		# https://github.com/TISUnion/QuickBackupM/tree/master/mcdreforged.plugin.json
		return self.get_page_url_base(tag=tag) + '/' + path

	async def request_repos_file(self, path: str, *, tag: Optional[str] = None, in_plugin_relative: bool = True) -> request_utils.SimpleResponse:
		return await request_utils.request_get(self.resolve_raw(path, tag=tag, in_plugin_relative=in_plugin_relative))

	@property
	def plugin_homepage(self) -> str:
		return self.get_page_url_base()

	@property
	def api_root(self) -> str:
		# https://api.github.com/repos/TISUnion/QuickBackupM
		return f'https://api.github.com/repos/{self.repos_pair}'

	def update_from_api(self, plugin_id: str, ri: 'RepositoryInfo'):
		if ri.full_name != self.repos_pair:
			log.warning('({}) Repository has been renamed from {!r} to {!r}'.format(plugin_id, self.repos_pair, ri.full_name))
			reporter.record_warning(plugin_id, 'Repository has been renamed from {!r} to {!r}'.format(self.repos_pair, ri.full_name), None)
			self.__set_from(GithubRepository(ri.html_url, self.branch, self.related_path))
