import re

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"


def is_roman(s):
    return bool(s) and re.match(regex_pattern, s) is not None
