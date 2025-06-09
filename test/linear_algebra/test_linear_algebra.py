import unittest
from src.linear_algebra.util import calculate_determinant

class TestDeterminant(unittest.TestCase):

    def test_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(calculate_determinant(matrix), -2.0)

    def test_3x3_matrix(self):
        matrix = [[6,1,1],[4,-2,5],[2,8,7]]
        self.assertEqual(calculate_determinant(matrix), -306.0)

    def test_identity_matrix(self):
        matrix = [[1,0,0],[0,1,0],[0,0,1]]
        self.assertEqual(calculate_determinant(matrix), 1.0)

    def test_zero_matrix(self):
        matrix = [[0,0],[0,0]]
        self.assertEqual(calculate_determinant(matrix), 0.0)

if __name__ == '__main__':
    unittest.main()
