def probability_of_a(letters, k):
    n, a = len(letters), letters.count("a")
    p_none = 1.0
    for i in range(k):
        p_none *= (n - a - i) / (n - i)
    return 1 - p_none
