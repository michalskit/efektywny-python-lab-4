import unittest
from types import GeneratorType
from lab4_1 import _filter

class TestFilterFunction(unittest.TestCase):

    def test_returns_generator(self):
        self.assertTrue(isinstance(_filter(lambda x: True, []), GeneratorType))

    def test_filter_with_function(self):
        self.assertEqual(list(filter(lambda x: x > 0, [0, -3, 1, 6])),
                        list(_filter(lambda x: x > 0, [0, -3, 1, 6])))

    def test_filter_without_function(self):
        self.assertEqual(list(filter(None, [2, -3, 1, 6])), 
                        list(_filter(None, [2, -3, 1, 6])))

    def test_filter_bool_values(self):
        self.assertEqual(list(filter(None, [True, False, False])), 
                        list(_filter(None, [True, False, False])))

    def test_filter_with_none_function(self):
        self.assertEqual(list(filter(None, [0, -3, 1, 6])), 
                        list(_filter(None, [0, -3, 1, 6])))

if __name__ == '__main__':
    unittest.main()
