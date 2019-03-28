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
                    unparsed_lines = []
                current_parser_directive = line.parser_content
                self.update_node_heap(current_parser_directive)
            else:
                unparsed_lines.append(line.text)

        if unparsed_lines:
            self._add_html_item(unparsed_lines)

    def update_node_heap(self, command):
        if command[0] == "begin":
            candidate = self._node_heap[-1]
            if command[1] == "item":
                for key in command[2:]:
                    candidate = candidate[key]
            elif command[1] == "value":
                next_item = ParsedObject()
                candidate.items.append(next_item)
                candidate = next_item
            self._node_heap.append(candidate)
        elif command[0] == "end":
            del self._node_heap[-1]

    def _add_html_item(self, unparsed_lines):
        self._node_heap[-1].set_value("\n".join(unparsed_lines), self._markdown.convert("\n".join(unparsed_lines)).strip())

    @staticmethod
    def parse_markdown(input_text):
        parser = MarkdownParser()
        parser._parse(input_text)
        if len(parser._node_heap) > 1:
            raise Exception("There are {} open nodes on the heap".format(len(parser._node_heap) - 1))
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
