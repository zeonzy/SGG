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
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
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