import unittest

from solutions.errors.exceptions import safe_divide
from solutions.errors.incorrect_regex import is_valid_regex


class TestExceptions(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(safe_divide("3", "1"), "3")

    def test_zero_division(self):
        self.assertEqual(safe_divide("1", "0"), "Error Code: integer division or modulo by zero")

    def test_bad_int(self):
        self.assertEqual(safe_divide("2", "$"), "Error Code: invalid literal for int() with base 10: '$'")


class TestIncorrectRegex(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(is_valid_regex(".*\\+"))
        self.assertFalse(is_valid_regex(".*+"))


if __name__ == "__main__":
    unittest.main()
