import unittest

from solutions.data_types.finding_the_percentage import average_marks
from solutions.data_types.list_comprehensions import coordinates
from solutions.data_types.lists import run_commands
from solutions.data_types.nested_lists import second_lowest_names
from solutions.data_types.runner_up_score import runner_up
from solutions.data_types.tuples import tuple_hash


class TestListComprehensions(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(
            coordinates(1, 1, 1, 2),
            [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
        )


class TestRunnerUp(unittest.TestCase):
    def test_duplicates_of_max(self):
        self.assertEqual(runner_up([2, 3, 6, 6, 5]), 5)


class TestNestedLists(unittest.TestCase):
    def test_sample(self):
        students = [("Harry", 37.21), ("Berry", 37.21), ("Tina", 37.2), ("Akriti", 41), ("Harsh", 39)]
        self.assertEqual(second_lowest_names(students), ["Berry", "Harry"])


class TestFindingThePercentage(unittest.TestCase):
    def test_sample(self):
        marks = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}
        self.assertEqual(average_marks(marks, "Malika"), "56.00")


class TestLists(unittest.TestCase):
    def test_sample(self):
        commands = [
            "insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9",
            "append 1", "sort", "print", "pop", "reverse", "print",
        ]
        self.assertEqual(run_commands(commands), [[6, 5, 10], [1, 5, 9, 10], [9, 5, 1]])


class TestTuples(unittest.TestCase):
    def test_matches_builtin_hash(self):
        self.assertEqual(tuple_hash([1, 2]), hash((1, 2)))


if __name__ == "__main__":
    unittest.main()
