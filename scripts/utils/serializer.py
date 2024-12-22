from pydantic import BaseModel, ValidationError
from typing_extensions import Self

__all__ = [
	'Serializable'
]


class Serializable(BaseModel):
	def serialize(self) -> dict:
		return self.model_dump(mode='json')

	@classmethod
	def deserialize(cls, data: dict) -> Self:
		try:
			return cls.model_validate(data, strict=True)
		except ValidationError as e:
			from common import log
			log.error('Failed to deserialize to {} from data {}'.format(cls, data))
			raise e from None
