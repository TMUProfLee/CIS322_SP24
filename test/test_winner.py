import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from CardGames import Card, Poker, Player, Deck

@pytest.fixture
def setup_poker():
    # Create and configure a new Poker game instance for each test case
    deck = Deck()
    deck.shuffle()  # Ensure the deck is shuffled before each test
    players = [Player("Alice", 100), Player("Bob", 100)]
    poker_game = Poker(players, deck)
    return poker_game

def test_evaluate_flush_true(setup_poker):
    # This should test for a non-sequential flush
    flush_hand = [
        Card("Hearts", 2, None, None),
        Card("Hearts", 10, None, None),
        Card("Hearts", 4, None, None),
        Card("Hearts", 9, None, None),
        Card("Hearts", 7, None, None),
    ]
    result = setup_poker.evaluate_hand(flush_hand)
    assert result == ("Flush", [10, 9, 7, 4, 2]), "Expected to recognize a flush."

def test_evaluate_straight_false(setup_poker):
    # This should test for a straight that is incorrectly identified
    non_straight_hand = [
        Card("Hearts", 2, None, None),
        Card("Clubs", 3, None, None),
        Card("Hearts", 8, None, None),
        Card("Diamonds", 5, None, None),
        Card("Hearts", 6, None, None),
    ]
    result = setup_poker.evaluate_hand(non_straight_hand)
    assert result == ("High Card", 8), "Expected not to recognize as a straight."

def test_find_winner_with_flush(setup_poker):
    setup_poker.players[0].hand = [
        Card("Hearts", 2, None, None),
        Card("Hearts", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Hearts", 5, None, None),
        Card("Hearts", 6, None, None),
    ]
    setup_poker.players[1].hand = [
        Card("Hearts", 2, None, None),
        Card("Clubs", 3, None, None),
        Card("Hearts", 4, None, None),
        Card("Diamonds", 5, None, None),
        Card("Hearts", 6, None, None),
    ]
    winners = setup_poker.find_winner()
    assert len(winners) == 1 and winners[0].name == "Alice", "Alice should win with a flush."


