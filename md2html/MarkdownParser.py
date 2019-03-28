from markdown2 import Markdown

from md2html.ParsedObject import ParsedObject


class MarkdownParser:

    def __init__(self):
        self._result = ParsedObject()
        self._node_heap = [self._result]
        self._markdown = Markdown()

    def _parse(self, input_text):
        """
        :type input_text: str
        """
        unparsed_lines = []
        input_iterator = InputIterator(input_text)

        while input_iterator.next():
            line = input_iterator.get()
            if line.is_parser:
                if unparsed_lines:
                    self._add_html_item(unparsed_lines)
                current_parser_directive = line.parser_content
                self.update_node_heap(current_parser_directive)
            else:
                unparsed_lines.append(line.text)

        self._add_html_item(unparsed_lines)

    def update_node_heap(self, current_parser_directive):
        if current_parser_directive[0] == "begin":
            if current_parser_directive[1] == "item":
                candidate = self._node_heap[-1]
                for key in current_parser_directive[2:]:
                    candidate = candidate[key]
                self._node_heap.append(candidate)

    def _add_html_item(self, unparsed_lines):
        self._node_heap[-1].set_value("\n".join(unparsed_lines), self._markdown.convert("\n".join(unparsed_lines)).strip())

    @staticmethod
    def parse_markdown(input_text):
        parser = MarkdownParser()
        parser._parse(input_text)
        return parser._result


class InputIterator:

    def __init__(self, input_value):
        self._pos = -1
        self._lines = input_value.split("\n")

    def next(self):
        self._pos += 1
        if self._pos < len(self._lines):
            return self.get()
        else:
            return None

    def get(self):
        text = self._lines[self._pos]  # type: str
        if text.startswith("[parser]:"):
            return IteratorItem(
                True,
                text.split("(")[1].rsplit(")")[0].split(" "),
                None
            )
        return IteratorItem(False, [], text)


class IteratorItem:

    def __init__(self, is_parser, parser_content, text):
        self.is_parser=is_parser
        self.parser_content = parser_content
        self.text = text
