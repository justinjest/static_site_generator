import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        # same
        node = HTMLNode("a", "Hello world", None, {"href": "https://boot.dev"})
        node2 = HTMLNode("a", "Hello world", None, {"href": "https://boot.dev"})
        self.assertEqual(node,node2)
        # Different block
        node = HTMLNode("a", "Hello world", None, {"href": "https://boot.dev"})
        node2 = HTMLNode("p", "Hello world", None, {"href": "https://boot.dev"})
        self.assertNotEqual(node, node2)
        # Different text
        node = HTMLNode("p", "Hello world", None, {"href": "https://boot.dev"})
        node2 = HTMLNode("p", "Goodbye world", None, {"href": "https://boot.dev"})
        self.assertNotEqual(node, node2)

        # LeafNode tests
        node = LeafNode("a", "Hello world", {"href": "https://boot.dev"})
        node2 = LeafNode("a", "Hello world", {"href": "https://boot.dev"})
        self.assertEqual(node, node2)
        node = LeafNode(None, "Hello world", None)
        node2 = LeafNode(None, "Hello world", None)
        self.assertEqual(node, node2)
        node = LeafNode(None, "Hello world", {}).to_html()
        node2 = "Hello world"
        self.assertEqual(node, node2)
        node = LeafNode("a","Hello world", None).to_html()
        html = "<a>Hello world</a>"
        self.assertEqual(node, html)
        node = LeafNode("a","Hello world", {"href":"https://boot.dev"}).to_html()
        html = '<a href="htttps://boot.dev">Hello world</a>'
        self.assertEqual(node, html)
        # ParentNode tests
        '''node = ParentNode(
                        "p",
                        [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                        ],
                    ).to_html()
        result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node, result)'''

if __name__ == "__main__":
    unittest.main()