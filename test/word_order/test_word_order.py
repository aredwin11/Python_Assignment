import unittest
from src.word_order.util import count_words

class TestWordCount(unittest.TestCase):

    def test_basic(self):
        words = ["a", "b", "a", "c", "b"]
        self.assertEqual(count_words(words), (3, [2, 2, 1]))

    def test_single(self):
        words = ["hello"]
        self.assertEqual(count_words(words), (1, [1]))

    def test_all_unique(self):
        words = ["one", "two", "three"]
        self.assertEqual(count_words(words), (3, [1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
