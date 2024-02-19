# Function to determine the highest card in hand
def highest_card(hand):
    # Create a dictionary with the rank and point values of the cards
    ranks = {
        '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14
    }

    # Create an empty list to store the point values of the cards
    points = []
    # Iterate over the hand
    for card in hand:
        # Get the rank of the card and its point value
        rank = card[0]
        point = ranks[rank]
        # Append the point value to the list
        points.append(point)

    # Return the highest point value in the list
    return max(points)

# Main Code
hand = ['4S','AH','KD','9C','10S']
print(highest_card(hand))