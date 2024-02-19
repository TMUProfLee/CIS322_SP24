from testing_base import *
# Sophia Nicolas
# Unit test for multiple player hand display.

def test_MHD():
        # Initialize deck:
    deck = Deck()
    dealer = Dealer(deck)
    players = {}

        # Initialize game players:
    all_names = []
    num_players = int(input("Enter number of players: "))
    num_cards = int(input("Enter number of cards per hand: "))
    
    for n in range(1, num_players+1):
        all_names.append(input(f"Player {n} name: "))
    players = {name: Player(name) for name in all_names}

        # Deal player hands:
    dealer.dealCards(num_cards, players.values())

        # Test output of the multi-hand display:
    assert type(displayHands(players, all_names)) is dict

# Perform test:
test_MHD()