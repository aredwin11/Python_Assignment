import unittest
from src.second_maximum_in_the_list.util import second_largest

class TestSecondLargest(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(second_largest([1, 2, 3, 4, 5]), 4)

    def test_with_duplicates(self):
        self.assertEqual(second_largest([2, 3, 6, 6, 5]), 5)

    def test_all_same(self):
        with self.assertRaises(ValueError):
            second_largest([1, 1, 1])

    def test_negative_numbers(self):
        self.assertEqual(second_largest([-1, -2, -3, -4]), -2)

if __name__ == '__main__':
    unittest.main()
