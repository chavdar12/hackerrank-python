import unittest

from solutions.errors.exceptions import safe_divide
from solutions.errors.incorrect_regex import is_valid_regex


class TestExceptions(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(safe_divide("3", "1"), "3")

    def test_zero_division(self):
        # the message differs between Python versions, so compare with the running interpreter's
        try:
            1 // 0
        except ZeroDivisionError as e:
            expected = f"Error Code: {e}"
        self.assertEqual(safe_divide("1", "0"), expected)

    def test_bad_int(self):
        self.assertEqual(safe_divide("2", "$"), "Error Code: invalid literal for int() with base 10: '$'")


class TestIncorrectRegex(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(is_valid_regex(".*\\+"))
        # HackerRank's sample ".*+" is valid since Python 3.11 (possessive quantifier); "a**" is invalid in every version
        self.assertFalse(is_valid_regex("a**"))


if __name__ == "__main__":
    unittest.main()
