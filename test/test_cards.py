from testing_base import *
#Nick Busman

# def test_win_screen():
#     nick = Player("Nick")
#     logan = Player("Logan")
#     win_player = ["nick", "logan"]
#     Win_screen(win_player)
#     assert Win_screen(win_player) == True

def test_hand_sort():
    nick = Player("Nick")
    five_spades = getCard("Spades", 5)
    four_hearts = getCard("Hearts", 4)
    three_clubs = getCard("Clubs", 3)
    two_diamonds = getCard("Diamonds", 2)
    three_diamonds = getCard("Diamonds", 3)
    one_spades = getCard("Spades", 1)
    cards = [three_clubs, five_spades, four_hearts, two_diamonds, three_diamonds, one_spades]
    assert hand_sort(cards) == [three_diamonds, two_diamonds,  five_spades, one_spades, four_hearts, three_clubs]


# def test_no_pair():
# #deck = Deck()
# #dealer = Dealer(deck)
# #matthew = Player("Matthew")
# five_spades = getCard("spades", 5)
# four_spades = getCard("Spades", 4)
# three_spades = getCard("spades", 3)
# two_spades = getCard("Spades", 2)
# one_spades = getCard("Spades", 1)
# cards = [ five_spades, four_spades, three_spades, two_spades, one_spades ]
# assert Detect_Pair(cards) == False
# def test_with_pair():
# five_spades = getCard("spades", 5)
# four_spades = getCard("Spades", 4)
# two_hearts = getCard("hearts", 2)
# two_spades = getCard("Spades", 2)
# one_spades = getCard("Spades", 1)
# cards = [ five_spades, four_spades, two_hearts, two_spades, one_spades ]
# assert Detect_Pair(cards) == True

