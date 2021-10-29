"""Module for running a Blackjack game."""
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
        self.aces = {"Ace of Spades", "Ace of Diamonds", "Ace of Hearts", "Ace of Clubs"}
        self._dealer = Dealer()
        self._player = Player()
        self.player_finished = False
        self.dealer_finished = False
        
    
    def card_deal(self):       
        self._player.take_card(self._deck.pop(0))  # Player card 1
        self._dealer.take_card(self._deck.pop(0))  # Dealer card 1
        self._player.take_card(self._deck.pop(0))  # Player card 2
        self._dealer.take_card(self._deck.pop(0))  # Dealer card 2        
    '''
    def ace_value(self):
        final_value = self.Person.get_value()
        if self.aces & set(self.Person._cards) and self.Person.get_value() > 21 :
            return final_value - 10
        else:
            return final_value
    '''     
        
    def play(self):
        print("------------------------------------------------------------------------------------------------")
        print(f"You have been dealt {self._player._cards[0]} and {self._player._cards[1]}.")
        print(f"The Dealer has {self._dealer._cards[0]}.")
        if self._player.ace_value() == 21:
            self.player_finished = True
        while not self.player_finished:
            player_choice = input(f"You have {self._player.ace_value()}. Do you want to stand or hit? ")
            print("------------------------------------------------------------------------------------------------")
            if player_choice.startswith("h") and self._player.ace_value() < 21:
                self._player.take_card(self._deck.pop(0))
                print("You now have " + ' and '.join(self._player._cards))
                if self._player.ace_value() > 21:  
                    print("Bust!")
                    self._player._bust = True
                    self.player_finished = self.dealer_finished = True
            elif player_choice.startswith("s"):
                self.player_finished = True
        while self._dealer.ace_value() < 17 and not self.dealer_finished:
            self._dealer.take_card(self._deck.pop(0))
            if self._dealer.ace_value() > 21:
                print("Dealer Bust!")
                self._dealer._bust = True    
        BlackJackGame.result(self)

    def result(self):
        print(f"You: {self._player._cards} [{self._player.ace_value()}]")
        print(f"Dealer: {self._dealer._cards} [{self._dealer.ace_value()}]")
        if (self._player.ace_value() < self._dealer.ace_value() and self._dealer._bust == False) or self._player._bust == True:
            print("Dealer Wins!")
        elif (self._player.ace_value() > self._dealer.ace_value() and self._player._bust == False) or self._dealer._bust == True:
            print("You Win!")
        else:
            print("It's a push!")  

class Hand:

    def __init__(self, cards):
        self._cards = cards
        self.card_value = 0

    def value_of_cards(self):        
        values = {'02': 2, '03': 3, '04': 4,
                  '05': 5, '06': 6, '07': 7, 
                  '08': 8, '09': 9, '10': 10, 
                  'Ja': 10, 'Qu': 10, 'Ki': 10,
                  'Ac': 11}
        for card in self._cards:
            self.card_value += values[card[:2]]
        return self.card_value
        
    def display(self):
        return self._cards    
    
class Person:

    def __init__(self):
        self._cards = [] 
        self._bust = False
        self.aces = {"Ace of Spades", "Ace of Diamonds", "Ace of Hearts", "Ace of Clubs"}
           
    def take_card(self, card):
        self._cards.append(card)

    def get_value(self):
        hand = Hand(self._cards) 
        return hand.value_of_cards()
    
    def ace_value(self):
        final_value = Person.get_value(self)
        if self.aces & set(self._cards) and Person.get_value(self) > 21 :
            return final_value - 10
        else:
            return final_value
        
class Player(Person):
    def __init__(self):
        super().__init__()    

class Dealer(Person):
    def __init__(self):
        super().__init__()
