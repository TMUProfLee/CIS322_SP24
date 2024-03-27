import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../"))

from CardGames_test import *
#from sum import sum_cards
#from Connection import Server