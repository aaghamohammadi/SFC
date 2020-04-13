import unittest
from src.example import add_even_numbers


class TestAddEvenNumbers(unittest.TestCase):
    
    def test_by_an_odd_number(self):
        self.assertEqual(2, add_even_numbers(n=3))
