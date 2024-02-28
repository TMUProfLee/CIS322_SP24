from testing_base import *

def test_deck_functionality_escape_card():
    test_deck = Deck()
    escape_card = test_deck.getCard()
    assert split_card() [0] == escape_card

def test_deck_functionality_deck_3_highest():

    test_list = split_card() [1]
    card41 = test_list[0].value

    assert card41 == 41

def test_deck_functionality_deck_3_lowest():

    test_list = split_card() [1]
    card29 = test_list[12].value

    assert card29 == 29

def test_deck_functionality_deck_2_highest():

    test_list = split_card() [2]
    card28 = test_list[0].value

    assert card28 == 28

def test_deck_functionality_deck_2_lowest():

    test_list = split_card() [2]
    card15 = test_list[13].value

    assert card15 == 15

def test_deck_functionality_deck_1_highest():

    test_list = split_card() [3]
    card14 = test_list[0].value

    assert card14 == 14

def test_deck_functionality_deck_1_lowest():

    test_list = split_card() [3]
    card4 = test_list[10].value

    assert card4 == 4

def test_deck_functionality_startingdeck_highest():

    test_list = split_card() [4]
    card3 = test_list[0].value

    assert card3 == 3

def test_deck_functionality_startingdeck_lowest():

    test_list = split_card() [4]
    card1 = test_list[2].value

    assert card1 == 1