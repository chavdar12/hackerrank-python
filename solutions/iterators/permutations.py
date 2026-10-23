from itertools import permutations


def sorted_permutations(s, r):
    return ["".join(p) for p in permutations(sorted(s), r)]
