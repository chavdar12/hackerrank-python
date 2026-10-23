import unittest
from fractions import Fraction

from solutions.functionals.email_filter import filter_mail, fun
from solutions.functionals.fibonacci_cubes import cube, fibonacci
from solutions.functionals.reduce_function import product


class TestFibonacciCubes(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(list(map(cube, fibonacci(5))), [0, 1, 1, 8, 27])

    def test_short(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])


class TestEmailFilter(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(fun("lara@hackerrank.com"))
        self.assertTrue(fun("brian-23@hackerrank.com"))
        self.assertTrue(fun("britts_54@hackerrank.com"))

    def test_invalid(self):
        self.assertFalse(fun("harsh@gmail"))
        self.assertFalse(fun("its@gmail.com1"))
        self.assertFalse(fun("abc.def@gmail.com"))

    def test_filter(self):
        self.assertEqual(filter_mail(["a@b.c", "bad"]), ["a@b.c"])


class TestReduceFunction(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(product([Fraction(1, 2), Fraction(3, 4), Fraction(10, 6)]), (5, 8))


if __name__ == "__main__":
    unittest.main()
