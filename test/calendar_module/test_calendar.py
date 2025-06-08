import unittest
from src.calendar_module.util import find_day

class TestFindDay(unittest.TestCase):

    def test_known_dates(self):
        self.assertEqual(find_day(6, 8, 2025), 'SUNDAY')
        self.assertEqual(find_day(1, 1, 2000), 'SATURDAY')
        self.assertEqual(find_day(12, 25, 2023), 'MONDAY')

    def test_leap_year(self):
        self.assertEqual(find_day(2, 29, 2024), 'THURSDAY')

    def test_edge_case(self):
        self.assertEqual(find_day(12, 31, 1999), 'FRIDAY')

if __name__ == '__main__':
    unittest.main()
