'''
This file is part of scripts of MCDReforged Plugin Catalogue.

This is a free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
in the `scripts` folder of the project root. If not, see 
<https://www.gnu.org/licenses/>.
'''

import datetime as dt
import json
import os
from enum import Enum
from typing import Iterable, Optional

from common.constants import REPOS_ROOT
from common.report import reporter
from meta.release import ReleaseInfo
from plugin.plugin_list import Plugin, PluginList

COMMENT_SIGN = '<!-- report -->'


#! ---- Classes ---- ##

class EventType(Enum):
    '''Workflow event types that script accepts'''
    OPENED = 'opened'
    SYNCHRONIZE = 'synchronize'
    LABELED = 'labeled'
    CLOSED = 'closed'


class Tag(str, Enum):
    '''Issue (PR) tags'''
    PLG_ADD = 'plugin add'
    PLG_MODIFY = 'plugin modify'
    PLG_REMOVE = 'plugin remove'
    WORKFLOW = 'github workflow'
    SCRIPTS = 'scripts'

    @property
    def label(self) -> str:
        '''Pull request label name from tags

        All plugin changes labels `plugins`
        '''
        if self in (self.PLG_ADD, self.PLG_MODIFY, self.PLG_REMOVE):
            return 'plugins'
        return self.value


class Action:
    '''PR actions'''
    tag: Tag
    plugin_id: Optional[str]

    def __init__(self, tag: Tag, plugin_id: str = None):
        self.tag = tag
        self.plugin_id = plugin_id

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Action):
            return self.tag == value.tag and self.plugin_id == value.plugin_id
        return False

    def __hash__(self) -> int:
        return hash((self.tag, self.plugin_id))

    def __str__(self) -> str:
        return f'[{self.tag.value}]' + f'({self.plugin_id})' if self.plugin_id else ''

    def __repr__(self) -> str:
        return self.__str__()


class ActionList(set[Action]):
    '''PR Action list with a [plugin, tag] dict'''

    plugins: dict[str, Tag]

    def __init__(self) -> None:
        super().__init__()
        self.plugins = {}

    def add(self, action: Action) -> None:
        super().add(action)
        if action.plugin_id:
            self.plugins[action.plugin_id] = action.tag

    @property
    def tags(self) -> set[Tag]:
        '''Returns all tags of actions'''
        return {action.tag for action in self}

    @property
    def labels(self) -> set[str]:
        '''Returns all labels of actions'''
        return {tag.label for tag in self.tags}

    @property
    def modified_plugins(self) -> list[str]:
        '''Returns all modified plugins'''
        return [plugin_id for plugin_id, tag in self.plugins.items() if tag in (Tag.PLG_ADD, Tag.PLG_MODIFY)]

    @property
    def removed_plugins(self) -> list[str]:
        '''Returns all removed plugins'''
        return [plugin_id for plugin_id, tag in self.plugins.items() if tag == Tag.PLG_REMOVE]

    @property
    def plugin_ids(self) -> Iterable[str]:
        '''Returns all plugin ids of actions'''
        return self.plugins.keys()


#! ---- Workflow related ---- ##

def get_changed(change_type: str) -> list[str]:
    with open(REPOS_ROOT / f'.github/outputs/{change_type}.json', 'r', encoding='utf8') as f:
        return json.load(f)


#! ---- Validation report ---- ##

def _row(*args):
    return f'| {" | ".join(args)} |\n'


def _rowval(info, value, valid, valid_icon='✅', invalid_icon='❌'):
    return _row(info, value, valid_icon if valid else invalid_icon)


def _check(value: str, src: Optional[list[str]]):
    return not src or not any(value in s for s in src)


def get_icon(tag: Tag) -> str:
    match tag:
        case Tag.PLG_ADD:
            return '➕'
        case Tag.PLG_MODIFY:
            return '🔧'
        case Tag.PLG_REMOVE:
            return '🗑️'


def report_removed(plugin_id: str):
    report = f'''
### {get_icon(Tag.PLG_REMOVE)} `{plugin_id}`
'''
    directory = os.path.join('plugins', plugin_id)
    try:
        if os.path.isdir(directory) and os.listdir(directory):
            report += '''
> [!WARNING]
> - The plugin directory is still not empty.
'''
    except Exception as e:
        report += f'''
> [!WARNING]
> - Failed to check if the plugin directory cleared. {e}
'''
    return report


