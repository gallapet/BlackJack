from Dealer import Dealer
from Player import Player
from Deck import PlayingCardDeck

class BlackJackGame:
    """Deal 2 cards to the player and the dealer, only show one of the dealer's cards."""

    def __init__(self):
        playing_card_deck = PlayingCardDeck()
        playing_card_deck.make_deck()
        playing_card_deck.shuffle()
        self.deck = playing_card_deck.deck * 6  # Put 6 decks of cards in the game
        self.dealer = Dealer()
        self.player = Player()

    def initial_card_deal(self):
        """Deal 2 cards to the player and the dealer"""
        for i in range(2):
            self.player.take_card(self.deck)
            self.dealer.take_card(self.deck)

    def play(self):
        """Function that displays the player's hand and one of the dealer's cards. Then gives the player a choice of
        stand(stop) or hit(play)
        After every card dealt it checks if either person is bust and continues if not."""
        print("------------------------------------------------------------------------------------------------")
        print(f"You have been dealt {self.player.cards[0]} and {self.player.cards[1]}.")
        print(f"The Dealer has {self.dealer.cards[0]}.")
        if self.player.get_value() == 21:
            self.player_dealt_21()
        if self.dealer.get_value() == 21:
            self.dealer.blackjack = self.dealer_dealt_21()

        while not self.player.finished:
            if self.player.get_value() >= 21:
                if self.player.get_if_bust():
                    self.player.is_bust()
                    self.dealer.is_finished()
                break
            player_choice = input(f"You have {self.player.get_value()}. Do you want to stand or hit? ")
            print("------------------------------------------------------------------------------------------------")
            if player_choice.startswith("h"):
                self.player_hit()
            elif player_choice.startswith("s"):
                self.player.is_finished()
        while not self.dealer.finished:
            if self.dealer.get_value() > 16:
                if self.dealer.get_if_bust():
                    self.dealer.is_bust()
                break
            else:
                self.dealer.take_card(self.deck)

        self.result()

    def result(self):
        """Function that returns the result of the game"""
        print(f"You: {self.player.cards} [{self.player.get_value()}]")
        print(f"Dealer: {self.dealer.cards} [{self.dealer.get_value()}]")
        if self.player.blackjack:
            print("Blackjack! You win!")
        elif self.dealer.blackjack:
            print("Dealer has blackjack! Dealer wins!")
        elif self.player.bust_status:
            print("You Bust! Dealer wins!")
        elif self.dealer.bust_status:
            print("Dealer Bust! You win!")
        elif self.player.get_value() < self.dealer.get_value() and not self.dealer.bust_status:
            # Dealer wins if: player is bust or has a lower card value
            print("Dealer Wins!")
        elif self.player.get_value() > self.dealer.get_value() and not self.player.bust_status:
            # Player wins if: dealer is bust or has a lower card value
            print("You Win!")
        else:
            # Otherwise it's a draw
            print("It's a push!")

    def player_dealt_21(self):
        self.player.finished = True  # Auto stand on being dealt 21
        if self.dealer.get_value() != 21:  # Check if dealer also has 21, if not then blackjack!
            self.player.blackjack = True
            self.dealer.is_finished()

    def dealer_dealt_21(self):
        # Check if dealer has blackjack
        if self.player.get_value() < 21:
            self.player.is_finished()
            return True
        return False

    def player_hit(self):
        self.player.take_card(self.deck)
        print("You now have " + ' and '.join(self.player.cards))
