"""cli arg parser"""

from sys import argv

from .menu import help_menu
from .need_help import need_help
from .no_help import no_help
from .print import print_file
from .topics import get_topics


def parse_args() -> str:
    """parse cli args"""
    if len(argv) == 1:
        return help_menu()
    if argv[1] == "need_help":
        return need_help()
    if argv[1] in get_topics():
        return print_file(argv[1])
    return no_help(argv[1])
