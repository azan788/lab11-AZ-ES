# https://github.com/azan788/lab11-AZ-ES
# Partner 1: Azan Zaman
# Partner 2: Evelyn Simmons
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEquals(add(2, 2), 4)
        self.assertEquals(add(-1, 0), -1)
        self.assertEquals(add(10, -3), 7)

    def test_subtract(self): # 3 assertions
        self.assertEquals(subtract(2, 2), 4)
        self.assertEquals(subtract(-1, 0), -1)
        self.assertEquals(subtract(10, -3), 7)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEquals(mul(2, 3), 6)
        self.assertEquals(mul(1, 3), 3)
        self.assertEquals(mul(2, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(8, 4), 2)
        self.assertAlmostEqual(div(1, 2), 0.5)
        self.assertAlmostEqual(div(7, 4), 1.75)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        self.assertRaises(ZeroDivisionError, div(0,5))

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        self.assertRaises(ValueError, logarithm(10, 0))
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(4, 3), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 2), 5 ** 0.5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-2)
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()