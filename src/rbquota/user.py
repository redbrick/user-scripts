"""function for parsing user"""
import sys
from os import getuid


def get_user():
    """get username to look quota for"""
    if len(sys.argv) == 2:
        return sys.argv[1]
    from pwd import getpwuid

    return getpwuid(getuid())[0]
