from flask import Flask, request, render_template
from CardGames import *

app = Flask(__name__)

# Game contents not included and game.fold() commented out due to the Game class fold() method being currently empty in CardGames.py

@app.route('/', methods=['GET', 'POST'])
def fold_button():
    # if button clicked:
        # game.fold()
    return render_template('fold.html') # Opens a page with button

if __name__ == '__main__':
    print("Player folds.") # Proof of running
    app.run(debug=True)