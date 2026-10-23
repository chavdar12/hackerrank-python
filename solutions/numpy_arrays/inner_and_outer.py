import numpy


def inner_and_outer(a, b):
    a, b = numpy.array(a, int), numpy.array(b, int)
    return numpy.inner(a, b), numpy.outer(a, b)
