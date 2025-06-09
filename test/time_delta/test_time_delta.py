# test_util.py
import unittest
from src.time_delta.util import time_delta

class TestTimeDelta(unittest.TestCase):

    def test_case_1(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "25200")

    def test_case_2(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "88200")

    def test_zero_diff(self):
        t1 = "Sun 10 May 2015 13:54:36 -0000"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "0")

if __name__ == '__main__':
    unittest.main()
