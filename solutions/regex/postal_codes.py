import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


def is_valid_postal_code(p):
    return bool(re.match(regex_integer_in_range, p)) and len(re.findall(regex_alternating_repetitive_digit_pair, p)) < 2
