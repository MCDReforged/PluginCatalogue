import collections
import os
import sys
from threading import Lock
from typing import Dict, List, TYPE_CHECKING, IO

if TYPE_CHECKING:
	from plugin_list import PluginList


class Reporter:
	def __init__(self):
		self.__lock = Lock()
		self.__command = None
		self.__warnings: Dict[str, List[str]] = collections.defaultdict(list)
		self.__failures: Dict[str, List[str]] = collections.defaultdict(list)
		self.__disabled_plugins: Dict[str, str] = {}
		self.__rate_limit_remaining = '?'
		self.__rate_limit_limit = '?'

	def record_command(self, command: str):
		with self.__lock:
			self.__command = command

	def record_warning(self, plugin_id: str, message: str, err: Exception):
		with self.__lock:
			self.__warnings[plugin_id].append(message + ': ({}) {}'.format(type(err).__name__, err))

	def record_failure(self, plugin_id: str, message: str, err: Exception):
		with self.__lock:
			self.__failures[plugin_id].append(message + ': ({}) {}'.format(type(err).__name__, err))

	def record_plugin_disabled(self, plugin_id: str, reason: str):
		with self.__lock:
			self.__disabled_plugins[plugin_id] = reason

	def record_rate_limit(self, remaining: int, limit: int):
		with self.__lock:
			self.__rate_limit_remaining = remaining
			self.__rate_limit_limit = limit

	def __dump(self, plugin_list: 'PluginList', f: IO[str]):
		f.write('-----------------------------------\n\n')
		f.write('# Report for command "{}"\n\n'.format(self.__command))
		f.write('Script args: {}\n\n'.format(sys.argv[1:]))

		f.write('## Summary\n\n')
		f.write('Activated plugins: {}\n\n'.format(len(plugin_list)))
		f.write('Disabled plugins: {}\n\n'.format(len(self.__disabled_plugins)))
		f.write('API rate limit: {} / {}\n\n'.format(self.__rate_limit_remaining, self.__rate_limit_limit))

		f.write('## Disabled plugins\n\n')
		for plugin_id, reason in self.__disabled_plugins.items():
			f.write('- {}: {}\n'.format(plugin_id, reason))
		f.write('\n')

		f.write('## Failures\n\n')
		f.write('Plugins with failure: {}\n\n'.format(len(self.__failures)))
		f.write('Failure amount: {}\n\n'.format(sum(map(lambda msgs: len(msgs), self.__failures.values()))))
		for plugin_id, messages in self.__failures.items():
			f.write('### `{}`\n\n'.format(plugin_id))
			for msg in messages:
				f.write('- {}\n'.format(msg))
			f.write('\n')

		f.write('## Warnings\n\n')
		f.write('Plugins with warning: {}\n\n'.format(len(self.__warnings)))
		f.write('Warning amount: {}\n\n'.format(sum(map(lambda msgs: len(msgs), self.__warnings.values()))))
		for plugin_id, messages in self.__warnings.items():
			f.write('### `{}`\n\n'.format(plugin_id))
			for msg in messages:
				f.write('- {}\n'.format(msg))
			f.write('\n')

	def report(self, plugin_list: 'PluginList'):
		self.__dump(plugin_list, sys.stdout)
		if 'GITHUB_STEP_SUMMARY' in os.environ:
			with open(os.environ['GITHUB_STEP_SUMMARY'], 'w') as f:
				self.__dump(plugin_list, f)


reporter = Reporter()

