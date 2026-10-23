def wrapper(f):
    def fun(numbers):
        return f([f"+91 {n[-10:-5]} {n[-5:]}" for n in numbers])
    return fun


@wrapper
def sort_phone(numbers):
    return sorted(numbers)
