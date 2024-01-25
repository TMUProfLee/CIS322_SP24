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
    expected_output = "\nname: \"%s\"\nmoney: %d\nThe Player has no cards in their hand." % (name, money)
    assert output == expected_output


"""
A test for if the player has cards in their hand and the cards are known.
"""
def test_Player_CardsShown():
    # Setup
    name = "Player 1"
    money = random.randint(0, 1000000000)
    player = Player(name, money)
    player.addCard(getCard("spades", 5), isKnown=True)
    player.addCard(getCard("spades", 4), isKnown=True)
    player.addCard(getCard("spades", 3), isKnown=True)
    player.addCard(getCard("spades", 2), isKnown=True)
    player.addCard(getCard("spades", 1), isKnown=True)

    # Testing
    output = player.display(returnOutput=True)
    expected_output = "\nname: \"%s\"\nmoney: %d\n" % (name, money)
    assert output.startswith(expected_output)
    # Requires manual inspection

"""
A test for if the player has cards in their hand and the cards are not known.
"""

def test_Player_CardsNotShown():
    # Setup
    name = "Player 1"
    money = random.randint(0, 1000000000)
    player = Player(name, money)
    player.addCard(getCard("spades", 5), isKnown=False)
    player.addCard(getCard("spades", 4), isKnown=False)
    player.addCard(getCard("spades", 3), isKnown=False)
    player.addCard(getCard("spades", 2), isKnown=False)
    player.addCard(getCard("spades", 1), isKnown=False)

    # Testing
    output = player.display(returnOutput=True)
    expected_output = "\nname: \"%s\"\nmoney: %d\n" % (name, money)
    assert output.startswith(expected_output)
    # Requires manual inspection