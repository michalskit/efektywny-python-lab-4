import unittest
from lab4_5 import all_are_positive_2

class TestAllArePositive(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertTrue(all_are_positive_2([]))

    def test_all_positive_numbers(self):
        self.assertTrue(all_are_positive_2([1, 2, 3]))

    def test_contains_negative_number(self):
        self.assertFalse(all_are_positive_2([-1, 2, 3]))

    def test_multiple_negative_number(self):
        self.assertFalse(all_are_positive_2([5, 6, -2, 1]))

if __name__ == "__main__":
    unittest.main()