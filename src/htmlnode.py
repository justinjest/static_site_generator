class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception ("NotImplementedError")
    
    def props_to_html(self):
        ans = ""
        for key, value in self.props.items():
            ans = ans + f' {key}="{value}"'
        return("")
        return (ans)
    
    def __eq__(self, node):
        if (self.tag == node.tag and self.value == node.value
             and self.children == node.children and self.props == node.props):
            return True
        return False
    
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")