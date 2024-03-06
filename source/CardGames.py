import random
import os

cardImages = []

values = list(range(1,43))
sprint_value = [1, 2]

def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd

#Card class adjusted
class Card:
  def __init__(self, sprint_value, value, image, cardBack):
    self.cardBack = cardBack
    self.sprint_value = sprint_value
    self.value = value
    self.image = image
    self.shortImage = []
    if self.image:
      for line in self.image:
        self.shortImage.append(line[:4])
  def __eq__(self, other):
    if not type(other) == Card:
      return False
    return self.value == other.value and \
      self.sprint_value == other.sprint_value

#Deck class adjusted
class Deck:
  def __init__(self):
    root_dir = os.path.join( find_root_dir(), 'source')
    cards_file = f'{root_dir}{os.path.sep}new_playing_cards.txt'
    with open(cards_file, "r") as cards:
      cardBack = []
      for _ in range(6):
        line = cards.readline()
        cardBack.append(line.replace("\n",""))
      card = []
      level = 0
      for line in cards.readlines():
        if len(line) == 1:
          cardImages.append(card)
          level = 0
          card = []
          continue
        card.append(line.replace("\n",""))
        level += 1
      cardImages.append(card)
    
    deck = []
    index = 0
    for value in values:
        if value % 2 == 0:
            deck.append(Card(2, value, cardImages[index], cardBack))
        else:
            deck.append(Card(1, value, cardImages[index], cardBack))
        index += 1
    
    self.cards = deck
    self.size = len(deck)
    self.cardBack = cardBack
    self.discarded = []
  def reset(self):
    self.cards += self.discarded
    self.discarded = []
    self.size = len(self.cards)
  def shuffle(self):
    random.shuffle(self.cards)
  def getCard(self):
    card = self.cards.pop()
    self.size -= 1
    self.discarded.append(card)
    return card

class Player:
  def __init__(self, name, role, money: int = 0):
    self.name = name
    self.hand = []
    self.knownCards = []
    self.money = money
    self.role = role  #This would be to distinguish whether the object is either acting as Marshall or Fugitive
  def addMoney(self, amount: int):
    self.money += amount
    return self.money
  def makeBet(self, amount: int):
    if amount > self.money:
      print("%s does not have enough money to make this bet." % self.name)
      return self.money
    self.money -= amount
    return self.money
  def addCard(self, card: Card, isKnown: bool = True):
    self.hand.append(card)
    if isKnown:
      self.knownCards.append(True)
    else:
      self.knownCards.append(False)
  def setHand(self, cards: "list[Card]", isKnown: bool = False):
    self.hand = cards
    self.knownCards = [isKnown for _ in self.hand]
  def showHand(self, printShort: bool = False):
    for idx in range(6):
      for i, card in enumerate(self.hand):
        if printShort and i < len(self.hand)-1:
          image = card.shortImage[idx]  if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
          print(image, end="")
      print()
  def clearHand(self):
    self.hand = []
    self.knownCards = []

class Dealer:
  def __init__(self, deck: Deck):
    self.deck = deck
    self.deck.shuffle()
  def printCards(self, cards: "list[Card]", showFront: bool, printShort: bool = True):
    for idx in range(6):
      for i, card in enumerate(cards):
        if printShort and i < len(cards)-1:
          image = card.shortImage[idx] if showFront else card.cardBack[idx]
          print(image, end="")
        else:
          image = card.image[idx] if showFront else card.cardBack[idx]
          print(image, end="")
      print()
  def dealCards(self, numCards: int, players: "list[Player]"):
    if numCards * len(players) > self.deck.size:
      return False
    for player in players:
      for _ in range(numCards):
        player.addCard(self.deck.getCard())
    return True
  def resetDeck(self):
    self.deck.reset()
    self.deck.shuffle()

#Split deck into 3 piles and escape_card/starting_cards
def split_card():
  game_deck=Deck()
  #Get card 42
  escape_card = game_deck.getCard()
  #Get cards 41 - 29
  HighRangeDeck = []
  for card in range(13):
    test_card = game_deck.getCard()
    HighRangeDeck.append(test_card)

  #Get cards 28 - 15
  MidRangeDeck = []
  for card in range(14):
    test_card = game_deck.getCard()
    MidRangeDeck.append(test_card)

  #Get cards 14 - 4
  LowRangeDeck = []
  for card in range(11):
    test_card = game_deck.getCard()
    LowRangeDeck.append(test_card)

  #Get cards 3 - 1
  starting_cards = []
  for i in range(3):
    test_card = game_deck.getCard()
    starting_cards.append(test_card)

  return escape_card, HighRangeDeck, MidRangeDeck, LowRangeDeck, starting_cards
    
