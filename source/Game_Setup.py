from source.NewCardGames import *

class GameSetup:
    def __init__(self):
        #Initialize the objects that need to be initialized
        self.cards_in_play = []
        #Evolve this into creating a Fugitive object and setting object's deck to starting_cards
        self.fugitive_deck = starting_cards
        self.fugitive_deck.append(escape_card)
        #Evolve this into creating a Marshall object (deck should be empty by default
        self.marshall_deck = []
        self.fugitive_name = ""
        self.marshall_name = ""
        self.done = False
    
    def start_game(self):
        #Evolve this into accessing Fugitive object's 'Name' attribute and setting it to input
        while len(self.fugitive_name) == 0:
            self.fugitive_name = input("Fugitive, what is your name? --> ").strip()
        while len(self.marshall_name) == 0:
            self.marshall_name = input("Marshall, what is your name? --> ").strip()
        print(f"{self.fugitive_name} will go first!")
        first_turn = True

        while self.done != True:
            #Different rule sequence for first turn
            while first_turn:
                #Fugitive places 1 or 2 new hideouts
                print(f"{self.fugitive_name} please choose a hideout to pick.")
                #Marshall draws 2 cards; chooses which deck to draw from
                print(f"{self.marshall_name} please choose which deck to draw your cards from.")
                return
            #Outside of first turn
            #Fugitive draws 1 card from any deck. 
            #Can choose to place 1 new hideout, or pass
            
            #Marshall draws 1 card from any deck.
            #Makes a singular guess to find a hideout (possible expand into guessing multiple hideouts)
        
                
            #Fugitive's Win Condition --> Fugitive plays card with value 42.
            #Marshall's Win Condition --> Wins by guessing all cards (hideouts) currently in play
            return
        