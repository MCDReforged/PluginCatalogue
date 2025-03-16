import os
from typing import Optional, Dict

from pydantic import Field

from utils import date_utils
from utils.serializer import Serializable

REQUEST_META_DEFAULT_TTL = 20


def _get_github_action_id() -> Optional[int]:
	try:
		return int(os.environ['GITHUB_RUN_ID'])
	except (KeyError, ValueError):
		return None


class RequestMeta(Serializable):
	"""
	/<plugin_id>/.request_meta.json
	"""
	NOTICE: str = 'Not public API, DO NOT use this file'

	class Item(Serializable):
		created_at: str = Field(default_factory=date_utils.get_datetime_utc_now)
		created_by_github_action_id: Optional[int] = Field(default_factory=_get_github_action_id)

		ttl: int
		last_failure: Optional[str]

	introduction: Dict[str, Item] = Field(default_factory=dict)
	meta: Optional[Item] = None
	release: Optional[Item] = None
	repository: Optional[Item] = None
