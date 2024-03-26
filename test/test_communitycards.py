import sys
import os
import pytest

# Adjust the path to find your module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from CardGames import Card, Deck, Player, Dealer, Poker

@pytest.fixture
def poker_game_with_community_cards():
    deck = Deck()  # Assuming Deck is properly implemented in CardGames.py
    dealer = Dealer(deck)
    players = [Player("Alice", 100), Player("Bob", 100)]
    poker_game = Poker(players, dealer)
    dealer.deal_community_cards(3, players)  # Deal 3 community cards to all players
    return poker_game, players

def test_community_cards_shared_among_players(poker_game_with_community_cards):
    _, players = poker_game_with_community_cards
    # All players should have the same 3 community cards in their hands
    community_cards = players[0].hand[-3:]  # Assuming the last 3 cards are community cards
    for player in players[1:]:  # Skip the first player as it's used as reference
        assert player.hand[-3:] == community_cards, "All players should share the same community cards"

def test_reveal_community_cards(poker_game_with_community_cards):
    poker_game, players = poker_game_with_community_cards
    # Initially, let's assume all community cards are not revealed (knownCards is False)
    for player in players:
        player.reveal_cards(3)  # Reveal 3 cards, assuming they are the community cards
        assert all(player.knownCards[-3:]), "Community cards should be revealed and known to all players"
