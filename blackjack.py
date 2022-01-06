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
        """Shuffle deck"""
        self.deck = random.sample(self.deck, len(self.deck))            

class BlackJackGame:
    """Deal 2 cards to the player and the dealer, only show one of the dealer's cards."""
    
    def __init__(self):
        playingCardDeck = PlayingCardDeck()
        playingCardDeck.shuffle()
        self._deck = playingCardDeck.deck * 6  # Put 6 decks of cards in the game    
        self._dealer = Dealer()
        self._player = Player()
        self.player_finished = False
        self.dealer_finished = False
    
    def card_deal(self):       
        """Deal 2 cards to the player and the dealer"""
        self._player.take_card(self._deck.pop(0))  # Player card 1
        self._dealer.take_card(self._deck.pop(0))  # Dealer card 1
        self._player.take_card(self._deck.pop(0))  # Player card 2
        self._dealer.take_card(self._deck.pop(0))  # Dealer card 2         
        
    def play(self):
        "Function that displays the player's hand and one of the dealer's cards. Then gives the player a choice of stand(stop) or hit(play)"
        "After every card dealt it checks if either person is bust and continues if not. Finally, the result is displayed"
        print("------------------------------------------------------------------------------------------------")
        print(f"You have been dealt {self._player._cards[0]} and {self._player._cards[1]}.")
        print(f"The Dealer has {self._dealer._cards[0]}.")
        if self._player.get_value() == 21:  # Auto stand on being dealt 21
            self.player_finished = True
            if self._dealer.get_value() != 21:  # Check if dealer also has 21, if not then blackjack!
                self._player._blackjack = True
                self.dealer_finished = True
        if self._dealer.get_value() == 21 and self._player.get_value() < 21:
            # Check if dealer has blackjack
            self._dealer._blackjack = True
            self.player_finished = True
            self.dealer_finished = True
            
        while not self.player_finished:
            if self._player.get_value() == 21:
                self.player_finished = True
                break
            player_choice = input(f"You have {self._player.get_value()}. Do you want to stand or hit? ")
            print("------------------------------------------------------------------------------------------------")
            if player_choice.startswith("h") and self._player.get_value() < 21:
                self._player.take_card(self._deck.pop(0))
                print("You now have " + ' and '.join(self._player._cards))
                if self._player.get_value() > 21:  # Check if player is bust
                    print("Bust!")
                    self._player._bust = True
                    self.player_finished = self.dealer_finished = True
            elif player_choice.startswith("s"):
                self.player_finished = True
        while self._dealer.get_value() < 17 and not self.dealer_finished:
            self._dealer.take_card(self._deck.pop(0))
            if self._dealer.get_value() > 21:  # Check if dealer is bust
                print("Dealer Bust!")
                self._dealer._bust = True    
        BlackJackGame.result(self)  # Display result of the game

    def result(self):
        """Function that returns the result of the game"""
        print(f"You: {self._player._cards} [{self._player.get_value()}]")
        print(f"Dealer: {self._dealer._cards} [{self._dealer.get_value()}]")
        if self._player._blackjack == True:
            print("Blackjack! You win!")
        elif self._dealer._blackjack == True:
            print("Dealer has blackjack! Dealer wins!")
        elif (self._player.get_value() < self._dealer.get_value() and self._dealer._bust == False) or self._player._bust == True:
            # Dealer wins if: player is bust or has a lower card value
            print("Dealer Wins!")
        elif (self._player.get_value() > self._dealer.get_value() and self._player._bust == False) or self._dealer._bust == True:
            # Player wins if: dealer is bust or has a lower card value 
            print("You Win!")
        else:
            # Otherwise it's a draw
            print("It's a push!")  

class Hand:

    def __init__(self, cards):
        self._cards = cards
        self.card_value = 0
        self.ace_count = 0
        self.values =  {'02': 2, '03': 3, '04': 4,
                        '05': 5, '06': 6, '07': 7, 
                        '08': 8, '09': 9, '10': 10, 
                        'Ja': 10, 'Qu': 10, 'Ki': 10,
                        'Ac': 11}

    def value_of_cards(self):
        """Calculates the value of the cards in play"""
        for card in self._cards:
            if card[:2] == 'Ac':
                self.ace_count += 1
            self.card_value += self.values[card[:2]]
        """Adjust values of aces if player is bust"""
        while self.card_value > 21 and self.ace_count > 0:
            self.card_value -= 10
            self.ace_count -= 1
        return self.card_value
    
class Person:

    def __init__(self):
        self._cards = [] 
        self._hand = Hand(self._cards)
        self._bust = False
        self._blackjack = False
                   
    def take_card(self, card):
        """This function allows a player to hit after the initial deal"""
        self._cards.append(card)

    def get_value(self):
        """Gets the value of each players' hand"""
        hand = Hand(self._cards) 
        return hand.value_of_cards()
class Player(Person):
    def __init__(self):
        super().__init__()    

class Dealer(Person):
    def __init__(self):
        super().__init__()