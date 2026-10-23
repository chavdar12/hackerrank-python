import numpy


def mean_var_std(matrix):
    a = numpy.array(matrix, int)
    return numpy.mean(a, axis=1), numpy.var(a, axis=0), round(numpy.std(a), 11)
