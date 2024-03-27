import random
import os
import textwrap
import time
#from CardGames import Player, Dealer, Deck, find_root_dir, getCard, DisplayPlayerInfo, TextFormat
from CardGamesSprint2 import StartScreen
from CardGames import *

class GoFish:
    def __init__(self,Players):
        print("building Game")
        self.deck = Deck()
        print('deck built')
        #player1 = Player(name="player1")
        #player2 = Player(name="player2")
        self.deck.shuffle()
        print("deck shuffled")
        self.Players = Players
        print('players accepted')
        #put code for 
        #   - getting the player information
        #        - use player class
        #   - set the deck up
        #        - use deck class
        #   - turn tracker
        #        - needs to be created
        #   - keep track of cards

    def start_game(self):
        print('Begin Game')
        while True:
            print(Players)
            #if player.deck = []
        #   - This is where were gonna have the game 
        #   - logic go 


#Main function will handle only the starting of the program. 
def main():
    StartGame = StartScreen()
    formattedAnswer = StartGame.upper()
    if formattedAnswer == 'YES':
        numPlayer = int(input("how many players do you want: "))
        Plist = []
        for i in range(numPlayer):
            playerNumb = str(i)
            playerName = ("player" + playerNumb)
            Plist.append(Player(name=playerName))
        game = GoFish(Plist)
        game.start_game()
    else:
        print('sorry you feel that way')

if __name__ == "__main__":
    main()


        