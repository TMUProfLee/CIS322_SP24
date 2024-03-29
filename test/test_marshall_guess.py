import sys
sys.path.append("../")

from source.CardGames import *
game = GameSetup()

def test_guess_locations():
    # Relies on input, so loops through possible input
    # 1. Bad input == reprompt user
    # 2. Wrong single input == no cards revealed
    # 3. Right single input == first card revealed
    # 4. Wrong multiple input == no cards revealed
    # 5. Right multiple input == all cards revealed
    game.cards_in_play = [game.LowRangeDeck[0], game.LowRangeDeck[1]]
    print(game.cards_in_play[0].value, game.cards_in_play[1].value)
    for _ in range(5):
        game.cards_in_play[0].revealed = False # Rehide cards
        game.cards_in_play[1].revealed = False
        assert(game.marshall_guess() == None)


test_guess_locations()
