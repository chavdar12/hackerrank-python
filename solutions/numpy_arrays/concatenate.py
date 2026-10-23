import numpy


def concatenate(a, b):
    return numpy.concatenate((numpy.array(a, int), numpy.array(b, int)), axis=0)
