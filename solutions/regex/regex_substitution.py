import re


def sub_func(s):
    s = re.sub(r"(?<= )\|\|(?= )", "or", s)
    return re.sub(r"(?<= )&&(?= )", "and", s)
