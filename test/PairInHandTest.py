from testing_base import *
def test_function():
    matthew = Player("Matthew")
    five_spades = getCard("spades", 5)
    four_spades = getCard("Spades", 4)
    three_spades = getCard("spades", 3)
    two_spades = getCard("Spades", 2)
    one_spades = getCard("Spades", 1)
    cards = [ five_spades, four_spades, three_spades, two_spades, one_spades ]
test_function()