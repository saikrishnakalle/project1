import unittest
from calculator import add, sub, mul, div

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-2, 2), 0)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(2, 5), -3)

    def test_mul(self):
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(-2, 3), -6)

    def test_div(self):
        self.assertAlmostEqual(div(5, 3), 5/3)
        self.assertAlmostEqual(div(10, 2), 5)

    # Optional: check division by zero
    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

if __name__ == '__main__':
    unittest.main()
    