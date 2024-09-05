import unittest
from markdown_to_html import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test = markdown_to_html_node("Simple text")
        print(test)

if __name__ == "__main__":
    unittest.main()