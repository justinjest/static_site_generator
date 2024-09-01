import unittest
from textnode import TextNode
from split_md import split_nodes_delimiter

class TestSplit(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        result = [TextNode("This is text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text")]
        for i in range(len(new_nodes)):
                self.assertEqual(new_nodes[i], result[i])

if __name__ == "__main__":
    unittest.main()