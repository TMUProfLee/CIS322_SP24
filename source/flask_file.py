from flask import Flask, request, render_template, session, redirect, flash
from CardGames import Deck, Dealer, Player, Poker, Pot

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Create instances of game components
deck = Deck()
dealer = Dealer(deck)
players = []  # Add more players as needed
game = Poker(players, dealer, Pot())

current_turn = game.currentPlayer


# Define a route to handle form submission
@app.route('/process_form', methods=['POST', 'GET'])
def process_form():
    # Check if player_id is already set
    if 'player_id' in session:
        # Assign it to the corresponding player
        player_id = session['player_id']
        found = False
        for player in players:
            if str(player.id) == player_id:
                found = True
                break
        if not found:
            session.pop('player_id', None)
            return render_template('create_player.html')
        print('Player ID:', session['player_id'])
    else:
        # Get the input data from the form
        if request.method == 'POST':
            input_name = request.form['input_name']
            input_money = int(request.form['input_money'])

            # Create a new player and add them to the game
            new_player = Player(input_name, input_money)
            players.append(new_player)

            # Generate a unique identifier for this player
            session['player_id'] = new_player.id

            # DEBUG
            print('Player ID:', session['player_id'])
        else:
            return render_template('create_player.html')

    # Return a response to the HTML page
    return render_template('game.html', players=players, pot=game.pot.show_pot())

# Define a route to handle player actions in the game loop
@app.route('/player_action', methods=['POST'])
def player_action():
    # Check if the player's identifier matches the current player
    player_id = session.get('player_id')
    if player_id != str(players[game.currentPlayer].id):
        flash('It is not your turn')
        return redirect('/process_form')

    # Perform the player action in the game
    amount = int(request.form['amount'])
    player = players[game.currentPlayer]
    game.bet(player, amount, game.pot)


    # Return a response to the HTML page
    return render_template('result.html', players=players, pot=game.pot.show_pot())


@app.route('/', methods=['GET', 'POST'])
def main():
    return redirect('/process_form')
if __name__ == '__main__':
    app.run(debug=True)