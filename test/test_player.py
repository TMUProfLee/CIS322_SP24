from testing_base import *
import random

"""
Expected output:
name: "Player 1"
money: 100
The Player has no cards in their hand.
"""
def test_Player():
    # Setup
    name = "Player 1"
    money = random.randint(0, 1000000000)
    player = Player(name, money)

    # Testing
    assert player.name == name
    assert player.money == money
    assert player.hand == []

    output = player.display(returnOutput=True)
    expected_output = "name: \"%s\"\nmoney: %d\nThe Player has no cards in their hand." % (name, money)
    assert output == expected_output


