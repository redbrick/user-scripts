"""friends function"""
from os import path


def load_friends():
    """load users .friends file"""
    try:
        friends_file = open(path.expanduser("~/.friends"), "r")
        return [i.rstrip() for i in friends_file.readlines()]
    except IOError:
        return []
