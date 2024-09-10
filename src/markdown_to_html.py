from split_blocks import *
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode
from split_md import *
from leafnode import LeafNode
# Consumes a markdown file
# Outputs the valid HTML
def markdown_to_html_node(markdown):
    # Markdown -> Blocks
    # Blocks -> TextNode
    # TextNode -> HTML node
    # For basic textbolcks we wrap this with <p>

    blocks = markdown_to_blocks(markdown)
    leaf_nodes = block_to_html(blocks)
    # Add the div wrapper
    final_node = ParentNode("div", [leaf_nodes])
    return(final_node.to_html())

# Consumes a single block of markdown
# Outputs HTMLNode for that block
def block_to_html(blocks):
        block_wrapper={"quote":"blockquote",
                "unordered_list":"ul",
                "ordered_list":"ol",
                "code":"code",
                "heading":"h1",
                "paragraph":"p"}
        for block in blocks:
            # Each block must now be converted into the parent HTML item
            block_type = block_to_block_type(block)
            text_nodes = text_to_textnodes(block)
            leaf_nodes = []
            if block_type == "unordered_list" or block_type == "ordered_list":
                text_nodes = list_to_text_nodes(block)
                for text_node in text_nodes:
                     leaf_nodes.append(ParentNode("li", [text_node.text_node_to_html_node()]))
            elif block_type == "paragraph":
                for text_node in text_nodes:
                    leaf_nodes.append(text_node.text_node_to_html_node())
            else:
                 raise Exception ("Block type not defined", block)
            node = ParentNode(f"{block_wrapper[block_type]}", leaf_nodes)
        return node

# Consumes a unordered list text object
# Outputs a text_node list
def list_to_text_nodes(text):
    new_line_breaks = text.split("\n")
    results = []
    for line in new_line_breaks:
        line = line.lstrip(" *-")
        tmp = text_to_textnodes(line)
        for text_node in tmp:
            results.append(text_node)
    return results

def header_to_text_nodes(text):
     # TODO

     pass

def code_to_text_nodes(text):
     # TODO

     pass

def quote_to_text_nodes(text):
     # TODO

     pass