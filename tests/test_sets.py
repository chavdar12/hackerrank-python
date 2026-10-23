import unittest

from solutions.sets.add import distinct_count
from solutions.sets.captains_room import captains_room
from solutions.sets.check_strict_superset import is_strict_superset
from solutions.sets.check_subset import is_subset
from solutions.sets.difference import difference_count
from solutions.sets.discard_remove_pop import apply_commands
from solutions.sets.intersection import intersection_count
from solutions.sets.introduction_to_sets import average
from solutions.sets.mutations import apply_mutations
from solutions.sets.no_idea import happiness
from solutions.sets.symmetric_difference import symmetric_difference
from solutions.sets.symmetric_difference_operation import symmetric_difference_count
from solutions.sets.union import union_count

ENGLISH = {1, 2, 3, 4, 5, 6, 7, 8, 9}
FRENCH = {10, 1, 2, 3, 11, 21, 55, 6, 8}


class TestIntroductionToSets(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]), 169.375)


class TestNoIdea(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(happiness([1, 5, 3], {3, 1}, {5, 7}), 1)


class TestSymmetricDifference(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(symmetric_difference({2, 4, 5, 9}, {2, 4, 11, 12}), [5, 9, 11, 12])


class TestAdd(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(distinct_count(["UK", "China", "USA", "France", "New Zealand", "UK", "France"]), 5)


class TestDiscardRemovePop(unittest.TestCase):
    def test_remove_and_discard(self):
        self.assertEqual(apply_commands([1, 2, 3, 4], ["remove 4", "discard 9", "discard 1"]), 5)

    def test_pop_removes_one(self):
        self.assertIn(apply_commands([1, 2], ["pop"]), (1, 2))

    def test_remove_missing_raises(self):
        with self.assertRaises(KeyError):
            apply_commands([1], ["remove 5"])


class TestSetOperationCounts(unittest.TestCase):
    def test_union(self):
        self.assertEqual(union_count(ENGLISH, FRENCH), 13)

    def test_intersection(self):
        self.assertEqual(intersection_count(ENGLISH, FRENCH), 5)

    def test_difference(self):
        self.assertEqual(difference_count(ENGLISH, FRENCH), 4)

    def test_symmetric_difference(self):
        self.assertEqual(symmetric_difference_count(ENGLISH, FRENCH), 8)


class TestSetMutations(unittest.TestCase):
    def test_sample(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52]
        operations = [
            ("intersection_update", {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}),
            ("update", {55, 66}),
            ("symmetric_difference_update", {22, 7, 35, 62, 58}),
            ("difference_update", {11, 22, 35, 55, 58, 62, 66}),
        ]
        self.assertEqual(apply_mutations(numbers, operations), 38)


class TestCaptainsRoom(unittest.TestCase):
    def test_sample(self):
        rooms = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
        self.assertEqual(captains_room(5, rooms), 8)


class TestCheckSubset(unittest.TestCase):
    def test_subset(self):
        self.assertTrue(is_subset({1, 2, 3, 5, 6}, {9, 8, 5, 6, 3, 2, 1, 4, 7}))
        self.assertFalse(is_subset({2}, {3, 6, 5, 4, 1}))


class TestCheckStrictSuperset(unittest.TestCase):
    def test_sample(self):
        a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78}
        self.assertFalse(is_strict_superset(a, [{1, 2, 3, 4, 5}, {100, 11, 12}]))

    def test_equal_set_is_not_strict(self):
        self.assertFalse(is_strict_superset({1, 2}, [{1, 2}]))
        self.assertTrue(is_strict_superset({1, 2, 3}, [{1, 2}, {3}]))


if __name__ == "__main__":
    unittest.main()
