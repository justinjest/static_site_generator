from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
    def text_node_to_html_node(self):
        types = {"text": LeafNode(None, self.text),
                 "bold": LeafNode("b", self.text), 
                 "italic": LeafNode("i", self.text), 
                 "code": LeafNode("code", self.text), 
                 "link": LeafNode("a", self.text, {"href":self.url}), 
                 "image": LeafNode("img", "", {"src":self.url, "alt":self.text})}
        if self.text_type.lower() not in types:
            raise Exception ("Not a valid text type") 
        return (types[self.text_type]) 
    
    def __eq__(self, node):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        return False