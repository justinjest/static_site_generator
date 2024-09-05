from split_blocks import *
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode
from split_md import *
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    # Markdown -> Blocks
    # Blocks -> TextNode
    # TextNode -> HTML node
    # For basic textbolcks we wrap this with <p>
    block_wrapper={"quote":"blockquote",
                   "unordered_list":"ul",
                   "ordered_list":"ol",
                   "code":"code",
                   "heading":"h1",
                   "paragraph":"p"}
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        # Each block must now be converted into the parent HTML item
        block_type = block_to_block_type(block)
        text_nodes = text_to_textnodes(block)
        leaf_nodes = []
        for text_node in text_nodes:
            # This creates the LeafNodes that we need for this
            leaf_nodes.append(text_node.text_node_to_html_node())
        node = ParentNode(f"{block_wrapper[block_type]}", leaf_nodes)
        print(node.to_html())
