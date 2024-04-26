from flask import Flask, request, render_template
from source.CardGames import *

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
    action = request.form['action']
    amount = int(request.form['amount'])
    player_index = int(request.form.get('player_index', 0))
    player = players[player_index]

    if action == 'raise':
            response = Call(player, amount, pot)
            print(f"Action failed with error: {response}")
            if response:
                message = response  # Store the error message
            else:
                message = 'Raise successful'
                print(f"Action successful. New pot amount: {pot.show_pot()}")
    else:
        message = 'Action not supported'

    return render_template('game.html', players=players, pot=pot.show_pot(), message=message)
    
if __name__ == '__main__':
    app.run(debug=True)