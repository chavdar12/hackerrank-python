def door_mat(n, m):
    top = [(i * ".|.").center(m, "-") for i in range(1, n, 2)]
    return top + ["WELCOME".center(m, "-")] + top[::-1]
