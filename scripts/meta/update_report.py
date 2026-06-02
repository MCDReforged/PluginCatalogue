from typing import List, Optional

from pydantic import Field

from utils.serializer import Serializable


class PluginUpdateReportEntry(Serializable):
	message: str
	error_type: Optional[str] = None
	error_message: Optional[str] = None

	def format(self) -> str:
		if self.error_type is None:
			return self.message
		return '{}: ({}) {}'.format(self.message, self.error_type, self.error_message)

	def __str__(self):
		return self.format()


class PluginUpdateReport(Serializable):
	"""
	/<plugin_id>/update_report.json
	"""
	failures: List[PluginUpdateReportEntry] = Field(default_factory=list)
	warnings: List[PluginUpdateReportEntry] = Field(default_factory=list)
