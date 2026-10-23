import numpy


def transpose_and_flatten(matrix):
    m = numpy.array(matrix, int)
    return m.transpose(), m.flatten()
