from typing import TypeVar, Type

from mcdreforged.utils.serializer import Serializable as mcdr_Serializable

Self = TypeVar('Self', bound='Serializable')


class Serializable(mcdr_Serializable):
	@classmethod
	def deserialize(cls: Type[Self], data: dict, **kwargs) -> Self:
		try:
			return super().deserialize(data, **kwargs)
		except Exception as e:
			print('Failed to deserialize to {} from data {}'.format(cls, data))
			raise e from None
