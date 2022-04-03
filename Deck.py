import random


class PlayingCardDeck:
    """Generate a pack of cards."""

    def __init__(self):
        """Generate a card deck."""
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        ranks = ['Ace', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'Jack', 'Queen', 'King']
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(rank + ' of ' + suit)

    def shuffle(self):
        """Shuffle deck"""
        self.deck = random.sample(self.deck, len(self.deck))
