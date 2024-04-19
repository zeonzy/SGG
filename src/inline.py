from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for old_node in old_nodes:
        # If an "oldnode" is not a text type TextNode, you should just add it to the new list as-is, we only attempt to split text type TextNode objects.
        if old_node.text_type != "text":
            output.append(old_node)
        # If a matching closing delimiter is not found, just raise an exception with a helpful error message, that's invalid Markdown syntax.
        elif old_node.text.count(delimiter) % 2 == 1:
            raise ValueError(f"missing closing delimiter [{delimiter}]")
        else:
            split_text = old_node.text.split(delimiter)
            # if it starts or ends with the delimiter it adds an empty "" string, if 2 delimites are next to eachother this also happends.
            # because of this the delimited text always ends up being an even number (when ignoring empty strings), but because it starts with 0 it become's uneven instead 
            for enum, text in enumerate(split_text):
                if text:
                    if enum % 2 == 0:
                        output.append(TextNode(text, "text"))
                    else:
                        output.append(TextNode(text, text_type))
    return output