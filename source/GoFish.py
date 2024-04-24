import random
import os
import textwrap
import time
import sys
#from CardGames import Player, Dealer, Deck, find_root_dir, getCard, DisplayPlayerInfo, TextFormat
from CardGamesSprint2 import StartScreen
from CardGames import *

def four_of_a_kind(list):
    counts = {}
    for item in list:
        counts[item] = counts.get(item, 0) + 1
    if counts[item] == 4:
        return True, item
    return False, None

def slow_print(text, delay=0):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class GoFish:
    def __init__(self):
        slow_print("building Game")

        #DECK Generation
        self.gameDeck = Deck()
        slow_print('deck built')
        self.gameDeck.shuffle()
        slow_print("deck shuffled")

        time.sleep(0)
        #Players + CPU Generation
        self.playerName = input("What do you want your name to be?: " )
        self.realPlayer = Player(name=self.playerName)

        time.sleep(0)
        print("Welcome to Go Fish ", self.playerName)

        "possible future implementation"
        '''numPlayer = int(input("how many computer players do you want: "))
        Plist = []
        for i in range(numPlayer):
            playerNumb = str(i)
            playerName = ("player" + playerNumb)
            Plist.append(Player(name=playerName))'''
        
        self.CPU1 = Player(name="Cpu1")
        self.CPU2 = Player(name="Cpu2")    
        self.CPU3 = Player(name="Cpu3")
        print('players accepted')

        self.playList = [self.realPlayer, self.CPU1, self.CPU2, self.CPU3]

        self.dealer = Dealer(self.gameDeck)
        for i in range(0,5):
            self.dealer.dealCards(1, self.playList)
        
        #self.CPU2.showHand()
        print("CPU1's hand")
        self.CPU1.showHand()
        print("CPU2's hand")
        self.CPU2.showHand()
        print("CPU3's hand")
        self.CPU3.showHand()
        #self.realPlayer.showHand()
        #put code for 
        #   - getting the player information
        #        - use player class
        #   - set the deck up
        #        - use deck class
        #   - turn tracker
        #        - needs to be created
        #   - keep track of cards
        self.playerTable = []
        self.cpu1Table = []
        self.cpu2Table = []
        self.cpu3Table = []

    def start_game(self):
        print('''
            ''')
        print('Begining Game')
        time.sleep(0)
        while True:
            if not self.gameDeck.cards and self.realPlayer.hand and self.CPU1.hand and self.CPU2.hand and self.CPU3.hand:
                print("Game Deck is empty")
                break
            print('''
            ''')
            print('YOUR CURRENT HAND')
            self.realPlayer.showHand()
            print('''
            ''')
            #----------------players turn starts------------
            slow_print('''It is your turn
            ''')
            CPUOptions = ["CPU1", "CPU2", "CPU3"]
            #self.pAnswer1 = input('''Which player will you ask for cards from? (Answer should be of the following: "CPU1" "CPU2 "CPU3") : ''')
            while True:
                self.pAnswer1 = input('''Which player will you ask for cards from? (Answer should be of the following: "CPU1" "CPU2 "CPU3") : ''')
                if self.pAnswer1 in CPUOptions:
                    break
                else:
                    print("invalid entry bruv")
            time.sleep(0)
            #self.pAnswer2 = input("what card would you like to ask for? (format:value, suit): ")
            realPlayerHand = []
            CPU1Hand = []
            CPU2Hand = []
            CPU3Hand = []
            for i, self.Card in enumerate (self.realPlayer.hand):
                realPlayerHand.append(self.Card.value)
            #for i, self.Card in enumerate (self.CPU1.hand):
                #CPU1Hand.append(self.Card.value)
            #for i, self.Card in enumerate (self.CPU2.hand):
                #CPU2Hand.append(self.Card.value)
            #for i, self.Card in enumerate (self.CPU3.hand):
                #CPU3Hand.append(self.Card.value)
            while True:
                self.pAnswer3 = int(input("what number would you like to ask for? (format:number): "))
                if self.pAnswer3 in realPlayerHand:
                    break
                else:
                    print("invalid entry bruv")

            if self.pAnswer1 == "CPU1":
                print("asking CPU1 for ", self.pAnswer3)
                Value1 = False
                for i, self.Card in enumerate (self.CPU1.hand):
                    print("a check")
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.pAnswer3:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU1.hand.pop(i)
                        self.realPlayer.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.realPlayer]
                    self.dealer.dealCards(1, xList)
                    self.realPlayer.showHand()
                    #print("You playin with the deck")
                    #self.realPlayer.showHand()
            elif self.pAnswer1 == "CPU2":
                print("asking CPU2 for ", self.pAnswer3)
                Value1 = False
                for i, self.Card in enumerate (self.CPU2.hand):
                    
                    #tempTestCard = str(self.Card.value) + " " + self.Card.suit
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.pAnswer3:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU2.hand.pop(i)
                        self.realPlayer.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.realPlayer]
                    self.dealer.dealCards(1, xList)
                    #print("You playin with the deck")
                    self.realPlayer.showHand()
                    #self.realPlayer.showHand()
                print("asking CPU2 for ", self.pAnswer3)
            elif self.pAnswer1 == "CPU3":
                print("asking CPU3 for ", self.pAnswer3)
                Value1 = False
                for i, self.Card in enumerate (self.CPU3.hand):
                    
                    #tempTestCard = str(self.Card.value) + " " + self.Card.suit
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.pAnswer3:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU3.hand.pop(i)
                        self.realPlayer.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.realPlayer]
                    self.dealer.dealCards(1, xList)
                    print('''
                        YOUR CURRENT HAND''')
                    self.realPlayer.showHand()
                    #print("You playin with the deck")
                    #self.realPlayer.showHand()
                print("asking CPU3 for ", self.pAnswer3)
            tempL = []
            for i, self.Card in enumerate (self.realPlayer.hand):
                tempL.append(self.Card.value)
            hasFour, RepeatedNum = four_of_a_kind(tempL) 
            #if hasFour:
            #    print("four of", RepeatedNum)
            #    cards_removed = []
            #    while len(cards_removed) < 4:
            #        for i, card in enumerate(self.realPlayer.hand):
            #            if card.value == RepeatedNum:
            #                temp15 = card
            #               cards_remove.append(temp15)

            if hasFour:
                print("four of", RepeatedNum)
                cards_remove = []
                for _ in range(2):
                    for i, card in enumerate(self.realPlayer.hand):
                        if card.value == RepeatedNum:
                            temp15 = card
                            cards_remove.append(temp15)

                print(cards_remove)
                for i in range(1, len(cards_remove)):
                    print("this is your hint: ", i)
                    temp3 = self.realPlayer.hand.pop(i)
                    self.playerTable.append(temp3)
                """ for i, self.Card in enumerate (self.realPlayer.hand * 3):
                    print(len(self.realPlayer.hand))
                    if RepeatedNum == self.Card.value:
                        tempHoldFour = self.realPlayer.hand.pop(i)
                        self.playerTable.append(tempHoldFour) """
                self.realPlayer.showHand()
                print(self.playerTable)    
            else:
                print("don't have a four pair")

            
        #ADD IN CHECK FOR FOUR OF A KIND -------------------------------------
        #---------------------------------------------------------------------
