import sys

import pytest

sys.path.append('C:/Users/peter/Documents/Code/Python/BlackJack')

from Game import BlackJackGame
from Deck import PlayingCardDeck
from Player import Player
from Dealer import Dealer

@pytest.fixture
def set_up_card_deal():
    p = PlayingCardDeck()
    p.make_deck()
    b = BlackJackGame()
    b.deck = p.deck * 6
    b.player = Player()
    b.player.cards = []
    b.initial_card_deal()
    return p, b

@pytest.fixture
def player_blackjack():
    b = BlackJackGame()
    b.player = Player()
    b.dealer = Dealer()
    b.player.cards = ['Ace of Hearts', '10 of Hearts']
    b.dealer.cards = ['02 of Hearts', '03 of Hearts']
    return b

@pytest.fixture
def dealer_blackjack():
    b = BlackJackGame()
    b.player = Player()
    b.dealer = Dealer()
    b.player.cards = ['02 of Hearts', '03 of Hearts']
    b.dealer.cards = ['Ace of Hearts', '10 of Hearts']
    return b

def test_size_initial_card_deal(set_up_card_deal):
    assert len(set_up_card_deal[1].player.cards) == 2

def test_card_deal_takes_top_two_cards(set_up_card_deal):
    expected = ['Ace of Hearts', '03 of Hearts']
    assert set_up_card_deal[1].player.cards == expected

def test_player_has_blackjack(player_blackjack):
    player_blackjack.play()
    assert player_blackjack.player.blackjack == True

def test_dealer_does_not_have_blackjack(player_blackjack):
    player_blackjack.play()
    assert player_blackjack.dealer.blackjack == False

def test_dealer_has_blackjack(dealer_blackjack):
    dealer_blackjack.play()
    assert dealer_blackjack.dealer.blackjack == True

def test_player_does_not_have_blackjack(dealer_blackjack):
    dealer_blackjack.play()
    assert dealer_blackjack.player.blackjack == False
