from source.CardGames import *

marshall = Player("Marshall")
deck = Deck()

def marshall_first_turn():
    # Waiting for deck to be divided into three groups
    input("Select which deck to draw two cards from ['1' (1-14), '2' (15-28), '3' (29-42)] and press enter...")

    for i in range(2):
        draw_card = deck.getCard()
        marshall.addCard(draw_card, isKnown=True)

    marshall.showHand()

    #Display board
    
    while(True):
        guess_all = input("Would you like to guess all fugitive locations? (y/n)").lower()
        if guess_all == 'y' or guess_all == 'yes':
            while(True):
                guess = input("Enter locations separated only by a comma (1,2,3...)").split(',')
                """
                if len_list < placed_locations:
                    print("Must guess all locations")
                    guess = input("Enter locations separated only by a comma (1,2,3...)").split(',')
                    continue
                """
                # Check that input is a valid list of ints
                bad = False
                for ele in guess:
                    try:
                        ele = int(ele)
                    except:
                        TypeError
                        print("Invalid input, try again")
                        bad = True
                        break
                if bad:
                    continue
                break
            break
        elif guess_all == 'n' or guess_all == 'no':
            while True:
                try:
                    guess = int(input("Enter futitive location..."))
                except:
                    ValueError
                    print("Invalid input, try again")
                    continue
                break
            break
        else:
            print("Invalid input, try again")

    #marshall.add_guess(guess)
    print("Guesses added")
    """
    if check_location(marshall_current_idx, guess):
        print("Correct location!")
        reveal_location(marshall_current_idx)
    else:
        print("Incorrect guess.")
    """