#CPU1 TURN --------------------------------------------------------------------------------------------                
            self.playListCPU1 = ["realPlayer", "CPU2", "CPU3"]
            print('''
            ''')
            slow_print('''it is CPU1's turn''')
            for i, self.Card in enumerate (self.CPU1.hand):
                CPU1Hand.append(self.Card.value)
            self.playerAsk1 = random.choice(self.playListCPU1)
            self.cardValueAsk1 = random.choice(CPU1Hand)
            print("CPU1 is picking ", str(self.playerAsk1), "to ask for", str(self.cardValueAsk1))
            #randomly generate a value for CPU1
            if str(self.playerAsk1) == "realPlayer":
                print("asking YOU for ", str(self.cardValueAsk1))
                Value1 = False
                for i, self.Card in enumerate (self.realPlayer.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk1:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.realPlayer.hand.pop(i)
                        self.CPU1.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU1 HAND ------------ ")
                        self.CPU1.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU1]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU1 CURRENT HAND''')
                    self.CPU1.showHand()
            elif str(self.playerAsk1) == "CPU2":
                print("asking CPU2 for ", str(self.cardValueAsk1))
                Value1 = False
                for i, self.Card in enumerate (self.CPU2.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk1:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU2.hand.pop(i)
                        self.CPU1.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU1 HAND ------------ ")
                        self.CPU1.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU1]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU1 CURRENT HAND''')
                    self.CPU1.showHand()
            elif str(self.playerAsk1) == "CPU3":
                print("asking CPU3 for ", str(self.cardValueAsk1))
                Value1 = False
                for i, self.Card in enumerate (self.CPU3.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk1:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU3.hand.pop(i)
                        self.CPU1.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU1 HAND ------------ ")
                        self.CPU1.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU1]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU1 CURRENT HAND''')
                    self.CPU1.showHand()
                    print("You playin with the deck")
                    #self.realPlayer.showHand()
            #print(self.playList)
        #ADD IN CHECK FOR FOUR OF A KIND -------------------------------------
        #---------------------------------------------------------------------
#CPU2 TURN -------------------------------------------------------------------------------------------- 
            self.playListCPU2 = ["realPlayer", "CPU1", "CPU3"]
            print('''
            ''')
            slow_print('''it is CPU2's turn''')
            for i, self.Card in enumerate (self.CPU2.hand):
                CPU2Hand.append(self.Card.value)
            self.playerAsk2 = random.choice(self.playListCPU2)
            self.cardValueAsk2 = random.randint(1,13)
            print("CPU2 is picking ", str(self.playerAsk2), "to ask for", str(self.cardValueAsk2))
            #randomly generate a value for CPU1
            if str(self.playerAsk2) == "realPlayer":
                print("asking YOU for ", str(self.cardValueAsk2))
                Value1 = False
                for i, self.Card in enumerate (self.realPlayer.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk2:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.realPlayer.hand.pop(i)
                        self.CPU2.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU2 HAND ------------ ")
                        self.CPU2.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU2]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU2 CURRENT HAND''')
                    self.CPU2.showHand()
            elif str(self.playerAsk2) == "CPU1":
                print("asking CPU1 for ", str(self.cardValueAsk2))
                Value1 = False
                for i, self.Card in enumerate (self.CPU1.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk2:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU1.hand.pop(i)
                        self.CPU2.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU2 HAND ------------ ")
                        self.CPU2.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU2]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU2 CURRENT HAND''')
                    self.CPU2.showHand()
            elif str(self.playerAsk2) == "CPU3":
                print("asking CPU3 for ", str(self.cardValueAsk2))
                Value1 = False
                for i, self.Card in enumerate (self.CPU3.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk2:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU3.hand.pop(i)
                        self.CPU2.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU2 HAND ------------ ")
                        self.CPU2.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU2]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU2 CURRENT HAND''')
                    self.CPU2.showHand()
                    #print("You playin with the deck")
                    #self.realPlayer.showHand()
                print("asking CPU3 for ", self.pAnswer3)

        #ADD IN CHECK FOR FOUR OF A KIND -------------------------------------
        #---------------------------------------------------------------------
#CPU3 TURN -------------------------------------------------------------------------------------------- 
            self.playListCPU3 = ["realPlayer", "CPU1", "CPU2"]
            print('''
            ''')
            slow_print('''it is CPU3's turn''')
            for i, self.Card in enumerate (self.CPU3.hand):
                CPU3Hand.append(self.Card.value)
            self.playerAsk3 = random.choice(self.playListCPU3)
            self.cardValueAsk3 = random.randint(1,13)
            print("CPU1 is picking ", str(self.playerAsk3), "to ask for", str(self.cardValueAsk3))
            #randomly generate a value for CPU1
            if str(self.playerAsk3) == "realPlayer":
                print("asking YOU for ", str(self.cardValueAsk3))
                Value1 = False
                for i, self.Card in enumerate (self.realPlayer.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk3:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.realPlayer.hand.pop(i)
                        self.CPU3.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU3 HAND ------------ ")
                        self.CPU3.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU3]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU3 CURRENT HAND''')
                    self.CPU3.showHand()
            elif str(self.playerAsk3) == "CPU2":
                print("asking CPU2 for ", str(self.cardValueAsk3))
                Value1 = False
                for i, self.Card in enumerate (self.CPU2.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk3:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU2.hand.pop(i)
                        self.CPU3.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU3 HAND ------------ ")
                        self.CPU3.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU3]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU3 CURRENT HAND''')
                    self.CPU3.showHand()
            elif str(self.playerAsk3) == "CPU1":
                print("asking CPU1 for ", str(self.cardValueAsk3))
                Value1 = False
                for i, self.Card in enumerate (self.CPU1.hand):
                    tempTestCard = self.Card.value
                    #print(tempTestCard)
                    if tempTestCard == self.cardValueAsk3:
                        Value1 =True
                        print('''
                    ''')
                        print("Nice! They had at least one!")
                        tempCard = self.CPU1.hand.pop(i)
                        self.CPU3.addCard(tempCard)
                        print('''
                        YOUR CURRENT HAND''')
                        self.realPlayer.showHand()

                        print("CPU3 HAND ------------ ")
                        self.CPU3.showHand()
                    else:
                        print('''''')
                if Value1 == False:
                    slow_print('''no such luck...''')
                    print(''')
                            ''')
                    xList = [self.CPU3]
                    self.dealer.dealCards(1, xList)
                    print('''
                        CPU3 CURRENT HAND''')
                    self.CPU3.showHand()
            # if player.deck = []
        #   - This is where were gonna have the game 
        #   - logic go  a


#Main function will handle only the starting of the program. 
def main():
    print('''
    
    
    ''')
    def find_root_dir():
        cwd = os.getcwd()
        print("Current working directory:", cwd)
        # Add more print statements as needed
        # ...
    find_root_dir()
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


        