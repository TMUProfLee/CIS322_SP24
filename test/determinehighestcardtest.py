from source.cardfunctions import highest_card  # Replace 'your_module' with the name of your module

def test_highest_card_regular():
    assert highest_card(['4S', '5H', 'KD', '9C', '10S']) == 13  # KD is the highest

def test_highest_card_with_ace():
    assert highest_card(['4S', 'AH', 'KD', '9C', '10S']) == 14  # AH is the highest

def test_highest_card_all_same_rank():
    assert highest_card(['4S', '4H', '4D', '4C', '4S']) == 4   # All cards are 4
