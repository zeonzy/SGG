import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
from block import *

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test1 = markdown_to_blocks('''# This is a heading            

                                   
                                                                      
                   This is a paragraph of text. It has some **bold** and *italic* words inside of it.             


* This is a list item                                  
      * This is another list item     
                                   
                                   
                                                       
                                   
                                   
                                   ''')
        result1 = ['# This is a heading', 
                   'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                   '* This is a list item\n* This is another list item']
        self.assertEqual(test1, result1)

        test2 = markdown_to_blocks('''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items''')
        result2 = ['This is **bolded** paragraph', 
                  'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                  '* This is a list\n* with items']
        self.assertEqual(test2, result2)
        

    

       


if __name__ == "__main__":
    unittest.main()
