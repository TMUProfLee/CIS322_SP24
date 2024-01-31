from Sum import sum, Player, suits, cardImages, Card, Deck

deck = Deck()
player = Player("Ethan")
#adds 4 cards of 10 to player's hand
for suit in suits:
  player.addCard(Card(suit, 10,cardImages[0], False), True)

def test_sum():
    assert sum(player) == 40


  
