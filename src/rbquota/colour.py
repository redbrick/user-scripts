"""colour functions"""


def colour(percent):
    """return colour code for given percentage"""
    if percent > 80:
        return 31  # red
    if percent > 60:
        return 33  # yellow
    return 32  # green
