import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
from textnode import TextNode
from inline import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        new_nodes_result = [TextNode("This is text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text")]
        self.assertEqual(new_nodes, new_nodes_result)

        node1 = TextNode("`code block`", "text")
        new_nodes1 = split_nodes_delimiter([node1], "`", "code")
        new_nodes_result1 = [TextNode("code block", "code")]
        self.assertEqual(new_nodes1, new_nodes_result1)

        node2 = TextNode("code block", "code")
        new_nodes2 = split_nodes_delimiter([node2], "`", "code")
        new_nodes_result2 = [TextNode("code block", "code")]
        self.assertEqual(new_nodes2, new_nodes_result2)

        node3 = TextNode("`code block``code block``code block`", "text")
        new_nodes3 = split_nodes_delimiter([node3], "`", "code")
        new_nodes_result3 = [TextNode("code block", "code"), TextNode("code block", "code"), TextNode("code block", "code")]
        self.assertEqual(new_nodes3, new_nodes_result3)

        node4 = TextNode("'text', `code`, *italic*, **bold**", "text")
        new_nodes4 = split_nodes_delimiter([node4], "`", "code")
        new_nodes_result4 = [TextNode("'text', ", "text"), TextNode("code", "code"), TextNode(", *italic*, **bold**", "text")]
        self.assertEqual(new_nodes4, new_nodes_result4)

        new_nodes5 = split_nodes_delimiter([node4], "**", "bold")
        new_nodes_result5 = [TextNode("'text', `code`, *italic*, ", "text"), TextNode("bold", "bold")]
        self.assertEqual(new_nodes5, new_nodes_result5)

        new_nodes6 = split_nodes_delimiter([node4], "*", "italic")
        new_nodes_result6 = [TextNode("'text', `code`, ", "text"), TextNode("italic", "italic"), TextNode(", ", "text"), TextNode("bold", "text")]
        self.assertEqual(new_nodes6, new_nodes_result6)

        node7 = TextNode("*Only Italic!!!*", "text")
        new_nodes7 = split_nodes_delimiter([node7], "`", "code")
        new_nodes_result7 = [TextNode("*Only Italic!!!*", "text")]
        self.assertEqual(new_nodes7, new_nodes_result7)

        new_nodes8 = split_nodes_delimiter([node, node4, node7], "`", "code")
        new_nodes_result8 = [TextNode("This is text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text"),TextNode("'text', ", "text"), TextNode("code", "code"), TextNode(", *italic*, **bold**", "text"), TextNode("*Only Italic!!!*", "text")]       
        self.assertEqual(new_nodes8, new_nodes_result8)

        try:
            node9 = TextNode("`code block``", "text")
            split_nodes_delimiter([node9], "`", "code")
        except ValueError as e:
            self.assertEqual(str(e), "missing closing delimiter [`]")

if __name__ == "__main__":
    unittest.main()

