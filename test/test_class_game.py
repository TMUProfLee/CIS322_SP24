import pytest
from source.CardGames import Game, Player, Pot  # Adjust the import as necessary

@pytest.fixture
def setup_game():
    # Create a fixture that sets up the game environment before each test
    players = [Player("Alice", 1000), Player("Bob", 1000)]
    pot = Pot()
    game = Game(players, pot)
    return game, players, pot

def test_raise_bet(setup_game):
    game, players, pot = setup_game
    player_index = 0  # Alice
    raise_amount = 100
    assert game.raise_bet(player_index, raise_amount) == True
    assert players[player_index].money == 900
    assert pot.show_pot() == 100
    assert game.current_raise == raise_amount

def test_next_turn(setup_game):
    game, players, _ = setup_game
    game.next_turn()
    assert game.current_turn == 1  # Ensure the turn has moved to Bob

def test_match_raise(setup_game):
    game, players, pot = setup_game
    player_index = 0  
    raise_amount = 100
    game.raise_bet(player_index, raise_amount)
    game.next_turn()  
    game.match_raise(1) 
    assert players[1].money == 900  
    assert pot.show_pot() == 200  

def test_insufficient_funds_to_match_raise(setup_game):
    game, players, _ = setup_game
    # Set a player's money to less than the raise amount but more than 0
    players[1].money = 50  
    game.raise_bet(0, 100)  # First player raises
    assert players[1].money == 50, "Player with insufficient funds should still have their remaining money"
   

def test_player_folding(setup_game):
    game, players, pot = setup_game
    game.raise_bet(0, 100)  # First player raises
    players.pop(1)  # Remove the second player, simulating a fold
    assert len(game.players) == 1, "The game should now have one fewer player after a fold"

def test_sequential_raises(setup_game):
    game, players, pot = setup_game
    initial_pot = pot.show_pot()
    game.raise_bet(0, 100)  # First player raises
    game.next_turn()
    game.raise_bet(1, 200)  # Second player re-raises
    assert game.current_raise == 200, "The current raise should reflect the latest raise amount"
    assert pot.show_pot() == initial_pot + 300, "Pot should accumulate total of all raises"
