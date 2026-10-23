import unittest

from solutions.decorators.name_directory import name_format
from solutions.decorators.standardize_mobile_number import sort_phone


class TestStandardizeMobileNumber(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sort_phone(["07895462130", "919875641230", "9195969878"]),
                         ["+91 78954 62130", "+91 91959 69878", "+91 98756 41230"])


class TestNameDirectory(unittest.TestCase):
    def test_sample(self):
        people = [["Mike", "Thomson", "20", "M"], ["Robert", "Bustle", "32", "M"], ["Andria", "Bustle", "30", "F"]]
        self.assertEqual(name_format(people), ["Mr. Mike Thomson", "Ms. Andria Bustle", "Mr. Robert Bustle"])

    def test_ties_keep_input_order(self):
        people = [["B", "X", "20", "F"], ["A", "Y", "20", "M"]]
        self.assertEqual(name_format(people), ["Ms. B X", "Mr. A Y"])


if __name__ == "__main__":
    unittest.main()
