import json
import os

from constants import ROOT
from main import check

with open(os.path.join(ROOT, '.github/outputs/all_changed_and_modified_files.json'), 'r', encoding='utf8') as f:
    modified_files = json.load(f)

folders = []

for f in modified_files:
    folder_name = os.path.split(os.path.dirname(f))[-1]
    if folder_name not in folders:
        folders.append(folder_name)

print(folders)
# check(folders)
