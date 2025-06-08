import unittest
import numpy as np
from src.floor_ceil_rint.util import apply_numpy_operations

class TestNumpyOperations(unittest.TestCase):

    def test_basic_operations(self):
        numbers = [1.1, 2.5, 3.9, -1.2, -2.8]
        floor_expected = np.array([1., 2., 3., -2., -3.])
        ceil_expected = np.array([2., 3., 4., -1., -2.])
        rint_expected = np.array([1., 2., 4., -1., -3.])

        floor, ceil, rint = apply_numpy_operations(numbers)

        np.testing.assert_array_equal(floor, floor_expected)
        np.testing.assert_array_equal(ceil, ceil_expected)
        np.testing.assert_array_equal(rint, rint_expected)

if __name__ == '__main__':
    unittest.main()
