
class ParsedObject(object):

    def __init__(self):
        self.items = []
        self._children = {}
        self._html_value = None
        self._raw_value = None

    def is_list(self):
        return not self.is_map() if self.items else False

    def is_map(self):
        return True if self._children else False

    def has_value(self):
        return self._html_value is not None

    def set_value(self, raw_value, html_value):
        self._raw_value = raw_value
        self._html_value = html_value

    def text(self):
        # type: () -> str
        if self.has_value():
            return self._raw_value
        elif self.is_map():
            return "\n".join(map(lambda x: x.text(), self._children.values()))
        else:
            return "\n".join(map(lambda x: x.text(), self.items))

    def html(self):
        # type: () -> str
        if self.has_value():
            return self._html_value
        elif self.is_map():
            return "\n".join(map(str, self._children.values()))
        else:
            return "\n".join(map(str, self.items))

    def __str__(self):
        return self.html()

    def __len__(self):
        return len(self.items)

    def __getattr__(self, item):
        if item not in self._children:
            self._children[item] = ParsedObject()
            self.items.append(item)
        return self._children[item]

    def __getitem__(self, item):
        return self.__getattr__(item)
