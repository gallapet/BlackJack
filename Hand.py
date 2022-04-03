class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.card_value = 0
        self.ace_count = 0
        self.values = {'02': 2, '03': 3, '04': 4,
                       '05': 5, '06': 6, '07': 7,
                       '08': 8, '09': 9, '10': 10,
                       'Ja': 10, 'Qu': 10, 'Ki': 10,
                       'Ac': 11}

    def value_of_cards(self):
        """Calculates the value of the cards in play"""
        for card in self.cards:
            if card[:2] == 'Ac':
                self.ace_count += 1
            self.card_value += self.values[card[:2]]
        """Adjust values of aces if player is bust"""
        while self.card_value > 21 and self.ace_count > 0:
            self.card_value -= 10
            self.ace_count -= 1
        return self.card_value

    def players_hand(self):
        return self.cards
