import collections
import os
import sys
import time
from threading import Lock
from typing import Dict, List, TYPE_CHECKING, IO, Optional, Tuple

from meta.update_report import PluginUpdateReport, PluginUpdateReportEntry

if TYPE_CHECKING:
	from plugin.plugin_list import PluginList


class Reporter:
	def __init__(self):
		self.__lock = Lock()
		self.__command = None
		self.__start_time = None
		self.__end_time = None
		self.__warnings: Dict[str, List[PluginUpdateReportEntry]] = collections.defaultdict(list)
		self.__failures: Dict[str, List[PluginUpdateReportEntry]] = collections.defaultdict(list)
		self.__script_error: Optional[Tuple[Exception, str]] = None
		self.__script_error_exc: str = ''
		self.__disabled_plugins: Dict[str, str] = {}
		self.__rate_limit_remaining = '?'
		self.__rate_limit_limit = '?'

	@classmethod
	def __make_entry(cls, message: str, err: Optional[Exception] = None) -> PluginUpdateReportEntry:
		return PluginUpdateReportEntry(
			message=message,
			error_type=type(err).__name__ if err is not None else None,
			error_message=str(err) if err is not None else None,
		)

	@classmethod
	def __format_entry(cls, entry: PluginUpdateReportEntry) -> str:
		if entry.error_type is None:
			return entry.message
		return '{}: ({}) {}'.format(entry.message, entry.error_type, entry.error_message)

	def record_command(self, command: str):
		with self.__lock:
			self.__command = command

	def record_script_start(self):
		with self.__lock:
			self.__start_time = time.time()

	def record_script_end(self):
		with self.__lock:
			self.__end_time = time.time()

	def record_script_failure(self, e: Exception, exec_str: str):
		with self.__lock:
			self.__script_error = e
			self.__script_error_exc = exec_str

	def record_warning(self, plugin_id: str, message: str, err: Optional[Exception]):
		with self.__lock:
			self.__warnings[plugin_id].append(self.__make_entry(message, err))

	def record_plugin_failure(self, plugin_id: str, message: str, err: Exception):
		with self.__lock:
			self.__failures[plugin_id].append(self.__make_entry(message, err))

	def record_plugin_disabled(self, plugin_id: str, reason: str):
		with self.__lock:
			self.__disabled_plugins[plugin_id] = reason

	def record_rate_limit(self, remaining: int, limit: int):
		with self.__lock:
			self.__rate_limit_remaining = remaining
			self.__rate_limit_limit = limit

	@property
	def failures(self):
		return self.__failures
	
	@property
	def warnings(self):
		return self.__warnings

	def create_plugin_update_report(self, plugin_id: str) -> PluginUpdateReport:
		with self.__lock:
			return PluginUpdateReport(
				failures=list(self.__failures.get(plugin_id, [])),
				warnings=list(self.__warnings.get(plugin_id, [])),
			)

	def __dump(self, plugin_list: 'PluginList', f: IO[str]):
		f.write('---------------------------------------\n\n')
		f.write('# Report for command "{}"\n\n'.format(self.__command))
		f.write('Script arguments: {}\n\n'.format(sys.argv[1:]))

		f.write('## Summary\n\n')
		f.write('- Activated plugins: {}\n'.format(len(plugin_list)))
		f.write('- Disabled plugins: {}\n'.format(len(self.__disabled_plugins)))
		f.write('- API rate limit: {} / {}\n'.format(self.__rate_limit_remaining, self.__rate_limit_limit))
		if self.__start_time is not None and self.__end_time is not None:
			f.write('- Time cost: {}s\n'.format(round(self.__end_time - self.__start_time, 1)))
		f.write('- Failure amount: {}\n'.format(sum(map(lambda msgs: len(msgs), self.__failures.values()))))
		f.write('- Warning amount: {}\n'.format(sum(map(lambda msgs: len(msgs), self.__warnings.values()))))
		f.write('\n')

		f.write('## Disabled plugins\n\n')
		for plugin_id, reason in self.__disabled_plugins.items():
			f.write('- `{}`: {}\n'.format(plugin_id, reason))
		f.write('\n')

		if self.__script_error is not None:
			f.write('## Script failure\n\n')
			f.write('`Exception: ({}) {}`\n\n'.format(type(self.__script_error), self.__script_error))
			f.write('```\n{}\n```\n\n'.format(self.__script_error_exc.rstrip('\n')))

		f.write('## Failures\n\n')
		f.write('Plugins with failure: {}\n\n'.format(len(self.__failures)))
		for plugin_id in sorted(self.__failures.keys()):
			f.write('### `{}`\n\n'.format(plugin_id))
			for entry in self.__failures[plugin_id]:
				f.write('- {}\n'.format(self.__format_entry(entry)))
			f.write('\n')

		f.write('## Warnings\n\n')
		f.write('Plugins with warning: {}\n\n'.format(len(self.__warnings)))
		for plugin_id in sorted(self.__warnings.keys()):
			f.write('### `{}`\n\n'.format(plugin_id))
			for entry in self.__warnings[plugin_id]:
				f.write('- {}\n'.format(self.__format_entry(entry)))
			f.write('\n')

	def report(self, plugin_list: 'PluginList'):
		self.__dump(plugin_list, sys.stdout)
		if 'GITHUB_STEP_SUMMARY' in os.environ:
			with open(os.environ['GITHUB_STEP_SUMMARY'], 'w') as f:
				self.__dump(plugin_list, f)


reporter = Reporter()
