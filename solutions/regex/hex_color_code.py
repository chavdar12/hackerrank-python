import re

PATTERN = re.compile(r"[ :]+(#[\da-fA-F]{6}|#[\da-fA-F]{3})\b")


def hex_colors(css_lines):
    return [color for line in css_lines for color in PATTERN.findall(line)]
