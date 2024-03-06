from CardGames import *
# Write a function that can sum the value of a player’s hand.

# Input: Player object or list of cards (player’s hand)
# Output: Total value of the cards

def sum_cards(hand):
    sum = 0
    for card in hand:
        sum += card.value
    return sum

deck = Deck()
dealer = Dealer(deck)

player = Player('Example Player')

print(f"Initial deck size: {deck.size}")

# Deal 5 cards to each player
dealer.dealCards(5, [player])
print(f"Deck size after dealing: {deck.size}")

print(f"{player.name}'s hand: {[str(card) for card in player.hand]}")

hand_value = sum_cards(player.hand)
print(f"Sum of {player.name}'s hand: {hand_value}")




