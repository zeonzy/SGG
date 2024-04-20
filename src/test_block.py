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

    def test_block_to_block_type(self):
        test1 = block_to_block_type("just an ordinary paragraph")
        self.assertEqual(test1, "paragraph")

        test2 = block_to_block_type(".# just an ordinary paragraph")
        self.assertEqual(test2, "paragraph")
        
        test3 = block_to_block_type("# heading 1X")
        self.assertEqual(test3, "heading")

        test4 = block_to_block_type("###### heading 6X")
        self.assertEqual(test4, "heading")

        test5 = block_to_block_type("####### heading 7X is just a paragraph")
        self.assertEqual(test5, "paragraph")

        test6 = block_to_block_type("#missing space makes this a paragraph")
        self.assertEqual(test6, "paragraph")

        test7 = block_to_block_type("###### ###########weird but allowed")
        self.assertEqual(test7, "heading")

        test8 = block_to_block_type("####### ###########weird but to many starting # for a heading")
        self.assertEqual(test8, "paragraph")

        test21 = block_to_block_type("```just an ordinary paragraph")
        self.assertEqual(test21, "paragraph")

        test22 = block_to_block_type("```just an ordinary paragraph''")
        self.assertEqual(test22, "paragraph")

        test23 = block_to_block_type("just an ordinary paragraph```")
        self.assertEqual(test23, "paragraph")

        test24 = block_to_block_type("```CODE DETECTED```")
        self.assertEqual(test24, "code")

        test25 = block_to_block_type(".``` wrong starter ```")
        self.assertEqual(test25, "paragraph")

        test26 = block_to_block_type("``` wrong ender ```!")
        self.assertEqual(test26, "paragraph")

        test31 = block_to_block_type(">valid quoteblock")
        self.assertEqual(test31, "quote")

        test32 = block_to_block_type(">valid quoteblock\n>still valid\n>still valid\n>ends valid")
        self.assertEqual(test32, "quote")

        test33 = block_to_block_type(">valid quoteblock\n>still valid\nINVALID\n>ends valid")
        self.assertEqual(test33, "paragraph")

        test34 = block_to_block_type(">valid quoteblock\n>still valid\n>still valid\n<ends INVALID")
        self.assertEqual(test34, "paragraph")

        test41 = block_to_block_type("*missing space")
        self.assertEqual(test41, "paragraph")

        test42 = block_to_block_type("-*Missing space")
        self.assertEqual(test42, "paragraph")

        test43 = block_to_block_type("* VALID")
        self.assertEqual(test43, "unordered_list")

        test44 = block_to_block_type("* VALID")
        self.assertEqual(test44, "unordered_list")

        test45 = block_to_block_type("* VALID\n* VALID\n* VALID\n* VALID")
        self.assertEqual(test45, "unordered_list")

        test46 = block_to_block_type("- VALID\n- VALID\n- VALID\n- VALID")
        self.assertEqual(test46, "unordered_list")

        test47 = block_to_block_type("- VALID\n* VALID\n- VALID\n* VALID")
        self.assertEqual(test47, "unordered_list")

        test48 = block_to_block_type("- VALID\n* VALID\n# INVALID\n* VALID")
        self.assertEqual(test48, "paragraph")

        test49 = block_to_block_type("- VALID\n* VALID\n- VALID\nINVALID")
        self.assertEqual(test49, "paragraph")

        test51 = block_to_block_type("1. VALID list")
        self.assertEqual(test51, "ordered_list")

        test52 = block_to_block_type("2. INVALID list start")
        self.assertEqual(test52, "paragraph")

        test53 = block_to_block_type("1 INVALID missing dot")
        self.assertEqual(test53, "paragraph")

        test54 = block_to_block_type("1. VALID\n2. VALID\n3. VALID\n4. VALID")
        self.assertEqual(test54, "ordered_list")

        test55 = block_to_block_type("1. VALID\n2. VALID\n2. INVALID\n4. VALID")
        self.assertEqual(test55, "paragraph")

        test56 = block_to_block_type("1. VALID\n2. VALID\n3. VALID\n4. VALID\nINVALID")
        self.assertEqual(test56, "paragraph")



        

    

       


if __name__ == "__main__":
    unittest.main()
