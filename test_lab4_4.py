import unittest
from lab4_4 import squares_of_odds

class TestSquaresOfOddsFunction(unittest.TestCase):

    def test_squares_of_odds(self):
        self.assertEqual(squares_of_odds([1, 2, 3, 4, 5, 6]), 35)
        self.assertEqual(squares_of_odds([10, 13, 5, 6]), 194)

if __name__ == "__main__":
    unittest.main()