def report_init_failed(failures: dict[str, list[str]]):
    '''Check if there's any plugin failed to initialize. If so, report it.'''

    report = ''
    header = '''
### 🚨 `{plugin_id}`

> [!CAUTION]
{message}
'''
    for plugin_id, messages in failures.items():
        if any('Failed to initialize' in msg for msg in messages):
            report += header.format(
                plugin_id=plugin_id,
                message='\n'.join(f'> - {i}' for i in messages)
            )
    return report


def report_plugin(plugin: Plugin, tag: Tag) -> str:
    report = f'''
### {get_icon(tag)} `{plugin.id}`

| Info | Value | Valid |
| --- | --- | --- |
'''
    failures: Optional[list[str]] = reporter.failures.get(plugin.id)
    warnings: Optional[list[str]] = reporter.warnings.get(plugin.id)
    latest_release: Optional[ReleaseInfo] = plugin.release_summary.get_latest_release()

    # --- PluginInfo rows --- #

    report += _rowval(
        'URL',
        # `AnzhiZhang/MCDReforgedPlugins@master/src/qq_chat`
        '[`{}@{}{}`]({})'.format(
            plugin.repos.repos_pair,
            plugin.repos.branch,
            '/' + plugin.repos.related_path if plugin.repos.related_path != '.' else '',
            plugin.repos.get_page_url_base()
        ),
        _check('fetch repository', failures)
    )
    report += _row(
        'Authors',
        # [`Someone`](//...), `SomeoneElse`
        ', '.join(
            f'[`{i.name}`]({i.link})' if i.link else f'`{i.name}`'
            for i in plugin.authors
        ),
        '-'
    )
    report += _row(
        '[Labels](https://docs.mcdreforged.com/en/latest/plugin_dev/plugin_catalogue.html#label)',
        # `Tool`, `API`
        ' '.join(f'`{i}`' for i in plugin.labels),
        '-'
    )
    report += _rowval(
        'Introduction',
        # [`en_us`](//...) [`zh_cn`](//...)
        ' '.join(f'[`{lang}`]({url})'
                 for lang, url in plugin.get_introduction_urls(kind='page').items()),
        _check('introduction', failures)
    )
    report += _rowval(
        'Meta',
        '`mcdreforged.plugin.json`',
        _check('meta', failures)
    )
    report += _rowval(
        'Latest Release',
        # [`v1.0.0`](//...) || `None`
        f'[`{latest_release.meta.version}`]({latest_release.url})' if latest_release else '`None`',
        latest_release,
        invalid_icon='⚠️'
    )
    report += '\n'

    # --- PluginMeta rows --- #

    if plugin.meta_info:
        report += '''
| Meta | Value |
| --- | --- |
'''
        meta = plugin.meta_info
        report += _row(
            'Name',
            meta.name
        )
        report += _row(
            'Version',
            meta.version
        )
        report += _row(
            'Authors',
            ', '.join(meta.authors)
        )
        report += _row(
            'Description',
            # `en_us` Description content
            # `zh_cn` 简介内容
            '<br/>'.join(f'`{lang}` {desc}'
                         for lang, desc in meta.description.items())
        )
        report += '\n'

    if failures:
        report += '> [!CAUTION]\n'
        report += ''.join(f'> - {f}\n' for f in failures)
        report += '\n'

    if warnings:
        report += '> [!WARNING]\n'
        report += ''.join(f'> - {w}\n' for w in warnings)
        report += '\n'

    return report


def report_all(plugin_list: PluginList, action_list: ActionList, removed_list: list[str], reached_limit: bool) -> str:
    time = dt.datetime.now(dt.timezone(dt.timedelta(hours=+8), 'UTC+8')).strftime(r'%Y-%m-%d %H:%M:%S (%Z)')
    header = f'''{COMMENT_SIGN}
_Last updated at: `{time}`_
_Add label `recheck` to regenerate manually_
## Plugin Validation Report
'''

    if reached_limit:
        modified_report = '''
Plugin check limit reached. Check workflow log for details.
Add label `recheck` to regenerate without limit.
'''
    else:
        plugins = sorted(
            [(plugin, action_list.plugins.get(plugin.id)) for plugin in plugin_list],
            key=lambda x: x[1].value
        )
        modified_report = '\n'.join(report_plugin(*plugin) for plugin in plugins)

    removed_report = '\n'.join(report_removed(plugin) for plugin in removed_list)

    init_failed_report = '\n'.join(report_init_failed(reporter.failures))

    return header + modified_report + removed_report + init_failed_report
