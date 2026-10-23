import unittest

from solutions.built_ins.any_or_all import any_or_all
from solutions.built_ins.athlete_sort import sort_by_attribute
from solutions.built_ins.ginorts import ginorts
from solutions.built_ins.input_eval import polynomial_equals
from solutions.built_ins.python_evaluation import evaluate
from solutions.built_ins.zipped import student_averages


class TestZipped(unittest.TestCase):
    def test_sample(self):
        subjects = [[89, 90, 78, 93, 80], [90, 91, 85, 88, 86], [91, 92, 83, 89, 90.5]]
        averages = student_averages(subjects)
        self.assertEqual([round(a, 1) for a in averages], [90.0, 91.0, 82.0, 90.0, 85.5])


class TestInput(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(polynomial_equals(1, 4, "x**3 + x**2 + x + 1"))
        self.assertFalse(polynomial_equals(2, 4, "x**3 + x**2 + x + 1"))


class TestPythonEvaluation(unittest.TestCase):
    def test_expression(self):
        self.assertEqual(evaluate("2 + 3 * 4"), 14)


class TestAthleteSort(unittest.TestCase):
    def test_stable(self):
        rows = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
        self.assertEqual(sort_by_attribute(rows, 1), [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]])


class TestGinorts(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(ginorts("Sorting1234"), "ginortS1324")


class TestAnyOrAll(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(any_or_all([12, 9, 61, 5, 14]))

    def test_negative(self):
        self.assertFalse(any_or_all([-1, 5]))

    def test_no_palindrome(self):
        self.assertFalse(any_or_all([12, 34]))


if __name__ == "__main__":
    unittest.main()
