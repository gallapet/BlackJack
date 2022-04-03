import random

class PlayingCardDeck:
    """Generate a pack of cards."""

    def __init__(self):
        """Generate a card deck."""
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.ranks = ['Ace', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'Jack', 'Queen', 'King']
        self.deck = []

    def make_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(rank + ' of ' + suit)
        return self.deck

    def shuffle(self):
        """Shuffle deck"""
        self.deck = random.sample(self.deck, len(self.deck))
        return self.deck
