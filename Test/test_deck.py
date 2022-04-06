import sys

# sys.path.append('C:/Users/peter/Documents/Code/Python/BlackJack')
sys.path.append('D:/Peter/Code/Python/BlackJack')

from Deck import PlayingCardDeck

def test_size_make_deck():
    p = PlayingCardDeck()
    assert len(p.make_deck()) == 52

def test_make_deck():
    p = PlayingCardDeck()
    expected = ['Ace of Hearts', '02 of Hearts', '03 of Hearts', '04 of Hearts', '05 of Hearts', '06 of Hearts',
                '07 of Hearts', '08 of Hearts', '09 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts',
                'King of Hearts', 'Ace of Spades', '02 of Spades', '03 of Spades', '04 of Spades', '05 of Spades',
                '06 of Spades', '07 of Spades', '08 of Spades', '09 of Spades', '10 of Spades', 'Jack of Spades',
                'Queen of Spades', 'King of Spades', 'Ace of Clubs', '02 of Clubs', '03 of Clubs', '04 of Clubs',
                '05 of Clubs', '06 of Clubs', '07 of Clubs', '08 of Clubs', '09 of Clubs', '10 of Clubs',
                'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Diamonds', '02 of Diamonds',
                '03 of Diamonds', '04 of Diamonds', '05 of Diamonds', '06 of Diamonds', '07 of Diamonds',
                '08 of Diamonds', '09 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
                'King of Diamonds']
    assert p.make_deck() == expected

def test_shuffle():
    p = PlayingCardDeck()
    p.make_deck()
    expected = ['Ace of Hearts', '02 of Hearts', '03 of Hearts', '04 of Hearts', '05 of Hearts', '06 of Hearts',
                '07 of Hearts', '08 of Hearts', '09 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts',
                'King of Hearts', 'Ace of Spades', '02 of Spades', '03 of Spades', '04 of Spades', '05 of Spades',
                '06 of Spades', '07 of Spades', '08 of Spades', '09 of Spades', '10 of Spades', 'Jack of Spades',
                'Queen of Spades', 'King of Spades', 'Ace of Clubs', '02 of Clubs', '03 of Clubs', '04 of Clubs',
                '05 of Clubs', '06 of Clubs', '07 of Clubs', '08 of Clubs', '09 of Clubs', '10 of Clubs',
                'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Diamonds', '02 of Diamonds',
                '03 of Diamonds', '04 of Diamonds', '05 of Diamonds', '06 of Diamonds', '07 of Diamonds',
                '08 of Diamonds', '09 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
                'King of Diamonds']
    assert p.shuffle() != expected

def test_check_shuffle_has_no_effect_on_deck_size():
    p = PlayingCardDeck()
    p.make_deck()
    assert len(p.shuffle()) == 52
