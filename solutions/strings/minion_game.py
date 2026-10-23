def minion_game(string):
    n = len(string)
    kevin = sum(n - i for i, c in enumerate(string) if c in "AEIOU")
    stuart = n * (n + 1) // 2 - kevin
    if kevin > stuart:
        return "Kevin {}".format(kevin)
    if stuart > kevin:
        return "Stuart {}".format(stuart)
    return "Draw"
