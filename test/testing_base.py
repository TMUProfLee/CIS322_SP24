import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../"))

from CardGames import Poker, Dealer, Player, Deck
#from sum import sum_cards
#from Connection import Server