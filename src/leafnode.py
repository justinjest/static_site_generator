from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    _SelfClosingTags = [
        "img", "br", "hr", "input", "meta", "link"
    ]

    def __init__(self, tag = None, value = None, props = None):
        if value is None:
            raise ValueError
        if tag == "":
            tag = None
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.tag == None:
            return (self.value)
        if self.tag in LeafNode._SelfClosingTags:
            return(f'<{self.tag}{self.props_to_html()}>')
        else:
            return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")