from testing_base import *
# Sophia Nicolas
# Unit test for Poker class functions.

def test_Poker():
    # Initialize deck:
    deck = Deck()
    dealer = Dealer(deck)
    
    # Initialize players:
    players = [Player("Player 1"), Player("Player 2"), Player("Player 3")]
    
    # Initialize Poker game:
    poker = Poker(players, dealer)
    
    # Test addMoneyToPot() function:
    assert poker.addMoneyToPot(100) == 100
    
    # Test addBet() function:
    assert poker.addBet(players[0], 50) == 50
    
    # Test collectBets() function:
    poker.collectBets()
    assert poker.pot == 50
    
    # Test checkBets() function:
    assert poker.checkBets() == True
    
    # Test callAmount() function:
    assert poker.callAmount(players[1]) == 0

# Perform test:
test_Poker()