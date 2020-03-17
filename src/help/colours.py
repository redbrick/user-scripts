"""functions for colouring"""
from typing import Callable


def reset(msg: str) -> str:
    return f"{msg}\033[;0m"


def colour(color: str) -> Callable:
    def _colour(msg: str) -> str:
        return reset(f"{color}{msg}")

    return _colour


black = colour("\u001b[30m")
red = colour("\u001b[31m")
green = colour("\u001b[32m")
yellow = colour("\u001b[33m")
blue = colour("\u001b[34m")
magenta = colour("\u001b[35m")
cyan = colour("\u001b[36m")
white = colour("\u001b[37m")
bright_black = colour("\u001b[30;1m")
bright_red = colour("\u001b[31;1m")
bright_green = colour("\u001b[32;1m")
bright_yellow = colour("\u001b[33;1m")
bright_blue = colour("\u001b[34;1m")
bright_magenta = colour("\u001b[35;1m")
bright_cyan = colour("\u001b[36;1m")
bright_white = colour("\u001b[37;1m")
