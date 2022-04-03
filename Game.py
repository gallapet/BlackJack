from Dealer import Dealer
from Player import Player
from Deck import PlayingCardDeck


class BlackJackGame:
    """Deal 2 cards to the player and the dealer, only show one of the dealer's cards."""

    def __init__(self):
        playingCardDeck = PlayingCardDeck()
        playingCardDeck.shuffle()
        self.deck = playingCardDeck.deck * 6  # Put 6 decks of cards in the game
        self.dealer = Dealer()
        self.player = Player()
        self.player_finished = False
        self.dealer_finished = False

    def card_deal(self):
        """Deal 2 cards to the player and the dealer"""
        self.player.take_card(self.deck.pop(0))  # Player card 1
        self.dealer.take_card(self.deck.pop(0))  # Dealer card 1
        self.player.take_card(self.deck.pop(0))  # Player card 2
        self.dealer.take_card(self.deck.pop(0))  # Dealer card 2

    def play(self):
        "Function that displays the player's hand and one of the dealer's cards. Then gives the player a choice of stand(stop) or hit(play)"
        "After every card dealt it checks if either person is bust and continues if not. Finally, the result is displayed"
        print("------------------------------------------------------------------------------------------------")
        print(f"You have been dealt {self.player.cards[0]} and {self.player.cards[1]}.")
        print(f"The Dealer has {self.dealer.cards[0]}.")
        if self.player.get_value() == 21:  # Auto stand on being dealt 21
            self.player_finished = True
            if self.dealer.get_value() != 21:  # Check if dealer also has 21, if not then blackjack!
                self.player.blackjack = True
                self.dealer_finished = True
        if self.dealer.get_value() == 21 and self.player.get_value() < 21:
            # Check if dealer has blackjack
            self.dealer.blackjack = True
            self.player_finished = True
            self.dealer_finished = True

        while not self.player_finished:
            if self.player.get_value() == 21:
                self.player_finished = True
                break
            player_choice = input(f"You have {self.player.get_value()}. Do you want to stand or hit? ")
            print("------------------------------------------------------------------------------------------------")
            if player_choice.startswith("h") and self.player.get_value() < 21:
                self.player.take_card(self.deck.pop(0))
                print("You now have " + ' and '.join(self.player.cards))
                if self.player.get_value() > 21:  # Check if player is bust
                    print("Bust!")
                    self.player.is_bust = True
                    self.player_finished = self.dealer_finished = True
            elif player_choice.startswith("s"):
                self.player_finished = True
        while self.dealer.get_value() < 17 and not self.dealer_finished:
            self.dealer.take_card(self.deck.pop(0))
            if self.dealer.get_value() > 21:  # Check if dealer is bust
                print("Dealer Bust!")
                self.dealer.is_bust = True
        BlackJackGame.result(self)  # Display result of the game

    def result(self):
        """Function that returns the result of the game"""
        print(f"You: {self.player.cards} [{self.player.get_value()}]")
        print(f"Dealer: {self.dealer.cards} [{self.dealer.get_value()}]")
        if self.player.blackjack:
            print("Blackjack! You win!")
        elif self.dealer.blackjack:
            print("Dealer has blackjack! Dealer wins!")
        elif (
                self.player.get_value() < self.dealer.get_value() and not self.dealer.is_bust) or self.player.is_bust:
            # Dealer wins if: player is bust or has a lower card value
            print("Dealer Wins!")
        elif (
                self.player.get_value() > self.dealer.get_value() and not self.player.is_bust) or self.dealer.is_bust:
            # Player wins if: dealer is bust or has a lower card value
            print("You Win!")
        else:
            # Otherwise it's a draw
            print("It's a push!")