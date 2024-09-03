from textnode import TextNode
import re

text_type_text = "text"
text_type_code = "code"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_link = "link"
text_type_image = "image"

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

def extract_markdown_images(md_text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", md_text)
def extract_markdown_links(md_text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", md_text)

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images == []:
            result.append(node)
        else:
            split_text = node.text
            for i in images:
                split_text = split_text.split(f"![{i[0]}]({i[1]})", 1)
                result.append(TextNode(f"{split_text[0]}", text_type_text))
                result.append(TextNode(f"{i[0]}", text_type_image, f"{i[1]}"))
                split_text = split_text[1]
            if split_text != "":
                result.append(TextNode(f"{split_text}", text_type_text))
    return(result)

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            result.append(node)
        else:
            split_text = node.text
            for i in links:
                split_text = split_text.split(f"[{i[0]}]({i[1]})", 1)
                result.append(TextNode(f"{split_text[0]}", text_type_text))
                result.append(TextNode(f"{i[0]}", text_type_link, f"{i[1]}"))
                split_text = split_text[1]
            if split_text != "":
                result.append(TextNode(f"{split_text}", text_type_text))
    return(result)