import unittest
from src.colections_namedtuples.util import calculate_average_marks

class TestCalculateAverageMarks(unittest.TestCase):

    def test_average_case(self):
        students = ["A001 90", "A002 80", "A003 70", "A004 60"]
        self.assertEqual(calculate_average_marks(4, ['ID', 'MARKS'], students), 75.0)

    def test_all_same_marks(self):
        students = ["A001 100", "A002 100", "A003 100"]
        self.assertEqual(calculate_average_marks(3, ['ID', 'MARKS'], students), 100.0)

    def test_mixed_data(self):
        students = ["S1 0", "S2 50", "S3 100"]
        self.assertEqual(calculate_average_marks(3, ['ID', 'MARKS'], students), 50.0)

if __name__ == '__main__':
    unittest.main()
