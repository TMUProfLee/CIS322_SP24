from testing_base import *

def test01_three_of_kind():
        # Test expected value of successful Three of Kind:
    rank1_01 = getCard("Hearts", 3)
    rank1_02 = getCard("Spades", 3)
    rank1_03 = getCard("Diamonds", 3)
    rank2_01 = getCard("Hearts", 8)
    rank3_01 = getCard("Clubs", 5)

    hand01 = [ rank1_01, rank1_02, rank1_03, rank2_01, rank3_01 ]

    ID_test = Identification(hand01)

    test_result = ID_test.three_of_kind() 
    print(test_result)
    
    assert ID_test.hand == hand01
    assert ID_test.name == "Three of a Kind"
    assert ID_test.name in test_result
    assert type(test_result) is str
    assert test_result == "Hand is Three of a Kind!"
    

def test02_three_of_kind():
        # Test hand with different values for each card:
    rank1 = getCard("Hearts", 4)
    rank2 = getCard("Spades", 2)
    rank3 = getCard("Diamonds", 1)
    rank4 = getCard("Clubs", 7)
    rank5 = getCard("Clubs", 3)

    hand02 = [ rank1, rank2, rank3, rank4, rank5 ]

    ID_test = Identification(hand02)

    test_result02 = ID_test.three_of_kind() 

    assert ID_test.hand == hand02
    assert ID_test.name == ""
    assert isinstance(test_result02, type(None))
    assert test_result02 is None
    

def test03_three_of_kind():
        # Test hand with same values for each card:
    rank6_01 = getCard("Diamonds", 4)
    rank6_02 = getCard("Spades", 4)
    rank6_03 = getCard("Hearts", 4)
    rank6_04 = getCard("Spades", 4)
    rank6_05 = getCard("Clubs", 4)

    hand03 = [ rank6_01, rank6_02, rank6_03, rank6_04, rank6_05 ]

    ID_test = Identification(hand03)

    test_result03 = ID_test.three_of_kind() 

    assert ID_test.hand == hand03
    assert ID_test.name == ""
    assert isinstance(test_result03, type(None))
    assert test_result03 is None


test01_three_of_kind()
test02_three_of_kind()
test03_three_of_kind()