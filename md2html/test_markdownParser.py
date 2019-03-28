from unittest import TestCase

from md2html.MarkdownParser import MarkdownParser
from md2html.ParsedObject import ParsedObject


class TestMarkdownParser(TestCase):

    def setUp(self):
        super(TestMarkdownParser, self).setUp()

    def test_parse_simple_text(self):
        input_value = "test content"
        result = MarkdownParser.parse_markdown(input_value)

        assert isinstance(result, ParsedObject)
        self.assert_string(result.text(), input_value)
        self.assert_string(result.html(), "<p>test content</p>")
        self.assert_string(result, "<p>test content</p>")

    def test_parse_text_with_item(self):
        input_value = """[parser]: # (begin item body)
test content
[parser]: # (end item)"""

        result = MarkdownParser.parse_markdown(input_value)
        assert result.is_map()
        assert "body" in result._children
        assert result._children["body"] == result.body
        self.assert_string(result.body, "<p>test content</p>")
        self.assert_string(result, "<p>test content</p>")
        self.assert_string(result.text(), "test content")

    def test_parse_tree(self):
        input_value = """[parser]: # (begin item a)
[parser]: # (begin item b)
text on b
[parser]: # (end item)
[parser]: # (end item)
[parser]: # (begin item c)
text on c
[parser]: # (end item)
        """

        result = MarkdownParser.parse_markdown(input_value)
        self.assert_string(result.a.b.text(), "text on b")
        self.assert_string(result.c.text(), "text on c")

    def assert_string(self, first, second, msg=None):
        self.assertMultiLineEqual(str(first), str(second), msg)
