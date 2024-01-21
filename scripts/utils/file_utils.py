import gzip
import json
import os
from contextlib import contextmanager


@contextmanager
def open_for_read(file_path: str):
	"""
	ensure utf8
	"""
	with open(file_path, 'r', encoding='utf8') as file:
		yield file


@contextmanager
def open_for_write(file_path: str):
	"""
	Just like open() in 'w' mode, but create the directory automatically
	"""
	dir_path = os.path.dirname(file_path)
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	with open(file_path, 'w', encoding='utf8') as file:
		yield file


def load_json(file_path: str) -> dict:
	if os.path.isfile(file_path):
		with open_for_read(file_path) as file:
			return json.load(file)
	else:
		raise FileNotFoundError('File {} not found when loading json'.format(file_path))


def save_json(data: dict, file_path: str, *, compact: bool = False, with_gz: bool = False):
	if compact:
		s = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
	else:
		s = json.dumps(data, indent=2, ensure_ascii=False)

	with open_for_write(file_path) as f:
		f.write(s)
	if with_gz:
		with gzip.GzipFile(file_path + '.gz', 'wb', mtime=0) as zf:
			zf.write(s.encode('utf8'))
