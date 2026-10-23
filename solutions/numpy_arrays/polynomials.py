import numpy


def evaluate_polynomial(coefficients, x):
    return numpy.polyval(numpy.array(coefficients, float), x)
