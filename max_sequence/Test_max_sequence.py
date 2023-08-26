import unittest
from max_sequence import max_sequence   # import our module

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA
# TDD link: https://www.youtube.com/watch?v=kwj6Hk1kJYU&t=47s
class is_max_sequenceTestCase(unittest.TestCase):
    def test_return_max_sequence(self):
        self.assertEqual(max_sequence([1, 1, 1, 1]),4)
        self.assertEqual(max_sequence([-1, -1, -1, -1]), 0)
        self.assertEqual(max_sequence([4, -1, 2, -1]), 6)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 12)
        self.assertEqual(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
        self.assertEqual(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 274)

    def test_return_max_sequence_ErrorHandling(self):
        self.assertEqual(max_sequence([1, "hi", 1, 1]),"Error, list has a string value")

if __name__ == '__main__':
    unittest.main()