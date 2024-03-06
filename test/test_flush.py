import sys, os, pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from CardGames import Card, Poker 
@pytest.fixture

def poker_game():
    # Fixture to create a new Poker game instance for each test case
    return Poker([], None)

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

def test_check_flush_mixed_suits(poker_game):
    mixed_hand = [
        Card("Hearts", 2, None, None),
        Card("Clubs", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Diamonds", 5, None, None),
        Card("Spades", 6, None, None),
    ]
    assert poker_game.check_flush(mixed_hand) == False, "Hand with mixed suits should not be a flush."

def test_check_flush_same_suit_different_values(poker_game):
    flush_hand_different_values = [
        Card("Hearts", 10, None, None),
        Card("Hearts", 11, None, None),
        Card("Hearts", 12, None, None),
        Card("Hearts", 13, None, None),
        Card("Hearts", 1, None, None),
    ]
    assert poker_game.check_flush(flush_hand_different_values) == True, "Flush with different values should pass."

def test_check_flush_in_larger_hand(poker_game):
    larger_flush_hand = [
        Card("Hearts", 2, None, None),
        Card("Hearts", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Hearts", 5, None, None),
        Card("Hearts", 6, None, None),
        Card("Clubs", 9, None, None),
        Card("Diamonds", 10, None, None),
    ]
    assert poker_game.check_flush(larger_flush_hand) == True, "Flush within a larger hand should pass."

def test_check_flush_with_distractions(poker_game):
    distracted_flush_hand = [
        Card("Hearts", 2, None, None),
        Card("Hearts", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Hearts", 5, None, None),
        Card("Hearts", 6, None, None),
        Card("Clubs", 2, None, None),
        Card("Diamonds", 3, None, None),
    ]
    assert poker_game.check_flush(distracted_flush_hand) == True, "Flush with other suits present should pass."

def test_check_straight_flush(poker_game):
    straight_flush_hand = [
        Card("Hearts", 2, None, None),
        Card("Hearts", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Hearts", 5, None, None),
        Card("Hearts", 6, None, None),
    ]
    assert poker_game.check_flush(straight_flush_hand) == True, "Straight flush should still be recognized as a flush."

