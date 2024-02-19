from NewCardGames import *

class GameSetup:
    def __init__(self):
        #Initialize the objects that need to be initialized
        self.cards_in_play = []
        #Evolve this into creating a Fugitive object and setting object's deck to starting_cards
        self.fugitive_deck = starting_cards
        self.fugitive_deck.append(escape_card)
        #Evolve this into creating a Marshall object (deck should be empty by default
        self.marshall_deck = []

        self.done = False
    
    def start_game(self):
        #Evolve this into accessing Fugitive object's 'Name' attribute and setting it to input
        fugitive_name = input("Fugitive, what is your name? --> ")
        marshall_name = input("Marshall, what is your name? --> ")
        
        first_turn = True

        while self.done != True:
            #Different rule sequence for first turn
            while first_turn:
                #Fugitive places 1 or 2 new hideouts

                #Marshall draws 2 cards; chooses which deck to draw from

            #Outside of first turn
            #Fugitive draws 1 card from any deck. 
            #Can choose to place 1 new hideout, or pass
            
            #Marshall draws 1 card from any deck.
            #Makes a singular guess to find a hideout (possible expand into guessing multiple hideouts)
        
                
            #Fugitive's Win Condition --> Fugitive plays card with value 42.
            #Marshall's Win Condition --> Wins by guessing all cards (hideouts) currently in play
            

            
        

        

game = GameSetup()
game.start_game()

