
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


# Pot class----------------------------------------------------------------------
class Pot:
  def __init__(self, pot: int = 0):
    self.pot = pot

  def add(self, amount: int):
    self.pot += amount
    return self.pot

  def subtract(self, amount: int):
    if (self.pot - amount) >= 0:
      self.pot -= amount
    else:
      print("Not enough money in the pot.")
    return self.pot
  
  def show_pot(self):
    return self.pot

#------------------------------------------------------------------------------

class Game:
    def __init__(self, players, pot):
        self.players = players  # Assuming players is a list of Player objects
        self.pot = pot  # Pot object
        self.current_turn = 0  # Index of the current player's turn
        self.current_raise = 0  # Track the current raise amount

    def next_turn(self):
        # Advance to the next player's turn, wrapping around to the first player if necessary
        self.current_turn = (self.current_turn + 1) % len(self.players)
        print(f"It's now {self.players[self.current_turn].name}'s turn.")

    def raise_bet(self, player_index, amount):
        player = self.players[player_index]
        if player.money < amount:
            print(f"{player.name} does not have enough money to raise.")
            return False
        player.money -= amount
        self.pot.add(amount)
        self.current_raise = amount
        print(f"{player.name} raises the bet by {amount}. The pot is now {self.pot.show_pot()}.")
        self.reset_round(player_index)
        self.next_turn()  # Automatically advance to the next turn
        return True

    def reset_round(self, raising_player_index):
        # Make other players match the raise or fold
        for index, player in enumerate(self.players):
            if index == raising_player_index:
                continue  # Skip the player who made the raise

            print(f"{player.name}, you need to match the raise of {self.current_raise} or fold.")
          

    def match_raise(self, player_index):
        # Assume a method where players can match the current raise
        player = self.players[player_index]
        if player.money < self.current_raise:
            print(f"{player.name} doesn't have enough money to match the raise and is folded.")
        else:
            player.money -= self.current_raise
            self.pot.add(self.current_raise)
            print(f"{player.name} matches the raise. The pot is now {self.pot.show_pot()}.")

    def player_action(self, player_index, action, amount=0):
        # This method can be expanded to handle different player actions (raise, call, fold)
        if action == "raise":
            self.raise_bet(player_index, amount)
        elif action == "call":
            self.match_raise(player_index)
        # Add more actions as needed
        self.next_turn()  # Move to the next turn after the action




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
  
  def __repr__(self) -> str:
    return f"Card(suit='{self.suit}', value={self.value})"

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
  def makeBet(self, amount: int, pot: Pot): # amount - integer number of money to remove from player
    if amount > self.money:
      print("%s does not have enough money to make this bet." % self.name)
      return self.money
    else:
      self.money -= amount
      pot.add(amount)  # Call function implemented here--------------------------------
      return self.money

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


# has_pair function---------------------------------------------------------------

def has_pair(player):
    Hand = player.hand
    values = [card.value for card in Hand]
    compare = set()
    print(values, compare)
    for i in values:
        if i in compare:
            return True
        compare.add(i)
    else:
        return False
#---------------------------------------------------------------------------------


# call function--------------------------------------------------------------

def Call(player, bet: int, pot):
    player.makeBet(bet, pot)



def highest_card(hand):
    # Check if the hand is empty
      if not hand:
          return None

    # Find the card with the highest value
      highest_card = max(hand, key=lambda card: card.value)
    
    # Return the highest card
      return highest_card


class Poker:
  def __init__(self, players: "list[Player]", dealer: Dealer):
    self.players = players
    self.dealer = dealer
    self.pot = 0
    self.bets = [0 for _ in range(len(players))]
    self.round = 0
    self.currentPlayer = 0


  # Add all functions pertaining to the game of poker below
  # Add global variables to the __init__ function above

  # Keep Track of Pot, Bets, and current round
  def addMoneyToPot(self, amount: int):
    self.pot += amount
    return self.pot
  
  def addBet(self, player: Player, amount: int):
    idx = self.players.index(player)
    self.bets[idx] += amount
    return self.bets[idx]
  
  # Add all bets to the pot
  def collectBets(self):
    for bet in self.bets:
      self.addMoneyToPot(bet)
    self.bets = [0 for _ in range(len(self.players))]

  # Check if all bets are equal
  def checkBets(self):
    return len(set(self.bets)) == 1
  
  # Check how much is needed to call
  def callAmount(self, player: Player):
    idx = self.players.index(player)
    return max(self.bets) - self.bets[idx]
  
class Identification:
  def __init__(self):
    self.hand = [] # Hold values of cards in hand
    self.name = "" # Name defined by the rank definition functions

  # Include functions that return what defines the various poker hand ranks.
  
  def twoPair(self):
    # iterate through the hand to count occurrences of each card value
    count = {} # dictionary to count the occurences
    
    # make dictionary
    for card in self.hand: 
      if card.value in count:
        count[card.value] += 1
      else:
        count[card.value] = 1
    
    pairs = [value for value,freq in count.items() if freq == 2]
        
    if len(pairs) == 2:
      # return this list that contains the values of cards that form 2 pairs in paired_values.
      pair_cards = [card for card in self.hand if card.value in pairs]
      return pair_cards
    else:
      #return empty list since it's not exactly two pairs.
      return []