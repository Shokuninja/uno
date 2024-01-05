from card import Card
import random

""""
**WERE NOT USING THIS CLASS ANYMORE**
"""

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        """
        The cards attribute is populated by iterating over every possible suit
        and value in a nested loop to get every combination (in other words,
        the Cartesian product of the two sets)
        (this comment was from pycard)
        """
        self.cards.clear()
        colors = {"red", "yellow", "green", "blue"}
        values = {
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            "skip",
            "draw two",
            "reverse",
            "draw four",
            "wild",
        }

        for c in colors:
            for v in values:
                self.cards.append(Card(color=c, value=v))
                if v in {"skip", "draw two", "reverse", "draw four", "wild"}:
                    self.cards.append(Card(color=c, value=v))
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    @property
    def has_cards(self):
        return len(self.cards) > 0

    def deal_card(self):
        if not self.has_cards:
            raise ValueError("cannot deal from empty deck")
        return self.cards.pop()
