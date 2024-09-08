import unittest
from markdown_to_html import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test = markdown_to_html_node("Simple text")
        print(test)
    
        test = markdown_to_html_node("""Slightly more complicated text.

two sentences""")
        print(test)

        test = markdown_to_html_node("""This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)""")
        print(test)

        test = text_to_textnodes("""* this is an unordered list
* there are two things in it""")
        print(test)
if __name__ == "__main__":
    unittest.main()