from typing import List, Union, Optional, NamedTuple, Dict, Set, Iterable

from mcdreforged.plugin.meta.version import Version

from common import constants, log
from common.report import reporter
from meta.plugin import MetaInfo
from plugin.plugin import Plugin
from utils import value_utils, request_utils
from utils.serializer import Serializable
from utils.thread_pools import downloader_pool


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
			version = value_utils.remove_prefix(version, plugin_id + '-')
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
		url = f'{plugin.repos.api_root}/releases'
		resp, new_etag = request_utils.request_github_api(url, etag=old_etag, params={'page': page_index, 'per_page': constants.MAX_RELEASE_PER_PAGE})
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
				log.error('Failed to deserialize fetched ReleaseInfo from {}: {}'.format(item, e))
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


class ReleasePageCache(Serializable):
	"""
	/<plugin_id>/.release_page_cache.json
	"""
	NOTICE: str = 'Not public API, DO NOT use this file'
	release_pages: List[ReleasePage] = []

	@property
	def page_amount(self) -> int:
		return len(self.release_pages) - 1


class ReleaseSummary(Serializable):
	"""
	/<plugin_id>/release.json
	"""
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
				log.warning('Failed to fetch release meta for tag {} for plugin {}: {}'.format(tag, plugin, e))
				reporter.record_warning(plugin.id, 'Failed to fetch release meta for tag {}'.format(tag), e)
				new_release_meta[tag] = str(e)

		for release in self.releases:
			meta = new_release_meta[release.tag_name]
			if isinstance(meta, str):
				release.meta = meta
				continue

			r_ver = Version(release.parsed_version, allow_wildcard=False)
			try:
				m_ver = Version(meta.version, allow_wildcard=False)
			except ValueError as e:
				log.warning('Bad meta version {} for tag {} for plugin {}: {}'.format(repr(meta.version), release.tag_name, plugin, e))
				reporter.record_warning(plugin.id, 'Bad meta version {} for tag {}'.format(repr(meta.version), release.tag_name), e)
				release.meta = 'bad meta version {}: {}'.format(repr(meta.version), e)
				continue

			m_ver_seq = '.'.join(map(str, m_ver.component))
			r_ver_seq = '.'.join(map(str, r_ver.component))
			if not m_ver_seq.startswith(r_ver_seq):
				what = 'release version {}, meta version {}'.format(release.parsed_version, meta.version)
				log.warning('Plugin version mismatched for tag {} for plugin {}: {}'.format(release.tag_name, plugin, what))
				reporter.record_warning(plugin.id, 'Plugin version mismatched for tag {}: {}'.format(release.tag_name, what), None)
			else:
				release.meta = meta

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
