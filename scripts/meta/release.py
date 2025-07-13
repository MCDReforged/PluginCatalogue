import contextlib
from typing import List, Optional, Dict, TYPE_CHECKING

from mcdreforged.plugin.meta.version import Version
from pydantic import Field

from common import constants, log
from common.report import reporter
from meta.plugin import MetaInfo
from utils import value_utils
from utils.serializer import Serializable

if TYPE_CHECKING:
	from plugin.plugin import Plugin
	from plugin.cache import PluginRequestCacheManager
	from meta.cache import ReleasePageResponse, AssetData


class _GitHubAssetJson(Serializable):
	id: int  # GitHub asset ID
	name: str
	size: int
	download_count: int
	created_at: str
	browser_download_url: str


class AssetInfo(_GitHubAssetJson):
	hash_md5: str
	hash_sha256: str


class _GitHubReleaseJson(Serializable):
	html_url: str
	name: str
	tag_name: str
	created_at: str
	body: Optional[str]
	prerelease: bool
	assets: List[_GitHubAssetJson]


class _InvalidReleaseError(Exception):
	pass


class ReleaseInfo(Serializable):
	url: str
	name: str
	tag_name: str
	created_at: str
	description: Optional[str]
	prerelease: bool

	asset: AssetInfo
	meta: MetaInfo

	@classmethod
	async def create_from(cls, plugin: 'Plugin', cache_manager: 'PluginRequestCacheManager', js: _GitHubReleaseJson) -> 'ReleaseInfo':
		if js.prerelease:
			raise _InvalidReleaseError('pre-release')

		tag_version = cls.__parse_version(js.tag_name, plugin.id)
		if tag_version is None:
			raise _InvalidReleaseError('tag {!r} is not a valid version for current plugin'.format(js.tag_name))
		t_ver = Version(tag_version, allow_wildcard=False)

		asset_info: AssetInfo
		meta_info: MetaInfo

		for asset in js.assets:
			if asset.name.endswith('.mcdr') or asset.name.endswith('.pyz'):
				data: AssetData = await cache_manager.fetch_asset_data(asset.id, asset.browser_download_url)
				if data.size != asset.size:
					# it should not happen, but just in case
					raise AssertionError('fetched data size {} not equals to asset size {}'.format(data.size, asset.size))
				meta_info = data.meta
				asset_info = AssetInfo(
					id=asset.id,
					name=asset.name,
					size=asset.size,
					download_count=asset.download_count,
					created_at=asset.created_at,
					browser_download_url=asset.browser_download_url,
					hash_md5=data.hash_md5,
					hash_sha256=data.hash_sha256,
				)
				break
		else:
			raise _InvalidReleaseError('no valid asset')

		info = cls(
			url=js.html_url,
			name=js.name,
			tag_name=js.tag_name,
			created_at=js.created_at,
			description=js.body,
			prerelease=js.prerelease,
			asset=asset_info,
			meta=meta_info,
		)

		if info.meta.id != plugin.id:
			log.warning('({}) Bad plugin id in tag {!r} asset {!r}, found {!r}'.format(plugin.id, js.tag_name, info.asset.name, info.meta.id))
			reporter.record_warning(plugin.id, 'Bad plugin id in tag {!r} asset {!r}, found {!r}'.format(js.tag_name, info.asset.name, info.meta.id), None)
			raise _InvalidReleaseError('bad asset plugin id')

		meta_version = info.meta.version
		try:
			m_ver = Version(meta_version, allow_wildcard=False)
		except ValueError as e:
			log.warning('({}) Bad meta version {!r} for tag {!r}: {}'.format(plugin.id, meta_version, info.tag_name, e))
			reporter.record_warning(plugin.id, 'Bad meta version {!r} for tag {!r}'.format(meta_version, info.tag_name), e)
			raise _InvalidReleaseError('bad meta version')

		t_ver_seq = '.'.join(map(str, t_ver.component))
		m_ver_seq = '.'.join(map(str, m_ver.component))
		if not m_ver_seq.startswith(t_ver_seq):
			log.warning('({}) Tag {!r} version {!r} does not match meta version {!r}'.format(plugin.id, js.tag_name, tag_version, meta_version))
			reporter.record_warning(plugin.id, 'Tag {!r} version {!r} does not match meta version {!r}'.format(js.tag_name, tag_version, meta_version), None)
			raise _InvalidReleaseError('version mismatched')
		elif m_ver != t_ver:
			# Example cases:
			# - ipanel_mcdreforged: tag version '2.1', meta version '2.1.7.29'
			# - chatbridgereforged_mc: tag version '0.2.7', meta version '0.2.7-dev032'
			log.warning('({}) Mismatched but acceptable tag/meta version: tag version {!r}, meta version {!r}'.format(plugin.id, tag_version, meta_version))

		return info

	@classmethod
	def __parse_version(cls, tag_name: str, plugin_id: str) -> Optional[str]:
		# Possible tag names
		#   plugin_id-v1.2.3
		#   plugin_id-1.2.3
		#   v1.2.3
		#   1.2.3

		def test_and_return(version_str: str) -> Optional[str]:
			try:
				Version(version_str, allow_wildcard=False)
			except ValueError:
				return None
			else:
				return version_str

		version = tag_name
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


