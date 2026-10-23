import unittest

from solutions.debugging.default_arguments import OddStream, values_from_stream
from solutions.debugging.words_score import score_words


class TestDefaultArguments(unittest.TestCase):
    def test_default_stream_is_fresh_each_call(self):
        self.assertEqual(values_from_stream(3), [0, 2, 4])
        self.assertEqual(values_from_stream(2), [0, 2])

    def test_odd_stream(self):
        self.assertEqual(values_from_stream(3, OddStream()), [1, 3, 5])


class TestWordsScore(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(score_words(["hacker", "book"]), 4)
        self.assertEqual(score_words(["programming", "is", "awesome"]), 4)

    def test_y_is_a_vowel(self):
        self.assertEqual(score_words(["by"]), 1)


if __name__ == "__main__":
    unittest.main()
