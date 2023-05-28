import unittest
import coverage
# import python unittest
from square_number import is_square   # import our module

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA

class is_squareTestCase(unittest.TestCase):

    # def test_return_number(self):
    #     self.assertEqual(is_square(5), 5)

    def test_negative_number(self):
        self.assertEqual(is_square(-1), False, "Negative numbers cannot be square numbers")

    def test_number_is_zero(self):
        self.assertEqual(is_square(0), True, "0 is a square number")

    def test_square_number(self):
        self.assertEqual(is_square(3), False, "3 is not a square number")
        self.assertEqual(is_square(4), True, "4 is a square number")
        self.assertEqual(is_square(25), True, "25 is a square number")
        self.assertEqual(is_square(26), False, "26 is not a square number")

if __name__ == '__main__':
    unittest.main()