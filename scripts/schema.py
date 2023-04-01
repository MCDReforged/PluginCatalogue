from typing import Optional, List, Dict, NamedTuple, Iterable, Union, TYPE_CHECKING, Set

from mcdreforged.plugin.meta.metadata import Metadata
from mcdreforged.plugin.meta.version import Version

import constants
import utils
from report import reporter
from serializer import Serializable
from thread_pools import downloader_pool
from translation import Text, BundledText, DEFAULT_LANGUAGE

if TYPE_CHECKING:
	from plugin import Plugin


class Author(Serializable):
	name: str = ''
	link: Optional[str] = None

	def to_markdown(self) -> str:
		if self.link is None:
			return self.name
		return '[{}]({})'.format(self.name, self.link)


class FormattedPluginInfo(Serializable):
	"""
	The processed PluginInfo, that will be stored in the meta branch
	"""
	schema_version: int = constants.PLUGIN_INFO_SCHEMA_VERSION
	id: str
	authors: List[str]  # author names
	repository: str
	branch: str
	related_path: str
	labels: List[str]
	introduction: Dict[str, str]  # lang -> content


class PluginInfo(Serializable):
	"""
	Content of plugin_info.json
	"""
	id: str
	authors: List[Union[str, Author]] = []
	repository: str
	branch: str
	related_path: str = '.'
	labels: List[str] = []
	introduction: Dict[str, str] = {}  # lang -> file path in repos


class MetaInfo(Serializable):
	schema_version: int = constants.META_INFO_SCHEMA_VERSION
	id: str
	name: str
	version: str
	repository: str
	link: Optional[str]
	authors: List[str]
	dependencies: Dict[str, str]
	requirements: List[str]
	description: Dict[str, str]

	@property
	def translated_description(self) -> str:
		text = BundledText(self.description).get()
		if text is None:
			text = '*{}*'.format(Text('none'))
		else:
			text = utils.format_markdown(text)
		return text

	@classmethod
	def fetch(cls, plugin: 'Plugin', *, tag: Optional[str] = None) -> 'MetaInfo':
		metadata_json = plugin.get_repos_json('mcdreforged.plugin.json', tag=tag)
		metadata = Metadata(metadata_json)
		assert metadata.id == plugin.id, 'wrong plugin id in mcdreforged.plugin.json, expected {} but found {}'.format(plugin.id, metadata.id)
		meta_info = MetaInfo()
		meta_info.id = metadata.id
		meta_info.name = metadata.name
		meta_info.version = str(metadata.version)
		meta_info.repository = plugin.repository
		meta_info.link = metadata.link
		meta_info.authors = [author.name for author in plugin.authors]
		meta_info.dependencies = dict(map(
			lambda t: (str(t[0]), str(t[1])),
			metadata.dependencies.items()
		))
		meta_info.requirements = list(filter(
			lambda l: len(l) > 0, map(
				lambda l: l.split('#', 1)[0].strip(),
				plugin.get_repos_text('requirements.txt', default='', tag=tag).splitlines()
			)
		))
		if isinstance(metadata.description, str):
			meta_info.description = {DEFAULT_LANGUAGE: metadata.description}
		elif isinstance(metadata.description, dict):
			meta_info.description = metadata.description
		else:
			meta_info.description = {}
		return meta_info


class AssetInfo(Serializable):
	name: str
	size: int
	download_count: int
	created_at: str
	browser_download_url: str


class ReleaseInfo(Serializable):
	url: str
	name: str
	tag_name: str
	created_at: str
	assets: List[AssetInfo]
	description: str
	prerelease: bool
	parsed_version: str
	meta: Union[MetaInfo, str]

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

	def get_mcdr_assets(self) -> List[AssetInfo]:
		return [asset for asset in self.assets if asset.name.endswith('.mcdr') or asset.name.endswith('.pyz')]


class ReleasePage(Serializable):
	index: int = -1
	etag: str = ''
	release_tags: List[str]  # list of tags
	empty: bool

	class FetchResult(NamedTuple):
		page: 'ReleasePage'
		release_map: Dict[str, ReleaseInfo]

	@classmethod
	def fetch_page(cls, plugin: 'Plugin', page_index: int, old_etag: str) -> Optional['ReleasePage.FetchResult']:
		"""
		:return: None if page unchanged
		"""
		url = f'https://api.github.com/repos/{plugin.repos_path}/releases'
		resp, new_etag = utils.request_github_api(url, etag=old_etag, params={'page': page_index, 'per_page': constants.MAX_RELEASE_PER_PAGE})
		if resp is None:
			return None

		page = ReleasePage(index=page_index, etag=new_etag)
		page.release_tags = []
		release_map: Dict[str, ReleaseInfo] = {}  # tag name -> ReleaseInfo
		for item in resp:
			item['url'] = item['html_url']
			item['description'] = item['body'] or 'N/A'
			try:
				r_info = ReleaseInfo.deserialize(item)
			except Exception as e:
				print('Failed to deserialize fetched ReleaseInfo from {}: {}'.format(item, e))
				continue
			if not cls.check_release(plugin, r_info):
				continue
			r_info.meta = 'not fetched'
			release_map[r_info.tag_name] = r_info
			page.release_tags.append(r_info.tag_name)
		page.empty = len(resp) == 0
		return cls.FetchResult(page, release_map)

	@classmethod
	def check_release(cls, plugin: 'Plugin', r_info: ReleaseInfo) -> bool:
		if r_info.parse_version(plugin.id) is None:
			return False
		if r_info.prerelease:
			return False
		return len(r_info.get_mcdr_assets()) > 0


class SchemaVersionHolder(Serializable):
	schema_version: int


