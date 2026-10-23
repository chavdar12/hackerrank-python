import re


def decode(rows):
    text = "".join("".join(column) for column in zip(*rows))
    return re.sub(r"(?<=\w)[^\w]+(?=\w)", " ", text)
