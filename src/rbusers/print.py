"""outpu rb users"""
from __future__ import print_function

from .colours import get_colours


def print_users(logged_in_users, encoding=False):
    """ Pretty Print"""
    title_message = (
        "\033[;31mTotal \033[;0mNumber \033[;33mof \033[;34mUsers \033[;35monline\033[;0m:"
        if encoding
        else "Total Number of Users Online:"
    )
    colours = get_colours(encoding)

    print(
        "                         %s %s\n"
        % (title_message, len(logged_in_users.keys())),
        "                      %s %s friends   %s %s committee  %s %s associate\n"
        % (
            colours["white"],
            colours["default"],
            colours["red"],
            colours["default"],
            colours["cyan"],
            colours["default"],
        ),
        "                      %s %s society   %s %s club       %s %s guest"
        % (
            colours["magenta"],
            colours["default"],
            colours["yellow"],
            colours["default"],
            colours["green"],
            colours["default"],
        ),
        "\n     ",
        end=" ",
    )
    # go through and print the users.
    # we only want 5 users for a line which is what iter is for
    itera = 0
    for user in sorted(logged_in_users.keys()):
        itera = itera + 1

        # two format strings, to take a/c of users with >10 sessions
        print(
            (
                "%s%s \033[;0m\033[;032m(\033[;033m%d\033[;032m) "
                if logged_in_users[user]["logins"] < 10
                else "%s%s\033[;0m\033[;032m(\033[;033m%d\033[;032m) "
            )
            % (
                logged_in_users[user]["colour"],
                user.ljust(8)[:8],
                logged_in_users[user]["logins"],
            ),
            end=" ",
        )
        if itera >= 5:
            itera = 0
            print("\n     ", end=" ")
    # reset to default colour for stupid terms
    print(colours["default"])
