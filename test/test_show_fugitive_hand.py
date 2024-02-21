from testing_base import *
fugitive = Player('Fugitive')
# Waiting for card images to be updated
one = getCard(1, 1)
two = getCard(2, 2)
three = getCard(3, 1)
four = getCard(4, 2)
five = getCard(5, 1)
cards = [one, two, three, four, five]
    
fugitive.setHand(cards, isKnown=True)

def test_show_hand():
    assert(fugitive.showHand() == None)
test_show_hand()




