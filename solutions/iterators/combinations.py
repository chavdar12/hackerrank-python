from itertools import combinations


def sorted_combinations(s, k):
    return ["".join(c) for size in range(1, k + 1) for c in combinations(sorted(s), size)]
