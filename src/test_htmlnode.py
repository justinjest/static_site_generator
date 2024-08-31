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
        html = '<a href="https://boot.dev">Hello world</a>'
        self.assertEqual(node, html)
        node = LeafNode("a", "Hello world", {}).to_html()
        html = "<a>Hello world</a>"
        self.assertEqual(node, html)
        node = LeafNode("b", "Bold text").to_html()
        html = "<b>Bold text</b>"
        self.assertEqual(node, html)
        node = LeafNode("img", "", {"src":"image.url","alt":"test"}).to_html()
        result = '<img src="image.url" alt="test">'
        self.assertEqual(node,result)
        node = LeafNode("p", "test", {}).to_html()
        result = '<p>test</p>'
        self.assertEqual(node,result)
        node = LeafNode("", "test", {}).to_html()
        result = 'test'
        self.assertEqual(node,result)

        # ParentNode tests
        node = ParentNode(
                        "p",
                        [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                        ],
                    ).to_html()
        result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node, result)

        node = ParentNode(
            "p",
            [ParentNode(
                "a",
                [LeafNode("b", "Bold text"),
                 LeafNode(None, "Normal text")]
            ),
            LeafNode("i","italic text"),
            LeafNode(None, "Normal text")]
        ).to_html()
        result = "<p><a><b>Bold text</b>Normal text</a><i>italic text</i>Normal text</p>"
        self.assertEqual(node, result)


if __name__ == "__main__":
    unittest.main()