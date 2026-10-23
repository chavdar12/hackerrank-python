import unittest

from solutions.strings.alphabet_rangoli import rangoli
from solutions.strings.capitalize import solve
from solutions.strings.designer_door_mat import door_mat
from solutions.strings.find_a_string import count_substring
from solutions.strings.merge_the_tools import merge_the_tools
from solutions.strings.minion_game import minion_game
from solutions.strings.mutations import mutate_string
from solutions.strings.split_and_join import split_and_join
from solutions.strings.string_formatting import formatted
from solutions.strings.string_validators import validate
from solutions.strings.swap_case import swap_case
from solutions.strings.text_alignment import logo
from solutions.strings.text_wrap import wrap
from solutions.strings.whats_your_name import full_name_greeting


class TestSwapCase(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(swap_case("HackerRank.com presents \"Pythonist 2\"."),
                         "hACKERrANK.COM PRESENTS \"pYTHONIST 2\".")


class TestSplitAndJoin(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(split_and_join("this is a string"), "this-is-a-string")


class TestWhatsYourName(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(full_name_greeting("Ross", "Taylor"),
                         "Hello Ross Taylor! You just delved into python.")


class TestMutations(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(mutate_string("abracadabra", 5, "k"), "abrackdabra")


class TestFindAString(unittest.TestCase):
    def test_overlapping(self):
        self.assertEqual(count_substring("ABCDCDC", "CDC"), 2)

    def test_absent(self):
        self.assertEqual(count_substring("ABC", "Z"), 0)


class TestStringValidators(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(validate("qA2"), (True, True, True, True, True))

    def test_symbols_only(self):
        self.assertEqual(validate("#$%"), (False,) * 5)


class TestTextAlignment(unittest.TestCase):
    def test_shape(self):
        rows = logo(5)
        self.assertEqual(len(rows), 5 + 6 + 3 + 6 + 5)
        self.assertEqual(rows[0], "    H    ")
        self.assertEqual(rows[-1].strip(), "H")


class TestTextWrap(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4),
                         "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ")


class TestDesignerDoorMat(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(door_mat(7, 21), [
            "---------.|.---------",
            "------.|..|..|.------",
            "---.|..|..|..|..|.---",
            "-------WELCOME-------",
            "---.|..|..|..|..|.---",
            "------.|..|..|.------",
            "---------.|.---------",
        ])


class TestStringFormatting(unittest.TestCase):
    def test_rows(self):
        rows = formatted(17)
        self.assertEqual(rows[0], "    1     1     1     1")
        self.assertEqual(rows[-1], "   17    21    11 10001")


class TestAlphabetRangoli(unittest.TestCase):
    def test_size_3(self):
        self.assertEqual(rangoli(3), [
            "----c----",
            "--c-b-c--",
            "c-b-a-b-c",
            "--c-b-c--",
            "----c----",
        ])


class TestCapitalize(unittest.TestCase):
    def test_keeps_spacing(self):
        self.assertEqual(solve("chris  alan 12abc"), "Chris  Alan 12abc")


class TestMinionGame(unittest.TestCase):
    def test_stuart(self):
        self.assertEqual(minion_game("BANANA"), "Stuart 12")

    def test_kevin(self):
        self.assertEqual(minion_game("A"), "Kevin 1")

    def test_draw(self):
        self.assertEqual(minion_game("BAA"), "Draw")


class TestMergeTheTools(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(merge_the_tools("AABCAAADA", 3), ["AB", "CA", "AD"])


if __name__ == "__main__":
    unittest.main()
