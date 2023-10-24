import unittest
from types import GeneratorType
from lab4_2 import _map


class TestMapFunction(unittest.TestCase):
    def test_generator_type(self):
        self.assertRaises(TypeError, _map(None, None))

    def test_single_iterable(self):
        result = _map(lambda x: x.upper(), 'ala ma kota')
        self.assertIsInstance(result, GeneratorType)
        self.assertEqual(list(result), ['A', 'L', 'A', ' ', 'M', 'A', ' ', 'K', 'O', 'T', 'A'])

    def test_multiple_iterables(self):
        result = _map(lambda x, y: x + y, [1, 2, 3, 4], [5, 6, 7, 8])
        self.assertIsInstance(result, GeneratorType)
        self.assertEqual(list(result), [6, 8, 10, 12])


if __name__ == '__main__':
    unittest.main()
