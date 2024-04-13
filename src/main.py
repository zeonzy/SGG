from textnode import TextNode

def text_node_to_html_node(text_node):
    if text_node == "ext_type_text":
        pass
    elif text_node == "text_type_bold":
        pass
    elif text_node == "text_type_italic":
        pass
    elif text_node == "text_type_code":
        pass
    elif text_node == "text_type_link":
        pass
    elif text_node == "text_type_image":
        pass
    else:
        raise Exception("Unknown TextNode type")

def main():
    dummy_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    dummy_node2 = TextNode("note2", "test", "localhost")
    dummy_node3 = TextNode("note2", "test", "localhost")


    print(dummy_node1)
    print(dummy_node2)
    print(dummy_node1 == dummy_node2)
    print(dummy_node2 == dummy_node3)

main()