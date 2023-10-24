import unittest
from lab4_7 import celsius_to_fahrenheit

class TestTemperatureConversion(unittest.TestCase):

    def test_conversion(self):
        self.assertEqual(list(celsius_to_fahrenheit([0, 10, 100])), [32.0, 50.0, 212.0])

    def test_negative_conversion(self):
        self.assertEqual(list(celsius_to_fahrenheit([-123, 0])), [-189.4, 32.0])

if __name__ == "__main__":
    unittest.main()
