import unittest
from lab4_6 import flatten_2 

class TestFlattenFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_2([[]]), [])

    def test_non_empty_lists(self):
        self.assertEqual(flatten_2([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_mixed_types_and_empty_list(self):
        self.assertEqual(flatten_2([["1", 1.1], []]), ["1", 1.1])

if __name__ == '__main__':
    unittest.main()