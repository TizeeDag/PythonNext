from numbers import Number


class BigThing:
    def __init__(self, value):
        self._value = value

    def size(self):
        if isinstance(self._value, Number):
            return self._value
        return len(self._value)


class BigCat(BigThing):
    def __init__(self, value, weight):
        super().__init__(value)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        if self._weight > 15:
            return "Fat"
        return "OK"


if __name__ == "__main__":
    print(BigThing("balloon").size())
    print(BigCat("mitzy", 22).size())
