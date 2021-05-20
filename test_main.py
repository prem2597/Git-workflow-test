import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(calc.subtraction(5, 5), 0)
        self.assertEqual(calc.subtraction(-3, 3), -6)
        self.assertEqual(calc.subtraction(-5, -5), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    