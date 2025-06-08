import unittest
import numpy as np
from src.mean_var_std.util import calculate_value

class TestStatistics(unittest.TestCase):

    def test_small_matrix(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        mean_expected = np.array([1.5, 3.5])
        var_expected = np.array([1.0, 1.0])
        std_expected = round(np.std(np.array(matrix)), 11)

        mean, var, std = calculate_value(matrix)
        np.testing.assert_array_almost_equal(mean, mean_expected)
        np.testing.assert_array_almost_equal(var, var_expected)
        self.assertEqual(std, std_expected)

    def test_single_element(self):
        matrix = [[5]]
        mean_expected = np.array([5.0])
        var_expected = np.array([0.0])
        std_expected = 0.0

        mean, var, std = calculate_value(matrix)
        np.testing.assert_array_equal(mean, mean_expected)
        np.testing.assert_array_equal(var, var_expected)
        self.assertEqual(std, std_expected)

if __name__ == '__main__':
    unittest.main()
