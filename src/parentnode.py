from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        if children == None:
            raise Exception ("Children element required for ParentNode")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        html_content = ''
        if self.tag == None:
            raise ValueError ("Tags required for ParentClass")
        if self.children == None:
            raise ValueError ("Children required for Parent Class") 
        for child in self.children:
            html_content += child.to_html() 
        if self.props == None:
            return (f"<{self.tag}>{html_content}</{self.tag}>")
        return (f"<{self.tag}>{self.props_to_html}{html_content}</{self.tag}>")