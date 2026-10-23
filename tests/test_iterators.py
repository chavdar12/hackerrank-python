import unittest

from solutions.iterators.combinations import sorted_combinations
from solutions.iterators.combinations_with_replacement import sorted_combinations_with_replacement
from solutions.iterators.compress_the_string import compress
from solutions.iterators.iterables_and_iterators import probability_of_a
from solutions.iterators.maximize_it import maximize
from solutions.iterators.permutations import sorted_permutations
from solutions.iterators.product import cartesian_product


class TestProduct(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(cartesian_product([1, 2], [3, 4]), [(1, 3), (1, 4), (2, 3), (2, 4)])


class TestPermutations(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sorted_permutations("HACK", 2), [
            "AC", "AH", "AK", "CA", "CH", "CK", "HA", "HC", "HK", "KA", "KC", "KH",
        ])


class TestCombinations(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sorted_combinations("HACK", 2), [
            "A", "C", "H", "K", "AC", "AH", "AK", "CH", "CK", "HK",
        ])


class TestCombinationsWithReplacement(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sorted_combinations_with_replacement("HACK", 2), [
            "AA", "AC", "AH", "AK", "CC", "CH", "CK", "HH", "HK", "KK",
        ])


class TestCompressTheString(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(compress("1222311"), [(1, 1), (3, 2), (1, 3), (2, 1)])


class TestIterablesAndIterators(unittest.TestCase):
    def test_sample(self):
        self.assertAlmostEqual(probability_of_a(["a", "a", "c", "d"], 2), 0.8333, places=4)

    def test_no_a(self):
        self.assertEqual(probability_of_a(["b", "c"], 1), 0)


class TestMaximizeIt(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(maximize(1000, [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]), 206)


if __name__ == "__main__":
    unittest.main()
