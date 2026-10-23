def average(arr):
    distinct = set(arr)
    return round(sum(distinct) / len(distinct), 3)
