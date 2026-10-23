def max_depth(elem):
    return max((1 + max_depth(child) for child in elem), default=0)
