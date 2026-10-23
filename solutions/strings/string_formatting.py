def formatted(number):
    width = len(bin(number)[2:])
    return [f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}" for i in range(1, number + 1)]
