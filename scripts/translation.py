import os
import threading
from contextlib import contextmanager
from typing import Dict

import constants
import utils

EN_US = 'en_us'
ZH_CN = 'zh_cn'
DEFAULT_LANGUAGE = EN_US
_TLS = threading.local()
LANGUAGES = [EN_US, ZH_CN]


def get_language() -> str:
	try:
		return _TLS.language
	except AttributeError:
		set_language(DEFAULT_LANGUAGE)
		return DEFAULT_LANGUAGE


def set_language(lang: str):
	_TLS.language = lang


@contextmanager
def with_language(lang: str):
	prev = get_language()
	set_language(lang)
	try:
		yield
	finally:
		set_language(prev)


_TRANSLATION_TYPE = Dict[str, str]
_TRANSLATION_COLLECTION_TYPE = Dict[str, _TRANSLATION_TYPE]

_TRANSLATION: _TRANSLATION_COLLECTION_TYPE = {}
for file_name in os.listdir(constants.TRANSLATION_FOLDER):
	file_path = os.path.join(constants.TRANSLATION_FOLDER, file_name)
	if os.path.isfile(file_path) and file_name.endswith('.json'):
		lang = utils.remove_suffix(file_name, '.json')
		_TRANSLATION[lang] = utils.load_json(file_path)


class Text:
	def __init__(self, key: str):
		self.__key = key

	def get(self) -> str:
		result = _TRANSLATION[get_language()].get(self.__key)
		if result is None:
			result = _TRANSLATION[DEFAULT_LANGUAGE].get(self.__key, self.__key)
		return result

	def __str__(self):
		return self.get()


class BundledText(Text):
	def __init__(self, mapping: _TRANSLATION_TYPE):
		super().__init__('')
		self.__mapping: _TRANSLATION_TYPE = mapping

	def get(self) -> str:
		result = self.__mapping.get(get_language())
		if result is None:
			result = self.__mapping.get(DEFAULT_LANGUAGE)
		return result
