from itertools import combinations_with_replacement


def sorted_combinations_with_replacement(s, k):
    return ["".join(c) for c in combinations_with_replacement(sorted(s), k)]