class ReleasePageCache(Serializable):
	NOTICE: str = 'Not public API, DO NOT use this file'
	release_pages: List[ReleasePage] = []

	@property
	def page_amount(self) -> int:
		return len(self.release_pages) - 1


class ReleaseSummary(Serializable):
	schema_version: int = None
	id: str = None
	latest_version: str = None
	releases: List[ReleaseInfo] = []

	def sanity_check(self, page_cache: ReleasePageCache):
		releases_tags: Set[str] = {release.tag_name for release in self.releases}
		page_cache_tags: Set[str] = set()
		for page in page_cache.release_pages:
			page_cache_tags.update(page.release_tags)
		assert releases_tags == page_cache_tags, 'release tag mismatch: ReleaseSummary tags {}, ReleasePageCache tags {}'.format(
			list(sorted(releases_tags)), list(sorted(page_cache_tags))
		)

	def update(self, plugin: 'Plugin'):
		assert plugin.release_page_cache is not None, 'updating ReleaseSummary with empty ReleasePageCache'
		self.schema_version = constants.RELEASE_INFO_SCHEMA_VERSION
		self.id = plugin.id

		self.__update_release_data(plugin)
		self.__update_release_meta(plugin)

	def __update_release_data(self, plugin: 'Plugin'):
		old_page_map: Dict[int, ReleasePage] = {page.index: page for page in plugin.release_page_cache.release_pages}  # page index -> page
		old_release_map: Dict[str, ReleaseInfo] = {release.tag_name: release for release in self.releases}  # tag name -> ReleaseInfo
		new_page_map: Dict[int, ReleasePage] = {}  # page index -> page
		new_release_map: Dict[str, ReleaseInfo] = {}  # tag name -> ReleaseInfo

		def fetch_page(idx_: int):
			if idx_ in old_page_map:
				old_etag = old_page_map[idx_].etag
			else:
				old_etag = ''
			return downloader_pool.submit(lambda: ReleasePage.fetch_page(plugin, idx_, old_etag))

		# pages of existing indexes are probably not empty
		# fetch them in batch
		futures = {}  # idx -> future
		for idx in old_page_map.keys():
			futures[idx] = fetch_page(idx)

		# GitHub: Only the first 10000 results are available.
		# 10000 results == 100 pages
		for i in range(100):
			idx = i + 1  # idx in [1, 100]
			if idx in futures:
				result = futures[idx].result()
			else:
				result = fetch_page(idx).result()
			if result is not None:  # page updated
				new_page_map[idx] = result.page
				new_release_map.update(result.release_map)
			else:  # page unchanged, use the old releases
				assert old_page_map[idx] is not None, 'unchanged page does not exist in page_map'
				new_page_map[idx] = old_page_map[idx]
				new_release_map.update({tag: old_release_map[tag] for tag in old_page_map[idx].release_tags})
			if new_page_map[idx].empty:  # not that many releases
				break

		release_pages = list(new_page_map.values())
		release_pages.sort(key=lambda p: p.index)
		plugin.release_page_cache.release_pages = release_pages

		self.releases = []
		for page in release_pages:
			for tag in page.release_tags:
				self.releases.append(new_release_map[tag])

		self.latest_version = self.releases[0].parsed_version if len(self.releases) > 0 else 'N/A'

	def __update_release_meta(self, plugin: 'Plugin'):
		old_release_meta: Dict[str, Union[MetaInfo, str]] = {}  # tag -> meta
		new_release_meta: Dict[str, Union[MetaInfo, str]] = {}  # tag -> meta
		for release in self.releases:
			old_release_meta[release.tag_name] = release.meta

		futures = []
		for tag in self.release_tags:
			if tag in old_release_meta and isinstance(old_release_meta[tag], MetaInfo):
				futures.append((tag, downloader_pool.submit(old_release_meta.get, tag)))
			else:
				futures.append((tag, downloader_pool.submit(MetaInfo.fetch, plugin, tag=tag)))

		for tag, future in futures:
			try:
				new_release_meta[tag] = future.result()
			except Exception as e:
				print('[Warn] failed to fetch release meta for tag {} for plugin {}: {}'.format(tag, plugin, e))
				reporter.record_warning(plugin.id, 'Failed to fetch release meta for tag {}'.format(tag), e)
				new_release_meta[tag] = str(e)

		for release in self.releases:
			release.meta = new_release_meta[release.tag_name]

	@property
	def release_tags(self) -> Iterable[str]:
		return map(lambda r: r.tag_name, self.releases)

	def get_latest_release(self) -> Optional[ReleaseInfo]:
		if len(self.releases) > 0:
			return self.releases[0]
		return None

	def get_total_downloads(self) -> int:
		total = 0
		for release in self.releases:
			for asset in release.get_mcdr_assets():
				total += asset.download_count
		return total


class PluginMetaSummary:
	plugin_amount: int
	plugins: Dict[str, MetaInfo]
	plugin_info: Dict[str, FormattedPluginInfo]


class AuthorSummary:
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.amount = 0
		self.authors: Dict[str, Author] = {}
		self.__author_source: Dict[str, str] = {}  # author name -> source plugin id

	def add_author(self, author: Author, plugin_id: str):
		existed = self.authors.get(author.name)
		if existed is not None and existed.link is not None:
			if author.link is not None and existed.link != author.link:
				reporter.record_warning(plugin_id, 'Inconsistent link of author: plugin {} says {}, but plugin {} says {}'.format(
					plugin_id, repr(author.link), self.__author_source.get(author.name, '?'), repr(existed.link)
				), None)
			return
		self.authors[author.name] = author
		self.__author_source[author.name] = plugin_id

	def finalize(self):
		self.authors = {key: self.authors[key] for key in sorted(self.authors.keys(), key=str.lower)}
		self.amount = len(self.authors)
