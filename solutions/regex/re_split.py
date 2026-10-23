import re

regex_pattern = r"[\b\W\b]+"


def split_number(s):
    return re.split(regex_pattern, s)
