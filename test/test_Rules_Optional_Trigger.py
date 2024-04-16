import sys
sys.path.append("../")

from source.CardGames import GameSetup

def test_Rule_Optional_Trigger():
    game = GameSetup()
    game.ReadRules()

test_Rule_Optional_Trigger()
