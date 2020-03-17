"""get list of help topics"""
from typing import List

from .template import footer, heading
from .text import HELP_TEXT


def template_topic(topic) -> str:
    link = footer(HELP_TEXT[topic]["link"]) if "link" in HELP_TEXT[topic] else ""
    return f"{heading(topic)}{HELP_TEXT[topic]['text']}{link}"


def get_topics() -> List[str]:
    return list(HELP_TEXT.keys())
