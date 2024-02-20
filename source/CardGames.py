
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
    self.pot -= amount
    return self.pot
  
  def show_pot(self):
    return self.pot

#------------------------------------------------------------------------------

class Game:
    def __init__(self, players, dealer, pot):
        self.players = players
        self.dealer = dealer
        self.current_turn = 0  # Index current player's turn
        self.pot = pot

    def reset_round(self, raising_player, raise_amount):
        # Notify players of the raise
        print(f"{raising_player.name} has raised the bet by {raise_amount}.")
        self.pot.add(raise_amount)  # Assuming we want the raising player to already subtract the amount

        for i, player in enumerate(self.players):
            # Skip player who made the raise
            if player == raising_player:
                continue

            while True:
                print(f"{player.name}, it's your turn. You have {player.money}. The current pot is {self.pot.show_pot()}.")
                decision = input("Would you like to 'call', 'raise', or 'fold'? ").lower()

                if decision == 'call':
                    if player.money < raise_amount:
                        print(f"{player.name} does not have enough money to call and is automatically folded.")
                        self.players.remove(player) 
                    else:
                        player.makeBet(raise_amount, self.pot)
                        print(f"{player.name} calls.")
                    break
                elif decision == 'raise':
                    additional_raise = int(input("Enter the additional raise amount: "))
                    if player.raise_bet(additional_raise + raise_amount, self.pot, self):
                        print(f"{player.name} raises by {additional_raise}.")
                        # Reset round again with the new raise but not current player from being prompted again
                        self.reset_round(player, additional_raise + raise_amount)
                    else:
                        print("Not enough money to raise. Try a different action.")
                    break
                elif decision == 'fold':
                    print(f"{player.name} folds.")
                    self.players.remove(player)  # Assuming we want to remove the player from the game
                    break
                else:
                    print("Invalid decision. Please choose 'call', 'raise', or 'fold'.")

    def next_turn(self):
        # Advance to next player's turn start again if at the last player
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def handle_raise(self, player, raise_amount):
        if player.raise_bet(raise_amount, self.pot, self):
            self.reset_round(player, raise_amount)
            print(f"{player.name} raised the bet by {raise_amount}.")
        else:
            print("Raise failed.")


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

  def makeBet(self, amount: int, pot: Pot):
    if amount > self.money:
      print("%s does not have enough money to make this bet." % self.name)
      return self.money
    self.money -= amount
    pot.add(amount)  # Call function implemented here--------------------------------
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


