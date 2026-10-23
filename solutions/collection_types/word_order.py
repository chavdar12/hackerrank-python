from collections import Counter


def word_order(words):
    counts = Counter(words)
    return len(counts), list(counts.values())
