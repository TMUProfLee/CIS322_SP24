from testing_base import *
#For demonstrative purposes, marshall's hand will be set to the starting cards of fugitive.
#This is only to demonstrate the function show_marshall_hand()
def test_show_marshall_hand():
    game = GameSetup()
    game.marshall.hand = game.starting_cards
    game.marshall.knownCards = [False, False, False]
    game.start_game()

test_show_marshall_hand()