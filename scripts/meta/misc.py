from utils.serializer import Serializable


class SchemaVersionHolder(Serializable):
	schema_version: int
