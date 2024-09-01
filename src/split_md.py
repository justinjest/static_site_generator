from textnode import TextNode

text_type_text = "text"
text_type_code = "code"
text_type_bold = "bold"
text_type_italic = "italic"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for i in old_nodes:
        if i.text_type != text_type_text:
            result.append(old_nodes[i])
        try:
            split = i.text.split(delimiter)
            result.append(TextNode(f"{split[0]}", "text"))
            result.append(TextNode(f"{split[1]}", f"{text_type}"))
            result.append(TextNode(f"{split[2]}", "text"))
        except:
            raise Exception ("Unable to split along delimiter {delimiter} text {i.text}")
    return result
        