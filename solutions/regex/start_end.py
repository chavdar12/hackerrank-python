import re


def match_spans(s, k):
    spans = [(m.start(), m.start() + len(k) - 1) for m in re.finditer(r"(?=%s)" % re.escape(k), s)]
    return spans or [(-1, -1)]
