from collections import Counter


def top_three(s):
    return Counter(sorted(s)).most_common(3)
