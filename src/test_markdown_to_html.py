import unittest
from markdown_to_html import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):

        test = markdown_to_html_node("""This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)""")
        result = '<div><p>This is <b>text</b> with an <i>italic</i> word and a <code>code block</code> and an <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan image"> and a <a href="https://boot.dev">link</a></p></div>'
        self.assertEqual(test, result)

        test = markdown_to_html_node("""* this is an unordered list
* there are two things in it""")
        result = "<div><ul><li>this is an unordered list</li><li>there are two things in it</li></ul></div>"
        self.assertEqual(test, result)
if __name__ == "__main__":
    unittest.main()