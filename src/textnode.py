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