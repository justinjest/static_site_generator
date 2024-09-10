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
        if self.props == None:
            return ""
        for key, value in self.props.items():
            ans = ans + f' {key}="{value}"'
        return (ans)
    
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
    

    def __eq__(self, node):
        if node is None:
            return False
        if (self.tag == node.tag and self.value == node.value
             and self.children == node.children and self.props == node.props):
           return True
        return False