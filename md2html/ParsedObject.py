
class ParsedObject:

    def __init__(self):
        self._items = []
        self._value = None

    def is_list(self):
        return True if self._items else False

    def is_value(self):
        return self._value is not None
