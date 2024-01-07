import unittest
from sum_strings import sum_strings

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA
# TDD link: https://www.youtube.com/watch?v=kwj6Hk1kJYU&t=47s
class SumStringsTestCase(unittest.TestCase):
    def test_both_valid_inputs(self):
        # This should not raise an error
        result = sum_strings('1','2')
        self.assertEqual(result, '3')

        result = sum_strings('123', '456')
        self.assertEqual(result, '579')
    def test_none_input(self):
        with self.assertRaises(ValueError):
            sum_strings(None, '2')

        with self.assertRaises(ValueError):
            sum_strings('2', None)

    def test_invalid_recipe_input(self):
        with self.assertRaises(TypeError):
            sum_strings(2, '2')

    def test_invalid_available_input(self):
        with self.assertRaises(TypeError):
            sum_strings(2, "3")


if __name__ == '__main__':
    unittest.main()