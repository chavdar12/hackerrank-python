import re


def is_valid_phone(s):
    return re.fullmatch(r"[789]\d{9}", s) is not None
