from testing_base import *

# if hand has two pairs.
def test_TwoPair():
    hand = [Card('Hearts', 2, None, None), Card('Diamonds', 2, None, None), Card('Hearts', 4, None, None), Card('Spades',4, None, None), Card('Diamonds',5, None, None)]
    identification = Identification()
    identification.hand = hand
    result = identification.twoPair()
    
    # create expected result which will form two pair
    expected_values = sorted(card.value for card in result)
    expect = [2,2,4,4]
    
    # compare expected results with the actual result
    assert len(result) == 4 and expected_values == expect, "Failed to identify two pairs correctly"
    
# if hand has one pair.  
def test_OnePair():
    hand = [Card('Hearts',1,None, None), Card('Diamonds',1, None, None), Card('Hearts',2, None, None), Card('Spades',7, None, None), Card('Diamonds',13, None, None)]
    identification = Identification()
    identification.hand = hand
    result = identification.twoPair()
    assert len(result) == 0, "Failed, incorrectly identified one pair as two pairs."

# if hand has no pair. 
def test_NoPair():
    hand = [Card('Hearts',2, None, None), Card('Diamonds',6, None, None), Card('Hearts',3, None, None), Card('Spades',7, None, None), Card('Diamonds',13, None, None)]
    identification = Identification()
    identification.hand = hand
    result = identification.twoPair()
    assert len(result) == 0, "Failed, incorrectly identified no pairs."
    
# if hand has three of a kind, then failed to identify two pairs
def test_ThreeKind():
    hand = [Card('Hearts',2, None, None), Card('Diamonds',2, None, None), Card('Hearts',2, None, None), Card('Spades',7, None, None), Card('Diamonds',13, None, None)]
    identification = Identification()
    identification.hand = hand
    result = identification.twoPair()
    assert len(result) == 0, "Failed, incorrectly identified a three of a kind as having two pairs."