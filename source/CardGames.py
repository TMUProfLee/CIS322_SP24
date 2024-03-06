
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

class Deck:
  def __init__(self):
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

  def shuffle(self):
    random.shuffle(self.cards)

  def getCard(self):
    card = self.cards.pop()
    self.size -= 1
    self.discarded.append(card)
    return card

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
    self.hand = []
    self.knownCards = []
    self.money = money

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
    

def DisplayHands():
  P1 = Player("Nick", 100)
  five_spades = getCard("spades", 5)
  four_spades = getCard("Spades", 4)
  two_hearts = getCard("Hearts", 2)
  two_spades = getCard("Spades", 2)
  one_spades = getCard("Spades", 1)
  cards = [ five_spades, four_spades, two_hearts, two_spades, one_spades ]

  P2 = Player("Logan", 300)
  nine_spades = getCard("spades", 9)
  eight_spades = getCard("Spades", 8)
  seven_spades = getCard("spades", 7)
  six_spades = getCard("Spades", 6)
  five_hearts = getCard("Hearts", 5)
  cards2 = [ nine_spades, eight_spades, seven_spades, six_spades, five_hearts ]

  P1.setHand( cards, isKnown=True )
  assert P1.showHand() == None
  
  P2.setHand( cards2, isKnown=True )
  assert P2.showHand() == None

  #print(Detect_Pair(P1.hand))

def Detect_Pair(hand):
    
    count = 0
    cardlist = []
    #create list of card numbers
    for i in hand:
      cardlist.append(hand[count].value)
      count = count + 1
    #create list stripped of duplicates
    cardlistset=set(cardlist)
    #check if lists length are the same and return Boolean value
    if len(cardlistset) != len(cardlist):
      #print("True")
      return True  
    else:
      #print("False")
      return False

def Num_players():
  while True:
    num_players_str = input("Enter number of players:")
    if num_players_str.isdigit():
        num_players_int = int(num_players_str)
        if num_players_int > 0:
            break
        else:
            print("Please enter a positive number")
    else:
        print("Please enter a valid number")

def Win_screen(win_player):
    if len(win_player) >= 1:
      print("""
===============================================================
            

                        ———GAME OVER——— 
            

===============================================================
            """)

      print("""Congratuations to """, " & ".join(win_player))
      return True
    
    else:
      return False

    

    
    


def main():
  win_player = ["nick", "logan"]
  Win_screen(win_player)
 

if __name__ == '__main__':
  main()