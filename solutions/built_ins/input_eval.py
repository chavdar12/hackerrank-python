def polynomial_equals(x, k, polynomial):
    return eval(polynomial, {"__builtins__": {}}, {"x": x}) == k
