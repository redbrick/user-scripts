"""convert bytes to human readable values"""

from math import floor, log
from math import pow as power


def convert_size(size_bytes):
    """convert Btye Value to Pretty Value"""
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    size_index = int(floor(log(size_bytes, 1024)))
    return "%s%s" % (
        round(size_bytes / power(1024, size_index), 2),
        size_name[size_index],
    )
