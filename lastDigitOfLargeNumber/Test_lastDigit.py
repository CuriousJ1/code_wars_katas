import unittest
from lastDigit import last_digit   # import our module

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA
# TDD link: https://www.youtube.com/watch?v=kwj6Hk1kJYU&t=47s
class last_digit_TestCase(unittest.TestCase):
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            last_digit(-2, 3)

        with self.assertRaises(ValueError):
            last_digit(2, -3)
    def test_strings(self):
        with self.assertRaises(TypeError):
            last_digit(2, "string")

        with self.assertRaises(TypeError):
            last_digit("string", 2)
    def test_boolean(self):
        with self.assertRaises(TypeError):
            last_digit(2, True)

        with self.assertRaises(TypeError):
            last_digit(True, 2)
    def test_list_input(self):
        with self.assertRaises(TypeError):
            last_digit(2, [1, 2, 3])
    def test_tuple_input(self):
        with self.assertRaises(TypeError):
            last_digit(2, (1, 2, 3))

        with self.assertRaises(TypeError):
            last_digit((1, 2, 3), 2)
    def test_dict_input(self):
        with self.assertRaises(TypeError):
            last_digit(2, {"a": 1, "b": 2})

        with self.assertRaises(TypeError):
            last_digit({"a": 1, "b": 2}, 2)

    def test_none_input(self):
        with self.assertRaises(ValueError):
            last_digit(2, None)

        with self.assertRaises(ValueError):
            last_digit(None, 0)

    def test_return_lastDigit(self):
        self.assertEqual(last_digit(2, 2), 4)

    def test_return_lastDigit(self):
        self.assertEqual(last_digit(2, 2), 4)
        self.assertEqual(last_digit(4, 1), 4)
        self.assertEqual(last_digit(9, 7), 9)
        #self.assertEqual(last_digit(10, 10 ** 10), 0)
        #self.assertEqual(last_digit(2 ** 200, 2 ** 200), 6)


if __name__ == '__main__':
    unittest.main()