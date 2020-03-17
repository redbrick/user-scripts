#!/usr/bin/env python
# vim: ft=python
"""
Description: Print currently logged in users
Authors:     Cian Brennan <lil_cain@redbrick.dcu.ie>
             Craig Gavagan <creadak@redbrick.dcu.ie>
             Cian Butler <butlerx@redbrick.dcu.ie>
Date:        Sat Oct  8 16:11:42 IST 2005
"""

from sys import stdout

from .friends import load_friends
from .logged_in import get_logged_in_users
from .print import print_users


def main():
    encoding = stdout.encoding is not None
    print_users(get_logged_in_users(load_friends(), encoding), encoding)


if __name__ == "__main__":
    main()
