import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            value="click",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="hello", props=None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_empty_dict(self):
        node = HTMLNode(tag="p", value="hello", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_constructor_sets_fields(self):
        children = [HTMLNode(tag="span", value="child")]
        node = HTMLNode(tag="p", value="hello", children=children, props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "hello")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, {"class": "text"})