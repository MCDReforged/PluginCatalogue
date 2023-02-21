import json
import os
import ssl
from contextlib import contextmanager
from typing import Optional, Any, Tuple

import requests

import constants


def remove_prefix(text: str, prefix: str) -> str:
	pos = text.find(prefix)
	return text[pos + len(prefix):] if pos >= 0 else text


def remove_suffix(text: str, suffix: str) -> str:
	pos = text.rfind(suffix)
	return text[:pos] if pos >= 0 else text


def format_markdown(text: str) -> str:
	for c in ('\\', '<', '>'):
		text = text.replace(c, '\\' + c)
	return text


def load_json(file_path: str) -> dict:
	if os.path.isfile(file_path):
		with open(file_path, encoding='utf8') as file:
			return json.load(file)
	else:
		raise FileNotFoundError('File {} not found when loading json'.format(file_path))


@contextmanager
def read_file(file_path: str):
	"""
	ensure utf8
	"""
	with open(file_path, 'r', encoding='utf8') as file:
		yield file


@contextmanager
def write_file(file_path: str):
	"""
	Just like open() in 'w' mode, but create the directory automatically
	"""
	dir_path = os.path.dirname(file_path)
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	with open(file_path, 'w', encoding='utf8') as file:
		yield file


def save_json(data: dict, file_path: str, *, compact: bool = False):
	with write_file(file_path) as file:
		if compact:
			json.dump(data, file, ensure_ascii=False, separators=(',', ':'))
		else:
			json.dump(data, file, indent=2, ensure_ascii=False)


def request_get(url: str, *, headers: dict = None, params: dict = None, retries: int = 3) -> requests.Response:
	"""
	requests.get wrapper with retries for connection / ssl errors and token in header
	"""
	if headers is None:
		headers = {}
	if params is None:
		params = {}
	if 'github_api_token' in os.environ:
		headers['Authorization'] = 'token {}'.format(os.environ['github_api_token'])
	err = None
	for i in range(max(1, retries)):
		try:
			return requests.get(url, params=params, proxies=constants.PROXIES, headers=headers)
		except (requests.exceptions.ConnectionError, ssl.SSLError) as e:
			err = e
	if err is not None:
		raise err from None


def request_github_api(url: str, *, params: dict = None, etag: str = '', retries: int = 3) -> Tuple[Optional[Any], str]:
	"""
	Return None if etag doesn't change, in the other word, the response data doesn't change
	"""
	headers = {
		'If-None-Match': etag
	}
	response = request_get(url, headers=headers, params=params, retries=retries)
	try:
		new_etag = response.headers['ETag']
	except KeyError:
		print('No ETag in response! url={}, params={} status_code={}, content={}'.format(url, params, response.status_code, response.content))
		raise
	if constants.DEBUG.SHOW_RATE_LIMIT:
		print('\tRateLimit: {}/{}'.format(response.headers['X-RateLimit-Remaining'], response.headers['X-RateLimit-Limit']))
		print('ETag: {} -> {}, url={}, params={}'.format(etag, new_etag, url, params))

	# strange prefix. does not affect accuracy, but will randomly change from time to time
	# so yeets it here in advance
	if new_etag.startswith('W/'):
		new_etag = new_etag[2:]
	if response.status_code == 304:
		return None, new_etag
	if response.status_code != 200:
		raise Exception('Un-expected status code {}: {}'.format(response.status_code, response.content))
	return response.json(), new_etag


def pretty_file_size(size: int) -> str:
	for c in ('B', 'KB', 'MB', 'GB', 'TB'):
		unit = c
		if size < 2 ** 10:
			break
		size /= 2 ** 10
	return str(round(size, 2)) + unit

