import sys
import unittest
from src.calculations import addition, subtraction, multiplication, division, ne

class TestCalculations(unittest.TestCase):

    def test_addition(self):
        res = addition(10, 5)
        self.assertEqual(15, res, msg = 'Addition Error')

    def test_subtraction(self):
        res = subtraction(10, 5)
        self.assertEqual(5, res, msg = 'Subtraction Error')

    def test_multiplication(self):
        res = multiplication(10, 5)
        self.assertEqual(50, res, msg = 'Multiplication Error')

    def test_division(self):
        res = division(10, 5)
        self.assertEqual(2.0, res, msg = 'Division Error')

    @unittest.skipIf(sys.version_info > (3, 13), reason = 'Not impl yet')
    def test_ne(self):
        res = ne(5,10)
        self.assertTrue(res, msg = 'Ne')

    def test_diverr(self):
        with self.assertRaises(ZeroDivisionError, msg = 'No Exception Occures'):
            division(10, 0)