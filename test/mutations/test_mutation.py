import unittest
from src.mutations.util import mutate_string

class TestMutateString(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(mutate_string("hello", 1, "a"), "hallo")

    def test_start(self):
        self.assertEqual(mutate_string("world", 0, "W"), "World")

    def test_end(self):
        self.assertEqual(mutate_string("python", 5, "n"), "python")

    def test_replace_with_same_char(self):
        self.assertEqual(mutate_string("test", 2, "s"), "test")

if __name__ == '__main__':
    unittest.main()
