import unittest
from domain_name import domain_name   # import our module

# TDD link: https://www.youtube.com/watch?v=Tdpmo3bcjwA
# TDD link: https://www.youtube.com/watch?v=kwj6Hk1kJYU&t=47s
class is_domainTestCase(unittest.TestCase):

    def test_return_domain_name(self):
        self.assertEqual(domain_name("http://github.com/carbonfive/raygun"), "github")
        self.assertEqual(domain_name("http://www.zombie-bites.com"), "zombie-bites")
        self.assertEqual(domain_name("https://www.cnet.com"), "cnet")

    def test_non_string_argument(self):
        with self.assertRaises(TypeError):
            domain_name(123)

    # def test_non_url_argument(self):
    #     with self.assertRaises(AssertionError):
    #         domain_name("github.com")


if __name__ == '__main__':
    unittest.main()