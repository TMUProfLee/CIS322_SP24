
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
    print("\nYOUR HAND: ")
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
    for guess in self.guesses:
      print(guess, end='')

class GameSetup:
    def __init__(self):
        #Initialize the objects that need to be initialized
        self.escape_card, self.HighRangeDeck, self.MidRangeDeck, self.LowRangeDeck, self.starting_cards = self.split_card()
        self.cards_in_play = []
        self.fugitive = Player("", "Fugitive")
        self.marshall = Player("", "Marshall")
        self.done = False
        self.manhunt = False
        #Most recently correctly guessed hideout
        self.marshall_current_idx = 0

    def ReadRules(self):
        choice = ""
        while choice != "1" and choice != "0":
          choice = input("Would you like to read the rules (1 for yes or 0 for no)? ")
        if choice == "1":
          print(" ")
          rules = open("source/Rules.txt", "r")
          content = rules.read()
          print(content)
          rules.close()

    def start_game(self):
        self.ReadRules()
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
        
        if self.manhunt:
          time.sleep(1)
          print(self.fugitive.name + " has reached the last hideout!")
          time.sleep(1)
          
          # Check if marshall wants to begin manhun
          while True:
            hunt = input(self.marshall.name + ", would you like to begin a manhunt? (y/n): ")
            if hunt not in ['y', 'n']:
              continue
            break

          while True:
            win = self.marshall_guess()
            if win == None:
              continue
            elif win:
              os.system('cls')
              time.sleep(4)
              print("\nCorrect guess!")
              time.sleep(1)
              print("\n**" + self.fugitive.name + " has been caught!**")
              break
            else:
              os.system('cls')
              time.sleep(4)
              print("\nIncorrect guess")
              time.sleep(1)
              print("\n**" + self.fugitive.name + " got away!**")
              break         

    #Split deck into 3 piles and escape_card/starting_cards
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

    def reveal_cards(self, guess):
      repeat = len(guess) if type(guess) == list else 1
      for i in range(repeat):
        card = self.cards_in_play[self.marshall_current_idx + i][0] if type(self.cards_in_play[self.marshall_current_idx + i])\
            == list else self.cards_in_play[self.marshall_current_idx + i]
        card.revealed = True
    
    def display_board_general(self, player = 'marshall'):
      # Grab all the lists inside the cards_in_play list which represent sprints
      print("\nCARDS ON BOARD:")
      sprints = []
      for idx, stack in enumerate(self.cards_in_play):
        total_gap = 0
        if type(stack) == list:
          # Count all single cards behind to track gap for ascii
          for prev in range(idx - 1, -1, -1):
            if type(self.cards_in_play[prev]) == Card:
              total_gap += 1
            else:
              break
          sprints.append((stack, total_gap))

      # Print all cards/top cards
      for idx in range(6):
          for stack in self.cards_in_play:     
            if type(stack) == list:
              card = stack[0]
            else:
              card = stack
            if player == 'fugitive' or card.revealed: # Check if  should be placed face up
              image = card.image[idx]
            else:
              image = card.cardBack[idx]
            print(image, end="")
          print()

      # Print sprint cards under top cards
      if len(sprints):
        # Loop through cards under top card in sprint stacks
        for i in range(1, max([len(stack[0]) for stack in sprints])):
          # Loop for the 6 lines of ascii per card --Vertical--
          for idx in range(2, 6):
            # Loop for each stack of sprints --Horizontal--
            for stack in sprints:  
              # Print the preceding gap if previous placement(s) were single cards
              print(' ' * 7 * stack[1], end="")
              if len(stack[0]) > i:
                
                if idx == 5:
                  # Replace bottom line of ascii to hide the card number
                  print('|_____|', end="")
                else:
                  # Print card ascii face up without numbers
                  card = stack[0][i]
                  image = card.image[idx]
                  print(image, end="")
              else:
                print(' ' * 7, end="")
            print()


    def fugitive_first_turn(self):
      # Add starting cards to fugitive hand
      for c in self.starting_cards:
        self.fugitive.addCard(c)
      self.fugitive.addCard(self.escape_card)

      for x in range(3):
        self.fugitive.addCard(self.LowRangeDeck.pop())

      for x in range(2):
        self.fugitive.addCard(self.MidRangeDeck.pop())

      
      # Loop through 2 card choices
      for _ in range(2):
        # Set previous hideout to 0 if first go or the previous card
        if not len(self.cards_in_play):
          previous_hideout = 0
        else:
          previous_hideout = self.cards_in_play[-1] if type(self.cards_in_play[-1]) == Card else self.cards_in_play[-1][0]
        
        while True:
          self.fugitive.showHand()
          time.sleep(1.5)
          
          hideouts = input("\nSelect the card value you want to place as a hideout, followed by any sprint cards, separated only by a comma (1,2,3...): ").split(',')
          hideouts = [int(i) for i in hideouts]
          
          # Check if hideouts can be placed
          if not self.check_illegal_card(previous_hideout, hideouts):
            print("Illegal card choice, choose again")
            continue
          
          if len(hideouts) > 1:
            # Append stack of cards because sprints were chosen
            burn_list = []
            for num in hideouts:
              for x in self.fugitive.hand:
                if num == x.value:
                  burn_list.append(x)
                  # Remove chosen cards from hand
                  self.fugitive.hand.remove(x)
                  break
            self.cards_in_play.append(burn_list)
          else:
            # Append and remove single card with no sprints
            for x in self.fugitive.hand:
              if hideouts[0] == x.value:
                self.cards_in_play.append(x)
                self.fugitive.hand.remove(x)
                break

          time.sleep(0.5)
          self.display_board_general('fugitive')
          time.sleep(1)
          break

    #check if selected hideout is valid for first turncd
    def check_illegal_card(self, previous_hideout, hideouts):
      # Create set out of hideout choices
      cmpre = set(hideouts)
      
      fugitive_card_values = []
      #pull value of owned cards and add them to list
      for fug_card in self.fugitive.hand:
        fugitive_card_values.append(fug_card.value)
      
      # Check if hideout set is contained in the hand
      if not cmpre <= set(fugitive_card_values):
        return False

      burn_total = 0
      for idx, num in enumerate(reversed(hideouts)):
        # If current card is anything except top card, add sprint value to counter
        if idx != len(hideouts) - 1:
          burn_total += num
        else:
          # Set the card to track to top card. Works for single card too
          for x in self.fugitive.hand:
            if num == x.value:
              card = x
              break
          
          # Set previous hideout to count distance
          if type(previous_hideout) == Card:
            prev_hide = previous_hideout.value
          else:
            # If start of game and no cards placed yet
            prev_hide = previous_hideout
          
          # Check if card is within (3 + burn_total) distance of previous card
          if 1 <= (card.value - prev_hide) <= 3 + burn_total:
              return True
          else:
            return False

  
    def marshall_first_turn(self):
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

      os.system('cls')
      self.marshall_guess()


    def marshall_guess(self):
      time.sleep(1.5)
      # Show the cards marshall drew
      self.marshall.showHand()
      time.sleep(1)
      # Display the two cards the fugitive has placed, face down
      self.display_board_general()

      while(True):
          # Choose to guess single or all cards
          guess_all = input("\nWould you like to guess all fugitive locations? (y/n) ").lower()
          # Guessing all cards
          if not self.manhunt and (guess_all == 'y' or guess_all == 'yes'):
              # Loop until input is valid
              while(True):
                  guess = input("\nEnter locations separated only by a comma (1,2,3...) ").split(',')
                  # Make sure they are guessing all cards
                  num_unrevealed = 0
                  for card in self.cards_in_play:
                    card = card[0] if type(card) == list else card
                    if not card.revealed:
                      num_unrevealed += 1
                  if len(guess) < num_unrevealed:
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
          if type(guess) == list:
            self.reveal_cards(guess)
            os.system('cls')
            time.sleep(3)
            self.display_board_general()
            time.sleep(1.5)
            print("\n\n***CONGRATULATIONS! YOU GUESSED ALL THE HIDEOUTS AND CAUGHT THE FUGITIVE!***\n\n")
            self.done = True
            return
          else:
            guess = [guess]

          # If single guess, convert to list to update index
          if guess[0] == 42:
            return True
          
          print("\n**Correct location!**")
      
          # Reveal correct cards on the board
          self.reveal_cards(guess)

          # Update index based on how many locations were guessed correctly
          self.marshall_current_idx += len(guess)

          # Check for win
          guess_visual = '*'
      else:
        if self.manhunt:
          return False
        
        guess_visual = '#'
        print("\n**Incorrect guess.**")

      time.sleep(1.5)
      # Add guesses to a tracker variable
      self.marshall.add_guess((guess, guess_visual))
      print("\nGuesses added")
      
      time.sleep(1)
      # Print the board at the end of turn
      self.display_board_general()
      time.sleep(2)
      os.system('cls')

    def show_marshall_hand(self):
      if len(self.marshall.hand) == 0:
        print("There are no cards in your hand!")
      else:
        self.marshall.showHand()
  
    def fugitive_repeating_turn(self):
      time.sleep(1.5)
      self.fugitive.showHand()
      time.sleep(2)

      self.display_board_general("fugitive")
      time.sleep(1.5)

      cards_left = len(self.LowRangeDeck) or len(self.MidRangeDeck) or len(self.HighRangeDeck)
      if cards_left:
        # Loop through deck choice
        while True:
          try:
            draw = int(input(f"\n {self.fugitive.name}, select which deck to draw a card from ['1' (1-14), '2' (15-28), '3' (29-42)]: ").strip())
          except ValueError:
            print("Invalid input, try again")
            continue

          if draw == 1: 
            # Draw from low deck if there are cards left
            if len(self.LowRangeDeck):
              self.fugitive.addCard(self.LowRangeDeck.pop())
              break
            else:
              print("No cards remaining in that deck")
              time.sleep(1.5)
              continue
          elif draw == 2: 
            # Draw from mid deck if there are cards left
            if len(self.MidRangeDeck):
              self.fugitive.addCard(self.MidRangeDeck.pop())
              break
            else:
              print("No cards remaining in that deck")
              time.sleep(1.5)
              continue
          elif draw == 3: 
            # Draw from high deck if there are cards left
            if len(self.HighRangeDeck):
              self.fugitive.addCard(self.HighRangeDeck.pop())
              break
            else:
              print("No cards remaining in that deck")
              time.sleep(1.5)
              continue
      
      # Loop through card choices
      while(True):
        print("\n**Your new hand:**")
        self.fugitive.showHand()

        time.sleep(1)
        self.display_board_general("fugitive")
        time.sleep(2)

        while(True):
          hideout = input("\nSelect a viable card value you want to place as a hideout, followed by any sprint cards (0 to pass): ").split(",")
          bad = False
          # Check for valid input
          for ele in hideout:
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

        hideout = [int(i) for i in hideout]
        
        # Pass condition
        if hideout[0] == 0:
          print("\nPassing...") 
          time.sleep(1.5)
          os.system('cls')
          break
        
        # Set previous hideout to the top card
        previous_hideout = self.cards_in_play[-1] if type(self.cards_in_play[-1]) == Card else self.cards_in_play[-1][0]
        # Check if card is valid to place
        if not self.check_illegal_card(previous_hideout, hideout):
          print("Illegal card choice, choose again")
          continue

        if len(hideout) > 1:
          # Append and remove card with sprints
          burn_list = []
          for num in hideout:
            for x in self.fugitive.hand:
              if num == x.value:
                burn_list.append(x)
                self.fugitive.hand.remove(x)
                break
              
          self.cards_in_play.append(burn_list)
        else:
          # Append and remove single card
          for x in self.fugitive.hand:
            if hideout[0] == x.value:
              if x.value == 42:
                self.done = True
                self.manhunt = True
                time.sleep(1)
                self.display_board_general()
                time.sleep(1.5)
                print("\n" + self.fugitive.name + "Wins!")
                return
              self.cards_in_play.append(x)
              self.fugitive.hand.remove(x)
              break        
        if self.manhunt:
          break

    def marshall_repeating_turn(self):
      time.sleep(1.5)
      print("\nHere are your guesses (* is correct, # is wrong or possibly wrong):")
      self.marshall.show_guesses()
      time.sleep(1)
      #Obtain user's deck choice
      cards_left = len(self.LowRangeDeck) or len(self.MidRangeDeck) or len(self.HighRangeDeck)
      if cards_left:
        self.print_remaining_cards()
        while True:
          try:
            deck = int(input("\nSelect which deck to draw a card from ['1' (1-14), '2' (15-28), '3' (29-42)] and press enter... "))
          except ValueError:
            print("Invalid input, try again.")
            continue
        
          match deck:
            case 1:
              if len(self.LowRangeDeck):
                deck = self.LowRangeDeck
                break
              else:
                print("No cards remaining in that deck")
            case 2:
              if len(self.MidRangeDeck):
                deck = self.MidRangeDeck
                break
              else:
                print("No cards remaining in that deck")
            case 3: 
              if len(self.HighRangeDeck):
                deck = self.HighRangeDeck
                break
              else:
                print("No cards remaining in that deck")
      
        #Draw a card from selected deck
        self.marshall.addCard(deck.pop())
      self.marshall_guess()

    # Show how many cards are left in each deck
    def print_remaining_cards(self):
      print("\nRemaining Cards:\nLow Deck: {}\tMid Deck: {}\t High Deck: {}".format(len(self.LowRangeDeck), len(self.MidRangeDeck), len(self.HighRangeDeck)))

game = GameSetup()
game.start_game()

