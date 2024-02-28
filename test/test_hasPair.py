from testing_base import *


def test_noPair():
    billy = Player("Billy")

    five_spades = getCard("spades", 5)
    four_spades = getCard("Spades", 4)
    three_spades = getCard("spades", 3)
    two_spades = getCard("Spades", 2)
    one_spades = getCard("Spades", 1)
    cards = [ five_spades, four_spades, three_spades, two_spades, one_spades ]
    
    billy.setHand( cards, isKnown=True )
    assert has_pair(billy) == False
    
def test_yesPair():
    denny = Player("Denny")

    five_spades = getCard("spades", 5)
    five_hearts = getCard("Hearts", 5)
    three_spades = getCard("spades", 3)
    two_spades = getCard("Spades", 2)
    one_spades = getCard("Spades", 1)
    cards2 = [ five_spades, five_hearts, three_spades, two_spades, one_spades ]
    
    denny.setHand( cards2, isKnown=True )
    assert has_pair(denny) == True

