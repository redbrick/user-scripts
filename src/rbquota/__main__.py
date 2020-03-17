#!/usr/bin/env python
# vim: ft=python
"""
Description: Pretty display of RedBrick quota usage
Authors:     Charlie Von Metzradt <phaxx@redbrick.dcu.ie>
             Cian Butler <butlerx@redbrick.dcu.ie>
             Lucas Savva <m1cr0man@redbrick.dcu.ie>
Date:        Sat Oct  8 16:11:42 IST 2005
"""

from .print import print_usage
from .user import get_user


def main():
    print_usage(get_user())


if __name__ == "__main__":
    main()
