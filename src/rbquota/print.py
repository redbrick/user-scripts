"""print usage function"""
from __future__ import print_function

import sys

from .colour import colour
from .convert import convert_size
from .zfs import get_quota_from_zfs

# if you change the bar width, you'll also need to change the value in the
# format string in the print statement.
BAR_WIDTH = 35.0


def print_usage(username):
    """output users current usage of storage"""
    raw_quota = get_quota_from_zfs(username)

    if not raw_quota or raw_quota[0] == "-":
        sys.exit(1)

    home = [int(x) for x in raw_quota.decode().strip().split()]
    home.reverse()

    # here's the nasty bit. should really be using a list of filesystems.
    home_percent = 0.0

    if home[1] > 0:
        home_percent = (home[0] * 1.0 / home[1] * 1.0) * 100
    home_bar_width = home_percent * (BAR_WIDTH / 100)

    if home_bar_width > BAR_WIDTH:
        home_bar_width = BAR_WIDTH

    print(
        "Storage space report for %s \033[1;31mRedBrick\033[0m account:\n" % username,
        "%8s: |\033[1;%dm%-35s\033[0m|\033[0;36m%3d\033[0m%%, \033[0;36m%s\033[0m used, \033[0;36m%s\033[0m free"
        % (
            "  storage",
            colour(home_percent),
            "=" * int(home_bar_width),
            home_percent,
            convert_size(home[0]),
            convert_size(home[1] - home[0]),
        ),
    )
