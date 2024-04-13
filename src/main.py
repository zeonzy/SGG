from textnode import TextNode, text_node_to_html_node

def main():
    dummy_node1 = TextNode("This is a text node", "text")
    dummy_node2 = TextNode("Dit een bolde claim", "bold")
    dummy_node3 = TextNode("deze is schuin", "italic")
    dummy_node4 = TextNode("wat code", "code")
    dummy_node5 = TextNode("een linkje", "link", "https://www.boot.dev")
    dummy_node6 = TextNode("This is a text node", "image", "https://www.boot.dev")

    print(text_node_to_html_node(dummy_node1))
    print(text_node_to_html_node(dummy_node2))
    print(text_node_to_html_node(dummy_node3))
    print(text_node_to_html_node(dummy_node4))
    print(text_node_to_html_node(dummy_node5))
    print(text_node_to_html_node(dummy_node6))

'''
    print(dummy_node1)
    print(dummy_node2)
    print(dummy_node1 == dummy_node2)
    print(dummy_node2 == dummy_node3)

    print(dummy_node2.text)
    print(dummy_node2.text_type)
    print(dummy_node2.url)
'''



main()