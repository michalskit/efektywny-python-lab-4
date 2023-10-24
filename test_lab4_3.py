import unittest
from lab4_3 import reverse_nonpalindromes

class TestReverseNonPalindromes(unittest.TestCase):
    def test_reverse_nonpalindromes(self):
        # Testuje przypadek, gdy jedno słowo jest palindromem, a drugie nie.
        self.assertEqual(reverse_nonpalindromes(["aa", "ab"]), ["ba"])

        # Testuje przypadek, gdy jedno słowo jest palindromem, a dwa inne nie.
        self.assertEqual(reverse_nonpalindromes(["eht", "dog", "ala"]), ["the", "god"])

if __name__ == '__main__':
    unittest.main()
