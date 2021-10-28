"""Module for playing Blackjack."""
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
        self.deck = random.sample(self.deck, len(self.deck))            

class BlackJackGame:
    """Deal 2 cards to the player and the dealer, only show one of the dealer's cards."""
    
    def __init__(self):
        x = PlayingCardDeck()
        x.shuffle()
        self._deck = x.deck    
        self._dealer = Dealer()
        self._player = Player()
    
    def card_deal(self):       
        player_card_1 = self._player.take_card(self._deck.pop(0))
        dealer_card_1 = self._dealer.take_card(self._deck.pop(0))
        player_card_2 = self._player.take_card(self._deck.pop(0))
        dealer_card_1 = self._dealer.take_card(self._deck.pop(0))                
        
    def play(self):
        print(f"You have been dealt {self._player._cards[0]} and {self._player._cards[1]}. The Dealer has {self._dealer._cards[0]}.")
        player_finished = False
        while not player_finished:
            player_choice = input(f"You have {self._player.get_value()}. Do you want to stand or hit? ")
            if player_choice.startswith("h") and self._player.get_value() < 21:
                self._player.take_card(self._deck.pop(0))
                print("You now have " + ' and '.join(self._player._cards))
                if self._player.get_value() > 21:  
                    print("Bust!")
                    self._player._bust = True
                    player_finished = True
            elif player_choice.startswith("s"):
                player_finished = True
        dealer_finished = False
        while not dealer_finished:
            if self._dealer.get_value() < 17:
                self._dealer.take_card(self._deck.pop(0))
                if self._dealer.get_value() > 21:
                    print("Dealer Bust!")
                    self._dealer._bust = True
                    dealer_finished = True
            else:
                dealer_finished = True     
        BlackJackGame.result(self)

    def result(self):
        print(f"You: {self._player._cards}")
        print(f"Dealer: {self._dealer._cards}")
        if (self._player.get_value() > self._dealer.get_value() and self._player._bust == False) or self._dealer._bust == True:
            print("You Win!")
        elif (self._player.get_value() < self._dealer.get_value() and self._dealer._bust == False) or self._player._bust == True:
            print("You Lose!")
        else:
            print("It's a push!")    

class Hand:

    def __init__(self, cards):
        self._cards = cards

    def value_of_cards(self):
        card_value = 0
        values = {'02': 2, '03': 3, '04': 4,
                  '05': 5, '06': 6, '07': 7, 
                  '08': 8, '09': 9, '10': 10, 
                  'Ja': 10, 'Qu': 10, 'Ki': 10,
                  'Ac': 11}
        for card in self._cards:
            card_value += values[card[:2]]
        return card_value
        
    def display(self):
        return self._cards    
    
class Person:
    def __init__(self):
        self._cards = [] 
        self._bust = False
           
    def take_card(self, card):
        self._cards.append(card)

    def get_value(self):
        hand = Hand(self._cards) 
        return hand.value_of_cards()
        
class Player(Person):
    def __init__(self):
        super().__init__()    

class Dealer(Person):
    def __init__(self):
        super().__init__()
