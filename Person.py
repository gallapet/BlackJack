from Hand import Hand
from Deck import PlayingCardDeck

class Person:

    def __init__(self):
        self.cards = []
        self.hand = Hand(self.cards)
        self.deck = PlayingCardDeck()
        self.bust_status = False
        self.blackjack = False
        self.finished = False

    def take_card(self, deck):
        """This function allows a player to hit after the initial deal"""
        card = deck.pop(0)
        self.cards.append(card)

    def get_value(self):
        """Gets the value of each players' hand"""
        hand = Hand(self.cards)
        return hand.value_of_cards()

    def get_if_bust(self):
        if self.get_value() > 21:
            return True
        return False

    def is_bust(self):
        self.bust_status = True
        self.is_finished()

    def is_finished(self):
        self.finished = True


