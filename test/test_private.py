from testing_base import *

def test_twoCards():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("Player 1")
    player2 = Player("Player 2")
    
    dealer.dealPrivateHand(player)
    dealer.dealPrivateHand(player2)
    
    assert len(player.hand) == 2, "Player 1 should get exactly 2 cards"
    assert len(player2.hand) == 2, "Player 2 should get exactly 2 cards"
    
def test_visibility():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("Player 1")
    player2 = Player("Player 2")
    
    dealer.dealPrivateHand(player)
    dealer.dealPrivateHand(player2)
    
    # none of the player's card should be shown. 
    assert not any(player.knownCards), "All cards in private hand should be private"
    assert not any(player2.knownCards)
    
def test_private_visible():
    deck = Deck()
    dealer = Dealer(deck)
    
    player = Player("Player 1")
    player2 = Player("Player 2")
    
    dealer.dealPrivateHand(player)
    dealer.dealPrivateHand(player2)
    
    for card in player.hand:
        assert card not in player2.hand #Player 2 should not see Player's cardss
    
    print(f"Player's private hand: ")
    player.showHand(printShort=True)
    print(f"Player 2's private hand: ")
    player2.showHand(printShort=True)
    
