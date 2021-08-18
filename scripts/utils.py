import json
import os
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
		return {}


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


def save_json(data: dict, file_path: str):
	with write_file(file_path) as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


def request_github_api(url: str, *, etag: str = '') -> Tuple[Optional[Any], str]:
	"""
	Return None if etag doesnt change, in the other word, the response data doesnt change
	"""
	headers = {
		'If-None-Match': etag
	}
	if 'github_api_token' in os.environ:
		headers['Authorization'] = 'token {}'.format(os.environ['github_api_token'])
	response = requests.get(url, proxies=constants.PROXIES, headers=headers)
	new_etag = response.headers['ETag']
	# print('RateLimit: {}/{}'.format(response.headers['X-RateLimit-Remaining'], response.headers['X-RateLimit-Limit']))
	# print('ETag: {} -> {}'.format(etag, new_etag))
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

