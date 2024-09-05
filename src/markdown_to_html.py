from split_blocks import *
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode
from split_md import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        text_nodes = text_to_textnodes(block)
    # TODO: Insert ParentNode that surrounds text_node
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node.text_node_to_html_node())

    return (html_nodes)