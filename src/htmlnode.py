class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def __repr__(self):
        # returns debug string
        return f"|tag = [{self.tag}], value = [{self.value}], children = [{self.children}], props = [{self.props}]|"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        # This method should return a string that represents the HTML attributes of the node.
        if type(self.props) != dict:
            return ""       
        output = ""
        for key, value in self.props.items():
            output += f' {key}="{value}"'
        return str(output)


class LeafNode(HTMLNode):
    def __init__(self, tag= None, value = None, props = None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if not self.value:
            raise ValueError("Invalid HTML: no value")
        elif not self.tag:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag")
        elif not self.children:
            raise ValueError("Invalid HTML: no children")
        else:
            def recursion(item):
                if not item:
                    return ""
                return "" + item[0].to_html() + recursion(item[1:])
            return LeafNode(self.tag, recursion(self.children), self.props).to_html()
            
            
        


"""
<p> paragrapgh </p>| "p"
<b> bold </b>| "b"
<i> bold </i>| "i"
<a href="https://www.google.com">link</a>| "a"
<img src="url/of/image.jpg" alt="Description of image">| "img"
<blockquote> quote </blockquote>| "blockquote"
<code>This is code</code> | "code"

"""

