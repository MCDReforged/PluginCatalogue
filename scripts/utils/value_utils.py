from typing import TypeVar, Dict, List, Any, Union, Type, Tuple

_T = TypeVar('_T')
_K = TypeVar('_K')
_V = TypeVar('_V')


def remove_prefix(text: str, prefix: str) -> str:
	pos = text.find(prefix)
	return text[pos + len(prefix):] if pos >= 0 else text


def remove_suffix(text: str, suffix: str) -> str:
	pos = text.rfind(suffix)
	return text[:pos] if pos >= 0 else text


def sort_dict(d: Dict[_K, _V]) -> Dict[_K, _V]:
	def key_extractor(x: _K):
		if isinstance(x, str):
			return x.lower(), x

	keys: List[_K] = list(d.keys())
	return {k: d[k] for k in sorted(keys, key=key_extractor)}


def pretty_file_size(size: int) -> str:
	for c in ('B', 'KB', 'MB', 'GB', 'TB'):
		unit = c
		if size < 2 ** 10:
			break
		size /= 2 ** 10
	return str(round(size, 2)) + unit


def ensure_type(value: Any, clazz: Union[Type[_T], Tuple[Type[_T], ...]]) -> _T:
	if isinstance(clazz, type):
		clazz = (clazz,)
	if not isinstance(value, clazz):
		raise AssertionError('expected type {}, found type {}'.format(clazz, value))
	return value
