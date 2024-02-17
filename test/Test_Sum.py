from Sum import sum, Player, suits, cardImages, Card, Deck
import random

deck = Deck()
player1 = Player("Ethan")
#adds 4 cards of 10 to Ethan's hand
for suit in suits:
  player1.addCard(Card(suit, 10,cardImages[0], False), True)

def test_sum():
    assert sum(player1) == 40

player2 = Player("Bob")
summation = 0
#Adds 4 random cards to Bob's hand
for suit in suits:
  rand = random.randint(0,14)
  summation += rand
  player2.addCard(Card(suit,rand, cardImages[0],False),True)

def test_sum2():
    assert sum(player2) == summation




  
