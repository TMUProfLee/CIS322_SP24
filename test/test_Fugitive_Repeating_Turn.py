import sys
sys.path.append('/Users/ethom/Downloads/Godot/CIS322_SP24/source')
from CardGames import *

#Task requires user input

escape_card, HighRangeDeck, MidRangeDeck, LowRangeDeck, starting_cards = split_card()
fugitive_deck, NewHideouts = FugitiveRepeating([],LowRangeDeck,MidRangeDeck,HighRangeDeck)
print(fugitive_deck)
print(NewHideouts)
