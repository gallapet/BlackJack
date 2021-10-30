"""Module for playing Blackjack. Requires blackjack.py"""

import blackjack  # imports the blackjack module

"""Set up the game"""
p = blackjack.PlayingCardDeck()
g = blackjack.BlackJackGame()
g.card_deal()
#q = blackjack.Person()

#q.get_value()
"""Play the game"""
g.play()