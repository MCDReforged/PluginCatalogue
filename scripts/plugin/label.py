from typing import List, Dict, Optional, Set

from common import constants
from utils import utils
from common.translation import Text


class Label(Text):
	def __init__(self, id: str):
		super().__init__('label.{}'.format(id))
		self.id = id

	def __repr__(self):
		return 'Label[id={}]'.format(self.id)


class LabelSet(Set[Label]):
	def __init__(self):
		super().__init__()
		self.__labels: Dict[str, Label] = {}
		for label_id in utils.load_json(constants.LABEL_FILE):
			self.__labels[label_id] = Label(label_id)

	def get_label_list(self) -> List[Label]:
		return list(self.__labels.values())

	def get_label(self, key: str) -> Optional[Label]:
		return self.__labels.get(key)


_label_set = LabelSet()


def get_label_set() -> LabelSet:
	return _label_set
