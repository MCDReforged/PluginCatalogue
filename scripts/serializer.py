from typing import TypeVar, Type

import mcdreforged.utils.serializer as mcdr_serializer

__all__ = [
	'Serializable'
]


Self = TypeVar('Self', bound='Serializable')


class Serializable(mcdr_serializer.Serializable):
	@classmethod
	def deserialize(cls: Type[Self], data: dict, **kwargs) -> Self:
		try:
			return super().deserialize(data, **kwargs)
		except Exception as e:
			import log
			log.error('Failed to deserialize to {} from data {}'.format(cls, data))
			raise e from None
