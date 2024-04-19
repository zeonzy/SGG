import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
from textnode import TextNode, text_node_to_html_node


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

       


if __name__ == "__main__":
    unittest.main()
