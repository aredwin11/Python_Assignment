import unittest
from src.finding_the_percentage.util import calculate_student_average

class TestStudentAverage(unittest.TestCase):

    def test_average_for_existing_student(self):
        data = {
            'Alice': [80.0, 90.0, 100.0],
            'Bob': [60.0, 70.0, 80.0]
        }
        self.assertEqual(calculate_student_average(data, 'Alice'), 90.0)

    def test_student_not_found(self):
        data = {
            'Alice': [80.0, 90.0],
        }
        with self.assertRaises(ValueError):
            calculate_student_average(data, 'Charlie')

    def test_float_precision(self):
        data = {
            'Tom': [66.6666, 66.6666, 66.6666],
        }
        self.assertEqual(calculate_student_average(data, 'Tom'), 66.67)

if __name__ == '__main__':
    unittest.main()
