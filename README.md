# Uno Card Game

Welcome to the Uno Card Game! This Python program allows you to play the classic Uno card game against computer-controlled players. The game is implemented using classes for Game, Player, and Card.

## Getting Started

To start a game, simply run the provided Python script. You can personalize the game by specifying the number of players (between 2 and 4) when creating the `Game` object. Each player will be dealt a hand of cards to begin the game.

```python
# Example: Create a game with 3 players
game = Game(num_players=3)
```

## Gameplay

The game follows standard Uno rules. Players take turns playing cards that match the top card of the discard pile either by color or value. If a player cannot play a matching card, they must draw a card from the deck. Special cards such as "Skip," "Draw Two," and "Draw Four" introduce additional strategic elements.

### Player Input

- During a human player's turn, they can choose to play a card by entering the index of the card in their hand or draw a card by entering "d" when prompted.

### Winning the Game

The game continues until one player has no cards left in their hand. The player with an empty hand is declared the winner, and the game concludes.

## Card Deck

The Uno deck consists of cards with different colors and values. Special cards include "Skip," "Draw Two," "Reverse," "Draw Four," and "Wild." The deck is initialized at the start of the game, and cards are drawn and played throughout.

## Playing Against Bots

If you don't have enough human players, the game includes computer-controlled players. They follow the same rules as human players and add a challenging aspect to the game.

## Author

This Uno Card Game was created by Shokuninja.

Feel free to customize and enhance the game as you like! Have fun playing Uno!