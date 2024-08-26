"""
Script for Pull Request Actions.

When PR:
- opened: add a comment, label the PR, check and report plugins
- synchronize: update plugin report if plugin changed
- closed: congratulate if merged

Environ:
- EVENT_TYPE: opened, synchronize, closed
- IS_MERGED: true, false
"""

import asyncio
import datetime as dt
import json
import logging
import os
import sys
from pathlib import Path
from typing import List, Optional

sys.path.append('scripts')  # Make import and script runs from correct directory

import gh_cli as gh  # noqa
from classes import *  # noqa
from common.constants import REPOS_ROOT  # noqa
from common.log import logger  # noqa
from common.report import reporter  # noqa
from plugin.plugin import Plugin  # noqa
from plugin.plugin_list import get_plugin_list  # noqa

#! ---- Gather environs ---- ##

PLUGIN_CHECK_LIMIT = 5
COMMENT_SIGN = '<!-- report -->'
COMMENT_USER = 'github-actions'

EVENT_TYPE = EventType(os.environ.get('EVENT_TYPE'))
IS_MERGED = os.environ.get('IS_MERGED', 'false')

if EVENT_TYPE == EventType.CLOSED and IS_MERGED == 'true':
    EVENT_TYPE = EventType.MERGED

logger.info(f'Running with event type: {EVENT_TYPE}')


#! ---- On merged ---- ##
if EVENT_TYPE == EventType.MERGED:
    reply = """
Well done! 🎉

Your pull request has been successfully merged.

We appreciate your hard work and valuable input. If you have any further questions or need additional changes, feel free to reach out.

Happy coding!
""".strip()
    gh.pr_comment(reply)
    sys.exit(0)

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


#! ---- Identify actions and tags ---- ##

"""
In order of priority, the process shoule be:

1. A(CMR)D of `plugins/<plugin_id>/plugin_info.json` == AMD of plugin
2. Both A and D of `plugins/<plugin_id>/plugin_info.json` == Modify of plugin
3. ACMRD of `plugins/<plugin_id>/**` == Modify of plugin
4. ACMRD of `scripts/**` == `scripts`
5. ACMRD of `.github/workflows/**` == `github workflow`

In which, one plugin should only have one action.
"""

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
    elif path[0] == 'scripts':
        actions.add(Action(Tag.SCRIPTS))
    elif file.startswith('.github/workflows'):
        actions.add(Action(Tag.WORKFLOW))

tags = set(action.tag for action in actions)
if Tag.PLG_REMOVE in tags and Tag.PLG_ADD in tags:  # add + remove = modify
    tags.remove(Tag.PLG_REMOVE)
    tags.remove(Tag.PLG_ADD)
    tags.add(Tag.PLG_MODIFY)

logger.info(f"Identified actions: {', '.join(map(str, actions))}")
logger.info(f"Identified tags: {', '.join(map(str, tags))}")


#! ---- Run plugin checks and generate report ---- ##

def report_plugin(plugin: Plugin) -> str:
    def row(*args):
        return f"| {' | '.join(args)} |\n"

    def rowval(info, value, valid):
        return row(info, value, '✅' if valid else '❌')
    report = f"""
### `{plugin.id}`

| Info | Value | Valid |
| --- | --- | --- |
"""
    failures: Optional[List[str]] = reporter.failures.get(plugin.id)
    warnings: Optional[List[str]] = reporter.warnings.get(plugin.id)

    # PluginInfo rows
    report += rowval(
        'URL',
        # AnzhiZhang/MCDReforgedPlugins@master/src/qq_chat
        '[{}@{}{}]({})'.format(
            plugin.repos.repos_pair,
            plugin.repos.branch,
            '/' + plugin.repos.related_path if plugin.repos.related_path != '.' else '',
            plugin.repos.get_page_url_base()
        ),
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
        report += """
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
    time = dt.datetime.now(dt.timezone(dt.timedelta(hours=+8), 'UTC+8')).strftime(r"%Y-%m-%d %H:%M:%S (%Z)")
    header = f"""{COMMENT_SIGN}
_Last updated at: `{time}`_
## Plugin Validation Report
"""
    return header + '\n'.join(report_plugin(plugin) for plugin in plugin_list)


reply: str = f"""
Thanks for your contribution! 🎉

Please be patient before we done checking. If you have modified any plugins, a brief report shall be generated below.

Have a nice day!
""".strip()

if Tag.PLG_ADD in tags:
    reply += """
---
以下是供仓库维护者参考的合并前检查单。
- 所提交信息齐全、有效
- 插件名称符合其功能，没有歧义
- 提交者是版本库所有者/维护者/协作者
- 插件分类正确
- 插件说明足以帮助用户使用
- 其他应当作为合并前检查的事项
"""

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
        logger.warning(f'Too many plugins to check (>{PLUGIN_CHECK_LIMIT}), skipping')
        report = f'Too many plugins to check (>{PLUGIN_CHECK_LIMIT}), skipped'
        reporter.record_script_failure(report, ValueError(report))
    else:
        plugin_list = get_plugin_list(plugins)
        asyncio.run(plugin_list.fetch_data(fail_hard=False, skip_release=True))
        report = report_all(plugin_list)

    reporter.report(plugin_list)
else:
    logger.info('No plugins to check, skipping')

if EVENT_TYPE == EventType.OPENED:
    gh.pr_label(add_labels=[t.value for t in tags])
    gh.pr_comment(reply)

if report:
    gh.pr_update_or_comment(COMMENT_USER, COMMENT_SIGN, report)

if len(reporter.failures) > 0:
    raise PluginCheckError('Plugin check failed')
