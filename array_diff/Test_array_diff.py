import unittest
from array_diff import array_diff   # import our module

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA
# TDD link: https://www.youtube.com/watch?v=kwj6Hk1kJYU&t=47s
class array_diff_TestCase(unittest.TestCase):
    def test_strings(self):
        with self.assertRaises(TypeError):
            array_diff(2, "string")

        with self.assertRaises(TypeError):
            array_diff("string", 2)
    def test_boolean(self):
        with self.assertRaises(TypeError):
            array_diff(2, True)

        with self.assertRaises(TypeError):
            array_diff(True, 2)
    def test_list_input(self):
        with self.assertRaises(TypeError):
            array_diff(2, [1, 2, 3])

        with self.assertRaises(TypeError):
            array_diff(2, (1, 2, 3))

        with self.assertRaises(TypeError):
            array_diff((1, 2, 3), 2)
    def test_dict_input(self):
        with self.assertRaises(TypeError):
            array_diff(2, {"a": 1, "b": 2})

        with self.assertRaises(TypeError):
            array_diff({"a": 1, "b": 2}, 2)

    def test_none_input(self):
        with self.assertRaises(ValueError):
            array_diff(2, None)

        with self.assertRaises(ValueError):
            array_diff(None, 0)

    def test_mixed_list(self):
        # Test when both a and b are lists containing non-integer elements
        with self.assertRaises(TypeError):
            array_diff([1, 2, '3'], [2])

        with self.assertRaises(TypeError):
            array_diff([1, 2, 3], ['2'])

    def test_list_of_integers(self):
        # Test when both a and b are lists of integers
        result = array_diff([1,2,2,2,2,3], [2])
        self.assertEqual(result, [1,3])


    # def test_single_element(self):
    #     # Test when a and b are single-element lists
    #     result = array_diff([2], [2])
    #     self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()