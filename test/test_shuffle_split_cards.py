from testing_base import *

def test_highdeck_shuffle():
    #Setup for HighRangeDeck 
    game_deck=Deck()
    #Get card 42
    escape_card = game_deck.getCard()
    #Get cards 41 - 29
    HighRangeDeck = []
    for card in range(13):
        test_card = game_deck.getCard()
        HighRangeDeck.append(test_card)
    #DO NOT SHUFFLE 
        
      #Get cards 28 - 15
    MidRangeDeck = []
    for card in range(14):
        test_card = game_deck.getCard()
        MidRangeDeck.append(test_card)
    #Do Not SHUFFLE
        
      #Get cards 14 - 4
    LowRangeDeck = []
    for card in range(11):
        test_card = game_deck.getCard()
        LowRangeDeck.append(test_card)
    #DO NOT SHUFFLE

    #Grab actual shuffled decks 
    tuplee = split_card()
    highestCardDeck = tuplee[1]
    midCardDeck = tuplee[2]
    lowCardDeck = tuplee[3]


    #If function shuffled the deck, they should not be equal
    assert(HighRangeDeck == highestCardDeck) == False
    assert(MidRangeDeck == midCardDeck) == False
    assert(LowRangeDeck == lowCardDeck) == False

def test_true_shuffle():
    #Run function and get one version of HighDeck
    tuplee = split_card()
    highestCardDeck = tuplee[1]

    #Run function again and get a second version of Highdeck
    tuplee2 = split_card()
    highestCardDeck2 = tuplee2[1]

    #If it trully shuffles, no two versions should be the same
    assert(highestCardDeck == highestCardDeck2) == False