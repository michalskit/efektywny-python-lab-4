import unittest
from lab4_9 import create_sentence

class TestCreateSentence(unittest.TestCase):
    def test_basic_sentence(self):
        self.assertEqual(create_sentence(['ala', 'ma', 'kota']), 'ala ma kota')

    def test_single_word(self):
        self.assertEqual(create_sentence(['ala']), 'ala')

    def test_length_restriction(self):
        self.assertEqual(create_sentence(['ala', 'ma', 'pieknego', 'kota'], k=3), 'ala pieknego kota')

if __name__ == "__main__":
    unittest.main()