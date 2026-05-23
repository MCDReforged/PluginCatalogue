from typing import List, Optional

from pydantic import Field

from utils.serializer import Serializable


class PluginUpdateReportEntry(Serializable):
	message: str
	error_type: Optional[str] = None
	error_message: Optional[str] = None


class PluginUpdateReport(Serializable):
	"""
	/<plugin_id>/update_report.json
	"""
	failures: List[PluginUpdateReportEntry] = Field(default_factory=list)
	warnings: List[PluginUpdateReportEntry] = Field(default_factory=list)
