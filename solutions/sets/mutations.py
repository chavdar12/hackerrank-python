def apply_mutations(numbers, operations):
    s = set(numbers)
    for name, other in operations:
        getattr(s, name)(other)
    return sum(s)
