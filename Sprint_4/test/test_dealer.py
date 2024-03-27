from testing_base import *

def test_start_onecard():
    deck = Deck()
    dealer = Dealer(deck)
    print(f"Dealer's default hand: {len(dealer.hand)}")
    assert len(dealer.hand) == 1, "Dealer starts with one card in hand"

# explicitly adding 1 card
def test_add_singlecard():
    deck = Deck()
    dealer = Dealer(deck)
    dealer.addCardsToDealer(1)
    print(f"Dealer's hand after adding 1: {len(dealer.hand)}")
    assert len(dealer.hand) == 2, "Dealer should have 2 cards in hand"

def test_add_multiplecards():
    deck = Deck()
    dealer = Dealer(deck)
    dealer.addCardsToDealer(4)
    print(f"Dealer's default hand after adding 4: {len(dealer.hand)}")
    assert len(dealer.hand) == 5, "Dealer should have 5 cards after adding"
    
# if dealer is able to reach full capacity of the rest of the deck after taking 1 card. 
def test_handcapacity():
    deck = Deck()
    dealer = Dealer(deck)
    dealer.addCardsToDealer(51) # since dealer already used 1 card 
    print(f"Dealer's hand at full capacity: {len(dealer.hand)}")
    assert len(dealer.hand) == 52, "Dealer's hand should have equivalence of full deck."
    
# testing that there is no duplicate
def test_unique():
    deck = Deck()
    dealer = Dealer(deck)
    
    # Add all cards in the deck to the dealer's hand
    while len(deck.cards) > 0:
        dealer.addCardsToDealer(1)
    
    # create unique cards from dealer's hand by using set()
    unique_cards = set()
    for card in dealer.hand:
        card_str = str(card)
        unique_cards.add(card_str)
        
    print(f"Length of Unique cards: {len(unique_cards)} and Length of Dealer's hand: {len(dealer.hand)}")
    
    # unique cards should have same length as the dealer's hand if all cards are unique
    assert len(unique_cards) == len(dealer.hand), "All cards in the dealer's hand are unique."
