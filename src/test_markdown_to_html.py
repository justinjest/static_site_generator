import unittest
from markdown_to_html import *
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):

        test = markdown_to_html_node("""This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)""")
        result = '<div><p>This is <b>text</b> with an <i>italic</i> word and a <code>code block</code> and an <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan image"> and a <a href="https://boot.dev">link</a></p></div>'
        self.assertEqual(test, result)

        test = markdown_to_html_node("""* this is an unordered list
* there are two things in it""")
        result = "<div><ul><li>this is an unordered list</li><li>there are two things in it</li></ul></div>"
        self.assertEqual(test, result)

        test = markdown_to_html_node("""1. An ordered list
2. Nicely ordered""")
        result = "<div><ol><li>1. An ordered list</li><li>2. Nicely ordered</li></ol></div>"
        self.assertEqual(test,result)

        test = markdown_to_html_node("""# header""")
        result = "<div><h1>header</h1></div>"
        self.assertEqual(test,result)

        test = markdown_to_html_node("""# header

* list 1
* list 2""")
        result = "<div><h1>header</h1><ul><li>list 1</li><li>list 2</li></ul></div>"
        self.assertEqual(test, result)

        test = markdown_to_html_node("""```Codeing```""")
        result = "<div><pre><code>Codeing</code></pre></div>"
        self.assertEqual(test,result)

        test = markdown_to_html_node("""# Hello world

## Welcome to my website

```Code lives here```

And some *more complicated* things""")
        result = "<div><h1>Hello world</h1><h2>Welcome to my website</h2><pre><code>Code lives here</code></pre><p>And some <i>more complicated</i> things</p></div>"
        self.assertEqual(test,result)    

        test = markdown_to_html_node(""">You miss 100% of the shots you don't take
>Wayne Gretzky
>Michael Scott""")
        result = """<div><blockquote>You miss 100% of the shots you don't take
Wayne Gretzky
Michael Scott</blockquote></div>"""
        self.assertEqual(test, result)

        test = extract_title("# Hello")
        result = "Hello"
        self.assertEqual(test, result)

        test = extract_title(" # Hello")
        result = "Hello"
        self.assertEqual(test,result)

if __name__ == "__main__":
    unittest.main()