from collections import deque


def run_deque(operations):
    d = deque()
    for operation in operations:
        name, *args = operation.split()
        getattr(d, name)(*map(int, args))
    return list(d)
