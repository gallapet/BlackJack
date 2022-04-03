from Hand import Hand


class Person:

    def __init__(self):
        self.cards = []
        self.hand = Hand(self.cards)
        self.is_bust = False
        self.blackjack = False

    def take_card(self, card):
        """This function allows a player to hit after the initial deal"""
        self.cards.append(card)

    def get_value(self):
        """Gets the value of each players' hand"""
        hand = Hand(self.cards)
        return hand.value_of_cards()
