from mac_import import *
# Sophia Nicolas
# Unit test for Poker class functions.

def test_Poker():
    # Initialize deck:
    deck = Deck()
    dealer = Dealer(deck)
    
    # Initialize players:
    players = [Player("Player 1"), Player("Player 2"), Player("Player 3")]

    # Initialize pot:
    pot = Pot()
    
    # Initialize Poker game:
    poker = Poker(players, dealer, pot)
    
    # Test addMoneyToPot() function:
    assert str(poker.addMoneyToPot(100)) == "The pot is currently 100."
    
    # Test addBet() function:
    assert poker.addBet(players[0], 50) == 50
    
    # Test collectBets() function:
    poker.collectBets()
    assert str(poker.pot) == "The pot is currently 150."
    
    # Test checkBets() function:
    assert poker.checkBets() == True
    
    # Test callAmount() function:
    assert poker.callAmount(players[1]) == 0

# Perform test:
test_Poker()