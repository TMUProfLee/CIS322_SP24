from flask import Flask, request, render_template
from CardGames import *

app = Flask(__name__)

player = Player("Gambler")
player.setHand([getCard("Spades", 2), getCard("Spades", 2), getCard("Hearts", 5), getCard("Clubs", 6), getCard("Diamonds", 7)], True)

pot = 100
game = Game(player, pot)

# Player page
@app.route('/', methods=['GET', 'POST'])
def page():
    return render_template('player_board.html') # Opens player page

# Call()
@app.route('/call', methods=['GET', 'POST'])
def call_click():
    return game.player_action(0, "call") # Player calls

# Raise()
@app.route('/raise', methods=['GET', 'POST'])
def raise_click():
    return game.player_action(0, "raise") # Player raises

# Fold()
@app.route('/fold', methods=['GET', 'POST'])
def fold_click():
    return game.player_action(0, "fold") # Player folds

# Proof of running
if __name__ == '__main__':
    print("Player page template is up and running.")
    print("Player Hand:")
    player.showHand(True)
    app.run(debug=True)