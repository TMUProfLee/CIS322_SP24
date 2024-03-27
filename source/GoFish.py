import random
import os
import textwrap
import time
#from CardGames import Player, Dealer, Deck, find_root_dir, getCard, DisplayPlayerInfo, TextFormat
from CardGamesSprint2 import StartScreen
from CardGames import *

class GoFish:
    def __init__(self):
        print("building Game")

        #DECK Generation
        gameDeck = Deck()
        print('deck built')
        gameDeck.shuffle()
        print("deck shuffled")

        #Players + CPU Generation
        playerName = input("What do you want your name to be?: " )
        realPlayer = Player(name=playerName)
        print("Welcome to Go Fish ", playerName)

        "possible future implementation"
        '''numPlayer = int(input("how many computer players do you want: "))
        Plist = []
        for i in range(numPlayer):
            playerNumb = str(i)
            playerName = ("player" + playerNumb)
            Plist.append(Player(name=playerName))'''
        
        CPU1 = Player(name="Cpu1")
        CPU2 = Player(name="Cpu2")    
        CPU3 = Player(name="Cpu3")
        print('players accepted')

        playList = [realPlayer, CPU1, CPU2, CPU3]

        dealer = Dealer(gameDeck)
        for i in range(0,4):
            dealer.dealCards(1, playList)
        
        CPU2.showHand()

        #put code for 
        #   - getting the player information
        #        - use player class
        #   - set the deck up
        #        - use deck class
        #   - turn tracker
        #        - needs to be created
        #   - keep track of cards

    def start_game(self):
        print('Begining Game')
        time.sleep(10)
        while True:
            print(Players)
            #if player.deck = []
        #   - This is where were gonna have the game 
        #   - logic go 


#Main function will handle only the starting of the program. 
def main():
    StartGame = StartScreen()
    #playerName = input("What do you want your name to be?: " )
    formattedAnswer = StartGame.upper()
    if formattedAnswer == 'YES':
        game = GoFish()
        game.start_game()
    else:
        print('sorry you feel that way')

if __name__ == "__main__":
    main()


        