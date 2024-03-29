from testing_base import *


def test_summation():
    matthew = Player("Matthew")

    # input: list of hand of cards
    cards = [getCard('Clubs', 4), getCard('Hearts', 2), getCard('Spades', 3), getCard('Diamonds',1)]
    matthew.setHand(cards, isKnown=True)
    
    # call the sum_cards()
    total = sum_cards(matthew.hand)
    print(f"Total sum of cards in Matthew's hand: {total}")
    
    expect_value = 10
    assert total == expect_value, "Test failed: Summation incorrect"

def test_summation2():
    matthew = Player("Matthew")
    # input: list of hand of cards
    
    empty_cards = []
    matthew.setHand(empty_cards, isKnown=True)
    
    # call the sum_cards()
    total2 = sum_cards(matthew.hand)
    print(f"Total sum of cards in Matthew's hand: {total2}")
    
    expect_val = 0
    assert total2 == expect_val, "Test failed: Summation incorrect"

