import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
from textnode import TextNode


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



        


if __name__ == "__main__":
    unittest.main()
