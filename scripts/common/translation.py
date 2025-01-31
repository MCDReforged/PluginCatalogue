import contextvars
import os
from contextlib import contextmanager
from typing import Dict, Optional

from common import constants
from utils import file_utils, value_utils

EN_US = 'en_us'
ZH_CN = 'zh_cn'
DEFAULT_LANGUAGE = EN_US
_TLS_LANG = contextvars.ContextVar('language', default=DEFAULT_LANGUAGE)
LANGUAGES = [EN_US, ZH_CN]


def get_language() -> str:
	try:
		return _TLS_LANG.get()
	except AttributeError:
		set_language(DEFAULT_LANGUAGE)
		return DEFAULT_LANGUAGE


def set_language(lang: str):
	_TLS_LANG.set(lang)


@contextmanager
def with_language(lang: str):
	prev = get_language()
	set_language(lang)
	try:
		yield
	finally:
		set_language(prev)


def get_file_name(name: str) -> str:
	base, extension = name.rsplit('.', 1)
	split = base.rsplit('-', 1)
	if len(split) == 2 and split[1] in LANGUAGES:
		base = split[0]  # remove existed language suffix
	if get_language() == DEFAULT_LANGUAGE:
		return '{}.{}'.format(base, extension)
	else:
		return '{}-{}.{}'.format(base, get_language(), extension)


_TRANSLATION_TYPE = Dict[str, str]
_TRANSLATION_COLLECTION_TYPE = Dict[str, _TRANSLATION_TYPE]

_TRANSLATION: _TRANSLATION_COLLECTION_TYPE = {}

def __init_translation():
	for file_name in os.listdir(constants.TRANSLATION_FOLDER):
		file_path = constants.TRANSLATION_FOLDER / file_name
		if file_path.is_file() and file_name.endswith('.json'):
			lang = value_utils.remove_suffix(file_name, '.json')
			_TRANSLATION[lang] = file_utils.load_json(file_path)


__init_translation()


class Text:
	def __init__(self, key: str):
		self.__key = key

	def _key_not_found(self):
		raise KeyError('Unknown translation key {}'.format(self.__key))

	def get(self) -> Optional[str]:
		result = _TRANSLATION[get_language()].get(self.__key)
		if result is None:
			result = _TRANSLATION[DEFAULT_LANGUAGE].get(self.__key)
		return result

	def can_translate(self) -> bool:
		return self.get() is not None

	def __str__(self):
		rv = self.get()
		if rv is None:
			self._key_not_found()
		return rv

	def __repr__(self):
		return 'Text[key={}]'.format(self.__key)


class LiteralText(Text):
	def __init__(self, text: str):
		super().__init__('')
		self.__text = text

	def get(self) -> Optional[str]:
		return self.__text


class BundledText(Text):
	def __init__(self, mapping: _TRANSLATION_TYPE, default: Optional[str] = None):
		super().__init__('')
		self.__default = default
		self.__mapping: _TRANSLATION_TYPE = mapping

	def get_mapping(self) -> _TRANSLATION_TYPE:
		return self.__mapping.copy()

	def _key_not_found(self):
		raise KeyError('Unknown translation key in {}'.format(repr(self)))

	def __repr__(self):
		return 'BundledText[default={},mapping={}]'.format(self.__default, self.__mapping)

	def get(self) -> Optional[str]:
		result = self.__mapping.get(get_language())
		if result is None:
			result = self.__mapping.get(DEFAULT_LANGUAGE)
		if result is None:
			any(result := i for i in self.__mapping.values())
		if result is None:
			result = self.__default
		return result
