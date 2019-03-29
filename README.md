[parser]: # (begin item title)
# Markdown parser for MJLM templates
This is a MarkDown parser that transforms into html by the use of mjml as a jinja template

[parser]: # (end item title)

[parser]: # (begin item blog)

[parser]: # (begin value)
[parser]: # (begin item title)

# How it works

[parser]: # (end item value)
[parser]: # (begin item body)

This parser reads comments on Markdown files, and interpret them
 into parser directives. Then, those directives transform
 the markdown document structure into a python object.
 
After, that object is passed into a jinja template as the context variable `content`.

[parser]: # (end item body)
[parser]: # (end value)

[parser]: # (begin value)
[parser]: # (begin item title)

# How to test

[parser]: # (end item value)
[parser]: # (begin item body)

In order to execute this program, install the dependencies on
 `requiriments.txt` and run the next command:
 
`python md2html.py readme.md test_files/test_03/template.mjml > readme.mjml`

Yes. This readme is formatted and can be prettified by this tool ;-)

After that, you will have a fully functional mjml file that can be
 converted into html.

[parser]: # (end item body)
[parser]: # (end value)

[parser]: # (end blog)

[parser]: # (begin item end_motto)

*Go, now, and check this tool*

[parser]: # (end item end_motto)
[parser]: # (begin item credits title)

# Thanks and credits

[parser]: # (end item credits title)
[parser]: # (begin item credits body)

This tool was created during the EQUINOX 2019, a hackaton for, and by, Telefonica Digital employees.

[parser]: # (end item credits body)