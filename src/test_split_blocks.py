import unittest
from split_blocks import markdown_to_blocks
from split_blocks import block_to_block_type

class TestBlocks(unittest.TestCase):
    def test_eq(self):
        test = markdown_to_blocks("""# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item""")
        result = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                """* This is the first list item in a list block
            * This is a list item
            * This is another list item"""]
        self.assertEqual(test, result)

        test = markdown_to_blocks("")
        result = []
        self.assertEqual(test, result)
        
        test = markdown_to_blocks("""This has way too many newlines

                                  for some text""")
        result = ["This has way too many newlines", "for some text"]
        self.assertEqual(test,result)

        test = block_to_block_type("# Header")
        result = "heading"
        self.assertEqual(test, result)

        test = block_to_block_type("```code```")
        result = "code"
        self.assertEqual(test,result)

        test = block_to_block_type("Text with some # bold # characters")
        result = "paragraph"
        self.assertEqual(test,result)

        test = block_to_block_type("""> something
But not a list""")
        result = "paragraph"
        self.assertEqual(test, result)
        test = block_to_block_type("""something
> But not a list""")
        result = "paragraph"
        self.assertEqual(test, result)
        test = block_to_block_type("""> test
> I love pie""")
        result = "quote"
        self.assertEqual(test, result)

        test = block_to_block_type("""* One thing
* two things""")
        result = "unordered_list"
        self.assertEqual(test,result)

        test = block_to_block_type("""- One thing
- two things""")
        result = "unordered_list"
        self.assertEqual(test,result)

        test = block_to_block_type("""* One thing
 two things""")
        result = "paragraph"
        self.assertEqual(test,result)

        test = block_to_block_type("""1. One thing
2. Another thing""")
        result = "ordered_list"
        self.assertEqual(test,result)

        test = block_to_block_type("""1. One thing
. Another thing""")
        result = "paragraph"
        self.assertEqual(test,result)
if __name__ == "__main__":
    unittest.main()