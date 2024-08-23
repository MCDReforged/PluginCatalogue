"""
Check and tag pull requests.
"""
import asyncio
import json
import logging
import os
import sys
from enum import Enum
from pathlib import Path
from typing import List, Optional

sys.path.append('scripts') # Make import and script runs from correct directory

from common.constants import REPOS_ROOT
from common.log import logger
from common.report import reporter
from gh_cli import pr_comment, pr_label
from plugin.plugin import Plugin
from plugin.plugin_list import get_plugin_list

PLUGIN_CHECK_LIMIT = 5


class PluginCheckError(ValueError):
    pass


class Tag(str, Enum):
    PLG_ADD = 'plugin add'
    PLG_MODIFY = 'plugin modify'
    PLG_REMOVE = 'plugin remove'
    WORKFLOW = 'github workflow'
    OTHERS = 'others'


class Action:
    tag: Tag
    plugin_id: Optional[str]

    def __init__(self, tag: Tag, plugin_id: str = None):
        self.tag = tag
        self.plugin_id = plugin_id

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Action):
            return self.tag == value.tag and self.plugin_id == value.plugin_id

    def __hash__(self) -> int:
        return hash((self.tag, self.plugin_id))
    
    def __str__(self) -> str:
        return f'[{self.tag.value}]({self.plugin_id})'

    def __repr__(self) -> str:
        return self.__str__()


#! ---- Gather file changes ---- ##
# https://github.com/marketplace/actions/changed-files#outputs-

def get_changed(change_type: str) -> List[str]:
    with open(os.path.join(REPOS_ROOT, f'.github/outputs/{change_type}.json'), 'r', encoding='utf8') as f:
        return json.load(f)


# Add, Copied, Modified, Renamed, Deleted
added_files = set(get_changed('added_files'))  # A
changed_files = set(get_changed('all_changed_files'))  # ACMR
deleted_files = set(get_changed('deleted_files'))  # D
all_files = changed_files | deleted_files  # ACMRD


#! ---- Determine actions and tags ---- ##

actions: set[Action] = set()
tags: Optional[set[Tag]] = None

for file in sorted(all_files, key=lambda x: x.endswith('plugin_info.json'), reverse=True):
    path = Path(file).parts
    if len(path) > 1 and path[0] == 'plugins':
        if path[-1] == 'plugin_info.json':  # if plugin meta changed
            if file in added_files:
                actions.add(Action(Tag.PLG_ADD, path[1]))
            elif file in deleted_files:
                actions.add(Action(Tag.PLG_REMOVE, path[1]))
            else:
                actions.add(Action(Tag.PLG_MODIFY, path[1]))
        # if other plugin files changed
        elif not any(action.plugin_id == path[1] for action in actions):
            actions.add(Action(Tag.PLG_MODIFY, path[1]))
    elif file.startswith('.github/workflows'):
        actions.add(Action(Tag.WORKFLOW))
    else:
        actions.add(Action(Tag.OTHERS))

tags = set(action.tag for action in actions)
if Tag.PLG_REMOVE in tags and Tag.PLG_ADD in tags:  # add + remove = modify
    tags.remove(Tag.PLG_REMOVE)
    tags.remove(Tag.PLG_ADD)
    tags.add(Tag.PLG_MODIFY)

logger.info(f"Found actions: {', '.join(map(str, actions))}")
logger.info(f"Calculated tags: {', '.join(map(str, tags))}")


#! ---- Run plugin checks and generate report ---- ##

def report_plugin(plugin: Plugin) -> str:
    def row(*args):
        return f"| {' | '.join(args)} |\n"

    def rowval(info, value, valid):
        return row(info, value, '✅' if valid else '❌')
    report = \
        f"""
### `{plugin.id}`

| Info | Value | Valid |
| --- | --- | --- |
"""
    failures: Optional[List[str]] = reporter.failures.get(plugin.id)
    warnings: Optional[List[str]] = reporter.warnings.get(plugin.id)

    # PluginInfo rows
    report += rowval(
        'Repo',
        f'[`{plugin.repos.repos_pair}`]({plugin.repos.repos_url})',
        not failures or not any('repository' in f for f in failures)
    )
    report += row(
        'Labels',
        ' '.join(f'`{i}`' for i in plugin.labels),
        '❔'
    )
    report += rowval(
        'Introduction',
        ' '.join(f'[`{lang}`]({url})'
                 for lang, url in plugin.introduction_urls.items()),
        not failures or not any('introduction' in f for f in failures)
    )
    report += rowval(
        'Meta',
        '-',
        not failures or not any('meta' in f for f in failures)
    )
    report += '\n'

    # PluginMeta rows
    if plugin.meta_info:
        report += \
            """
| Meta | Value |
| --- | --- |
"""
        report += row(
            'Authors',
            ', '.join(plugin.meta_info.authors)
        )
        report += row(
            'Description',
            '<br/>'.join(f'`{lang}` {desc}'
                         for lang, desc in plugin.meta_info.description.items())
        )
        report += '\n'

    if failures:
        report += "> [!CAUTION]\n"
        report += ''.join(f'> - {f}\n' for f in failures)
        report += '\n'

    if warnings:
        report += "> [!WARNING]\n"
        report += ''.join(f'> - {w}\n' for w in warnings)
        report += '\n'

    return report


def report_all(plugin_list: List[Plugin]) -> str:
    return '\n'.join(report_plugin(plugin) for plugin in plugin_list)


reply: str = f"""
Thanks for your contribution! 🎉
{
    '\nSeems that you are modifying multiple parts of the project. We suggest you to split it into multiple PRs. If this is not the case, ignore this message. \n'
    if len(tags) > 1 else ''
}
Please wait patiently before we done checking. If you have modified any plugins, a brief report shall be generated below.

Have a nice day!

---
以下是供仓库维护者参考的合并前检查单。
- 所提交信息齐全、有效
- 插件名称符合其功能，没有歧义
- 提交者是版本库所有者或维护者
- 插件分类正确
- 插件说明足以帮助用户使用
- 其他应当作为合并前检查的事项
""".strip()

with open('reply.md', 'w', encoding='utf-8') as f:
    f.write(reply)

report: Optional[str] = None

# https://github.com/MCDReforged/PluginCatalogue/pull/372
logger.setLevel(logging.INFO)

plugins = [
    action.plugin_id for action in actions if
    action.tag == Tag.PLG_MODIFY or action.tag == Tag.PLG_ADD
]

if plugins:
    logger.info(f'Checking {len(plugins)} plugins: {", ".join(plugins)}')
    reporter.record_script_start()
    reporter.record_command('pr_check')
    if len(plugins) > PLUGIN_CHECK_LIMIT:
        logger.warning('Too many plugins to check (>{}), skipping'.format(PLUGIN_CHECK_LIMIT))
        report = 'Too many plugins to check (>{}), skipped'.format(PLUGIN_CHECK_LIMIT)
        reporter.record_script_failure(report)
    else:
        plugin_list = get_plugin_list(plugins)
        asyncio.run(plugin_list.fetch_data(fail_hard=False, skip_release=True))
        report = report_all(plugin_list)
    reporter.report(plugin_list)
    with open('report.md', 'w', encoding='utf8') as f:
        f.write(report)
else:
    logger.info('No plugins to check, skipping')

pr_label(add_labels=[t.value for t in tags])
pr_comment('reply.md')
pr_comment('report.md')

if len(reporter.failures) > 0:
    raise PluginCheckError('Plugin check failed')
