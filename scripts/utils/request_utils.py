import asyncio
import contextlib
import dataclasses
import functools
import json
import os
import ssl
from functools import cached_property
from typing import Tuple, Optional, Any, AsyncGenerator

import aiohttp
from multidict import CIMultiDictProxy
from typing_extensions import Self

from common import constants, log
from common.report import reporter


@dataclasses.dataclass(frozen=True)
class SimpleResponse:
	url: str
	status_code: int
	headers: CIMultiDictProxy[str]
	content: bytes

	@cached_property
	def text(self) -> str:
		return self.content.decode('utf8')

	def json(self) -> Any:
		return json.loads(self.content)


class RequestClientSessionHolder:
	def __init__(self):
		self.__sem = asyncio.Semaphore(constants.REQUEST_MAX_CONCURRENCY)
		self.__client: Optional[aiohttp.ClientSession] = None

	async def init(self):
		self.__client = aiohttp.ClientSession(trust_env=True)

	async def shutdown(self):
		if self.__client is not None:
			await self.__client.close()
			self.__client = None

	@contextlib.asynccontextmanager
	async def acquire(self) -> AsyncGenerator[aiohttp.ClientSession, Any]:
		if self.__client is None:
			await self.init()

		async with self.__sem:
			yield self.__client

	@classmethod
	@functools.lru_cache(None)
	def get(cls) -> Self:
		return cls()


async def request_get(url: str, *, headers: dict = None, params: dict = None, retries: int = 3) -> SimpleResponse:
	"""
	requests.get wrapper with retries for connection / ssl errors
	"""
	err = None
	for i in range(max(1, retries)):
		async with RequestClientSessionHolder.get().acquire() as client:
			if constants.DEBUG.REQUEST_GET:
				log.debug('    Requesting {}/{} url={} params={}'.format(i + 1, retries, url, params))
			try:
				# Sometimes SSL error might take a long time before the request failed,
				# so set a connect timeout to reduce the time wait
				connect_timeout = max(2, i * 10)  # 2, 10, 20, 30...
				if connect_timeout > 60:
					connect_timeout = None
				timeout = aiohttp.ClientTimeout(connect=connect_timeout)

				async with client.get(url, params=params, headers=headers, timeout=timeout) as response:
					rsp = SimpleResponse(
						url=str(response.url),
						status_code=response.status,
						headers=response.headers,
						content=await response.read(),
					)
					if constants.DEBUG.REQUEST_GET:
						log.debug('    Requested {}/{} url={} params={} status_code={}'.format(i + 1, retries, url, params, rsp.status_code))
					return rsp
			except (aiohttp.ClientError, ssl.SSLError) as e:
				log.warning('{}Request error {}/{} url={} params={} error=({}) {}'.format('    ' if constants.DEBUG.REQUEST_GET else '', i + 1, retries, url, params, type(e), e))
				err = e
	if err is not None:
		raise err from None
	raise AssertionError()


async def request_github_api(url: str, *, params: dict = None, etag: str = '', retries: int = 3) -> Tuple[Optional[Any], str]:
	"""
	Return None if etag doesn't change, in the other word, the response data doesn't change
	"""
	headers = {
		'If-None-Match': etag
	}
	if (api_token := os.environ.get('github_api_token', '')) != '':
		headers['Authorization'] = 'token {}'.format(api_token)
	response = await request_get(url, headers=headers, params=params, retries=retries)
	if response.status_code != 200 and response.status_code != 304:
		raise Exception('Un-expected status code {}: {}'.format(response.status_code, response.content))
	try:
		new_etag = response.headers['ETag']
	except KeyError:
		log.error('No ETag in response! url={}, params={} status_code={}, content={}'.format(url, params, response.status_code, response.content))
		raise
	try:
		remaining, limit = response.headers['X-RateLimit-Remaining'], response.headers['X-RateLimit-Limit']
	except KeyError as e:
		log.error('Get RateLimit headers from response failed: {}, header: {}'.format(e, response.headers))
	else:
		reporter.record_rate_limit(remaining, limit)
		if constants.DEBUG.SHOW_RATE_LIMIT:
			log.debug('\tRateLimit: {}/{}'.format(remaining, limit))
			log.debug('\tETag: {} -> {}, url={}, params={}'.format(etag, new_etag, url, params))

	# strange prefix. does not affect accuracy, but will randomly change from time to time
	# so yeets it here in advance
	if new_etag.startswith('W/'):
		new_etag = new_etag[2:]
	if response.status_code == 304:
		return None, new_etag
	return response.json(), new_etag
