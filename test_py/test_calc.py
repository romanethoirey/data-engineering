import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)
        self.assertEqual(calc.add(-1,1), 0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(2,3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(6,3), 2)

if __name__ == '__main__':
    unittest.main()