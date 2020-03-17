#!/usr/bin/env python
"""help text for users"""

from sys import argv

from .menu import help_menu, need_help, no_help
from .topics import get_topics, template_topic


def parse_args() -> str:
    """parse cli args"""
    if len(argv) == 1:
        return help_menu()
    if argv[1] == "need_help":
        return need_help()
    if argv[1] in get_topics():
        return template_topic(argv[1])
    return no_help(argv[1])


def main():
    print(parse_args())


if __name__ == "__main__":
    main()
