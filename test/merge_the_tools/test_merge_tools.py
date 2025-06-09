import unittest
from src.merge_the_tools.util import merge_the_tools

class TestMergeTheTools(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(
            merge_the_tools("AABCAAADA", 3),
            ['AB', 'CA', 'AD']
        )

    def test_all_unique(self):
        self.assertEqual(
            merge_the_tools("ABCDEFGHI", 3),
            ['ABC', 'DEF', 'GHI']
        )

    def test_all_duplicates(self):
        self.assertEqual(
            merge_the_tools("AAAAAAAAAA", 2),
            ['A'] * 5
        )

    def test_k_equals_len(self):
        self.assertEqual(
            merge_the_tools("ABCD", 4),
            ['ABCD']
        )

if __name__ == '__main__':
    unittest.main()
