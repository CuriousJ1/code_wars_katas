import unittest
from pig_latin import pig_latin   # import our module
class pig_latinTestCase(unittest.TestCase):
    def test_non_string_argument(self):
        with self.assertRaises(TypeError):
            pig_latin(123)
            pig_latin(1.03)
            pig_latin(["hello"])

    def test_return_pig_latin(self):
        self.assertEqual(pig_latin("hello"), "ellohay")
        #self.assertEqual(domain_name("http://www.zombie-bites.com"), "zombie-bites")
        #self.assertEqual(domain_name("https://www.cnet.com"), "cnet")



if __name__ == '__main__':
    unittest.main()