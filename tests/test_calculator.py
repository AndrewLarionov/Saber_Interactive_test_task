import unittest
from calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_calculate(self):

        self.assertEqual(calculate('2+2'), 4)
        self.assertEqual(calculate('2+2*5'), 12)
        self.assertEqual(calculate('2/2/2/2'), 0.25)
        self.assertEqual(calculate('10+100*0.1'), 20)
        self.assertIn('Please', calculate('a'))
        self.assertIn('Please', calculate('10+100*0,1'))
        self.assertIn('Please', calculate('2+2+'))

