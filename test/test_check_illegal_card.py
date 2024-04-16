from testing_base import GameSetup, getCard
game = GameSetup()

#Cards are valid:
def test_valid_cards():
    game.fugitive_deck = game.starting_cards
    game.fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    game.fugitive_deck.append(card5)
    game.fugitive_deck.append(card7)
    game.fugitive_deck.append(card8)

    #hideouts = ["1", "3"]
    print(game.check_illegal_card() == True)

#Hideout gap is greater than 3
def test_gap_too_big():
    game.fugitive_deck = game.starting_cards
    game.fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    game.fugitive_deck.append(card5)
    game.fugitive_deck.append(card7)
    game.fugitive_deck.append(card8)

    #hideouts = ["1", "5"]
    print(game.check_illegal_card() == False)

#Attempt to play a card that they do not have
def test_dont_have_card():
    game.fugitive_deck = game.starting_cards
    game.fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    game.fugitive_deck.append(card5)
    game.fugitive_deck.append(card7)
    game.fugitive_deck.append(card8)

    #hideouts = ["1", "6"]
    print(game.check_illegal_card() == False)

#Attempt to play the same hideout twice
def test_same_card():
    game.fugitive_deck = game.starting_cards
    game.fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    game.fugitive_deck.append(card5)
    game.fugitive_deck.append(card7)
    game.fugitive_deck.append(card8)

    #hideouts = ["1", "1"]
    print(game.check_illegal_card() == False)

#place one hideout 
def test_one_card():
    game.fugitive_deck = game.starting_cards
    game.fugitive_deck.append(game.escape_card)

    card5 = getCard(5, 1)
    card7 = getCard(7, 1)
    card8 = getCard(8, 2)

    game.fugitive_deck.append(card5)
    game.fugitive_deck.append(card7)
    game.fugitive_deck.append(card8)

    #hideouts = ["2"]
    print(game.check_illegal_card() == True)

test_valid_cards()
test_gap_too_big()
test_dont_have_card()
test_same_card()
test_one_card()

