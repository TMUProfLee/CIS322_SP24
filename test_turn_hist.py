from testing_base import *

    # Testing values of player turn tracker output with extended display.
def test_1():
        # Test players.
    testp1 = Player("Sully")
    testp2 = Player("Wazowski")
    testp3 = Player("Boggs")
    test_players = [testp1, testp2, testp3]

    func_test = turn_hist(test_players)

    print("\n* ------ RUNNING TEST ONE: ----- *")
        # Display test:
    for i in range(1, 5): # 4 Betting rounds.
        print(f"\nBetting Round {i} begins.\n")
        for j in func_test:
            if j.lower() == f"current player: boo\nboo raises/calls/folds.\n":
                return print("This player is under 21. Please remove player and start a new game.")
            else:
                print(j)
        print(f"Betting Round {i} complete.\n\n")

    expected_1 = f"Current player: {testp1.name}\n{testp1.name} raises/calls/folds.\n"
    expected_2 = f"Current player: {testp2.name}\n{testp2.name} raises/calls/folds.\n"
    expected_3 = f"Current player: {testp3.name}\n{testp3.name} raises/calls/folds.\n"
    
        # Assertions for player turn history:
    assert func_test[0] == expected_1
    assert func_test[1] == expected_2
    assert func_test[2] == expected_3


    # Testing if player names are in function output.
def test_2():
        # Test players and output.
    test_players = [Player("Wazowski"), Player("Boggs"), Player("Sully")]
    test_output = turn_hist(test_players)

    print("\n* ------ RUNNING TEST TWO: ----- *")
        # Test player turn display.
    for player in test_players:
        if (player.name).lower() == f"current player: boo\nboo raises/calls/folds.\n":
            return print("This player is under 21. Please remove player and start a new game.")
        else:
            print(test_output[test_players.index(player)])
        # assert player.name in test_output[test_players.index(player)]
        
        # Assertions on test display, readable equivalent of previous comment above.
    assert test_players[0].name in test_output[0]
    assert test_players[1].name in test_output[1]
    assert test_players[2].name in test_output[2]


    # Testing that a list of strings is returned.
def test_3():
    test_players = [Player("Boggs"), Player("Sully"), Player("Wazowski")]
    test_output = turn_hist(test_players)

    print("\n* ------ RUNNING TEST THREE: ----- *")

    for player in test_players:
        if (player.name).lower() == f"current player: boo\nboo raises/calls/folds.\n":
            return print("This player is under 21. Please remove player and start a new game.")
        else:
            print(test_output[test_players.index(player)])

    assert type(test_output) is list
    assert type(test_output[0]) is str
    assert type(test_output[1]) is str
    assert type(test_output[2]) is str

test_1()
test_2()
test_3()