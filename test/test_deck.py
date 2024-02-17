from testing_base import *

    #Check for 42 cards:
def test_deck_lenghOfCards():
    test_deck = Deck()
    test_length = []
    for i in range(42):
        test_card = test_deck.getCard()
        test_length.append(test_card)
        print(test_card.value)
   # assert highestCard(testCardValues).value == 5
