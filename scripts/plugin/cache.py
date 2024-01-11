import json
import zipfile
from io import BytesIO
from typing import TYPE_CHECKING, Set

from common import constants, log
from common.report import reporter
from meta.cache import RequestCache, ReleasePageResponse, RepositoryResponse
from meta.plugin import MetaInfo
from utils import request_utils, file_utils

if TYPE_CHECKING:
	from plugin.plugin import Plugin


class PluginRequestCacheManager:
	def __init__(self, plugin: 'Plugin', cache_file_path: str):
		self.plugin = plugin
		self.cache_file_path = cache_file_path

		self.__cache = RequestCache()
		self.__used_release_page: Set[str] = set()
		self.__used_asset_meta: Set[str] = set()

	def load(self):
		try:
			self.__cache = RequestCache.deserialize(file_utils.load_json(self.cache_file_path))
		except FileNotFoundError:
			pass
		except Exception as e:
			log.warning('Failed to deserialized existed release_page_cache for plugin {}: {} {}'.format(self, type(e), e))
			reporter.record_warning(self.plugin.id, 'Failed to deserialized existed request cache', e)
		else:
			# remove invalid meta cache
			for asset_id in list(self.__cache.asset_metas.keys()):
				if self.__cache.asset_metas[asset_id].schema_version != constants.META_INFO_SCHEMA_VERSION:
					self.__cache.asset_metas.pop(asset_id)

	def dump_for_save(self) -> dict:
		cache = self.__cache.copy(deep=True)
		for page in list(cache.release_pages.keys()):
			if page not in self.__used_release_page:
				cache.release_pages.pop(page)
		for asset_id in list(cache.asset_metas.keys()):
			if asset_id not in self.__used_asset_meta:
				cache.asset_metas.pop(asset_id)
		return cache.serialize()

	async def fetch_release_page(self, page: int, per_page: int) -> ReleasePageResponse:
		page = str(page)

		url = f'{self.plugin.repos.api_root}/releases'
		if page in self.__cache.release_pages:
			old_etag = self.__cache.release_pages[page].etag
		else:
			old_etag = ''
		rsp, new_etag = await request_utils.request_github_api(url, etag=old_etag, params={'page': page, 'per_page': per_page})

		if rsp is not None:  # etag changed
			log.info('ETag changed for GitHub API {!r}: {!r} -> {!r}'.format(url, old_etag, new_etag))
			self.__cache.release_pages[page] = ReleasePageResponse.from_response(rsp, new_etag)
		self.__used_release_page.add(page)
		return self.__cache.release_pages[page]

	async def fetch_asset_meta(self, asset_id: int, download_url: str) -> MetaInfo:
		asset_id = str(asset_id)

		if asset_id not in self.__cache.asset_metas:
			log.info('Downloading asset {} from {!r} for inspection'.format(asset_id, download_url))
			rsp = await request_utils.request_get(download_url)
			if rsp.status_code != 200:
				raise Exception('download asset from {} failed: {} {}'.format(download_url, rsp.status_code, rsp.content))

			with zipfile.ZipFile(BytesIO(rsp.content), 'r') as f:
				meta_buf = f.read('mcdreforged.plugin.json')
				try:
					req_buf = f.read('requirements.txt')
				except KeyError:
					req_buf = b''

			self.__cache.asset_metas[asset_id] = MetaInfo.of(json.loads(meta_buf), req_buf.decode('utf8'))

		self.__used_asset_meta.add(asset_id)
		return self.__cache.asset_metas[asset_id]

	async def fetch_repository_info(self) -> RepositoryResponse:
		url = f'https://api.github.com/repos/{self.plugin.repos.repos_pair}'
		if self.__cache.repos_info is not None:
			old_etag = self.__cache.repos_info.etag
		else:
			old_etag = ''
		rsp, new_etag = await request_utils.request_github_api(url, etag=old_etag)

		if rsp is not None:  # etag changed
			log.info('ETag changed for GitHub API {!r}: {!r} -> {!r}'.format(url, old_etag, new_etag))
			self.__cache.repos_info = RepositoryResponse.from_response(rsp, new_etag)
		return self.__cache.repos_info
