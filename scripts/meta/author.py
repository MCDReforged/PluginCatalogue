from typing import Optional, Dict

from common.report import reporter
from utils import value_utils
from utils.serializer import Serializable


class Author(Serializable):
	name: str = ''
	link: Optional[str] = None

	def to_markdown(self) -> str:
		if self.link is None:
			return self.name
		return '[{}]({})'.format(self.name, self.link)


class AuthorSummary(Serializable):
	"""
	/authors.json
	"""
	amount: int = 0
	authors: Dict[str, Author] = {}

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.__author_source: Dict[str, str] = {}  # author name -> source plugin id

	def add_author(self, author: Author, plugin_id: str):
		existed = self.authors.get(author.name)
		if existed is not None and existed.link is not None:
			if author.link is not None and existed.link != author.link:
				reporter.record_warning(plugin_id, 'Inconsistent link of author: plugin {} says {}, but plugin {} says {}'.format(
					plugin_id, repr(author.link), self.__author_source.get(author.name, '?'), repr(existed.link)
				), None)
			return
		self.authors[author.name] = author
		self.__author_source[author.name] = plugin_id

	def finalize(self):
		self.authors = value_utils.sort_dict(self.authors)
		self.amount = len(self.authors)

