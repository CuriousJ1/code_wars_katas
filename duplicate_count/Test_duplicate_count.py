import unittest
from duplicate_count import duplicate_count   # import our module

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA
# TDD link: https://www.youtube.com/watch?v=kwj6Hk1kJYU&t=47s
class duplicate_count_TestCase(unittest.TestCase):
    def test_int(self):
        with self.assertRaises(TypeError):
            duplicate_count(2)
    def test_boolean(self):
        with self.assertRaises(TypeError):
            duplicate_count(True)
    def test_list_input(self):
        with self.assertRaises(TypeError):
            duplicate_count([1, 2, 3])
    def test_dict_input(self):
        with self.assertRaises(TypeError):
            duplicate_count({"a": 1, "b": 2})
    def test_none_input(self):
        with self.assertRaises(ValueError):
            duplicate_count(None)

    def test_duplicate_count(self):
        self.assertEqual(duplicate_count(""), 0)
        self.assertEqual(duplicate_count("abcde"), 0)
        #self.assertEqual(duplicate_count("abcdeaa"), 1)
        self.assertEqual(duplicate_count("aabbde"), 2)
        self.assertEqual(duplicate_count("aabBcde"), 2)
        self.assertEqual(duplicate_count("aA11"), 2)
        self.assertEqual(duplicate_count("abcdeaB"), 2)
        self.assertEqual(duplicate_count("indivisibilities"), 2)


if __name__ == '__main__':
    unittest.main()