import sys
sys.path.append("../")

from source.CardGames import *

def test_first_turn():
    setup = GameSetup()
    setup.marshall_first_turn()
    
test_first_turn()