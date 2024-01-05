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
                self.deck.append(Card(color=c, value=v))
                if v in {"skip", "draw two", "reverse", "draw four", "wild"}:
                    self.deck.append(Card(color=c, value=v))

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
                    print("")
                    print(f"Current Card: {self.pile[-1]}")
                    print("")
                    print("")
                    print(f"Hello {current_player}! Your hand is: ")
                    print(f"{list(enumerate(current_player.hand))}")
                    print("")
                    current_card_index = input("Pick your card by index, or draw (d): ")
                    if current_card_index.lower() == "d":
                        current_player.hand.append(self.deck.pop(0))
                        print("")
                        print("You drew a card")
                    elif current_card_index.lower != "d":
                        # later add color functionality

                        # while current_card_index not in range(len(current_player.hand)):
                        #     current_card_index = input("Number too high. Try again: ")
                        if (
                            current_player.hand[int(current_card_index)].value
                            == self.pile[-1].value
                            or current_player.hand[int(current_card_index)].color
                            == self.pile[-1].color
                        ):
                            # This is if they play the correct card
                            self.pile.append(
                                current_player.hand.pop(int(current_card_index))
                            )
                            print("")
                            print(f"You played: {self.pile[-1]}")
                            print("")
                            # current_player = self.players[1]
                        # elif current_card_index.lower() == 'd':
                        #     current_player.hand.append(self.deck.pop(0))
                        else:
                            print("")
                            current_card_index = input("Illegal card. Try again: ")
                            print("")
                else:
                    # during a bot's turn
                    can_play = False
                    # draw_count = 0
                    play_card_index = 0
                    bot_did_draw = False
                    for card in current_player.hand:
                        if (
                            card.value == self.pile[-1].value
                            or card.color == self.pile[-1].color
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
                    else:
                        current_player.hand.append(self.deck.pop(0))
                        # draw_count += 1
                        bot_did_draw = True
                    if bot_did_draw:
                        print("")
                        print(f"{current_player} drew a card. ")
                        print("")

                if len(current_player.hand) == 1:
                    print("")
                    print(f"{current_player}: Uno!")
                    print("")

                if len(current_player.hand) == 0:
                    print("")
                    print(f"{current_player} is out of cards! They win!")
                    print("")
                    self.game_over = True
                    return

        # def distribute_cards(self):
        """
        count from 0 to n, where n is the length of the number of
        cards in the deck. if the number is even, deal a card to
        player one, else deal a card to player 2
        (comment from pycard)

        **FOR LATER**
        We'll later have to change this for a variable amount of players
        """
        # for i in range(0, len(self.deck.card)):
        #     if i % 2 == 0:
        #         self.player.hand.append(self.deck.deal_card())
        #     else:
        #         self.player2.hand.append(self.deck.deal_card())

        """
        Let's write our own functionality to deal each player their hand
        """

    # def play(self):


"""
For now have deck be a list of cards in the game class

When we distribute the cards to the players,
we're going to pop cards from the deck list and append them to the player hand

Probably also need a game attribute called pile (discard pile?)

Need a new method maybe called "play"
While (self.game_over == False) loop over the players, play a card or draw a card
    Maybe:
        Display opponents hand length
        Display what each opponent played
    Display user's hand
    Display last card played
    if player.name == Player 1, ask user to pick a card
Maybe an attribute 
"""
