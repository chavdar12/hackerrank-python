import numpy


def determinant(matrix):
    return round(numpy.linalg.det(numpy.array(matrix, float)), 2)
