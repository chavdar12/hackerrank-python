import unittest

from solutions.collection_types.company_logo import top_three
from solutions.collection_types.counter import shoe_shop_earnings
from solutions.collection_types.defaultdict_tutorial import word_positions
from solutions.collection_types.deque import run_deque
from solutions.collection_types.namedtuple import average_marks
from solutions.collection_types.ordered_dict import net_prices
from solutions.collection_types.piling_up import can_pile
from solutions.collection_types.word_order import word_order


class TestCounter(unittest.TestCase):
    def test_sample(self):
        sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
        orders = [(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)]
        self.assertEqual(shoe_shop_earnings(sizes, orders), 200)


class TestDefaultdict(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(word_positions(["a", "a", "b", "a", "b"], ["a", "b", "c"]),
                         [[1, 2, 4], [3, 5], [-1]])


class TestNamedtuple(unittest.TestCase):
    def test_columns_in_any_order(self):
        rows = [["97", "Raymond", "7", "1"], ["50", "Steven", "4", "2"], ["91", "Adrian", "9", "3"],
                ["72", "Stewart", "5", "4"], ["80", "Peter", "6", "5"]]
        self.assertEqual(average_marks(["MARKS", "NAME", "CLASS", "ID"], rows), "78.00")


class TestOrderedDict(unittest.TestCase):
    def test_sample(self):
        lines = ["BANANA FRIES 12", "POTATO CHIPS 30", "APPLE JUICE 10", "CANDY 5",
                 "APPLE JUICE 10", "CANDY 5", "CANDY 5", "CANDY 5", "POTATO CHIPS 30"]
        self.assertEqual(net_prices(lines), [
            ("BANANA FRIES", 12), ("POTATO CHIPS", 60), ("APPLE JUICE", 20), ("CANDY", 20),
        ])


class TestWordOrder(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(word_order(["bcdef", "abcdefg", "bcde", "bcdef"]), (3, [2, 1, 1]))


class TestDeque(unittest.TestCase):
    def test_sample(self):
        operations = ["append 1", "append 2", "append 3", "appendleft 4", "pop", "popleft"]
        self.assertEqual(run_deque(operations), [1, 2])


class TestCompanyLogo(unittest.TestCase):
    def test_ties_broken_alphabetically(self):
        self.assertEqual(top_three("aabbbccde"), [("b", 3), ("a", 2), ("c", 2)])


class TestPilingUp(unittest.TestCase):
    def test_possible(self):
        self.assertTrue(can_pile([4, 3, 2, 1, 3, 4]))

    def test_impossible(self):
        self.assertFalse(can_pile([1, 3, 2]))

    def test_does_not_mutate_input(self):
        blocks = [2, 1, 2]
        can_pile(blocks)
        self.assertEqual(blocks, [2, 1, 2])


if __name__ == "__main__":
    unittest.main()
