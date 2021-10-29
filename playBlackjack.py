"""Module for playing Blackjack. Requires blackjack.py"""

import blackjack

p = blackjack.PlayingCardDeck()
g = blackjack.BlackJackGame()
g.card_deal()
g.play()