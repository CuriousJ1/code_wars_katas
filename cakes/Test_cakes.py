import unittest
from cakes import cakes   # import our module

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA
# TDD link: https://www.youtube.com/watch?v=kwj6Hk1kJYU&t=47s
class CakesTestCase(unittest.TestCase):
    def test_both_dict_input(self):
        # This should not raise an error
        result = cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
        self.assertEqual(result, 2)
    def test_none_input(self):
        with self.assertRaises(ValueError):
            cakes(None, {"x": 3, "y": 4})

        with self.assertRaises(ValueError):
            cakes({"x": 3, "y": 4}, None)

    def test_invalid_recipe_input(self):
        with self.assertRaises(TypeError):
            cakes("not a dictionary", {"x": 3, "y": 4})

    def test_invalid_available_input(self):
        with self.assertRaises(TypeError):
            cakes({"a": 1, "b": 2}, "not a dictionary")

    # def test_cakes(self):
    #     self.assertEqual(duplicate_count(""), 0)
    #
if __name__ == '__main__':
    unittest.main()