
import random
import os
import time

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
    #self.burn = burn
    self.image = image
    self.revealed = False


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

def getCard(value, burn):
  deck = Deck()
  my_card = Card(burn, value, None, None)
  for card in deck.cards:
    if card == my_card:
      return card
  return None


class Player:
  def __init__(self, name, role,):
    self.name = name
    self.hand = []
    self.knownCards = []
    self.guesses = []
    self.role = role  #This would be to distinguish whether the object is either acting as Marshall or Fugitive

  def addCard(self, card: Card):
    self.hand.append(card)
    self.hand.sort(key=lambda a:a.value)
    
  def setHand(self, cards: "list[Card]"):
    self.hand = cards

  def showHand(self):
    for idx in range(6):
      for i, card in enumerate(self.hand):
        image = card.image[idx]
        print(image, end="")
      print()

  def clearHand(self):
    self.hand = []
    self.knownCards = []

  def add_guess(self, guess):
    if type(guess) == list:
      for each in guess:
        self.guesses.append(each)
    else:
      self.guesses.append(guess)

  def show_guesses(self):
    print(self.guesses)


class GameSetup:
    def __init__(self):
        #Initialize the objects that need to be initialized
        self.escape_card, self.HighRangeDeck, self.MidRangeDeck, self.LowRangeDeck, self.starting_cards = self.split_card()
        self.cards_in_play = []
        self.fugitive = Player("", "Fugitive")
        self.marshall = Player("", "Marshall")
        self.done = False
        #Most recently correctly guessed hideout
        self.marshall_current_idx = 0
    
    def start_game(self):
        Player1, Player1Role, Player2, _ = self.character_selection()
        if (Player1Role == "fugitive"):
           self.fugitive.name = Player1
           self.marshall.name = Player2
        else:
           self.fugitive.name = Player2
           self.marshall.name = Player1

        os.system('cls')
        print(f"\n\n***LET THE GAME BEGIN!***\n\n{self.fugitive.name} shall go first!")
        time.sleep(2)
        #Fugitive places 1 or 2 new hideouts
        #Different rule sequence for first turn
        self.fugitive_first_turn()
        
        time.sleep(0.5)
        os.system('cls')
        self.display_board_general()
        time.sleep(1)
        #Marshall draws 2 cards; chooses which deck to draw from
        print(f"\n{self.marshall.name} is next!")
        
        time.sleep(1)
        # Marshall's first turn
        self.marshall_first_turn()
        if self.done:
          return
        os.system('cls')

        # Repeating turns
        while self.done != True: 
          print(f"\n{self.marshall.name} is next!")
          #Outside of first turn
          #Fugitive draws 1 card from any deck. 
          #Can choose to place 1 new hideout, or pass
          self.fugitive_repeating_turn()
            
          if self.done:
            break
          #Marshall draws 1 card from any deck.
          #Makes a singular guess to find a hideout (possible expand into guessing multiple hideouts)
          print("\n***Marshall's Turn***")
          
          self.marshall_repeating_turn()
            
    #Split deck into 3 piles and escape_card/starting_cards
    
    def ReadRules(self):
      rules = open("source/Rules.txt", "r")
      content = rules.read()
      print(content)
      rules.close()

    def split_card(self):
      game_deck=Deck()
      #Get card 42
      escape_card = game_deck.getCard()
      #Get cards 41 - 29
      HighRangeDeck = []
      for card in range(13):
        test_card = game_deck.getCard()
        HighRangeDeck.append(test_card)
      random.shuffle(HighRangeDeck)

      #Get cards 28 - 15
      MidRangeDeck = []
      for card in range(14):
        test_card = game_deck.getCard()
        MidRangeDeck.append(test_card)
      random.shuffle(MidRangeDeck)

      #Get cards 14 - 4
      LowRangeDeck = []
      for card in range(11):
        test_card = game_deck.getCard()
        LowRangeDeck.append(test_card)
      random.shuffle(LowRangeDeck)

      #Get cards 3 - 1
      starting_cards = []
      for i in range(3):
        test_card = game_deck.getCard()
        starting_cards.append(test_card)
      starting_cards[0], starting_cards[2], = starting_cards[2], starting_cards[0]
      return escape_card, HighRangeDeck, MidRangeDeck, LowRangeDeck, starting_cards

    def character_selection(self):
      Player1 = input("Player 1, please enter your name: ")
      Player2 = input("Player 2, please enter your name: ")
      Player1Role = ""
      Player2Role = ""
      rand = random.randint(0,1)
      if rand == 0:
        while Player1Role != "fugitive" and Player1Role != "marshall":
          Player1Role = input(str(Player1) + ", please pick your role(Fugitive or Marshall): ").lower()
          if Player1Role == "fugitive":
            Player2Role = "marshall"
            print(str(Player1) + ", you are the Fugitive.")
            print(str(Player2) + ", you are the Marshall.")
          elif Player1Role == "marshall":
            Player2Role = "fugitive"
            print(str(Player1) + ", you are the Marshall.")
            print(str(Player2) + ", you are the Fugitive.")
      else:
        while Player2Role != "fugitive" and Player2Role != "marshall":
          Player2Role = input(str(Player2) + ", please pick your role(Fugitive or Marshall): ").lower()
          if Player2Role == "fugitive":
            Player1Role = "marshall"
            print(str(Player2) + ", you are the Fugitive.")
            print(str(Player1) + ", you are the Marshall.")
          elif Player2Role == "marshall":
            Player1Role = "fugitive"
            print(str(Player2) + ", you are the Marshall.")
            print(str(Player1) + ", you are the Fugitive.")
      return Player1, Player1Role, Player2, Player2Role

  
    def check_location(self, guess, marshall_current_idx):
      # Loop if guessing multiple locations
      if type(guess) == list:
        for i in range(marshall_current_idx, len(self.cards_in_play)):
          guess_idx = i - marshall_current_idx
          item = self.cards_in_play[i]
          # Get top card if current location has burns
          card = item[0] if type(item) == list else item
          
          # If one is wrong return false
          if not guess[guess_idx] == card.value:
            return False
        return True
      # No loop for single guess
      item = self.cards_in_play[marshall_current_idx]
      
      # Get top card if current location has burns
      card = item[0] if type(item) == list else item
      return card.value == guess

    def reveal_cards(self, marshall_current_idx, repeat):
      for i in range(repeat):
        self.cards_in_play[marshall_current_idx + i].revealed = True
    
    def display_board_general(self, player = 'marshall'):
      sprints = [stack for stack in self.cards_in_play if type(stack) == list]
      has_sprints = False
      for idx in range(6):
          for stack in self.cards_in_play:     
            if type(stack) == list:
              has_sprints = True
              card = stack[0]
            else:
              card = stack
            if player == 'fugitive' or card.revealed:
              image = card.image[idx]
            else:
              image = card.cardBack[idx]
            print(image, end="")
          print()
      if has_sprints:
        spacing = len([s for s in self.cards_in_play if type(s) != list])

        for i in range(1, max([len(stack) for stack in sprints])):
          for idx in range(2, 6):
            print(' ' * 7 * spacing, end="")
            for stack in sprints:  
              if len(stack) > i:
                if idx == 5:
                  print('|_____|', end="")
                else:
                  card = stack[i]
                  image = card.image[idx]
                  print(image, end="")
              else:
                print(' ' * 7, end="")
            print()


    def fugitive_first_turn(self):
      for c in self.starting_cards:
        self.fugitive.addCard(c)
      self.fugitive.addCard(self.escape_card)

      for x in range(3):
        self.fugitive.addCard(self.LowRangeDeck.pop())

      for x in range(2):
        self.fugitive.addCard(self.MidRangeDeck.pop())

      if len(self.cards_in_play) == 0:
        previous_hideout = 0
      else:
        previous_hideout = self.cards_in_play[-1]
      
      while True:
        print("Here is your starting hand:")
        self.fugitive.showHand()

        time.sleep(1.5)
        hideouts = input("\nSelect two viable card values you want to place as hideouts separated only by a comma (1,2,3...): ").split(',')
        hideouts = [int(i) for i in hideouts]

        if len(hideouts) != 2:
          print("Select two inputs!")
          continue

        if not self.check_illegal_card(previous_hideout, hideouts):
          print("Illegal card choice, choose again")
          continue
        
        for num in sorted(hideouts):
          for x in self.fugitive.hand:
            if num == x.value:
              self.cards_in_play.append(x)
              self.fugitive.hand.remove(x)
              break
        break



    #check if selected hideout is valid for first turncd
    def check_illegal_card(self, previous_hideout, hideouts):
      cmpre = set(hideouts)
      
      fugitive_card_values = []
      #pull value of owned cards and add them to list
      for fug_card in self.fugitive.hand:
        fugitive_card_values.append(fug_card.value)

      if not cmpre <= set(fugitive_card_values):
        return False

      for num in sorted(hideouts):
        for x in self.fugitive.hand:
          if num == x.value:
            card = x
            break
        
        if type(previous_hideout) == Card:
          prev_hide = previous_hideout.value
        else:
          prev_hide = previous_hideout
        if 1 <= (card.value - prev_hide) <= 3:
          previous_hideout = card
        else:
          return False
      return True

  
    def marshall_first_turn(self):
      print("\nHere are your guesses (* is correct, # is wrong or possibly wrong):")
      self.marshall.show_guesses()
      time.sleep(1)
      # Get deck choice
      while True:
        try:
          deck = int(input("\nSelect which deck to draw two cards from ['1' (1-14), '2' (15-28), '3' (29-42)] and press enter... "))
        except ValueError:
          print("Invalid input, try again.")
          continue
        if deck in [1, 2, 3]:
          break

      if deck == 1:
        deck = self.LowRangeDeck
      elif deck == 2:
        deck = self.MidRangeDeck
      else:
        deck = self.HighRangeDeck

      # Draw two cards from the chosen deck
      for _ in range(2):
          draw_card = deck.pop()
          self.marshall.addCard(draw_card)

      time.sleep(0.5)
      os.system('cls')
      self.marshall_guess()


    def marshall_guess(self):
      time.sleep(1)
      # Show the cards marshall drew
      print("\nYour hand:")
      self.marshall.showHand()
      time.sleep(1)
      # Display the two cards the fugitive has placed, face down
      print("\nThe board:")
      self.display_board_general()

      while(True):
          # Choose to guess single or all cards
          guess_all = input("\nWould you like to guess all fugitive locations? (y/n) ").lower()
          # Guessing all cards
          if guess_all == 'y' or guess_all == 'yes':
              # Loop until input is valid
              while(True):
                  guess = input("\nEnter locations separated only by a comma (1,2,3...) ").split(',')
                  # Make sure they are guessing all cards
                  if len(guess) < len([card for card in self.cards_in_play if not card.revealed]):
                      print("Must guess all locations")
                      continue
                  bad = False
                  # Check for valid input
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
          # Guessing single card
          elif guess_all == 'n' or guess_all == 'no':
              # Loop until input is valid
              while True:
                  try:
                      guess = int(input("Enter fugitive location... "))
                  except:
                      ValueError
                      print("Invalid input, try again")
                      continue
                  break
              break
          else:
              print("Invalid input, try again")
      
      guess = [int(i) for i in guess] if type(guess) == list else guess
      
      time.sleep(1)
      guess_visual = '#'
      if self.check_location(guess, self.marshall_current_idx):
          print("\n**Correct location!**")
          self.reveal_cards(self.marshall_current_idx, len(guess) if type(guess) == list else 1)
          self.marshall_current_idx += 1
          guess_visual = '*'
          if self.marshall_current_idx == len(self.cards_in_play):
            time.sleep(1)
            self.display_board_general()
            time.sleep(1.5)
            print("\n" + self.marshall.name + "Wins!")
            self.done = True
            return
      else:
          print("\n**Incorrect guess.**")

      time.sleep(0.5)
      # Add guesses to a tracker variable
      self.marshall.add_guess((guess, guess_visual))
      print("\nGuesses added")
      
      time.sleep(1)
      # Print the board at the end of turn
      print("\nThe Board:")
      self.display_board_general()
      time.sleep(2)

    def show_marshall_hand(self):
      if len(self.marshall.hand) == 0:
        print("There are no cards in your hand!")
      else:
        self.marshall.showHand()
  
    def fugitive_repeating_turn(self):
      draw = 0

      print("\n**Your hand:**")
      self.fugitive.showHand()
      time.sleep(2)

      print("\nThe board")
      self.display_board_general("fugitive")
      time.sleep(1.5)

      while(True):
        while draw != 1 and draw != 2 and draw != 3:
          try:
            draw = int(input("\n Fugitive, select which deck to draw a card from ['1' (1-14), '2' (15-28), '3' (29-42)]: ").strip())
          except:
            ValueError
        if draw == 1:
          if len(self.LowRangeDeck):
            self.fugitive.addCard(self.LowRangeDeck.pop())
            break
          else:
            print("No cards remaining in that deck")
            time.sleep(1.5)
            continue
        elif draw == 2:
          if len(self.MidRangeDeck):
            self.fugitive.addCard(self.MidRangeDeck.pop())
            break
          else:
            print("No cards remaining in that deck")
            time.sleep(1.5)
            continue
        elif draw == 3:
          if len(self.HighRangeDeck):
            self.fugitive.addCard(self.HighRangeDeck.pop())
            break
          else:
            print("No cards remaining in that deck")
            time.sleep(1.5)
            continue
      

      while True:
        print("\n**Your new hand:**")
        self.fugitive.showHand()

        time.sleep(1)
        print("\nThe board:")
        self.display_board_general("fugitive")

        time.sleep(2)
        turn = 2
        while turn != 0 and turn != 1:
          try:
            turn = int(input("\nSelect if you want to place a hideout or pass ['0' for hideout or '1' for pass]: "))
          except ValueError:
            continue
          if turn not in [0,1]:
            continue
          break
        if turn == 0:
          previous_hideout = self.cards_in_play[-1]

          while(True):
            while(True):
              try:
                hideout = [int(input("\nSelect a viable card value you want to place as a hideout (0 to pass): "))]
              except ValueError:
                print("Invalid choice, try again")
                continue
              break
            
            if hideout == 0:
              print("\nPassing...") 
              break

            if not self.check_illegal_card(previous_hideout, hideout):
              print("Illegal card choice, choose again")
              continue

            for x in self.fugitive.hand:
              if hideout[0] == x.value:
                self.cards_in_play.append(x)
                self.fugitive.hand.remove(x)
                if x.value == 42:
                  self.done = True
                  time.sleep(1)
                  self.display_board_general()
                  time.sleep(1.5)
                  print("\n" + self.fugitive.name + "Wins!")
                break
            break
                    #Functions to check for illegally placed hideouts and burns would go here
        else:
          print("\nPassing...")  
          break  

    def print_remaining_cards(self):
      print("\nRemaining Cards:\nLow Deck: {}\tMid Deck: {}\t High Deck: {}".format(len(self.LowRangeDeck), len(self.MidRangeDeck), len(self.HighRangeDeck)))

game = GameSetup()
game.start_game()

