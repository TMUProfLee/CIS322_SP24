import sys
sys.path.append("../")

from source.CardGames import *

def test_first_turn():
    setup = GameSetup()
    setup.cards_in_play.append(setup.LowRangeDeck.pop())
    setup.cards_in_play.append(setup.LowRangeDeck.pop())
    setup.marshall_first_turn()
    
assert(test_first_turn() == None)