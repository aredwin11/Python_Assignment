import unittest
from src.no_idea.util import calculate_happiness

class TestHappinessScore(unittest.TestCase):

    def test_basic_case(self):
        arr = [1, 5, 3]
        A = {3, 1}
        B = {5, 7}
        self.assertEqual(calculate_happiness(arr, A, B), 1)

    def test_all_positive(self):
        arr = [1, 2, 3]
        A = {1, 2, 3}
        B = set()
        self.assertEqual(calculate_happiness(arr, A, B), 3)

    def test_all_negative(self):
        arr = [1, 2, 3]
        A = set()
        B = {1, 2, 3}
        self.assertEqual(calculate_happiness(arr, A, B), -3)

    def test_neutral(self):
        arr = [4, 5, 6]
        A = {1, 2}
        B = {7, 8}
        self.assertEqual(calculate_happiness(arr, A, B), 0)

if __name__ == '__main__':
    unittest.main()
