from flask import Flask, request, render_template
from mac_import import *
import pytest

# Initialize Flask app for testing
app = Flask(__name__)
app.config['TESTING'] = True

# Create instances of game components
deck = Deck()
dealer = Dealer(deck)
players = []  # Add more players as needed
game = Poker(players, dealer)
pot = Pot()

# Define the player_action route for testing
@app.route('/player_action', methods=['POST'])
def player_action():
    try:
        amount = int(request.form['amount'])
        if amount < 0:
            raise ValueError("Invalid amount")  # Raise an error for negative amount
        if game.currentPlayer >= len(players):
            raise IndexError("Player index out of range")  # Raise an error if currentPlayer index is out of range

        player = players[game.currentPlayer]  # Use index directly to access player
        # Perform the player action in the game
        bet_result = Call(player, amount, pot)
        if isinstance(bet_result, str):
            error_message = bet_result  # Store the error message
        else:
            error_message = None  # No error message
        return render_template('game.html', players=players, pot=pot.show_pot(), error=error_message)
    except Exception as e:
        return str(e), 500  # Return the error message and HTTP status code 500 for internal server error

# Define a test case using pytest
def test_player_action():
    with app.test_client() as client:
        # Make a POST request to the player_action route with valid data
        response = client.post('/player_action', data={'amount': '10'})
        assert b'Current Pot' in response.data  # Check if the response contains the expected content

        # Make a POST request to the player_action route with invalid data (triggering an error)
        response_error = client.post('/player_action', data={'amount': '-5'})  # Negative amount should raise ValueError
        assert b'Invalid amount' in response_error.data  # Check if the response contains the error message

if __name__ == '__main__':
    pytest.main()

