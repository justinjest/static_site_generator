import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
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
        node = LeafNode(None, "Hello world", {})
        node2 = LeafNode(None, "Hello world", {})
        self.assertEqual(node, node2)
if __name__ == "__main__":
    unittest.main()