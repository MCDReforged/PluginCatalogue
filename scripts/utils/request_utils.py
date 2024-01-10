import asyncio
import dataclasses
import json
import os
import ssl
from functools import cached_property
from typing import Tuple, Optional, Any

import aiohttp
from multidict import CIMultiDictProxy

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


__request_sem = asyncio.Semaphore(constants.REQUEST_MAX_CONCURRENCY)


async def request_get(url: str, *, headers: dict = None, params: dict = None, retries: int = 3) -> SimpleResponse:
	"""
	requests.get wrapper with retries for connection / ssl errors
	"""
	err = None
	for i in range(max(1, retries)):
		async with __request_sem:
			if constants.DEBUG.REQUEST_GET:
				log.debug('\tRequesting {}/{} url={} params={}'.format(i + 1, retries, url, params))
			try:
				async with aiohttp.ClientSession() as session:
					async with session.get(url, params=params, headers=headers) as response:
						return SimpleResponse(
							url=str(response.url),
							status_code=response.status,
							headers=response.headers,
							content=await response.read(),
						)
			except (aiohttp.ClientError, ssl.SSLError) as e:
				err = e
	if err is not None:
		raise err from None


async def request_github_api(url: str, *, params: dict = None, etag: str = '', retries: int = 3) -> Tuple[Optional[Any], str]:
	"""
	Return None if etag doesn't change, in the other word, the response data doesn't change
	"""
	headers = {
		'If-None-Match': etag
	}
	if 'github_api_token' in os.environ:
		headers['Authorization'] = 'token {}'.format(os.environ['github_api_token'])
	response = await request_get(url, headers=headers, params=params, retries=retries)
	try:
		new_etag = response.headers['ETag']
	except KeyError:
		log.error('No ETag in response! url={}, params={} status_code={}, content={}'.format(url, params, response.status_code, response.content))
		raise
	remaining, limit = response.headers['X-RateLimit-Remaining'], response.headers['X-RateLimit-Limit']
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
	if response.status_code != 200:
		raise Exception('Un-expected status code {}: {}'.format(response.status_code, response.content))
	return response.json(), new_etag
