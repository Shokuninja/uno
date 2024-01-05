from deck import Deck


class Player:
    def __init__(self, player_num):
        self.name = f"Player {player_num}"
        self.hand = []
        # self.games = []

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # def draw(self, n):
    #     for _ in range(n):
    #         self.hand.append(Deck.pop(0))
