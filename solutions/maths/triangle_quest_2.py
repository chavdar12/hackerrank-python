def palindromic_triangle(n):
    return [(10 ** i // 9) ** 2 for i in range(1, n + 1)]
