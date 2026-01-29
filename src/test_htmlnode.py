import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )