import re

def markdown_to_blocks(markdown):
    #first plits into individual lines and strips leading and trailing whitspaces
    output = []
    for block in "\n".join((map(lambda x: x.strip(), markdown.split("\n")))).split("\n\n"):
        #filter out any empty double enters
        if block != "":
            sub_output = []
            #filter out any empty enters while keeping the block markup
            for sub_block in block.split("\n"):
                if sub_block != "":
                    sub_output.append(sub_block)
            output.append("\n".join(sub_output))
    return output

def block_to_block_type(block):
    if re.findall(r"(?<!.)(#{1,6} .)",block) and block.startswith("#"):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    elif block.startswith("* ") or block.startswith("- "):
        for line in block.split("\n"):
            if line.startswith("- "):
                line = "* " + line[2:]
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    elif block.startswith("1. "):
        for enum, line in enumerate(block.split("\n"),1):
            if not line.startswith(f"{enum}. "):
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"