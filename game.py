import random
from player import Player
from card import Card

"""
THINGS TO PERSONALIZE:
I want to be able to put in a (2 >= number >= 4) to decide
how many are playing, so let's give game a players list attribute.
Each player will need to be dealt a hand.
"""


class Game:
    def __init__(self, num_players):
        # self.player1 = p1
        # self.player2 = p2
        self.players = []
        self.num_players = num_players
        self.game_over = False
        self.winner = None
        # self.last_card = Card
        self.deck = []
        self.pile = []
        self.skipped = False
        self.draw_two = False
        self.reverse = False
        self.draw_four = False
        self.special_card = False

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
                if v not in {"draw four", "wild"}:
                    self.deck.append(Card(value=v, color=c))
                    if v in {"skip", "draw two", "reverse"}:
                        self.deck.append(Card(value=v, color=c))

        for i in range(4):
            self.deck.append(Card(value="wild"))
            self.deck.append(Card(value="draw four"))

        self.pile.append(self.deck[random.randrange(0, 39)])

        self.shuffle()

        for i in range(num_players):
            p = Player(i + 1)
            self.players.append(p)

        for player in self.players:
            for i in range(5):
                player.hand.append(self.deck.pop(0))
                # player.hand.append(self.pile[-1])

        # self.player1.games.append(self)
        # self.player2.games.append(self)

    def shuffle(self):
        random.shuffle(self.deck)

    # def draw(self, player):
    #     player.hand.append(self.deck.pop(0))

    def play(self):
        while self.game_over == False:
            for current_player in self.players:
                if current_player == self.players[0]:
                    if not self.special_card:
                        print("")
                        print(f"Current Card: {self.pile[-1]}")
                        print("")
                        print("")
                        print(f"Hello {current_player}! Your hand is: ")
                        print(f"{list(enumerate(current_player.hand))}")
                        print("")
                        current_card_index = input(
                            "Pick your card by index, or draw (d): "
                        )
                        if current_card_index.lower() == "d":
                            current_player.hand.append(self.deck.pop(0))
                            print("")
                            print("You drew a card")
                            print("")
                        elif current_card_index.lower != "d":
                            # later add color functionality

                            # while current_card_index not in range(len(current_player.hand)):
                            #     current_card_index = input("Number too high. Try again: ")
                            if (
                                current_player.hand[int(current_card_index)].value
                                == self.pile[-1].value
                                or current_player.hand[int(current_card_index)].color
                                == self.pile[-1].color
                                or current_player.hand[int(current_card_index)].color
                                == "rainbow"
                                or self.pile[-1].color == "rainbow"
                            ):
                                # This is if you play the correct card
                                self.pile.append(
                                    current_player.hand.pop(int(current_card_index))
                                )
                                print("")
                                print(f"You played: {self.pile[-1]}")
                                print("")
                                if self.pile[-1].value == "skip":
                                    self.special_card = True
                                    self.skipped = True
                                elif self.pile[-1].value == "draw two":
                                    self.special_card = True
                                    self.draw_two = True
                                elif self.pile[-1].value == "draw four":
                                    self.special_card = True
                                    self.draw_four = True
                                # current_player = self.players[1]
                            # elif current_card_index.lower() == 'd':
                            #     current_player.hand.append(self.deck.pop(0))
                            else:
                                print("")
                                current_card_index = input("Illegal card. Try again: ")
                                print("")
                    else:
                        if self.skipped:
                            print("")
                            print(f"{current_player} is skipped. ")
                            print("")
                            self.skipped = False
                            self.special_card = False
                        elif self.draw_two:
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            print("")
                            print(f"{current_player} drew 2 cards. ")
                            print("")
                            self.draw_two = False
                            self.special_card = False
                        elif self.draw_four:
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            print("")
                            print(f"{current_player} drew 4 cards. ")
                            print("")
                            self.draw_four = False
                            self.special_card = False
                else:
                    if not self.special_card:
                        # during a bot's turn
                        can_play = False
                        # draw_count = 0
                        play_card_index = 0
                        bot_did_draw = False
                        for card in current_player.hand:
                            if (
                                card.value == self.pile[-1].value
                                or card.color == self.pile[-1].color
                                or card.color == "rainbow"
                                or self.pile[-1].color == "rainbow"
                            ):
                                can_play = True
                                play_card_index = current_player.hand.index(card)
                                # print(play_card_index)

                        if can_play:
                            card = current_player.hand.pop(play_card_index)
                            self.pile.append(card)
                            print("")
                            print(f"{current_player} played {card}")
                            print("")
                            if self.pile[-1].value == "skip":
                                self.special_card = True
                                self.skipped = True
                            elif self.pile[-1].value == "draw two":
                                self.special_card = True
                                self.draw_two = True
                            elif self.pile[-1].value == "draw four":
                                self.special_card = True
                                self.draw_four = True

                        else:
                            current_player.hand.append(self.deck.pop(0))
                            # draw_count += 1
                            bot_did_draw = True
                        if bot_did_draw:
                            print("")
                            print(f"{current_player} drew a card. ")
                            print("")
                    else:
                        if self.skipped:
                            print("")
                            print(f"{current_player} is skipped. ")
                            print("")
                            self.skipped = False
                            self.special_card = False
                        elif self.draw_two:
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            print("")
                            print(f"{current_player} drew 2 cards. ")
                            print("")
                            self.draw_two = False
                            self.special_card = False
                        elif self.draw_four:
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            current_player.hand.append(self.deck.pop(0))
                            print("")
                            print(f"{current_player} drew 4 cards. ")
                            print("")
                            self.draw_four = False
                            self.special_card = False

                if len(current_player.hand) == 1:
                    print("")
                    print(f"{current_player}: Uno!")
                    print("")

                if len(current_player.hand) == 0:
                    print("")
                    print(f"{current_player} is out of cards! {current_player} wins!")
                    print("")
                    self.game_over = True
                    return
