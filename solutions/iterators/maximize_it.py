def maximize(m, lists):
    reachable = {0}
    for values in lists:
        reachable = {(r + v * v) % m for r in reachable for v in values}
    return max(reachable)
