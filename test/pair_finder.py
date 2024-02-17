def has_pair(player):
    for card1 in player.hand:
        for card2 in player.hand:
            if card1.value == card2.value and not card1.suit == card2.suit:
                return True
    return False