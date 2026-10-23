import numpy


def max_of_row_mins(matrix):
    return numpy.max(numpy.min(numpy.array(matrix, int), axis=1))
