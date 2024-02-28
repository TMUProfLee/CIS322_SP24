from testing_base import *

    #Check for 42 cards:
def test_deck_lenghOfCards():
    test_deck = Deck()
    test_length = []
    for i in range(42):
        test_card = test_deck.getCard()
        test_length.append(test_card)
    assert len(test_length) == 42

    #Check get card functionality
def test_deck_getCard():
    test_deck = Deck()
    test_card = test_deck.getCard()
    assert test_card.value == 42

    #Check reset function
def test_deck_reset():
    test_deck = Deck()

    for i in range(14):
        card = test_deck.getCard()

    test_deck.reset()
    assert test_deck.size == 42