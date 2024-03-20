from CardGames_test import *
# Sophia Nicolas
# Display for multiple player hands

def displayHands(player_dict, full_name_list):
    show_names = []
    get_name = True

        # Request hands to display:
    while get_name == True:
        gather_name = input("Enter player hand to show: ")
        if gather_name == "":
            get_name = False
        elif gather_name.lower() == "all":
            show_names = full_name_list.copy()
            get_name = False
        else:
            show_names.append(gather_name)
    
        # Output specified hand display:
    print("Player hands displayed below.\n")
    allhand_display = {}

    for player in player_dict.values():
        if player.name in show_names:
            print(f'{player.name}:')
            allhand_display[player.name] = player.showHand(True)
            print()
    
    return allhand_display # More of a side-effect dictionary.