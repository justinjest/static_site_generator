import unittest
from textnode import TextNode
from split_md import * 

class TestSplit(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        result = [TextNode("This is text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text")]
        for i in range(len(new_nodes)):
                self.assertEqual(new_nodes[i], result[i])

        node = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(node,result)
        node = extract_markdown_images("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        result = [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(node,result)
        node = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(node, result)
        node = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)")
        result = [("to boot dev", "https://www.boot.dev"),]
        self.assertEqual(node, result)
        node = extract_markdown_images("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        result = []
        self.assertEqual(node, result) 

        node = TextNode(
        "This is text with a link ![to boot dev](https://www.boot.dev) and ",
        text_type_text,)
        new_nodes = split_nodes_image([node])
        ans = [
        TextNode("This is text with a link ", text_type_text),
        TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
        TextNode(" and ", text_type_text)]
        self.assertEqual(new_nodes, ans)

        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and ",
        text_type_text,)
        new_nodes = split_nodes_image([node])
        ans = [TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and ",
        text_type_text,)]
        self.assertEqual(new_nodes, ans)
        
        node = TextNode(
        "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
        )
        new_nodes = split_nodes_image([node]) 
        ans = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_image, "https://www.youtube.com/@bootdotdev"
            )]
        self.assertEqual(new_nodes, ans)
        node = TextNode(
             "This is a text node with no images", text_type_text
        )
        new_node = split_nodes_image([node])
        result = [TextNode("This is a text node with no images", text_type_text)]
        self.assertEqual(new_node, result)


        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and ",
        text_type_text,)
        new_nodes = split_nodes_link([node])
        ans = [
        TextNode("This is text with a link ", text_type_text),
        TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
        TextNode(" and ", text_type_text)]
        self.assertEqual(new_nodes, ans)

        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
        )
        new_nodes = split_nodes_link([node]) 
        ans = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            )]
        self.assertEqual(new_nodes, ans)
        node = TextNode(
             "This is a text node with no images", text_type_text
        )
        new_node = split_nodes_link([node])
        result = [TextNode("This is a text node with no images", text_type_text)]
        self.assertEqual(new_node, result)

        nodes = [TextNode("This is a node with a link [to boot dev](https://www.boot.dev)", text_type_text),
                 TextNode("This is a node with an image ![obi wan](chess.com)", text_type_text)]
        new_node = split_nodes_link(nodes)
        result = [TextNode("This is a node with a link ", text_type_text),
                  TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                  TextNode("This is a node with an image ![obi wan](chess.com)", text_type_text)]
        self.assertEqual(new_node, result)

        nodes = [TextNode("This is a node with a link [to boot dev](https://www.boot.dev)", text_type_text),
                 TextNode("This is a node with an image ![obi wan](chess.com)", text_type_text)]
        new_node = split_nodes_image(nodes)
        result = [TextNode("This is a node with a link [to boot dev](https://www.boot.dev)", text_type_text),
                  TextNode("This is a node with an image ", text_type_text),
                  TextNode("obi wan", text_type_image, "chess.com")]
        self.assertEqual(new_node, result)
if __name__ == "__main__":
    unittest.main()