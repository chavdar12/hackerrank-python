import unittest

import numpy
from numpy.testing import assert_array_equal

from solutions.numpy_arrays.array_mathematics import array_mathematics
from solutions.numpy_arrays.arrays import arrays
from solutions.numpy_arrays.concatenate import concatenate
from solutions.numpy_arrays.dot_and_cross import matrix_product
from solutions.numpy_arrays.eye_and_identity import eye
from solutions.numpy_arrays.floor_ceil_and_rint import floor_ceil_rint
from solutions.numpy_arrays.inner_and_outer import inner_and_outer
from solutions.numpy_arrays.linear_algebra import determinant
from solutions.numpy_arrays.mean_var_and_std import mean_var_std
from solutions.numpy_arrays.min_and_max import max_of_row_mins
from solutions.numpy_arrays.polynomials import evaluate_polynomial
from solutions.numpy_arrays.shape_and_reshape import reshape_3x3
from solutions.numpy_arrays.sum_and_prod import product_of_column_sums
from solutions.numpy_arrays.transpose_and_flatten import transpose_and_flatten
from solutions.numpy_arrays.zeros_and_ones import zeros_and_ones


class TestArrays(unittest.TestCase):
    def test_reversed_float(self):
        result = arrays(["1", "2", "3", "4", "-8", "-10"])
        self.assertEqual(result.dtype, numpy.float32)
        assert_array_equal(result, [-10, -8, 4, 3, 2, 1])


class TestShapeAndReshape(unittest.TestCase):
    def test_sample(self):
        assert_array_equal(reshape_3x3("1 2 3 4 5 6 7 8 9".split()), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


class TestTransposeAndFlatten(unittest.TestCase):
    def test_sample(self):
        t, flat = transpose_and_flatten([["1", "2"], ["3", "4"]])
        assert_array_equal(t, [[1, 3], [2, 4]])
        assert_array_equal(flat, [1, 2, 3, 4])


class TestConcatenate(unittest.TestCase):
    def test_rows_appended(self):
        assert_array_equal(concatenate([[1, 2]], [[3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])


class TestZerosAndOnes(unittest.TestCase):
    def test_shape_and_dtype(self):
        zeros, ones = zeros_and_ones((3, 3, 3))
        self.assertEqual(zeros.shape, (3, 3, 3))
        self.assertEqual(zeros.sum(), 0)
        self.assertEqual(ones.sum(), 27)
        self.assertTrue(numpy.issubdtype(ones.dtype, numpy.integer))


class TestEyeAndIdentity(unittest.TestCase):
    def test_non_square(self):
        assert_array_equal(eye(2, 3), [[1, 0, 0], [0, 1, 0]])


class TestArrayMathematics(unittest.TestCase):
    def test_sample(self):
        results = array_mathematics([[1, 2, 3, 4]], [[5, 6, 7, 8]])
        expected = [[[6, 8, 10, 12]], [[-4, -4, -4, -4]], [[5, 12, 21, 32]],
                    [[0, 0, 0, 0]], [[1, 2, 3, 4]], [[1, 64, 2187, 65536]]]
        for result, want in zip(results, expected):
            assert_array_equal(result, want)


class TestFloorCeilRint(unittest.TestCase):
    def test_sample(self):
        floor, ceil, rint = floor_ceil_rint(["1.1", "2.5", "-3.5"])
        assert_array_equal(floor, [1, 2, -4])
        assert_array_equal(ceil, [2, 3, -3])
        assert_array_equal(rint, [1, 2, -4])


class TestSumAndProd(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(product_of_column_sums([[1, 2], [3, 4]]), 24)


class TestMinAndMax(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(max_of_row_mins([[2, 5], [3, 7], [1, 3], [4, 0]]), 3)


class TestMeanVarStd(unittest.TestCase):
    def test_sample(self):
        mean, var, std = mean_var_std([[1, 2], [3, 4]])
        assert_array_equal(mean, [1.5, 3.5])
        assert_array_equal(var, [1, 1])
        self.assertEqual(std, 1.11803398875)


class TestDotAndCross(unittest.TestCase):
    def test_sample(self):
        assert_array_equal(matrix_product([[1, 2], [3, 4]], [[1, 2], [3, 4]]), [[7, 10], [15, 22]])


class TestInnerAndOuter(unittest.TestCase):
    def test_sample(self):
        inner, outer = inner_and_outer([0, 1], [2, 3])
        self.assertEqual(inner, 3)
        assert_array_equal(outer, [[0, 0], [2, 3]])


class TestPolynomials(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(evaluate_polynomial(["1.1", "2", "3"], 0), 3.0)
        self.assertEqual(evaluate_polynomial([1, 2, 3], 2), 11.0)


class TestLinearAlgebra(unittest.TestCase):
    def test_sample(self):
        self.assertAlmostEqual(determinant([[1.1, 1.1], [1.1, 1.1]]), 0.0)
        self.assertEqual(determinant([[2, 0], [0, 3]]), 6.0)


if __name__ == "__main__":
    unittest.main()
