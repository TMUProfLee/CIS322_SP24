from flask import Flask, request, render_template, session, redirect, flash, url_for
from CardGames import Deck, Dealer, Player, Poker, Pot
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Create instances of game components
deck = Deck()
dealer = Dealer(deck)
players = []  # Add more players as needed
game = Poker(players, dealer, Pot())

current_turn = game.currentPlayer

@app.route('/reset')
def reset_game():
    global deck, dealer, players, game, current_turn
    deck = Deck()
    dealer = Dealer(deck)
    players = []
    game = Poker(players, dealer, Pot())
    current_turn = game.currentPlayer

    return redirect(url_for('gameRoute'))

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
    request_player = None
    if 'player_id' in session:
        # Assign it to the corresponding player
        player_id = session['player_id']
        found = False
        for player in players:
            if str(player.id) == player_id:
                found = True
                request_player = player
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

            request_player = new_player
            # DEBUG
            print('Player ID:', session['player_id'])
        else:
            return render_template('create_player.html')
    print(game.bets)
    # Lookup the player by their session ID
    
    
    # Return a response to the HTML page
    return render_template('game.html', players=players, pot=game.pot.show_pot(), current_turn=game.players[game.currentPlayer].name, current_bet=max(game.bets), community_cards=game.dealer.hand, round=game.round, player=game.players[game.currentPlayer], player_cards=request_player.hand)

# Define a route to handle player actions in the game loop
@app.route('/bet', methods=['POST'])
@check_player_turn
def bet():
    # Perform the player action in the game
    amount = int(request.form['amount'])
    player = game.players[game.currentPlayer]
    # Remove the bet amount from the player's money
    player.makeBet(amount)
    # Add the bet amount to the bets list
    game.addBet(player=player, amount=amount)
    round_check()


    # Return a response to the HTML page
    return redirect(url_for('gameRoute'))

@app.route('/call', methods=['POST'])
@check_player_turn
def Call():
    player = game.players[game.currentPlayer]
    
    amount = max(game.bets) - game.bets[game.currentPlayer]
    player.makeBet(amount)
    # Add the bet amount to the bets list
    game.addBet(player=player, amount=amount)
    round_check()
    return redirect(url_for('gameRoute'))

def round_check():
    if game.checkBets():
        game.collectBets()
        game.round += 1
        if game.round == 3:
            winner = game.end_game()
            # Flash the winner
            flash('The winner is ' + winner.name)
            return redirect(url_for('gameRoute'))
        else:
            game.dealer.addCardsToDealer(1)
            game.next_turn()
    else:
        game.next_turn()

@app.route('/', methods=['GET', 'POST'])
def main():
    return redirect(url_for('gameRoute'))
if __name__ == '__main__':
    app.run(debug=True)

