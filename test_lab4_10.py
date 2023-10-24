import unittest
from lab4_10 import primes

class TestPrimesFunction(unittest.TestCase):

    def test_primes_up_to_5(self):
        self.assertEqual(primes(5), {2, 3, 5})

    def test_primes_up_to_10(self):
        self.assertEqual(primes(10), {2, 3, 5, 7})

    def test_primes_up_to_100(self):
        self.assertEqual(primes(100), {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                                        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})

if __name__ == '__main__':
    unittest.main()
