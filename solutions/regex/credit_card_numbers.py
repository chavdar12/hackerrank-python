import re

PATTERN = r"(?!.*(\d)(-?\1){3})^[456](\d{15}|\d{3}(-\d{4}){3})$"


def is_valid_card(s):
    return re.match(PATTERN, s) is not None
