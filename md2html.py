#!/usr/bin/python2
import sys

from md2html.markdown_parser import MarkdownParser
from jinja2 import Template

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: md2html input.md template.jinja"
        sys.exit(1)

    with open(sys.argv[1]) as input_md:
        content = MarkdownParser.parse_markdown(input_md.readlines())

    with open(sys.argv[2]) as input_jinja:
        print Template("".join(input_jinja.readlines())).render(content=content)
