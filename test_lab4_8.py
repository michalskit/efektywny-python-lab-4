import unittest
from lab4_8 import product_greater_than

class TestProductGreaterThan(unittest.TestCase):
    
    def test_product_no_condition(self):
        self.assertEqual(product_greater_than([1, 2, 3]), 6)
    
    def test_product_with_condition(self):
        self.assertEqual(product_greater_than([1, 2, 3], 2), 3)
    
    def test_product_with_negative(self):
        self.assertEqual(product_greater_than([-4, 5, 10, 23, 123], -5), -565800)

if __name__ == "__main__":
    unittest.main()
