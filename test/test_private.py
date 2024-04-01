from testing_base import *

def test_twoCards():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("Player 1")
    
    dealer.dealPrivateHand(player)
    
    assert len(player.hand) == 2, "Player should get exactly 2 cards"
    
def test_visibility():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("Player 1")
    
    dealer.dealPrivateHand(player)
    
    # none of the player's card should be shown. 
    assert not any(player.knownCards), "All cards in private hand should be private"
    
