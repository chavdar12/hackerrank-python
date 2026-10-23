from collections import OrderedDict


def net_prices(lines):
    items = OrderedDict()
    for line in lines:
        item, price = line.rsplit(" ", 1)
        items[item] = items.get(item, 0) + int(price)
    return list(items.items())
