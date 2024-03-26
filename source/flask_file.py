from flask import Flask, request, render_template
from CardGames import *

app = Flask(__name__)

# Create instances of game components
deck = Deck()
dealer = Dealer(deck)
players = []  # Add more players as needed
game = Poker(players, dealer)
pot = Pot()
# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Starting from index

# Define a route to handle form submission
@app.route('/process_form', methods=['POST'])
def process_form():
    # Get the input data from the form
    input_name = request.form['input_name']
    input_money = int(request.form['input_money'])

    # Create a new player and add them to the game
    new_player = Player(input_name, input_money)
    players.append(new_player)

    # Return a response to the HTML page
    return render_template('game.html', players=players)

# Define a route to handle player actions in the game loop
@app.route('/player_action', methods=['POST'])
def player_action():
    amount = int(request.form['amount'])
    player = players.copy()[game.currentPlayer]
    # Perform the player action in the game

    bet_result = Call(player, amount, pot)
    if isinstance(bet_result, str):
        error_message = bet_result  # Store the error message
    else:
        error_message = None  # No error message

    return render_template('game.html', players=players, pot=pot.show_pot(), error=error_message)

if __name__ == '__main__':
    app.run(debug=True)