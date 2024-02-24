
import random
import os

cardImages = []
values = list(range(1,14))
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def find_root_dir():
  cwd = os.getcwd()
  while 'source' not in os.listdir():
    os.chdir('..')
    cwd = os.path.join( cwd, '..')
  return cwd

class Card:
  def __init__(self, suit, value, image, cardBack):
    self.cardBack = cardBack 
    self.suit = suit
    self.value = value
    self.image = image 
    self.shortImage = []
    if self.image:
      for line in self.image:
        self.shortImage.append(line[:4])

  def __eq__(self, other):
    if not type(other) == Card:
      return False
    return self.suit == other.suit and \
      self.value == other.value
      
  def __str__(self):
    return f"{self.value} of {self.suit}"

class Deck:
  def __init__(self): # builds a deck of cards
    root_dir = os.path.join( find_root_dir(), 'source')
    cards_file = f'{root_dir}{os.path.sep}playing_cards.txt'
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
    for suit in suits:
      for value in values:
        deck.append(Card(suit, value, cardImages[index], cardBack))
        index += 1
    
    self.cards = deck
    self.size = len(deck)
    self.cardBack = cardBack
    self.discarded = []

  def reset(self):
    self.cards += self.discarded
    self.discarded = []
    self.size = len(self.cards)

  def shuffle(self): # randomizes self.cards
    random.shuffle(self.cards)
# removes first card from self.cards and puts it at the end of self.discarded, returns first card in self.cards
  def getCard(self): 
    card = self.cards.pop()
    self.size -= 1
    self.discarded.append(card)
    return card

# testing 
def getCard( suit, value):
  deck = Deck()
  my_card = Card( suit.capitalize(), value, None, None)
  for card in deck.cards:
    if card == my_card:
      return card
  return None

class Player:
  def __init__(self, name, money: int = 0):
    self.name = name
    self.hand = [] # list of Card objects representiing the player's cards
    self.knownCards = []
    self.money = money # integer for amount of money the player currently has
    
  def sum_cards(self):
      sum = 0
      for card in self.hand:
          sum += card.value
      return sum

  def addMoney(self, amount: int): # adds more money to the player
    self.money += amount
    return self.money

  # removes money from player only if player has at least the bet amount currently 
  def makeBet(self, amount: int): # amount - integer number of money to remove from player
    if amount > self.money:
      print("%s does not have enough money to make this bet." % self.name)
      return self.money
    self.money -= amount
    return self.money # new amount of money the player has

  # adds one card to player's hand
  def addCard(self, card: Card, isKnown: bool = True):
    self.hand.append(card) # Card object to add to self.hand
    if isKnown: # whether card is known to everyone
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

  # removes all cards from the player's hand 
  def clearHand(self):
    self.hand = []
    self.knownCards = []
  
  def display(self, returnOutput: bool = False, showHand: bool = True):
    output = "\nname: \"%s\"\nmoney: %d\n" % (self.name, self.money)
    if len(self.hand) == 0:
      output += "The Player has no cards in their hand."
    else:
      if showHand:
        self.showHand()
    print(output)
    if returnOutput:
      return output
    

class Dealer:
  def __init__(self, deck: Deck): 
    self.deck = deck
    self.deck.shuffle()
    self.hand = [self.deck.getCard()] # intialize dealer's hand default amount to 1

  # displays a list of cards, either face up or face down. showFront - whether to show front of card (Value). printShort - whether to show only part of the card.
  def printCards(self, cards: "list[Card]", showFront: bool, printShort: bool = True): 
    for idx in range(6):
      for i, card in enumerate(cards): # list of Card objects to display
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
  
  def addCardsToDealer(self, amount=1):
    for _ in range(amount):
      if len(self.deck.cards) > 0:
        self.hand.append(self.deck.getCard())
      else:
        print("No more cards left in deck to add.")
        break

  def resetDeck(self):
    self.deck.reset()
    self.deck.shuffle()
