"""groups functions"""


def get_groups(encoding=False):
    return (
        {
            100: "\033[;31m",
            107: "\033[;36m",
            108: "\033[;32m",
            102: "\033[;33m",
            101: "\033[;34m",
            103: "\033[;0m",
        }
        if encoding
        else {100: "", 107: "", 108: "", 102: "", 101: "", 103: ""}
    )
