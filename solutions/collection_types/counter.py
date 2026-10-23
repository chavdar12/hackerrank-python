from collections import Counter


def shoe_shop_earnings(sizes, orders):
    stock = Counter(sizes)
    total = 0
    for size, price in orders:
        if stock[size] > 0:
            total += price
            stock[size] -= 1
    return total
