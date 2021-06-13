""" gets logged in users"""
from pwd import getpwnam

from utmp import read

from .colours import get_colours
from .groups import get_groups


def get_logged_in_users(friends, encoding=False):
    """
    get a dict of logged in users
    returns {
        "noob": {
            "logins": 1,
            "colour": "COLOUR CODE"
        }
    }
    """
    # need a dict of users + times logged in
    logged_in_users = {}
    groups = get_groups(encoding)
    colours = get_colours(encoding)

    with open("/var/log/wtmp", "rb") as file:
        for entry in read(file.read()):
            # print(str(entry.type) == 'UTmpRecordType.login_process', entry.type, type(entry.type))
            # print(entry.user)
            if 'dead_process' in str(entry.type):
                continue
            user = entry.user
            # print(user)
            if user in logged_in_users:
                logged_in_users[user]["logins"] = logged_in_users[user]["logins"] + 1
                # print(logged_in_users)
            else:
                group = getpwnam(user)[3]
                logged_in_users[user] = dict(
                    logins=1,
                    colour=(
                        colours["white_text"]
                        if user in friends and group != 100
                        else groups.get(group, colours["default"])
                    ),
                )

    return logged_in_users
