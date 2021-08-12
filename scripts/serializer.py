from mcdreforged.utils.serializer import Serializable as mcdr_Serializable


class Serializable(mcdr_Serializable):
	@classmethod
	def deserialize(cls, data: dict, **kwargs):
		try:
			return super().deserialize(data, **kwargs)
		except Exception as e:
			print('Failed to deserialize to {} from data {}'.format(cls, data))
			raise e from None
