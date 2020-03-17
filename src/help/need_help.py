"""need help message"""
from .colours import blue, cyan, red


def need_help() -> str:
    return f"""
     {blue('--------------------------[')}  Need Help?  {blue(']--------------------------')}
     {blue('|')} A quick guide on how to use {red('Redbrick')} is available at any time by {blue('|')}
     {blue('|')} typing in the word {cyan('help')} (followed by RETURN) at the prompt below {blue('|')}
     {blue('----------------[')}  http://helpdesk.redbrick.dcu.ie {blue(']----------------')}"""
