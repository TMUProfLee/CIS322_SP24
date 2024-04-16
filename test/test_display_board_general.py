import sys
sys.path.append("../")

from source import CardGames

def test_display_board_general():
    start = CardGames.GameSetup()
    # One unrevealed card
    start.cards_in_play.append(start.LowRangeDeck.pop())
    assert(start.display_board_general() == None)
    # One revealed card
    start.cards_in_play[0].revealed = True
    assert(start.display_board_general() == None)
    # One revealed and one unrevealed
    start.cards_in_play.append(start.LowRangeDeck.pop())
    assert(start.display_board_general() == None)
    # Two revealed
    start.cards_in_play[1].revealed = True
    assert(start.display_board_general() == None)
    # Two revealed and one unrevealed with two sprints card under
    start.cards_in_play.append([start.LowRangeDeck.pop(), start.LowRangeDeck.pop(), start.LowRangeDeck.pop()])
    assert(start.display_board_general() == None)
    # Two revealed and one unrevealed with 3 sprint cards under
    start.cards_in_play[2].append(start.LowRangeDeck.pop())
    assert(start.display_board_general() == None)
    # Two revealed cards and two unrevealed cards 
    # one with 2 sprint cards under and one with one sprint card
    start.cards_in_play.append([start.LowRangeDeck.pop(), start.LowRangeDeck.pop(), start.LowRangeDeck.pop()])
    assert(start.display_board_general() == None)
    # Two revealed cards and two unrevealed cards 
    # each with 2 sprint cards under
    start.cards_in_play[3].append(start.LowRangeDeck.pop())
    assert(start.display_board_general() == None)

    ## Test for fugitive
    assert(start.display_board_general('fugitive') == None)

test_display_board_general()    