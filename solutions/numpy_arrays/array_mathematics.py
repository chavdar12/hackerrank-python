import numpy


def array_mathematics(a, b):
    a, b = numpy.array(a, int), numpy.array(b, int)
    return a + b, a - b, a * b, a // b, a % b, a ** b