def character_selection():
  Player1 = input("Player 1, please enter your name: ")
  Player2 = input("Player 2, please enter your name: ")
  Player1Role = ""
  Player2Role = ""
  rand = random.randint(0,1)
  if rand == 0:
    while Player1Role != "fugitive" and Player1Role != "marshall":
      Player1Role = input(str(Player1) + ", please pick your role(Fugitive or Marshall): ").lower()
      if Player1Role == "fugitive":
        print(str(Player1) + ", you are the Fugitive.")
        print(str(Player2) + ", you are the Marshall.")
      elif Player1Role == "marshall":
        print(str(Player1) + ", you are the Marshall.")
        print(str(Player2) + ", you are the Fugitive.")
  else:
    while Player2Role != "fugitive" and Player2Role != "marshall":
      Player2Role = input(str(Player2) + ", please pick your role(Fugitive or Marshall): ").lower()
      if Player2Role == "fugitive":
        print(str(Player2) + ", you are the Fugitive.")
        print(str(Player1) + ", you are the Marshall.")
      elif Player2Role == "marshall":
        print(str(Player2) + ", you are the Marshall.")
        print(str(Player1) + ", you are the Fugitive.")
  
  return Player1, Player1Role, Player2, Player2Role


def highestCard(cardList):
  highestCard = getCard("Spades", 1)
  for card in cardList:
    if card.value >= highestCard.value:
      highestCard = card
  return highestCard

  


class GameSetup:
    def __init__(self):
        #Initialize the objects that need to be initialized
        self.escape_card, self.HighRangeDeck, self.MidRangeDeck, self.LowRangeDeck, self.starting_cards = split_card()
        self.cards_in_play = []
        self.fugitive = Player("", "Fugitive", 0)
        self.marshall = Player("", "Marshall", 0)
        self.done = False
    
    def start_game(self):
        Player1, Player1Role, Player2, Player2Role = character_selection()
        if (Player1Role == "fugitive"):
           self.fugitive.name = Player1
           self.marshall.name = Player2
        else:
           self.fugitive.name = Player2
           self.marshall.name = Player1
        first_turn = True

        print(f"\n\n***LET THE GAME BEGIN!***\n\n{self.fugitive.name} shall go first!")

        while self.done != True:
            #Different rule sequence for first turn
            while first_turn:
                #Fugitive places 1 or 2 new hideouts
                fugitive_choices = self.fugitive_first_turn()
                #Marshall draws 2 cards; chooses which deck to draw from
                print(f"{self.marshall.name} is next!")
                marshall_choices = self.marshall_first_turn()
                
            #Outside of first turn
            #Fugitive draws 1 card from any deck. 
            #Can choose to place 1 new hideout, or pass
            
            #Marshall draws 1 card from any deck.
            #Makes a singular guess to find a hideout (possible expand into guessing multiple hideouts)
        
                
            #Fugitive's Win Condition --> Fugitive plays card with value 42.
            #Marshall's Win Condition --> Wins by guessing all cards (hideouts) currently in play
            return
    
    def fugitive_first_turn(self):
      fugitive_deck = self.starting_cards
      fugitive_deck.append(self.escape_card)
      for x in range(3):
        fugitive_deck.append(self.LowRangeDeck.pop())
                        
      for x in range(2):
        fugitive_deck.append(self.MidRangeDeck.pop())
      
      string = ""
      for i in fugitive_deck:
        string += str(i.value) + ", "
        string = string[:len(string)-2]

      print("Here is your starting hand: " + string) 

      #May have to check if burn is empty string in case fugitive does not want to burn anything
      burn = input("Enter which cards to burn separated only by a comma (1,2,3...)").split(',')
      hideouts = input("Select two viable cards you want to place as hideouts separated only by a comma (1,2,3...): ").split(',')
      #Would probably call function to check if hideouts are viable here. If hideouts aren't viable, reprompt fugitive
      
      return burn, hideouts
      

  
    def marshall_first_turn(self):
     
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
                      guess = int(input("Enter fugitive location..."))
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

game = GameSetup()
game.start_game()