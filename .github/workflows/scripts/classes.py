""" Utility classes """

from enum import Enum
from typing import Optional


class PluginCheckError(ValueError):
    """Occurs when there's any error on plugin check"""


class EventType(Enum):
    """Workflow event types"""
    OPENED = 'opened'
    SYNCHRONIZE = 'synchronize'
    CLOSED = 'closed'
    MERGED = 'merged'


class Tag(str, Enum):
    """Issue (PR) tags"""
    PLG_ADD = 'plugin add'
    PLG_MODIFY = 'plugin modify'
    PLG_REMOVE = 'plugin remove'
    WORKFLOW = 'github workflow'
    SCRIPTS = 'scripts'


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
        return f'[{self.tag.value}]({self.plugin_id})'

    def __repr__(self) -> str:
        return self.__str__()
