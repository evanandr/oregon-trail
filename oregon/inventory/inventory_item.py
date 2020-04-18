class InventoryItem(object):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = int(value)

    def add(self, value):
        self._value += int(value)

    def subtract(self, value):
        self._value -= int(value)

    def __init__(self):
        self._value = 0
