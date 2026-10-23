def sort_key(c):
    if c.islower():
        return 0, c
    if c.isupper():
        return 1, c
    return (2 if int(c) % 2 else 3), c


def ginorts(s):
    return "".join(sorted(s, key=sort_key))
