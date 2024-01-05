class Card:
    # colors = ["red", "blue", "yellow", "green"]
    # values = [
    #     0,
    #     1,
    #     2,
    #     3,
    #     4,
    #     5,
    #     6,
    #     7,
    #     8,
    #     9,
    #     "skip",
    #     "draw two",
    #     "reverse",
    #     "draw four",
    #     "wild",
    # ]

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        return f"{self.color} {self.value}"

    # @property
    # def color(self):
    #     return self._color

    # @color.setter
    # def color(self, color):
    #     self._color = color

    # @property
    # def value(self):
    #     return self._value

    # @value.setter
    # def value(self, value):
    #     self._value = value
