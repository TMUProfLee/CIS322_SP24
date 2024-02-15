from testing_base import *
from pair_finder import *

def test_one_pair():
    joe = Player("Joe")

    two_clubs = getCard("clubs", 2)
    ace_spades = getCard("spades", 1)
    five_hearts = getCard("hearts", 5)
    three_clubs = getCard("clubs", 3)
    two_hearts = getCard("hearts", 2)

    cards = [two_clubs, ace_spades, five_hearts, three_clubs, two_hearts]

    joe.setHand(cards, isKnown=True)
    assert(has_pair(joe)) == True

def test_no_pair():
    john = Player("John")

    two_clubs = getCard("clubs", 2)
    ace_spades = getCard("spades", 1)
    five_hearts = getCard("hearts", 5)
    three_clubs = getCard("clubs", 3)
    ten_hearts = getCard("hearts", 10)

    cards = [two_clubs, ace_spades, five_hearts, three_clubs, ten_hearts]

    john.setHand(cards, isKnown=True)
    assert(has_pair(john)) == False
    
def test_three_of_a_kind():

    jim = Player("Jim")

    two_clubs = getCard("clubs", 2)
    two_spades = getCard("spades", 2)
    five_hearts = getCard("hearts", 5)
    three_clubs = getCard("clubs", 3)
    two_hearts = getCard("hearts", 2)

    cards = [two_clubs, two_spades, five_hearts, three_clubs, two_hearts]

    jim.setHand(cards, isKnown=True)
    assert(has_pair(jim)) == True

def test_two_pair():
    jack = Player("Jack")

    two_clubs = getCard("clubs", 2)
    ace_spades = getCard("spades", 1)
    ace_hearts = getCard("hearts", 1)
    three_clubs = getCard("clubs", 3)
    two_hearts = getCard("hearts", 2)

    cards = [two_clubs, ace_spades, ace_hearts, three_clubs, two_hearts]

    jack.setHand(cards, isKnown=True)
    assert(has_pair(jack)) == True

