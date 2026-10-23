import re


def first_repeating(s):
    match = re.search(r"([a-zA-Z0-9])\1", s)
    return match.group(1) if match else -1
