def get_colours(encoding=False):
    """get colour code"""
    return {
        "default": "\033[;0m" if encoding else "",
        "white_text": "\033[;035m" if encoding else "",
        "white": "\033[;45m" if encoding else "",
        "red": "\033[;41m" if encoding else "",
        "cyan": "\033[;46m" if encoding else "",
        "green": "\033[;42m" if encoding else "",
        "magenta": "\033[;44m" if encoding else "",
        "yellow": "\033[;43m" if encoding else "",
    }
