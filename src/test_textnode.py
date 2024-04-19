import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
from textnode import TextNode, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node11 = TextNode("This is a text node", "bold")
        node12 = TextNode("This is a text node", "bold", None)
        node13 = TextNode("This is a text node", "bold", "www.url.com")
        node14 = TextNode("This is a text node", "bold", "www.url.nl")

        test = 12
        node21 = TextNode("completely different text", "bold")
        node22 = TextNode(test, "bold", None)
        node23 = TextNode("completely different text", "www.url.com")
        node24 = TextNode("completely different text", "www.url.nl")
        
        node31 = TextNode("This is a text node", "italic")
        node32 = TextNode("This is a text node", "italic", "www.www.com")
        node33 = TextNode("This is a text node", "italic", None)

        node41 = TextNode("completely different text", "bold")
        node42 = TextNode("completely different text", "underlinded", None)
        node43 = TextNode("completely different text", "italic", None)
        
        self.assertEqual(node11, node11)
        self.assertEqual(node11, node12)
        self.assertNotEqual(node11, node13)
        self.assertTrue(node11 == node11)
        self.assertTrue(node11 == node12)
        self.assertFalse(node11 == node13)
        self.assertFalse(node13 == node14)
        self.assertNotEqual(node21, node22)
        self.assertNotEqual(node23, node24)
        self.assertTrue(node31 == node33)
        self.assertFalse(node32 == node33)
        self.assertFalse(node11 == node31)
        self.assertEqual(node21, node41)
        self.assertNotEqual(node41, node42)
        self.assertNotEqual(node42, node43)

    def test_text_node_to_html_node(self):
        dummy_node1 = TextNode("This is a text node", "text")
        dummy1_result = '|tag = [None], value = [This is a text node], children = [None], props = [None]|'
        dummy_node2 = TextNode("Dit een bolde claim", "bold")
        dummy2_result = '|tag = [b], value = [Dit een bolde claim], children = [None], props = [None]|'
        dummy_node3 = TextNode("deze is schuin", "italic")
        dummy3_result = '|tag = [i], value = [deze is schuin], children = [None], props = [None]|'
        dummy_node4 = TextNode("wat code", "code")
        dummy4_result = '|tag = [code], value = [wat code], children = [None], props = [None]|'
        dummy_node5 = TextNode("een linkje", "link", "https://www.boot.dev")
        dummy5_result = "|tag = [a], value = [een linkje], children = [None], props = [{'href': 'https://www.boot.dev'}]|"
        dummy_node6 = TextNode("This is a text node", "image", "https://www.boot.dev")
        dummy6_result = "|tag = [img], value = [None], children = [None], props = [{'src': 'https://www.boot.dev', 'alt': 'This is a text node'}]|"

        self.assertEqual(str(text_node_to_html_node(dummy_node1)), dummy1_result)
        self.assertEqual(str(text_node_to_html_node(dummy_node2)), dummy2_result)
        self.assertEqual(str(text_node_to_html_node(dummy_node3)), dummy3_result)
        self.assertEqual(str(text_node_to_html_node(dummy_node4)), dummy4_result)
        self.assertEqual(str(text_node_to_html_node(dummy_node5)), dummy5_result)
        self.assertEqual(str(text_node_to_html_node(dummy_node6)), dummy6_result)

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
