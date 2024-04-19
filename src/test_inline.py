import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
from textnode import *
from inline import *

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

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        result = [('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png')]
        self.assertEqual(extract_markdown_images(text),result)

        text1 = "this is a text with ![image1](https://test.com/png1) and another ![image2](https://test.com/png2) and another ![image3](https://test.com/png3)."
        result1 = [('image1', 'https://test.com/png1'), ('image2', 'https://test.com/png2'), ('image3', 'https://test.com/png3')]
        self.assertEqual(extract_markdown_images(text1),result1)

        text2 = "This text contains a [link](www.google.nl), another link [link](www.boot.dev) and 1 more linke [link](www.test.org)"
        result2 = []
        self.assertEqual(extract_markdown_images(text2),result2)


    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and ![another](https://www.example.com/another)"
        result = [('link', 'https://www.example.com')]
        self.assertEqual(extract_markdown_links(text),result)

        text1 = "This text contains a [link1](www.google.nl), another link [link2](www.boot.dev) and 1 more linke [link3](www.test.org)"
        result1 = [('link1', 'www.google.nl'), ('link2', 'www.boot.dev'), ('link3', 'www.test.org')]
        self.assertEqual(extract_markdown_links(text1),result1)

        text2 = "this is a text with ![image](https://test.com/png1) and another ![image](https://test.com/png2) and another ![image](https://test.com/png3)."
        result2 = []
        self.assertEqual(extract_markdown_links(text2),result2) 

    def test_split_nodes_image(self):
        test1 = split_nodes_image([TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        "text")])
        test_result1 = [
        TextNode("This is text with an ", "text"),
        TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and another ", "text"),
        TextNode("second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
        ]
        self.assertEqual(test1, test_result1)

        test2 = split_nodes_image([TextNode("code block", "text"),
                                   TextNode("code block", "code"),
                                   TextNode("![image](www.image.png) text", "text"),
                                   TextNode("[link](www.link.com) text", "text"),
                                   TextNode("![image1](www.image1.png)![image2](www.image2.png)", "text"),
        ])
        test_result2 = [TextNode("code block", "text"),
                        TextNode("code block", "code"),
                        TextNode("image", "image", "www.image.png"), TextNode(" text", "text"),
                        TextNode("[link](www.link.com) text", "text"),
                        TextNode("image1", "image", "www.image1.png"), TextNode("image2", "image", "www.image2.png")
        ]
        self.assertEqual(test2, test_result2)

    def test_split_nodes_link(self):
        test1 = split_nodes_link([TextNode(
        "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        "text")])
        test_result1 = [
        TextNode("This is text with an ", "text"),
        TextNode("link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and another ", "text"),
        TextNode("second link", "link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        self.assertEqual(test1, test_result1)

        test2 = split_nodes_link([TextNode("code block", "text"),
                                   TextNode("code block", "code"),
                                   TextNode("![image](www.image.png) text", "text"),
                                   TextNode("[link](www.link.com) text", "text"),
                                   TextNode("[link1](www.link1.nl)[link2](www.link2.org)", "text")
        ])
        test_result2 = [TextNode("code block", "text"),
                        TextNode("code block", "code"),
                        TextNode("![image](www.image.png) text", "text"),
                        TextNode("link", "link", "www.link.com"), TextNode(" text", "text"),
                        TextNode("link1", "link", "www.link1.nl"), TextNode("link2", "link", "www.link2.org")
        ]
        self.assertEqual(test2, test_result2)

    def test_text_to_textnodes(self):
        test1 = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        test1 = text_to_textnodes(test1)
        result1 = [TextNode("This is ", "text"),
                    TextNode("text", "bold"),
                    TextNode(" with an ", "text"),
                    TextNode("italic", "italic"),
                    TextNode(" word and a ", "text"),
                    TextNode("code block", "code"),
                    TextNode(" and an ", "text"),
                    TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    TextNode(" and a ", "text"),
                    TextNode("link", "link", "https://boot.dev"),
                ]
        self.assertEqual(test1, result1)
    
        

if __name__ == "__main__":
    unittest.main()

