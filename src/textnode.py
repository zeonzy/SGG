from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text # The text content of the node
        self.text_type = text_type # The type of text this node contains, which is just a string like "bold" or "italic"
        self.url = url # The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

    def __eq__(self, other):
        # returns True if all of the properties of two TextNode objects are equal.
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
        
    def __repr__(self):
        # returns a string representation of the TextNode object. It should look like this:
        # TextNode(TEXT, TEXT_TYPE, URL)
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
def text_node_to_html_node(text_node):
    if text_node.text_type == "text_type_text" or text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "text_type_bold" or text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "text_type_italic" or text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "text_type_code" or text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "text_type_link" or text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "text_type_image" or text_node.text_type == "image":
        return LeafNode("img",None, {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Unknown TextNode type")
    
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
            for enum, text in enumerate(split_text):
                if text:
                    if enum % 2 == 0:
                        output.append(TextNode(text, "text"))
                    else:
                        output.append(TextNode(text, text_type))
    return output