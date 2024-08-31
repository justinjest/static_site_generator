import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):

        # same
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        # Weird URL
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
        # Different formatting
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "italics")
        self.assertNotEqual(node, node2)
        # Different text
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is not a test", "bold")
        self.assertNotEqual(node, node2)
        # Different formating and text
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is not a test", "italics")
        self.assertNotEqual(node, node2)
        # One has URL one doesn't
        node = TextNode("This is a test node", "bold", "https://boot.dev.com")
        node2 = TextNode("This is not a test", "bold")
        self.assertNotEqual(node, node2)
        # Testing functionality of text_node_to_html_node().to_html()
        # Should allow us to input the textnode that will be converted into a leaf node
        '''
            types = {"text":LeafNode(None, self.text),
                 "bold": LeafNode("b", self.text), 
                 "italic": LeafNode("i", self.text), 
                 "code": LeafNode("code", self.text), 
                 "link": LeafNode("a", self.text, {"href":self.url}), 
                 "image": LeafNode("img", "", {"SRC":self.url, "alt":self.text})}
        '''
        node = TextNode("This is a test", "text").text_node_to_html_node().to_html()
        html = "This is a test"
        self.assertEqual(node,html)
if __name__ == "__main__":
    unittest.main()