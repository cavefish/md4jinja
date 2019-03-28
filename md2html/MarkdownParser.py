from md2html.ParsedObject import ParsedObject


class MarkdownParser:

    def __init__(self):
        self._result = ParsedObject()

    def _parse(self, input_text):
        pass

    def parse_markdown(self, input_text):
        parser = MarkdownParser()
        parser._parse(input_text)
        return parser._result
