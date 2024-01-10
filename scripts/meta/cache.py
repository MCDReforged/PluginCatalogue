import base64
import gzip
import json
from functools import cached_property
from typing import Dict

from meta.plugin import MetaInfo
from utils.serializer import Serializable


class ReleasePageResponse(Serializable):
	etag: str
	empty: bool
	data: str  # GitHub api response json (gz compressed + base64 encoded)

	@cached_property
	def __decoded_data(self) -> list:
		return json.loads(gzip.decompress(base64.b64decode(self.data)))

	def get_release_data_list(self) -> list[dict]:
		"""
		Returned the GitHub api response json for the /releases endpoint
		"""
		return self.__decoded_data

	@classmethod
	def from_response(cls, data: list, etag: str) -> 'ReleasePageResponse':
		page = cls()
		page.etag = etag
		page.empty = len(data) == 0
		page.releases = {}
		page.data = base64.b64encode(gzip.compress(json.dumps(data).encode('utf8'))).decode('utf8')
		return page


class RequestCache(Serializable):
	"""
	/<plugin_id>/.request_cache.json
	"""
	NOTICE: str = 'Not public API, DO NOT use this file'

	release_pages: Dict[str, ReleasePageResponse] = {}  # page -> ReleasePage
	asset_metas: Dict[str, MetaInfo] = {}  # asset id -> MetaInfo
