import re

def markdown_to_blocks(text):
    # Split on double newline so that we don't split lists
    split_text = text.split("\n\n")
    output = []
    for paragraph in split_text:
        if paragraph != "" and paragraph != "\n":
            output.append(paragraph.strip())
    return (output)

def block_to_block_type(block):
    lines = block.split("\n")

    if is_header(block):
        return "heading" 
    
    if is_quote(block):
        return "quote"
    
    if is_unordered_list(block):
        return "unordered_list"
    
    if is_code(block):
        return "code"
    
    if is_ordered_list(lines):
        return "ordered_list"

    return "paragraph"

def is_header(block):
    if re.match(r"##* ", block) != None:
        return "heading"

def is_code(block):
    if block[0:3] == "```" and block[-3:] == "```":
        return True
    return False
    
def is_unordered_list(block):
    unordered_list_regex = re.compile(r"^(\s*[*-] .*)$", re.MULTILINE)
    unordered_list = unordered_list_regex.findall(block)
    if len(unordered_list) == len(block.split("\n")):
        return True
    return False

def is_quote(block):
    quote_regex =  re.compile(r"^(\s*>.*)$", re.MULTILINE)
    quote = quote_regex.findall(block)
    if len(quote) == len (block.split("\n")):
        return True
    return False

def is_ordered_list(lines):
        for i, line in enumerate(lines, start = 1):
            pattern = f"^{i}\\. .*$"
            if not re.match(pattern, line.strip()):
                return False
        return True