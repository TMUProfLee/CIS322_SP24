from flask import Flask, request, render_template
from CardGames import *

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Create instances of game components
deck = Deck()
dealer = Dealer(deck)
players = []  # Add more players as needed
game = Poker(players, dealer, Pot())

current_turn = game.currentPlayer

def check_player_turn(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        player_id = session.get('player_id')
        if player_id != str(players[game.currentPlayer].id):
            flash('It is not your turn')
            return redirect(url_for('gameRoute'))
        return f(*args, **kwargs)
    return decorated_function

# Define a route to handle form submission
@app.route('/game', methods=['POST', 'GET'])
def gameRoute():
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
            game.add_player(new_player)

            # Generate a unique identifier for this player
            session['player_id'] = new_player.id

            # DEBUG
            print('Player ID:', session['player_id'])
        else:
            return render_template('create_player.html')

    # Return a response to the HTML page
    return render_template('game.html', players=players, pot=game.pot.show_pot(), current_turn=game.players[game.currentPlayer].name, current_bet=max(game.bets), community_cards=game.dealer.hand, round=game.round, player=game.players[game.currentPlayer], player_cards=game.players[game.currentPlayer].hand)

# Define a route to handle player actions in the game loop
@app.route('/bet', methods=['POST'])
@check_player_turn
def bet():
    # Perform the player action in the game
    Call(player, amount, pot)
    # Return a response to the HTML page
    return render_template('result.html', players=players, pot=pot.show_pot())

if __name__ == '__main__':
    app.run(debug=True)