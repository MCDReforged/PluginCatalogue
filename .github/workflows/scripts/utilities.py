"""
This file is part of scripts of MCDReforged Plugin Catalogue.

This is a free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
in the `scripts` folder of the project root. If not, see 
<https://www.gnu.org/licenses/>.
"""

import datetime as dt
import json
import os
from enum import Enum
from typing import Optional

from plugin.plugin import Plugin
from common.report import reporter
from common.constants import REPOS_ROOT

COMMENT_SIGN = '<!-- report -->'


class PluginCheckError(ValueError):
    """Occurs when there's any error on plugin check"""


class EventType(Enum):
    """Workflow event types"""
    OPENED = 'opened'
    SYNCHRONIZE = 'synchronize'
    CLOSED = 'closed'


class Tag(str, Enum):
    """Issue (PR) tags"""
    PLG_ADD = 'plugin add'
    PLG_MODIFY = 'plugin modify'
    PLG_REMOVE = 'plugin remove'
    WORKFLOW = 'github workflow'
    SCRIPTS = 'scripts'

    @property
    def label(self) -> str:
        """Pull request label name from tags

        All plugin changes labels `plugins`
        """
        if self in (self.PLG_ADD, self.PLG_MODIFY, self.PLG_REMOVE):
            return 'plugins'
        return self.value


class Action:
    """PR actions"""
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
    """PR Action list with a [plugin, tag] dict"""

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
        """Returns all tags of actions"""
        return {action.tag for action in self}

    @property
    def labels(self) -> set[str]:
        """Returns all labels of actions"""
        return {tag.label for tag in self.tags}

    @property
    def modified_plugins(self) -> list[str]:
        """Returns all modified plugins"""
        return [plugin_id for plugin_id, tag in self.plugins.items() if tag in (Tag.PLG_ADD, Tag.PLG_MODIFY)]

    @property
    def removed_plugins(self) -> list[str]:
        """Returns all removed plugins"""
        return [plugin_id for plugin_id, tag in self.plugins.items() if tag == Tag.PLG_REMOVE]

    @property
    def plugin_ids(self) -> list[str]:
        """Returns all plugin ids of actions"""
        return self.plugins.keys()


def get_changed(change_type: str) -> list[str]:
    with open(os.path.join(REPOS_ROOT, f'.github/outputs/{change_type}.json'), 'r', encoding='utf8') as f:
        return json.load(f)


def _row(*args):
    return f"| {' | '.join(args)} |\n"


def _rowval(info, value, valid):
    return _row(info, value, '✅' if valid else '❌')


def get_icon(tag: Tag) -> str:
    match tag:
        case Tag.PLG_ADD:
            return '➕'
        case Tag.PLG_MODIFY:
            return '🔧'
        case Tag.PLG_REMOVE:
            return '🗑️'


def report_removed(plugin_id: str):
    report = f"""
### {get_icon(Tag.PLG_REMOVE)} `{plugin_id}`
"""
    directory = os.path.join('plugins', plugin_id)
    try:
        if os.path.isdir(directory) and os.listdir(directory):
            report += """
> [!WARNING]
> - The plugin directory is still not empty.
"""
    except Exception as e:
        report += f"""
> [!WARNING]
> - Failed to check if the plugin directory cleared. {e}
"""
    return report


def report_plugin(plugin: Plugin, tag: Tag) -> str:
    report = f"""
### {get_icon(tag)} `{plugin.id}`

| Info | Value | Valid |
| --- | --- | --- |
"""
    failures: Optional[list[str]] = reporter.failures.get(plugin.id)
    warnings: Optional[list[str]] = reporter.warnings.get(plugin.id)

    # PluginInfo rows
    report += _rowval(
        'URL',
        # AnzhiZhang/MCDReforgedPlugins@master/src/qq_chat
        '[`{}@{}{}`]({})'.format(
            plugin.repos.repos_pair,
            plugin.repos.branch,
            '/' + plugin.repos.related_path if plugin.repos.related_path != '.' else '',
            plugin.repos.get_page_url_base()
        ),
        not failures or not any('repository' in f for f in failures)
    )
    report += _row(
        'Labels',
        ' '.join(f'`{i}`' for i in plugin.labels),
        '❔'
    )
    report += _rowval(
        'Introduction',
        ' '.join(f'[`{lang}`]({url})'
                 for lang, url in plugin.introduction_urls.items()),
        not failures or not any('introduction' in f for f in failures)
    )
    report += _rowval(
        'Meta',
        '`mcdreforged.plugin.json`',
        not failures or not any('meta' in f for f in failures)
    )
    report += '\n'

    # PluginMeta rows
    if plugin.meta_info:
        report += """
| Meta | Value |
| --- | --- |
"""
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
            '<br/>'.join(f'`{lang}` {desc}'
                         for lang, desc in meta.description.items())
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


def report_all(plugin_list: list[Plugin], action_list: ActionList, removed_list: list[str]) -> str:
    time = dt.datetime.now(dt.timezone(dt.timedelta(hours=+8), 'UTC+8')).strftime(r"%Y-%m-%d %H:%M:%S (%Z)")
    header = f"""{COMMENT_SIGN}
_Last updated at: `{time}`_
## Plugin Validation Report
"""
    plugins = sorted(
        [(plugin, action_list.plugins.get(plugin.id)) for plugin in plugin_list],
        key=lambda x: x[1].value
    )
    return header + \
        '\n'.join(report_plugin(*plugin) for plugin in plugins) + \
        '\n'.join(report_removed(plugin) for plugin in removed_list)
