from itertools import groupby


def compress(digits):
    return [(len(list(group)), int(key)) for key, group in groupby(digits)]
