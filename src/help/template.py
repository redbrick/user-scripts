"""template help text"""
from .colours import blue, bright_cyan, green, yellow


def heading(title: str) -> str:
    return f"""{green('Help on:')} {bright_cyan(title)}
{blue('---------------')}

"""


def footer(link: str) -> str:
    return f"""

See also:
{yellow(link)}"""
