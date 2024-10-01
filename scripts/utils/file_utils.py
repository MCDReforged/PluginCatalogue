import gzip
import json
import lzma
from contextlib import contextmanager
from pathlib import Path
from typing import Union


@contextmanager
def open_for_read(file_path: Union[str, Path]):
	"""
	ensure utf8
	"""
	with open(file_path, 'r', encoding='utf8') as file:
		yield file


@contextmanager
def open_for_write(file_path: Union[str, Path]):
	"""
	Just like open() in 'w' mode, but create the directory automatically
	"""
	file_path = Path(file_path)
	file_path.parent.mkdir(parents=True, exist_ok=True)
	with open(file_path, 'w', encoding='utf8') as file:
		yield file


def load_json(file_path: Union[str, Path]) -> dict:
	file_path = Path(file_path)
	if file_path.is_file():
		with open_for_read(file_path) as file:
			return json.load(file)
	else:
		raise FileNotFoundError('File {} not found when loading json'.format(file_path))


def save_json(data: dict, file_path: Union[str, Path], *, compact: bool = False, with_gz: bool = False, with_xz: bool = False):
	file_path = Path(file_path)
	if compact:
		s = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
	else:
		s = json.dumps(data, indent=2, ensure_ascii=False)

	with open_for_write(file_path) as f:
		f.write(s)
	if with_gz:
		with gzip.GzipFile(file_path.parent / (file_path.name + '.gz'), 'wb', mtime=0) as zf:
			zf.write(s.encode('utf8'))
	if with_xz:
		with lzma.open(file_path.parent / (file_path.name + '.xz'), 'wb', format=lzma.FORMAT_XZ) as xf:
			xf.write(s.encode('utf8'))
