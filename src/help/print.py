"""print file to stdout"""
from .template import footer, heading
from .text import help_text


def print_file(topic) -> str:
    link = footer(help_text[topic]["link"]) if "link" in help_text[topic] else ""
    return f"{heading(topic)}{help_text[topic]['text']}{link}"
