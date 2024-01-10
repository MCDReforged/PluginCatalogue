import base64
import gzip
import json
from functools import cached_property
from typing import Dict, Union, Optional

from meta.plugin import MetaInfo
from utils.serializer import Serializable

_Json = Union[dict, list]


class _GitHubApiResponseBase(Serializable):
	etag: str
	data: str  # GitHub api response json (gz compressed + base64 encoded)

	@cached_property
	def __decoded_data(self) -> _Json:
		b64_buf = base64.b64decode(self.data.encode('utf8'))
		return json.loads(gzip.decompress(b64_buf))

	def get_json(self) -> _Json:
		"""
		Returned the GitHub api response json
		"""
		return self.__decoded_data

	@classmethod
	def encode_json(cls, json_obj: _Json) -> str:
		buf = gzip.compress(json.dumps(json_obj).encode('utf8'))
		return base64.b64encode(buf).decode('utf8')

	def set_encode_data(self, json_obj: _Json):
		self.data = self.encode_json(json_obj)


class ReleasePageResponse(_GitHubApiResponseBase):
	empty: bool

	def get_release_data_list(self) -> list[dict]:
		"""
		Returned the GitHub api response json for the /releases endpoint
		"""
		return super().get_json()

	@classmethod
	def from_response(cls, data: list, etag: str) -> 'ReleasePageResponse':
		page = cls()
		page.etag = etag
		page.empty = len(data) == 0
		page.releases = {}
		page.set_encode_data(data)
		return page


class RepositoryResponse(_GitHubApiResponseBase):
	@classmethod
	def from_response(cls, data: list, etag: str) -> 'RepositoryResponse':
		return cls(etag=etag, data=cls.encode_json(data))


class RequestCache(Serializable):
	"""
	/<plugin_id>/.request_cache.json
	"""
	NOTICE: str = 'Not public API, DO NOT use this file'

	release_pages: Dict[str, ReleasePageResponse] = {}  # page -> GitHub API response
	asset_metas: Dict[str, MetaInfo] = {}  # asset id -> MetaInfo
	repos_info: Optional[RepositoryResponse] = None  # GitHub API response
