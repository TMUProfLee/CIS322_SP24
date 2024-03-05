import pytest
from CardGames import Card, Poker, Player, Deck  

def test_check_flush_true():
    # Creating a flush hand
    flush_hand = [
        Card("Hearts", 2, None, None),
        Card("Hearts", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Hearts", 5, None, None),
        Card("Hearts", 6, None, None),
    ]
    poker_game = Poker([], None)  # Initialize Poker with empty player list and None as dealer
    assert poker_game.check_flush(flush_hand) == True, "Expected to recognize a flush."

def test_check_flush_false():
    # Creating a non-flush hand
    non_flush_hand = [
        Card("Hearts", 2, None, None),
        Card("Clubs", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Diamonds", 5, None, None),
        Card("Hearts", 6, None, None),
    ]
    poker_game = Poker([], None)  # Initialize Poker with empty player list and None as dealer
    assert poker_game.check_flush(non_flush_hand) == False, "Expected to not recognize as a flush."

# Additional tests for edge cases, other hand types, and game flow can be added here
