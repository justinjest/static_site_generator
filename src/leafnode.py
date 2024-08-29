from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        if value == None:
            raise ValueError
        super().__init__(tag, value, None, props)

    def to_html(self):
        # TODO add single closed tag support EG <img>
        if self.tag == None:
            return (self.value)
        if self.props == None:
            return (f"<{self.tag}>{self.value}</{self.tag}>")
        else:
            return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")