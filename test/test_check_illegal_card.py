from testing_base import GameSetup, getCard
game = GameSetup()

#Cards are valid:
def test_valid_cards():
    fugitive_deck = game.starting_cards
    fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    fugitive_deck.append(card5)
    fugitive_deck.append(card7)
    fugitive_deck.append(card8)

    hideouts = ["1", "3"]
    assert game.check_illegal_card(fugitive_deck, hideouts) == True

#Hideout gap is greater than 3
def test_gap_too_big():
    fugitive_deck = game.starting_cards
    fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    fugitive_deck.append(card5)
    fugitive_deck.append(card7)
    fugitive_deck.append(card8)

    hideouts = ["1", "5"]
    assert game.check_illegal_card(fugitive_deck, hideouts) == False

#Attempt to play a card that they do not have
def test_dont_have_card():
    fugitive_deck = game.starting_cards
    fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    fugitive_deck.append(card5)
    fugitive_deck.append(card7)
    fugitive_deck.append(card8)

    hideouts = ["1", "6"]
    assert game.check_illegal_card(fugitive_deck, hideouts) == False

#Attempt to play the same hideout twice
def test_same_card():
    fugitive_deck = game.starting_cards
    fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    fugitive_deck.append(card5)
    fugitive_deck.append(card7)
    fugitive_deck.append(card8)

    hideouts = ["1", "1"]
    assert game.check_illegal_card(fugitive_deck, hideouts) == False

#place one hideout 
def test_one_card():
    fugitive_deck = game.starting_cards
    fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    fugitive_deck.append(card5)
    fugitive_deck.append(card7)
    fugitive_deck.append(card8)

    hideouts = ["2"]
    assert game.check_illegal_card(fugitive_deck, hideouts) == True
