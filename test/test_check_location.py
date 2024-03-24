import sys
sys.path.append("../")

from source.CardGames import Card, Deck, Player, GameSetup

# Have to comment out the game initialization in CardGames.py for this to run
game = GameSetup()

# No burns
def test_single_wrong_guess():
    game.cards_in_play = [game.LowRangeDeck[0]]
    game.cards_in_play = [game.LowRangeDeck[1]]
    assert game.check_location(20, 0) == False

def test_single_correct_guess():
    game.cards_in_play = [game.LowRangeDeck[0], game.LowRangeDeck[1]]
    assert game.check_location(game.cards_in_play[0].value, 0) == True

def test_multiple_wrong_guesses():
    game.cards_in_play = [game.LowRangeDeck[0], game.LowRangeDeck[1]]
    assert game.check_location([20, 34], 0) == False

def test_multiple_correct_guesses():
    game.cards_in_play = [game.LowRangeDeck[0], game.LowRangeDeck[1]]
    assert game.check_location([game.cards_in_play[0].value, game.cards_in_play[1].value], 0) == True

# With burns
def test_single_wrong_guess_burn():
    game.cards_in_play = [[game.LowRangeDeck[0], game.MidRangeDeck[0]], [game.LowRangeDeck[1], game.MidRangeDeck[1]]]
    assert game.check_location(20, 0) == False

def test_single_correct_guess_burn():
    game.cards_in_play = [[game.LowRangeDeck[0], game.MidRangeDeck[0]], [game.LowRangeDeck[1], game.MidRangeDeck[1]]]
    assert game.check_location(game.cards_in_play[0][0].value, 0) == True

def test_multiple_wrong_guesses_burn():
    game.cards_in_play = [[game.LowRangeDeck[0], game.MidRangeDeck[0]], [game.LowRangeDeck[1], game.MidRangeDeck[1]]]
    assert game.check_location([20, 34], 0) == False

def test_multiple_correct_guesses_burn():
    game.cards_in_play = [[game.LowRangeDeck[0], game.MidRangeDeck[0]], [game.LowRangeDeck[1], game.MidRangeDeck[1]]]
    assert game.check_location([game.cards_in_play[0][0].value, game.cards_in_play[1][0].value], 0) == True