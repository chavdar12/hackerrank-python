import string


def rangoli(size):
    alpha = string.ascii_lowercase
    rows = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        rows.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    return rows[:0:-1] + rows
