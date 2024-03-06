import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../"))

from CardGames import *
#from sum import sum_cards
from CardGames import Card, Poker, Player, Deck
#from Connection import Server