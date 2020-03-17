"""get list of help topics"""
from typing import List

from .text import help_text


def get_topics() -> List[str]:
    return list(help_text.keys())
