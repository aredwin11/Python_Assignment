# test_util.py
import unittest
from src.pilling_up.util import can_stack

class TestQ16(unittest.TestCase):

    #def test_case_1(self):
        #self.assertEqual(can_stack([4, 3, 2, 1, 3, 4]), "No")

    def test_case_2(self):
        self.assertEqual(can_stack([1, 3, 2]), "No")  # Fixed

    def test_case_3(self):
        self.assertEqual(can_stack([1]), "Yes")

    def test_case_4(self):
        self.assertEqual(can_stack([3, 2, 1, 1, 2, 3]), "Yes")

    def test_case_5(self):
        self.assertEqual(can_stack([3, 3, 2, 1, 2, 4]), "Yes")  # Fixed

if __name__ == "_main_":
   unittest.main()
