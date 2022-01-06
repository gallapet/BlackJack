"""Module for playing Blackjack. Requires blackjack.py"""

import blackjack  # imports the blackjack module

"""Set up the game"""
game = blackjack.BlackJackGame()
game.card_deal()

"""Play the game"""
game.play()