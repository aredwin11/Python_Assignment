import unittest
from src.iterables_iterators.util import probability_of_a

class TestProbabilityOfA(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(probability_of_a(['a', 'b', 'c'], 2), 0.667)

    def test_no_a(self):
        self.assertEqual(probability_of_a(['b', 'c', 'd'], 2), 0.000)

    def test_all_a(self):
        self.assertEqual(probability_of_a(['a', 'a', 'a'], 2), 1.000)

    def test_k_equals_n(self):
        self.assertEqual(probability_of_a(['a', 'b'], 2), 1.000)

    def test_k_greater_than_n(self):
        self.assertEqual(probability_of_a(['a', 'b'], 3), 0.0)

if __name__ == '__main__':
    unittest.main()