class ReleaseSummary(Serializable):
	"""
	/<plugin_id>/release.json
	"""
	schema_version: int
	id: str
	latest_version: Optional[str] = None
	latest_version_index: Optional[int] = None
	releases: List[ReleaseInfo] = Field(default_factory=list)

	__latest_release: Optional[ReleaseInfo] = None

	@classmethod
	async def create_for(cls, plugin: 'Plugin', cache_manager: 'PluginRequestCacheManager') -> 'ReleaseSummary':
		rs = cls(
			schema_version=constants.RELEASE_INFO_SCHEMA_VERSION,
			id=plugin.id,
		)

		page_map: Dict[int, 'ReleasePageResponse'] = {}  # page index -> page

		# GitHub: Only the first 10000 results are available.
		# 10000 results == 100 pages
		for i in range(100):
			i += 1  # page index starts at 1
			log.info('({}) Fetching release page {}'.format(plugin.id, i))
			page = await cache_manager.fetch_release_page(page=i, per_page=constants.MAX_RELEASE_PER_PAGE)
			page_map[i] = page
			if page.empty:
				break

		releases: Dict[str, ReleaseInfo] = {}
		for i, page in value_utils.sort_dict(page_map).items():
			log.info('({}) Checking release page {} with {} releases'.format(plugin.id, i, len(page.get_release_data_list())))
			for item in page.get_release_data_list():
				try:
					data = _GitHubReleaseJson.deserialize(item)
				except Exception as e:
					log.error('Failed to deserialize fetched ReleaseInfo from {}: {}'.format(item, e))
					raise
				with contextlib.suppress(_InvalidReleaseError):
					r_info = await ReleaseInfo.create_from(plugin, cache_manager, data)
					releases[r_info.tag_name] = r_info

		rs.releases = list(releases.values())
		latest_version: Optional[Version] = None
		latest_version_index: Optional[int] = None
		for i, r_info in enumerate(rs.releases):
			version = Version(r_info.meta.version)
			if latest_version is None or version > latest_version:
				latest_version = version
				latest_version_index = i
		if latest_version_index is not None and latest_version is not None:
			r_info = rs.releases[latest_version_index]
			rs.latest_version = r_info.meta.version
			rs.latest_version_index = latest_version_index
			rs.__latest_release = r_info
		else:
			rs.latest_version = None
			rs.latest_version_index = None
			rs.__latest_release = None
		return rs

	def get_latest_release(self) -> Optional[ReleaseInfo]:
		return self.__latest_release

	def get_total_downloads(self) -> int:
		total = 0
		for release in self.releases:
			total += release.asset.download_count
		return total
