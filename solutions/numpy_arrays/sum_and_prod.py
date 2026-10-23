import numpy


def product_of_column_sums(matrix):
    return numpy.prod(numpy.sum(numpy.array(matrix, int), axis=0))
