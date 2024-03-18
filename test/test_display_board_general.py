import sys
sys.path.append("../")

from source.CardGames import *



class GameSetup:
    def __init__(self):
        #Initialize the objects that need to be initialized
        self.cards_in_play = []
        
    def display(self):
        display_board_general(self.cards_in_play)

def test_display():
    start = GameSetup()
    deck = Deck()
    deck.shuffle()
    # One unrevealed card
    start.cards_in_play.append(deck.getCard())
    assert(start.display() == None)
    # One revealed card
    start.cards_in_play[0].revealed = True
    assert(start.display() == None)
    # One revealed and one unrevealed
    start.cards_in_play.append(deck.getCard())
    assert(start.display() == None)
    # Two revealed
    start.cards_in_play[1].revealed = True
    assert(start.display() == None)
    # Two revealed and one unrevealed with two sprints card under
    start.cards_in_play.append([deck.getCard(), deck.getCard(), deck.getCard()])
    assert(start.display() == None)
    # Two revealed and one unrevealed with 3 sprint cards under
    start.cards_in_play[2].append(deck.getCard())
    assert(start.display() == None)
    # Two revealed cards and two unrevealed cards 
    # one with 2 sprint cards under and one with one sprint card
    start.cards_in_play.append([deck.getCard(), deck.getCard(), deck.getCard()])
    assert(start.display() == None)
    # Two revealed cards and two unrevealed cards 
    # each with 2 sprint cards under
    start.cards_in_play[3].append(deck.getCard())
    assert(start.display() == None)

test_display()