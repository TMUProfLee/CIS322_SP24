from testing_base import *
#Nick Busman

def test_win_screen():
    nick = Player("Nick")
    logan = Player("Logan")
    win_player = ["nick", "logan"]
    Win_screen(win_player)
    assert Win_screen(win_player) == True