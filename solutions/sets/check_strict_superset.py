def is_strict_superset(a, others):
    return all(a > other for other in others)
