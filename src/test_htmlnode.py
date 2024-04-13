import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test1 = HTMLNode("tag", "value", "children", "props")
        test1_output = "|tag = [tag], value = [value], children = [children], props = [props]|"
        test2 = HTMLNode()
        test2_output = "|tag = [None], value = [None], children = [None], props = [None]|"

        self.assertEqual(test1, test1)
        self.assertNotEqual(test1, test2)
        self.assertEqual(str(test1), str(test1_output))
        self.assertEqual(str(test2), str(test2_output))

        test3 = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
        test3_output = ' href="https://www.google.com" target="_blank"'
        test4 = HTMLNode(props ={"href": "https://www.google.com", "target": "_blank"})
        test4_output = ' href="https://www.google.com" target="_blank"'
    
        self.assertEqual(test3.props_to_html(), test3_output)
        self.assertEqual(test4.props_to_html(), test4_output)
        
        #LeafNode tests
        test1 = LeafNode("p", "text")
        test1_output = '<p>text</p>'
        test2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        test2_output = '<a href="https://www.google.com">Click me!</a>'
        test3  = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        test3_output = '<a href="https://www.google.com" target="_blank">Click me!</a>'

        self.assertEqual(str(test1.to_html()), str(test1_output))
        self.assertEqual(str(test2.to_html()), str(test2_output))
        self.assertEqual(str(test3.to_html()), str(test3_output))
        
        test4 = LeafNode("p")
        try:
            test4.to_html()
        except ValueError as e:
            self.assertEqual(str(e), "Invalid HTML: no value")
        
        test5 = LeafNode(value="This is some text!@#$%")
        self.assertEqual(test5.to_html(), "This is some text!@#$%")

        #ParentNode tests
        test1 = ParentNode(
        "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        test1_output = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(str(test1.to_html()), test1_output)

        test2 = ParentNode(
        "p",
            [
                ParentNode("p",[LeafNode("code", "C1"),LeafNode("i", "C2")]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("p",[LeafNode("code", "C3"),LeafNode("i", "C4")])
            ],
        )
        test2_output = '<p><p><code>C1</code><i>C2</i></p>Normal text<i>italic text</i>Normal text<p><code>C3</code><i>C4</i></p></p>'
        self.assertEqual(str(test2.to_html()), test2_output)

        test3 = ParentNode(
        "p",
            [
                ParentNode("p",[ParentNode("p", [ParentNode("p", [LeafNode("i", "italic text")])])])
            ],
        )
        test3_output = '<p><p><p><p><i>italic text</i></p></p></p></p>'
        self.assertEqual(str(test3.to_html()), test3_output)

        test4 = ParentNode(
        "p",
            [
                ParentNode("p",[LeafNode("a", "Click me!", {"href": "https://www.google.com"}),LeafNode("i", "C2")]),
                LeafNode(None, "Normal text")
            ],
        )
        test4_output = '<p><p><a href="https://www.google.com">Click me!</a><i>C2</i></p>Normal text</p>'
        self.assertEqual(str(test4.to_html()), test4_output)

        test5 =  ParentNode(None, [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")])
        try:
            test5.to_html()
        except ValueError as e:
            self.assertEqual(str(e), "Invalid HTML: no tag")

        test6 = ParentNode("P", None)
        try:
            test6.to_html()
        except ValueError as e:
            self.assertEqual(str(e), "Invalid HTML: no children")
        


if __name__ == "__main__":
    unittest.main()
