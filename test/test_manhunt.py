from testing_base import *

root_dir = os.path.join( find_root_dir(), 'source')
cards_file = f'{root_dir}{os.path.sep}new_playing_cards.txt'
with open(cards_file, "r") as cards:
    cardBack = []
    for _ in range(6):
        line = cards.readline()
        cardBack.append(line.replace("\n",""))

game = GameSetup()
game.cards_in_play = [Card(1, 3, cardImages[2], cardBack), Card(2, 6, cardImages[5], cardBack), Card(1, 25, cardImages[24], cardBack), Card(1, 39, cardImages[38], cardBack), Card(2, 42, cardImages[41], cardBack)]
game.manhunt = True
while True:
    win = game.marshall_guess()
    if win == None:
        continue
    elif win:
        os.system('cls')
        time.sleep(4)
        print("\nCorrect guess!")
        time.sleep(1)
        print("\n**" + game.fugitive.name + " has been caught!**")
        break
    else:
        os.system('cls')
        time.sleep(4)
        print("\nIncorrect guess")
        time.sleep(1)
        print("\n**" + game.fugitive.name + " got away!**")
        break         