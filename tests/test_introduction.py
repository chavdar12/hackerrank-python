import unittest

from solutions.introduction.arithmetic_operators import arithmetic
from solutions.introduction.division import divide
from solutions.introduction.hello_world import hello_world
from solutions.introduction.if_else import weird
from solutions.introduction.leap_year import is_leap
from solutions.introduction.loops import squares
from solutions.introduction.print_function import concat_numbers


class TestHelloWorld(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(hello_world(), "Hello, World!")


class TestIfElse(unittest.TestCase):
    def test_ranges(self):
        self.assertEqual(weird(3), "Weird")
        self.assertEqual(weird(4), "Not Weird")
        self.assertEqual(weird(6), "Weird")
        self.assertEqual(weird(20), "Weird")
        self.assertEqual(weird(24), "Not Weird")


class TestArithmetic(unittest.TestCase):
    def test_sum_diff_product(self):
        self.assertEqual(arithmetic(3, 2), (5, 1, 6))


class TestDivision(unittest.TestCase):
    def test_integer_and_float(self):
        self.assertEqual(divide(4, 3), (1, 4 / 3))


class TestLoops(unittest.TestCase):
    def test_squares(self):
        self.assertEqual(squares(5), [0, 1, 4, 9, 16])


class TestLeapYear(unittest.TestCase):
    def test_years(self):
        self.assertTrue(is_leap(2000))
        self.assertTrue(is_leap(2024))
        self.assertFalse(is_leap(1900))
        self.assertFalse(is_leap(1990))


class TestPrintFunction(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(concat_numbers(3), "123")
        self.assertEqual(concat_numbers(12), "123456789101112")


if __name__ == "__main__":
    unittest.main()
