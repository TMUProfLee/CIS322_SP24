from testing_base import *

#setup

    #First5
def test_highestCard():
    card1 = getCard("Diamonds", 1)
    card2 = getCard("Diamonds", 2)
    card3 = getCard("Diamonds", 3)
    card4 = getCard("Diamonds", 4)
    card5 = getCard("Diamonds", 5)
    testCardValues = [card1, card2, card3, card4, card5]
    assert highestCard(testCardValues) == 5


    #last5
def test_highestCard_lastFive():
    card1 = getCard("Diamonds", 13)
    card2 = getCard("Diamonds", 12)
    card3 = getCard("Diamonds", 11)
    card4 = getCard("Diamonds", 10)
    card5 = getCard("Diamonds", 9)
    testCardValues = [card1, card2, card3, card4, card5]
    assert highestCard(testCardValues) == 13

    #random
def test_highestCard_random():
    card1 = getCard("Diamonds", 5)
    card2 = getCard("Diamonds", 12)
    card3 = getCard("Diamonds", 11)
    card4 = getCard("Diamonds", 1)
    card5 = getCard("Diamonds", 4)
    testCardValues3 = [card1, card2, card3, card4, card5]
    assert highestCard(testCardValues) == 12

    #samevalues
def test_hightestCard_sameValues():
    card1 = getCard("Diamonds", 5)
    card2 = getCard("Spades", 5)
    card3 = getCard("Diamonds", 2)
    card4 = getCard("Diamonds", 1)
    card5 = getCard("Diamonds", 4)
    testCardValues3 = [card1, card2, card3, card4, card5]
    assert highestCard(testCardValues) == 12

