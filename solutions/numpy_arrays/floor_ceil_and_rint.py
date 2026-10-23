import numpy


def floor_ceil_rint(values):
    a = numpy.array(values, float)
    return numpy.floor(a), numpy.ceil(a), numpy.rint(a)
