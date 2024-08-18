"""
A specified script to check plugins on pull requests.
"""
import asyncio
import json
import logging
import os
import sys

from common.constants import REPOS_ROOT
from common.log import logger
from common.report import reporter
from plugin.plugin_list import get_plugin_list

sys.path.append('scripts')


logger.setLevel(logging.INFO)


class PullRequestCheckError(ValueError):
	pass


async def pr_check(target_ids):
	plugin_list = get_plugin_list(target_ids)
	reporter.record_command('pr_check')
	reporter.record_script_start()
	await plugin_list.fetch_data(fail_hard=False, skip_release=True)
	reporter.report()
	if reporter.failures > 0:
		raise PullRequestCheckError(
			"Check fails since there's failure during the fetch process. Check messages above or workflow summary for more infomation.")


def main():
	with open(os.path.join(REPOS_ROOT, '.github/outputs/all_changed_and_modified_files.json'), 'r', encoding='utf8') as f:
		modified_files = json.load(f)

	folders = []

	for f in modified_files:
		folder_name = os.path.split(os.path.dirname(f))[-1]
		if folder_name not in folders:
			folders.append(folder_name)

	if folders:
		skip = False
		msg = 'Modified plugin(s): \n'
		for i in folders:
			msg += f'- {i}\n'
	else:
		msg = 'Skipped plugin checking as there are no checkable modifications.'
		skip = True

	print(msg)
	if 'GITHUB_STEP_SUMMARY' in os.environ:
		with open(os.environ['GITHUB_STEP_SUMMARY'], 'w') as f:
			f.write(msg)

	if not skip:
		asyncio.run(pr_check(folders))


if __name__ == '__main__':
	main()
