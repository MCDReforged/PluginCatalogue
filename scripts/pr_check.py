'''
A specified script to check plugins on pull requests.
'''

import json
import os
import sys

from constants import ROOT
from main import check

with open(os.path.join(ROOT, '.github/outputs/all_changed_and_modified_files.json'), 'r', encoding='utf8') as f:
	modified_files = json.load(f)

folders = []

for f in modified_files:
	folder_name = os.path.split(os.path.dirname(f))[-1]
	if folder_name not in folders:
		folders.append(folder_name)

if not folders:
	msg = 'Skipped plugin checking as there are no checkable modifications.'
	print(msg)
	if 'GITHUB_STEP_SUMMARY' in os.environ:
		with open(os.environ['GITHUB_STEP_SUMMARY'], 'w') as f:
			f.write(msg)
	sys.exit(0)

check(folders)
