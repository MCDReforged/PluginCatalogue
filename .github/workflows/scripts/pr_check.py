"""
A specified script to check plugins on pull requests.
"""
import asyncio
import json
import logging
import os
import sys

sys.path.append('scripts') # Make import and script runs from correct directory

from common.constants import REPOS_ROOT
from common.log import logger
from common.report import reporter
from plugin.plugin_list import get_plugin_list


logger.setLevel(logging.INFO) # https://github.com/MCDReforged/PluginCatalogue/pull/372


class PullRequestCheckError(ValueError):
	pass


def get_modified_plugins():
	# https://github.com/marketplace/actions/changed-files
	with open(os.path.join(REPOS_ROOT, '.github/outputs/all_changed_and_modified_files.json'), 'r', encoding='utf8') as f:
		modified_files = json.load(f)

	plugins = set()

	for path in modified_files:
		if path.startswith('plugins/'):
			plugin_id = os.path.split(os.path.dirname(path))[-1] # plugin/<id>/... -> <id>
			plugins.add(plugin_id)
	
	return plugins


async def main():
	target_ids = get_modified_plugins()

	reporter.record_script_start()
	reporter.record_command('pr_check')

	plugin_list = []
	
	if not target_ids:
		reporter.record_script_failure(ValueError("Empty plugin list"))
	else:
		plugin_list = get_plugin_list(target_ids)
		await plugin_list.fetch_data(fail_hard=False, skip_release=True)
		
	reporter.report(plugin_list)
	if reporter.failures > 0:
		raise PullRequestCheckError(
			"Check fails since there's failure during the fetch process. Check report messages above or workflow summary for more infomation.")


if __name__ == '__main__':
	asyncio.run(main())
