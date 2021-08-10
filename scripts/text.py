from contextlib import contextmanager


class Text:
	EN = 'en'
	CN = 'CN'
	__LANGUAGE = EN

	@classmethod
	@contextmanager
	def with_language(cls, lang: str):
		prev = cls.__LANGUAGE
		cls.set_language(lang)
		try:
			yield
		finally:
			cls.set_language(prev)

	@classmethod
	def set_language(cls, lang: str):
		cls.__LANGUAGE = lang

	def __init__(self, text: str, text_cn: str = None):
		self.text = text
		self.text_cn = text_cn

	def en(self) -> str:
		return self.text

	def cn(self) -> str:
		if self.text_cn is not None:
			return self.text_cn
		return self.en()

	def get(self) -> str:
		if self.__LANGUAGE == self.EN:
			return self.en()
		elif self.__LANGUAGE == self.CN:
			return self.cn()
		return self.en()

	def __str__(self):
		return self.get()
