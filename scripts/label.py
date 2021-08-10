import json
from typing import List, Dict, Optional

import constants
from text import Text


class Label:
	def __init__(self, id: str, js: dict):
		self.id = id
		self.name: Text = Text(js['name'], js['name_cn'])

	def __str__(self):
		return str(self.name)

	def __eq__(self, other):
		return isinstance(other, type(self)) and self.id == other.id

	def __hash__(self):
		return hash(self.id)


class LabelSet:
	def __init__(self):
		with open(constants.LABEL_FILE, 'r') as file_handler:
			js: dict = json.load(file_handler)
		self.__labels: Dict[str, Label] = {}
		for key, value in js.items():
			self.__labels[key] = Label(key, value)

	def get_label_list(self) -> List[Label]:
		return list(self.__labels.values())

	def get_label(self, key: str) -> Optional[Label]:
		return self.__labels.get(key, None)


_label_set = LabelSet()


def get_label_set() -> LabelSet:
	return _label_set
