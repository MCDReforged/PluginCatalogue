"""
A specified script to check plugins on pull requests.
"""
import asyncio
import json
import os
import sys

sys.path.append('scripts')

from common.constants import REPOS_ROOT
from main import check


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
		asyncio.run(check(folders, concise=True))


if __name__ == '__main__':
	main()
