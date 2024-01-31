from testing_base import *
# Justyn Lee
def test_show_hand():

    matthew = Player("Matthew")

    five_spades = getCard("spades", 5)
    four_spades = getCard("Spades", 4)
    three_spades = getCard("spades", 3)
    two_spades = getCard("Spades", 2)
    one_spades = getCard("Spades", 1)
    cards = [ five_spades, four_spades, three_spades, two_spades, one_spades ]
    
    matthew.setHand( cards, isKnown=True )
    assert matthew.showHand() == None

def test_show_hand_face_cards():

    matthew = Player("Matthew")

    five_spades = getCard("hearts", 10)
    four_spades = getCard("hearts", 11)
    three_spades = getCard("hearts", 12)
    two_spades = getCard("hearts", 13)
    one_spades = getCard("hearts", 1)
    cards = [ five_spades, four_spades, three_spades, two_spades, one_spades ]
    
    matthew.setHand( cards, isKnown=True )
    assert matthew.showHand() == None