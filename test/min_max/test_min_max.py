import unittest
from src.min_max.util import max_of_row_mins

class TestMaxOfRowMins(unittest.TestCase):

    def test_example(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # row mins = [1, 4, 7], max of those is 7
        self.assertEqual(max_of_row_mins(matrix), 7)

    def test_equal_rows(self):
        matrix = [
            [5, 5],
            [5, 5],
            [5, 5]
        ]
        self.assertEqual(max_of_row_mins(matrix), 5)

    def test_single_row(self):
        matrix = [[2, 3, 1, 4]]
        self.assertEqual(max_of_row_mins(matrix), 1)

if __name__ == '__main__':
    unittest.main()
