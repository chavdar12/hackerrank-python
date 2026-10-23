from collections import deque


def can_pile(blocks):
    d = deque(blocks)
    last = float("inf")
    while d:
        cube = d.popleft() if d[0] >= d[-1] else d.pop()
        if cube > last:
            return False
        last = cube
    return True
