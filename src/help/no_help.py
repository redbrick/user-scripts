"""message for no help of topic"""


def no_help(topic: str):
    return f"""Sorry, there is no help for {topic}
If {topic}  is a command, try the following commands:

    man {topic}
    info {topic}

Feel free to email or hey helpdesk for help."""
