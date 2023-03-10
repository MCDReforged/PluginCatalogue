from typing import TypeVar, Type

import mcdreforged.utils.serializer as mcdr_serializer

__all__ = [
	'serialize', 'Serializable'
]


Self = TypeVar('Self', bound='Serializable')


serialize = mcdr_serializer.serialize


class Serializable(mcdr_serializer.Serializable):
	@classmethod
	def deserialize(cls: Type[Self], data: dict, **kwargs) -> Self:
		try:
			return super().deserialize(data, **kwargs)
		except Exception as e:
			print('Failed to deserialize to {} from data {}'.format(cls, data))
			raise e from None

	def copy(self: Type[Self]) -> Self:
		return self.deserialize(self.serialize())
